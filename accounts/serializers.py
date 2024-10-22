# from rest_framework import serializers
# from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import validate_password
# from rest_framework.validators import UniqueValidator
# from django.db import IntegrityError

# class SignupSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#     username = serializers.CharField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     confirm_password = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'confirm_password']

#     def validate(self, data):
#         if data['password'] != data['confirm_password']:
#             raise serializers.ValidationError("Passwords do not match.")
#         return data

#     def create(self, validated_data):
#         try:
#             user = User.objects.create(
#                 username=validated_data['username'],
#                 email=validated_data['email']
#             )
#             user.set_password(validated_data['password'])
#             user.save()
#             return user
#         except IntegrityError:
#             raise serializers.ValidationError({"username": "This username is already taken."})


# serializers.py
from rest_framework import serializers
from mongoengine.errors import NotUniqueError
from .models import UserDetails
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password


class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        try:
            hashed_password = make_password(validated_data['password'])
            user = UserDetails(
                username=validated_data['username'],
                email=validated_data['email'],
                password=hashed_password
            )
            user.save()
            return user
        except NotUniqueError:
            raise serializers.ValidationError({"username": "This username or email is already taken."})


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'  # Include all fields in the UserDetails model

        # Alternatively, specify individual fields:
        # fields = ['id', 'username', 'email', 'created_at', 'profile_picture', 'registration_time', 'registration_date', ...]


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            # Retrieve the user by email
            user = UserDetails.objects.get(email=email)
        except DoesNotExist:
            raise serializers.ValidationError("Invalid email.")

        # Check if the password matches
        if not user.check_password(password):
                raise serializers.ValidationError("Invalid password.")
        # Generate JWT tokens
        refresh = RefreshToken()
        refresh['id'] = str(user.id)  # Use the user ID or username as the identifier

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
