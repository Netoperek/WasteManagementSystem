from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.forms import UserCreationForm
from .forms import WebAppUserForm
from django.contrib.auth.models import User
from userroles.models import set_user_role
from userroles import roles
from userroles.decorators import role_required
from webAppUser.models import WebAppUser

def setRole(user,role):
    if role == "admin":
        set_user_role(user, roles.admin)
    else:
        set_user_role(user, roles.manager)

def validate_user_data(data):
    data_dict = dict(data.iterlists())
    query_set = User.objects.values('username')
    names = list(query_set)
    pass1 = data['password1']
    name = data['username']
    pass2 = data['password2']
    if pass1 != pass2:
        return "Hasla nie pasuja"

    for ele in names:
        if ele['username'] == name:
            return "Login zajety"

    return ""

@role_required(roles.admin)
def addWebUser(request):
    if request.method == 'POST':
        req = request.POST
        role = request.POST.get("role", "")
        form = UserCreationForm(req)
        error_message = validate_user_data(req)
        if form.is_valid():
            new_user = form.save()
            setRole(new_user, role)
            webAppUser = WebAppUser(user = new_user)
            webAppUser.save()
            return HttpResponseRedirect('webAppUsers')
        else:
            return render_to_response("addWebUser.html",
                                                    locals(),
                                                    context_instance=RequestContext(request))
    else:
        form = UserCreationForm(request.POST)
        return render_to_response("addWebUser.html",
                                            locals(),
                                            context_instance=RequestContext(request))

def user_exists(user_id):
    users = WebAppUser.objects.all()
    for user in users:
        if user_id == user.user_id:
            return True

    return False
    

def webAppUsers(request):
	webUsers = WebAppUser.objects.all()

	_id = request.POST.get("_id")
        _modify = request.POST.get('_modify')
	if _id:
            result = remove(request, _id)
            if result != True:
                return HttpResponseRedirect('wrongPriviliges')
        elif _modify:
            num = _modify
            return HttpResponseRedirect('modifyWebAppUser' + str(num))
	else:
		if request.method == 'POST':
			Id = request.POST['id']
			Login = request.POST['username']
			if Login == None:
		            Login = r".*"
			if Id:
		            webUsers = WebAppUser.objects.filter(pk = Id)
			else:
		            users =  User.objects.filter(username__regex=Login)
                            webUsers = []
                            for user in users:
                                if user_exists(user.id):
                                    webUser = WebAppUser.objects.get(user_id = user.id)
                                    webUsers.append(webUser)

	return render_to_response("webUsers.html",
                                   locals(),
				   context_instance=RequestContext(request))

def username_taken(username):
    names = User.objects.all().values('username')
    for ele in names:
        if username in ele.values():
            return True

    return False

#To use decorator request arg has to be passed
#
@role_required(roles.admin)
def remove(request, q):
   _id = request.POST.get("_id")
   web_app_user = WebAppUser.objects.get(id=_id)
   user_id = web_app_user.user_id
   User.objects.filter(id=user_id).delete()
   web_app_user.delete()
   return True

@role_required(roles.admin)
def modifyWebAppUser(request, num):
    webUser = WebAppUser.objects.get(id = num)
    user_id = webUser.user_id
    user = User.objects.get(id = user_id)
    if request.method == 'POST':
	role = request.POST['role']
	name = request.POST['name']
	password = request.POST['password']
        if name:
            if username_taken(name):
                return HttpResponseRedirect('wrongUsernameWeb')
            webUser.username = name
            user.username = name
        if role:
            setRole(user, role)
        if password:
            user.set_password(password)
        user.save()
        webUser.save()
    
        return HttpResponseRedirect('webAppUsers')
        
    return render_to_response("modifyWebAppUser.html",
			      locals(),
			      context_instance=RequestContext(request))
def wrongUsernameWeb(request):
    return render_to_response(  "wrongUsernameWeb.html",
                                locals(),
				context_instance=RequestContext(request))
