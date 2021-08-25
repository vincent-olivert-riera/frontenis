from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

# pylint: disable=redefined-builtin
# pylint: disable=unused-argument
# pylint: disable=no-self-use


class Login(APIView):
    """
    Login a user into the system.
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return Response(
                {"msg": "authentication succeded"},
                status=status.HTTP_200_OK,
            )
        else:
            # No backend authenticated the credentials
            return Response(
                {"msg": "authentication failed"},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class Logout(APIView):
    """
    Logout a user from the system.
    """

    def post(self, request, format=None):
        logout(request)
        return Response({"msg": "logged out"}, status=status.HTTP_200_OK)
