from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserCreateModelSerializer, GetMeModelSerializer, LoginSerializer


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateModelSerializer


class GetMeApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None, *args, **kwargs):
        user = request.user
        serializer_data = GetMeModelSerializer(user).data
        return Response(serializer_data)



class LoginView(RetrieveAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            data = {
                'message': 'zor'
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

