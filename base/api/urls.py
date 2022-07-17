from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include
from . import views
from .views import MyTokenObtainPairView, UserViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet)


urlpatterns = [
    path('', views.home_api),
    path('notes/', views.notes_api),
    path('rest/', include(router.urls)),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
