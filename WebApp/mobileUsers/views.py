# -*- coding: utf-8 -*-

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
from django.contrib.auth.models import User

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
                            mobileUsers =  MobileUser.objects.filter(pk = Id, username__regex=Login)
                    else:
                            mobileUsers =  MobileUser.objects.filter(username__regex=Login)

    return render_to_response(
            "mobileUsers.html",
            locals(),
            context_instance=RequestContext(request))

def validate_user_data(data):
    data_dict = dict(data.iterlists())
    query_set = User.objects.values('username')
    names = list(query_set)
    pass1 = data['password1']
    name = data['username']
    pass2 = data['password2']
    if pass1 != pass2:
        return "Hasła nie pasują"

    for ele in names:
        if ele['username'] == name:
            return "Login zajęty"

    return ""


@role_required(roles.admin)
def addMobileUser(request):
    if request.method == 'POST':
        req = request.POST
        form = UserCreationForm(req)
        error_message = validate_user_data(req)
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
def remove(request, q):
    _id = request.POST['_id']
    mobile_user = MobileUser.objects.get(id=_id)
    user_id = mobile_user.user_id
    MobileUser.objects.filter(id=_id).delete()
    User.objects.get(id=user_id).delete()
    return True


def username_taken(username):
    names = User.objects.all().values('username')
    for ele in names:
        if username in ele.values():
            return True

    return False

@role_required(roles.admin)
def modifyMobileUser(request, num):
    mobile_user = MobileUser.objects.get(id = num)
    user_id = mobile_user.user_id
    user = User.objects.get(id = user_id)
    if request.method == 'POST':
        password = request.POST['password']
        name = request.POST['name']
        if password:
            user.set_password(password)
        if name:
            if username_taken(name):
                return HttpResponseRedirect('wrongUsername')
            user.username = name
            mobile_user.username = name
        user.save()
        mobile_user.save()
    
        return HttpResponseRedirect('mobileUsers')
    return render_to_response(  "modifyMobileUser.html",
                                locals(),
				context_instance=RequestContext(request))

def wrongUsername(request):
    return render_to_response(  "wrongUsername.html",
                                locals(),
                                context_instance=RequestContext(request))
