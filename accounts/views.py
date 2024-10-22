# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import SignupSerializer

# class SignupView(APIView):
#     def post(self, request):
#         serializer = SignupSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer, LoginSerializer, UserDetailsSerializer
from rest_framework.permissions import IsAuthenticated
import logging
from .models import UserDetails

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)  # Return the tokens here
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    # Remove or comment out the permission_classes line
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        users = UserDetails.objects.all()  # Fetch all user details
        serializer = UserDetailsSerializer(users, many=True)  # Serialize the data
        return Response(serializer.data)  # Return the serialized data
