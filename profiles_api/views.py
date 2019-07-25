from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API View"""

    def get(self, request, format=None):
        """ Returns a list of APIView features"""

        an_apiview =[
        "Uses HTTP Methos as funtions\
        (get, post, put, patch, delete)",
        "It Similar to a traditional Django View",
        "Gives you the most control over your application logic",
        "Is mapped manually to URLS"

        ]

        # must retrun a Response
        return Response({"message": 'Hello!', 'an_apiview': an_apiview})
