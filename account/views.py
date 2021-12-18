from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegistrationSerializer, UserSerializer
from .models import UserModel
from rest_framework.permissions import IsAuthenticated


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'status': 'fail',
                'data': serializer.errors
            })
        serializer.save()
        return Response({
            'status': 'success',
            'data': serializer.data
        })

#
# class LoginView(APIView):
#     def post(self, request):
#         username = request.data['username']
#         password = request.data['password']
#
#         user = UserModel.objects.filter(username=username).first()
#
#         if user is None:
#             return Response({
#                 'status': 'fail',
#                 'data': 'User not found'
#             })
#         if not user.check_password(password):
#             return Response({
#                 'status': 'fail',
#                 'data': 'Incorrect password'
#             })
#
#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }
#
#         token = jwt.encode(payload, 'secret', algorithm='HS256')
#
#         response = Response({
#             'status': 'success',
#             'data': {
#                 'token': token
#             }
#         })
#
#         response.set_cookie(key='jwt', value=token, httponly=True)
#
#         return response
#
#
# class LogoutView(APIView):
#     def post(self, request):
#         response = Response({
#             'status': 'success',
#             'data': 'bye!'
#         })
#         response.delete_cookie('jwt')
#
#         return response


class ProfileView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):

        user = UserModel.objects.filter(id=request.user.id).first()
        serializer = UserSerializer(user)

        return Response({
            'status': 'success',
            'data': serializer.data
        })
