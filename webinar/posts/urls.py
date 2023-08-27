from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    # CRUD посты FBV
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    
    # Контекст для шаблонов
    path('context_sandbox/', views.sandbox, name='sandbox'),
    
]
