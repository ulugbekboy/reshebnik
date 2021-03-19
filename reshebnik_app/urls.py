from django.urls import path,include
from .views import *
urlpatterns = [

    path('uz/' , index , name ='index1'),
    path('' , index , name ='index'),
    path('ru/' , rus , name ='rus'),
    path('contact/', contact , name ='contact')
]

