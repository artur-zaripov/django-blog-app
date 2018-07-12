from django.conf.urls import url, include
from blog.views import UserList, ArticleList, ArticleDetail

urlpatterns = [
    url(r'^users/$', UserList.as_view(), name="user-list"),
    url(r'^articles/$', ArticleList.as_view(), name="article-list"),
    url(r'^article/(?P<pk>[0-9]+)/$', ArticleDetail.as_view()),
    url(r'^', include('rest_framework.urls')),
]
