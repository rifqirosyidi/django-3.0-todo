from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update_task/<int:pk>', views.update_task, name='update'),
    path('delete_task/<int:pk>', views.delete_task, name='delete'),
]
