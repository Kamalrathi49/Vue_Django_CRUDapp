from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostDetail, PostList

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)