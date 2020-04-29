from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from testApp.taskserializer import UserRegisterserializer,UserLoginSerializer,TaskSerializer
class UserRegistration(APIView):
    def post(self,request):
        employee=request.data
        userserials=UserRegisterserializer(data=employee)
        if userserials.is_valid():
            userserials.save()
            msg={"Sucess":True}
        else:
            msg={"Sucess":False,"errors":[{userserials.errors}]}
        return Response(msg)

from testApp.models import  TaskModel
from rest_framework.authtoken.models import Token
class UserLogin(APIView):
    def post(self,request):
        logInData=request.data
        serializer=UserLoginSerializer(data=logInData)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created=Token.objects.get_or_create(user=user)
        return Response({"sucess":"true","token":token.key},status=200)

class TaskOperation(APIView):
    def post(self,request):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg={"sucess":"true","data":request.data}
        else:
            msg={"msg":serializer.errors}
        return Response(msg)
class TaskOperationUpdateRetriveDelete(RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

