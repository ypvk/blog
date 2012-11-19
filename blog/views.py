# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
#from rest_framework.response import Response

from django.http import Http404
from django.shortcuts import render_to_response

from blog.models import User
from blog.serializers import UserSerializer

import logging

logger = logging.getLogger(__name__)

class UserList(APIView):
    """
    get list of users or post to create new one
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users)
        return render_to_response('users.html.haml', {'users': serializer.object})
    def post(self, request, format=None):
        return

class UserItem(APIView):
    """
    deal with each user
    """
    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username, foramt=None):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        logger.error(serializer.data)
        return render_to_response('user.html.haml', {'user': 'anc'})

    def put(self, request, username, format=None):
        return

    def delete(self, request, username, format=None):
        return
