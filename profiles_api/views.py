from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):

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
