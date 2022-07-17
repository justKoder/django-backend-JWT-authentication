from django.forms import CharField
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

from django.contrib.auth.hashers import make_password

from base.models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class UserSerializer(ModelSerializer):
    password = serializers.CharField(
        min_length=3, required=True, error_messages={"min-length": f"Invalid password. Password did not matched"})
    # password2 = serializers.CharField(
    #     min_length=3, required=True, error_messages={"min-length": f"Invalid password. Password did not matched"})

    class Meta:
        model = User
        fields = "__all__"

    # def validate(self, data):
    #     if data["password"] != data["password2"]:
    #         raise serializers.ValidationError("Password mismatched")
    #     return data

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
