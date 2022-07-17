from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from django.contrib.auth.models import User

from .serializers import NoteSerializer, UserSerializer
from base.models import Note
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def home_api(request):
    routes = [
        'api/tokens',
        'api/tokens/refresh',
    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def notes_api(request):
    user = request.user
    notes = user.note_set.all()
    serializers = NoteSerializer(notes, many=True)
    return Response(serializers.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
