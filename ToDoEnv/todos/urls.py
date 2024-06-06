from django.urls import path
from . import views

urlpatterns = [
    path('all/update/<int:pk>/', views.generalview),
    path('', views.show_view),
    path('updel/<int:pk>/', views.updelete_view),
    path('all/<int:pk>/', views.generalview),
    path('all/', views.generalview),
    path('all/delete/<int:pk>/', views.generalview)

]