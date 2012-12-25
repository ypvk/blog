# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import Http404
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from django.contrib.auth.models import User
from blog.serializers import UserSerializer

import logging

logger = logging.getLogger(__name__)

class UserList(APIView):
    """
    get list of users or post to create new one
    """
    def get(self, request, format=None):
        """
        Index GET /users
        """
        users = User.objects.all()
        serializer = UserSerializer(users)
        return render_to_response('users.html.haml',
                {'users': serializer.object, 'format': format},
                context_instance=RequestContext(request))
    def post(self, request, format=None):
        """
        Create POST /users
        """
        return

class UserItem(APIView):
    """
    deal with each user
    """
    def get_object(self, username):
        """
        get user by username
        """
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        """
        Show: GET /users/:username
        """
        user = self.get_object(username)
        serializer = UserSerializer(user)
        if format == 'json':
            return Response(serializer.data)
        else:
            return render_to_response('user.html.haml',
                    {'user': serializer.object, 'format': format},
                    context_instance=RequestContext(request))

    def put(self, request, username, format=None):
        """
        Update : PUT /users/:username
        """
        return

    def delete(self, request, username, format=None):
        """
        Destroy: DELETE /users/:username
        """
        return

class UserNew(APIView):
    """
    new user
    """

    def get(self, request, format=None):
        """
        New GET /users/new
        """
        form = UserRegisterForm()
        return render_to_response('user_new.html.haml', {'form': form})

class UserEdit(APIView):
    """
    edit user
    """
    def get_object(self, username):
        """
        get user by username
        """
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username, foramt=None):
        """
        Edit GET /users/:username/edit
        """
        user = self.get_object(username)
        return Response({'yuping': user.username})
