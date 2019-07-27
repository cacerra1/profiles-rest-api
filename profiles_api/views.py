from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from profiles_api import serializers

from profiles_api import models

from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters

<<<<<<< HEAD
=======
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

>>>>>>> Section 12

class HelloApiView(APIView):
    ''' This is what connects us to the serializer we created'''
    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Will you work?????', "Who knows",
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = name
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        '''handling updating an object'''

        return Response({"method": 'PUT'})

    def patch(self, request, pk=None):
        '''handling partial updating  of an object'''

        return Response({"method": 'PATCH'})

    def delete(self, request, pk=None):
        '''delete an object'''

        return Response({"method": 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    '''Test APi viewset'''

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        '''return a hello message'''

        a_viewset = [

         "Users Actions (list, create, retirve , update, partial_update)",
         "Automatically maps to URLs using Routers",
         "Provides more functionality with less code"
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
<<<<<<< HEAD
=======

class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
>>>>>>> Section 12
