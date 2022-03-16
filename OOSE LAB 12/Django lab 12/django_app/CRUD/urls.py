from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.std_form, name = 'std_form'),
    path('show',views.show, name = 'std_show'),
    path('<int:id>/',views.std_form, name = 'std_update'),
    path('delete/<int:id>/',views.delete, name = 'std_delete') 
    #We inserted delete in it because the paths should be differnt from others
]