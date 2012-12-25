from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from django.contrib.auth.forms import UserCreationForm
# for user logout
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect

def user_logout(request):
    """
    GET /logout
    for user to logout
    """
    logout(request)
    return redirect('users')

@csrf_protect
def registration(request):
    """
    GET /registration
    """
    user = request.user
    if request.method == "GET":
        if user.is_authenticated():
            return redirect('users')
        else:
            form = UserCreationForm()
            return render_to_response('registration.html.haml',
                    {'form': form},
                    context_instance=RequestContext(request))
    """
    POST /registration
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('users')
        else:
            return render_to_response('registration.html.haml',
                    {'form': form},
                    context_instance=RequestContext(request))
