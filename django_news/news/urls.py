from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_url'),
    path('<int:post_id>/', views.post_detail, name='post_detail_url'),
    path('tags/', views.tags, name='tags_url')
]