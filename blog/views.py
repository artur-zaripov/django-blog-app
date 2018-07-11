from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from blog.models import Article
from blog.serializers import ArticleSerializer, UserSerializer
from blog.permissions import IsOwner


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'articles': reverse('article-list', request=request, format=format)
    })


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleList(APIView):
    permission_classes = (IsAuthenticated, IsOwner)

    def get(self, request, format=None):
        articles = Article.objects.filter(user=request.user)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleDetail(APIView):
    permission_classes = (IsAuthenticated, IsOwner)

    def get_object(self, request, pk):
        try:
            return Article.objects.filter(pk=pk).filter(user=request.user)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        articles = self.get_object(request, pk)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)