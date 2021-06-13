from django.urls import path
from . import views
from django.conf.urls import url
from django.template.context_processors import csrf
from django.conf.urls.static import static
from django.conf import settings
from User.views import Home,Packages,Hotels,Bookings,buyHotel,buyPackage

urlpatterns = [
    path('Home/',views.Home,name='Home'),
    path('Packages/',views.Packages,name='Packages'),
    path('Hotels/',views.Hotels,name='Hotels'),
    path('Bookings/',views.Bookings,name='Bookings'),
    url(r'^buyHotel',buyHotel),
    url(r'^buyPackage',buyPackage),
]+static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
