from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_active=False,
        )
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        current_site = get_current_site(self.context['request'])
        email_subject = 'Activate your account'
        email_body = f'Hi {user.username},\nPlease use the link below to activate your account:\n{current_site.domain}/verify-email/{uid}/{token}'
        user.email_user(email_subject, email_body)
        send_mail(
            email_subject,
            
        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if user is None:
            user = authenticate(email=attrs['email'], password=attrs['password'])
            if user is None:
                raise serializers.ValidationError("Invalid credentials")
        attrs['user'] = user
        return attrs
