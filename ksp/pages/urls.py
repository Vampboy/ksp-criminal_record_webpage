from django.urls import path
from . import views 
urlpatterns = [

    path('',views.base,name='base'),
    path('base/',views.base,name='base'),
    path('upload',views.criminal_view,name='upload'),
    path('success',views.success, name = 'success')
    
]

