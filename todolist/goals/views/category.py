from rest_framework.generics import (
    CreateAPIView, 
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    )
from rest_framework import permissions, filters
from rest_framework.pagination import LimitOffsetPagination
from goals.models import GoalCategory, Goal
from goals.serializers.category import CategoryCreateSerializer, CategorySerializer


class CategoryCreateView(CreateAPIView):
    model = GoalCategory
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategoryCreateSerializer


class CategoryView(RetrieveUpdateDestroyAPIView):
    model = GoalCategory
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GoalCategory.objects.filter(user=self.request.user, is_deleted=False)
    
    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
        return instance
    
    
class CategoryListView(ListAPIView):
    model = GoalCategory
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ['title', 'created']
    ordering = ['title']
    search_fields = ['title']

    def get_queryset(self):
        return GoalCategory.objects.filter(
            user=self.request.user, is_deleted=False
        )
        