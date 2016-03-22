from django.conf.urls import include, url
from django.contrib import admin

from stapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('stapp.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.login_user, name='login'),
    url(r'^create/', views.create_stack, name='create')
]
