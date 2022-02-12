from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('stories', views.StoryViewSet, basename='stories')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='login')
]