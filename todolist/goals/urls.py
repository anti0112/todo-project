from django.urls import path

from goals.views import category

urlpatterns = [
    path('goal_category/create', category.CategoryCreateView.as_view()),
    path("goal_category/list", category.CategoryListView.as_view()),
    path("goal_category/<pk>", category.CategoryView.as_view()),
]