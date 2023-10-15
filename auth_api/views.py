from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

# 測試確保驗證路徑使用的庫
from rest_framework.decorators import authentication_classes, permission_classes        
from rest_framework.authentication import TokenAuthentication, SessionAuthentication    
from rest_framework.permissions import IsAuthenticated

# 註冊
@api_view(['POST'])
def signup(request):

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=request.data['username'])
        token = Token.objects.get(user=user)

        serializer = UserSerializer(user)

        # 組 token資料回傳
        data = {
            'user': serializer.data,
            'token': token.key
        }

        return Response(data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 登入
@api_view(['POST'])
def login(request):
    data = request.data

    # 驗證登入者身份
    authenticate_user = authenticate(username=data['username'], password=data['password'])

    if authenticate_user is not None:
        user = User.objects.get(username=data['username'])
        serializer = UserSerializer(user)

        response_data = {
            'user': serializer.data
        }

        token, created_token = Token.objects.get_or_create(user=user)
        # 加入或建立 token
        if token:
            response_data['token'] = token.key
        elif created_token:
            response_data['token'] = created_token.key

        return Response(response_data, status=status.HTTP_200_OK)

    return Response({"message":"沒有這個使用者"}, status=status.HTTP_400_BAD_REQUEST)


# 測試確保路徑驗證 - 必須使用postman測試
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])   # 使用者必須帶有 token session 才可以進入
@permission_classes([IsAuthenticated])                                  # 使用者是否已驗證
def testView(request):

    return Response({"message":"測試驗證"}, status=200)


# 登出
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])  
@permission_classes([IsAuthenticated])                                 
def logout(request):

    request.user.auth_token.delete()

    return Response({"message":"登出成功"}, status=status.HTTP_200_OK)
