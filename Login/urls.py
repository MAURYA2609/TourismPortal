from django.urls import path
from . import views
from django.conf.urls import url
from django.template.context_processors import csrf
from Login.views import login,signup,authentication,validate

urlpatterns = [
    path('',views.login,name='login'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    url(r'^authentication',authentication),
    url(r'^validate',validate),
    path('logout/',views.logout,name='logout')
]
