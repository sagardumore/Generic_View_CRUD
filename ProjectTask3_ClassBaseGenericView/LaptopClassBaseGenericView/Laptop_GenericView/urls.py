from django.urls import  path
from .import views

urlpatterns=[
    path('addlaptop/',views.AddLaptopView.as_view(),name='add_laptop'),
    path('showlaptop/', views.ShowLaptopView.as_view(), name='show_laptop'),
    path('update/<int:pk>/', views.LaptopUpdateView.as_view(), name='update_laptop'),
    path('delete/<int:pk>/', views.LaptopDeleteView.as_view(), name='delete_laptop')

]