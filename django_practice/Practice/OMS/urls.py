from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.signup, name='signup'),
    path('show/', views.show, name='show'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='dl'),
    path('addproduct/',views.AddProduct,name='addproduct'),
    path('showproduct/',views.showproduct,name='showproduct'),
]