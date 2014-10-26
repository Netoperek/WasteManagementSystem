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

@role_required(roles.admin)
def addWebUser(request):
	if request.method == 'POST':
	        role = request.POST.get("role", "")
		form = UserCreationForm(request.POST)
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

def webAppUsers(request):
	webUsers = WebAppUser.objects.all()

	_id = request.POST.get("remove", "")
        _modify = request.POST.get('modify',"")
	if _id:
            result = remove(request, _id)
            if result != True:
                return HttpResponseRedirect('wrongPriviliges')
        elif _modify:
            num = int(_modify.split(' ')[2])
            return HttpResponseRedirect('modifyWebAppUser' + str(num))
	else:
		if request.method == 'POST':
			Id = request.POST['id']
			Login = request.POST['username']

			if Login == None:
				Login = r".*"

			if Id:
				webUsers =  User.objects.filter(pk = Id,
												username__regex=Login)
			else:
				webUsers =  User.objects.filter(username__regex=Login)

	return render_to_response("webUsers.html",
                                   locals(),
				   context_instance=RequestContext(request))

#To use decorator request arg has to be passed
#
@role_required(roles.admin)
def remove(request, _id):
   User.objects.filter(id=int(_id.split(' ')[2])).delete()
   return True

@role_required(roles.admin)
def modifyWebAppUser(request, num):
    webUser =  User.objects.get(pk = num)
    if request.method == 'POST':
	role = request.POST['role']
	name = request.POST['name']
	password = request.POST['password']
        if role:
            setRole(webUser, role)
        if name:
            webUser.username = name
        if password:
            webUser.set_password(password)
        webUser.save()
    
        return HttpResponseRedirect('webAppUsers')
        
    return render_to_response("modifyWebAppUser.html",
			      locals(),
			      context_instance=RequestContext(request))
