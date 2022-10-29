from django.urls import path

from goals.views import category, goal, comment



urlpatterns = [
    path('goal_category/create', category.CategoryCreateView.as_view()),
    path("goal_category/list", category.CategoryListView.as_view()),
    path("goal_category/<pk>", category.CategoryView.as_view()),
    path("goal/create", goal.GoalCreateView.as_view()),
    path("goal/list", goal.GoalListView.as_view()),
    path("goal/<pk>", goal.GoalView.as_view()),
    path("goal_comment/create", comment.CommentCreateView.as_view()),
    path("goal_comment/list", comment.CommentListView.as_view()),
    path("goal_comment/<pk>", comment.CommentView.as_view()),
]