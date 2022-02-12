from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, filters
from .serializers import UserSerializer, StorySerializer
from .models import Story
from .permissions import IsAuthorOrReadOnly
from .paginations import StoryPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.using('default').all().order_by('-date_joined')
    serializer_class = UserSerializer


class StoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    serializer_class = StorySerializer
    pagination_class = StoryPageNumberPagination
    queryset = Story.objects.using('lite').all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title', 'text']
    filterset_fields = ['read']
    ordering_fields = ['date']

