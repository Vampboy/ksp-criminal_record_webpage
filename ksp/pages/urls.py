
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views 
urlpatterns = [

    path('',views.base,name='base'),
    path('base/',views.base,name='base'),
    path('upload',views.criminal_view,name='upload'),
    path('success',views.success, name = 'success'),
    path('result',views.result,name = 'result')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
