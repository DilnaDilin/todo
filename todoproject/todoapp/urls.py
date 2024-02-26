from . import views
from django.urls import path


urlpatterns = [

    path('', views.home,name='home'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.edit,name='edit')
]