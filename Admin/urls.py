from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from Admin.views import AdminHome,AddHotel,AddPackage,AllHotels,AllPackages,addh,addp

urlpatterns = [
    path('AdminHome/',views.AdminHome,name='AdminHome'),
    path('AddHotel/',views.AddHotel,name='AddHotel'),
    path('AddPackage/',views.AddPackage,name='AddPackage'),
    path('AllHotels/',views.AllHotels,name='AllHotels'),
    path('AllPackages/',views.AllPackages,name='AllPackages'),
    url(r'^addh',addh),
    url(r'^addp',addp),
]+static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
