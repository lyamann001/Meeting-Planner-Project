
from django.urls import path
from . import views

urlpatterns = [
    path('meetings/<int:id>', views.detail, name='detail'),
    path('rooms', views.rooms_list, name='rooms'),
    path('new', views.new, name='new')
]