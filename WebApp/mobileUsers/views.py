from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest
from .forms import MobileUserForm
from mobileUsers.models import MobileUser
from routes.models import Route
from userroles import roles
from userroles.decorators import role_required
from django.contrib.auth.forms import UserCreationForm
from userroles.models import set_user_role
from userroles import roles
from userroles.decorators import role_required

def mobileUsers(request):
	mobileUsers = MobileUser.objects.all()
	
	_id = request.POST.get("remove", "")
        _modify = request.POST.get("modify", "")
	if _id:
            result = remove(request, _id)
            if result != True:
                return HttpResponseRedirect('wrongPriviliges')

        elif _modify:
            num = int(_modify.split(' ')[2])
            return HttpResponseRedirect('modifyMobileUser' + str(num))
	else:
		if request.method == 'POST':
			Id = request.POST['id']
			Login = request.POST['Login']

			if Login == None:
				Login = r".*"
			if Id:
				mobileUsers =  MobileUser.objects.filter(pk = Id, login__regex=Login)
			else:
				mobileUsers =  MobileUser.objects.filter(login__regex=Login)

	return render_to_response("mobileUsers.html",
								locals(),
								context_instance=RequestContext(request))

@role_required(roles.admin)
def addMobileUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            set_user_role(new_user, roles.mobile)
            mobileUser = MobileUser(user = new_user, username = new_user.username)
            mobileUser.save()

            return HttpResponseRedirect('mobileUsers')
        else:
            return render_to_response("addMobileUser.html",
                                        locals(),
                                        context_instance=RequestContext(request))
            
    else:
        form = UserCreationForm(request.POST)
        return render_to_response("addMobileUser.html",
                                    locals(),
                                    context_instance=RequestContext(request))

@role_required(roles.admin)
def remove(request, _id):
        MobileUser.objects.filter(id=int(_id.split(' ')[2])).delete()
        return True

@role_required(roles.admin)
def modifyMobileUser(request, num):
    mobileUser = MobileUser.objects.get(pk=num)
    if request.method == 'POST':
	password = request.POST['password']
	name = request.POST['name']
        if password:
            mobileUser.password = password
        if name:
            mobileUser.login = name
        mobileUser.save()
    
        return HttpResponseRedirect('mobileUsers')
    return render_to_response(  "modifyMobileUser.html",
                                locals(),
				context_instance=RequestContext(request))
