from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('all/update/<int:pk>/', views.generalview),
    path('', views.show_view),
    path('updel/<int:pk>/', views.updelete_view, name="todo-detail"),
    path('<int:pk>/', views.get_specific_view, name="todo-list"),
    path('all/<int:pk>/', views.generalview),
    path('<int:pk>/', views.generalview),
    path('all/', views.generalview),
    path('all/delete/<int:pk>/', views.generalview),
    path('auth/', obtain_auth_token),

]