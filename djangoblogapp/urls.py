from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    url(r'^$', views.api_root),
    path('admin/', admin.site.urls),
    path('api/v1/', include('blog.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
