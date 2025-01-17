from django.urls import path,include
from . import views


urlpatterns = [

    path('PM/', views.add,name='add'),
    path('view/',views.view,name='view'),
    path('delete/<pk>',views.delete,name='delete'),
    path('edit/<pk>',views.edit,name='edit'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('genpasswd/', views.generate_password, name='genpasswd'),
    path('',views.index,name='index'),
    #path('',views.login,name='login')
]
