from django.conf.urls import url, include
from blog.views import ArticleList, ArticleDetail

urlpatterns = [
    url(r'^articles/$', ArticleList.as_view()),
    url(r'^article/(?P<pk>[0-9]+)/$', ArticleDetail.as_view()),
    url(r'^', include('rest_framework.urls')),
]
