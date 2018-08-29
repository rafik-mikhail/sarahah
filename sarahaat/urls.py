from django.urls import path
from . import views


urlpatterns = [
    path('', views.sarahah_list_view, name='sarahah_list'),
    path('<int:pk>/', views.sarahah_detail_view, name='sarahah_detail'),
    path('new/', views.sarahah_create_view, name='sarahah_new'),
]
