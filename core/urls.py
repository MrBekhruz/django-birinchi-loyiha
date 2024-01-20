from django.urls  import path
from .views import * # vews fayl htmlga javobgar bulganligi uchun import qilib olib keldik 

urlpatterns = [
    path('',home, name ='home'), # '' ichi bush buladi chunki bu hom qism views fayldagi birinchi funksiya --home-- bulganligi uchun home deb chaqiramiz 
    path('postform/',Post),
    path('bulim/<int:pk>/',bulimdata,name='bulim')

]
