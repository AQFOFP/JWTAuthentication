from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer

from user.models import UserInfo
from user.utils.auth import JwtQueryParamAuthentication


class UserInfoModelSerializer(ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


# Create your views here.
class IndexView(APIView):
    authentication_classes = [JwtQueryParamAuthentication, ]

    def get(self, request, *args, **kwargs):
        print()
        users = UserInfo.objects.filter(username=request.user['data'].get('username'))
        userser = UserInfoModelSerializer(instance=users, many=True)

        return Response(userser.data)