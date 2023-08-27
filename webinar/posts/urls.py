from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    # Почти CRUD для постов FBV
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    
    # Контекст для шаблонов
    path('context_sandbox/', views.sandbox, name='sandbox'),
    # Роут с аргументами.
    # http://127.0.0.1:8000/sandbox_with_arg/22/some_var_string/bada_abra_bada/
    path('sandbox_with_arg/<int:pk>/<str:some_var>/bada_<slug:some_slug>_bada/',
         views.sandbox_with_arg, name='sandbox_with_arg'),
    # Страничка со статикой
    path('image_sandbox/', views.image_sandbox, name='image_sandbox'),
]
