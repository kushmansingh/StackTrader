from django.conf.urls import include, url
from django.contrib import admin

from stapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('stapp.urls'))
]
