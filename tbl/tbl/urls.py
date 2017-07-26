from django.conf.urls import url, include
from django.contrib import admin

# API Urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profile/', include('profiles.urls')),
]
