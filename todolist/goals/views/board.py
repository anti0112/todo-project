from rest_framework.generics import (
    CreateAPIView, 
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    )
from goals.permissions import BoardPermissions
from goals.serializers.board import BoardSerializer, BoardCreateSerializer, BoardListSerializer
from rest_framework import permissions, filters
from rest_framework.pagination import LimitOffsetPagination
from goals.models import Board, Goal
from django.db import transaction


class BoardCreateView(CreateAPIView):
    model = Board
    serializer_class = BoardCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class BoardView(RetrieveUpdateDestroyAPIView):
    model = Board
    permission_classes = [permissions.IsAuthenticated, BoardPermissions]
    serializer_class = BoardSerializer
    
    def get_queryset(self):
        return Board.objects.filter(
            participants__user=self.request.user, is_deleted=False
            )

    def perform_destroy(self, instance: Board):
        with transaction.atomic():
            instance.is_deleted = True
            instance.save()
            instance.categories.update(is_deleted=True)
            Goal.objects.filter(category__board=instance).update(
                status=Goal.Status.archived
            )
        return instance
    
class BoardListView(ListAPIView):
    model = Board
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination
    serializer_class = BoardListSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering = ['title']
    ordering_fields = ['title']
    
    
    def get_queryset(self):
        return Board.objects.filter(
            participants__user=self.request.user, is_deleted=False
        )