from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('article/create/', views.create_article, name='create_article'),
    path('article/edit/<int:pk>/', views.edit_article, name='edit_article'),
    path('article/delete/<int:pk>/', views.delete_article, name='delete_article'),
    path('category/<int:category_id>/', views.category_list, name='category_list'),
]
