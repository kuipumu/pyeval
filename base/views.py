"""
Base App Views.
https://docs.djangoproject.com/en/3.2/topics/http/views/
"""

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from .models import Log, Role
from .serializers import LogSerializer, RoleSerializer, UserSerializer


class MethodResponse():
    """
    Customize view method responses.
    """
    def create(self, request, *args, **kwargs):
        """
        Create method.
        """
        # Get response from request.
        response = super().create(request, *args, **kwargs)
        # Only return id on response data.
        response.data = {'id': f'{response.data["id"]}'}
        # Set response status code.
        response.status_code = 200
        return response

    def update(self, request, *args, **kwargs):
        """
        Update method.
        """
        # Get response from request.
        response = super().update(request, *args, **kwargs)
        # Return empty response data.
        response.data = None
        # Set response status code.
        response.status_code = 200
        return response

class RoleViewSet(MethodResponse, ModelViewSet):
    """
    API endpoint that allows roles to be viewed or edited.
    """
    # Set model view queryset.
    queryset = Role.objects.all()
    # Set serializer to use.
    serializer_class = RoleSerializer
    # Limit view to specific HTTP methods.
    http_method_names = [
        'get',
        'post',
        'put',
        'delete'
    ]

class UserViewSet(MethodResponse, ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # Set model view queryset and use prefetch to optimize query.
    queryset = get_user_model().objects.prefetch_related(
        "role_id"
    )
    # Set serializer to use.
    serializer_class = UserSerializer
    # Limit view to specific HTTP methods.
    http_method_names = [
        'get',
        'post',
        'put',
        'delete'
    ]

class LogViewSet(MethodResponse, ModelViewSet):
    """
    API endpoint that allows logs to be viewed or edited.
    """
    # Set model view queryset and use prefetch to optimize query.
    queryset = Log.objects.prefetch_related(
        "user_id"
    )
    # Set serializer to use.
    serializer_class = LogSerializer
    # Limit view to specific HTTP methods.
    http_method_names = [
        'get',
        'post'
    ]
    # Set fields to filter query from.
    filterset_fields = [
        'action'
    ]


class LoginView(ObtainAuthToken):
    """
    API endpoint that allows user to create or delte access token.
    """
    def post(self, request, *args, **kwargs):
        """
        POST method of login view.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(
            user=user
        )
        return Response(
            {
                'role_id': UserSerializer(user).data['role_id'],
                'access_token': token.key
            }
        )

    def delete(self, request):
        """
        Delete method of login view.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get(
            user=user
        )
        token.delete()
        return Response(status=HTTP_200_OK)

login_view = LoginView.as_view()
