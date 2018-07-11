from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from blog.models import Article
import json


class ArticleTestCase(TestCase):
    CONST_USERNAME_1 = "testuser"
    CONST_PASSWORD_1 = "testpass11"
    CONST_USERNAME_2 = "testuser2"
    CONST_PASSWORD_2 = "testpass22"

    def setUp(self):
        test_user1 = User.objects.create_user(username=ArticleTestCase.CONST_USERNAME_1,
                                              email="test@test.ru",
                                              password=ArticleTestCase.CONST_PASSWORD_1)
        test_user2 = User.objects.create_user(username=ArticleTestCase.CONST_USERNAME_2,
                                              email="test@test2.ru",
                                              password=ArticleTestCase.CONST_PASSWORD_2)
        Article.objects.create(user=test_user1,
                               text="test_text",
                               pub_date=timezone.now())
        Article.objects.create(user=test_user2,
                               text="test_text 2",
                               pub_date=timezone.now())

    def test_user_login(self):
        c = Client()
        response = c.post('/api/v1/login/',
                          {'username': ArticleTestCase.CONST_USERNAME_1,
                           'password': ArticleTestCase.CONST_PASSWORD_1})
        self.assertEqual(response.status_code, 302)

    def test_articles_list(self):
        c = Client()
        c.post('/api/v1/login/',
               {'username': ArticleTestCase.CONST_USERNAME_1,
                'password': ArticleTestCase.CONST_PASSWORD_1})
        response = c.get('/api/v1/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(
                str(response.content, encoding='utf8')
            )[0]['id'], 1
        )

    def test_article_access(self):
        c = Client()
        c.post('/api/v1/login/',
               {'username': ArticleTestCase.CONST_USERNAME_1,
                'password': ArticleTestCase.CONST_PASSWORD_1})
        response = c.get('/api/v1/article/2/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            not json.loads(
                str(response.content, encoding='utf8')
            )
        )

