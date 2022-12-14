from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    ) 
from rest_framework import permissions, filters
from rest_framework.pagination import LimitOffsetPagination

from goals.models import Goal
from goals.serializers.goal import GoalCreateSerializer, GoalSerializer
from goals.filters import GoalDateFilter
from goals.permissions import UserPermissions


class GoalCreateView(CreateAPIView):
    model = Goal
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCreateSerializer
    

class GoalListView(ListAPIView):
    model = Goal
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = GoalDateFilter
    search_fields = ["title", "description"]
    ordering_fields = ["due_date", "priority"]
    ordering = ["priority", "due_date"]
    
    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

class GoalView(RetrieveUpdateDestroyAPIView):
    model = Goal
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated, UserPermissions]
    
    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)
    
    def perform_destroy(self, instance):
        instance.status = Goal.Status.archived
        instance.save()
        return instance