from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from django.urls import reverse
from posts.models import Post

class PostsAPITestCase(APITestCase):

    def setUp(self):
        """ایجاد داده تستی قبل از اجرای تست‌ها"""
        self.post = Post.objects.create(title="Test Post", content="This is a test.")

    def test_get_posts(self):
        """تست دریافت لیست پست‌ها"""
        url = 'http://127.0.0.1:8000/posts/'  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # بررسی کد پاسخ
        self.assertEqual(len(response.data), 1)  # بررسی تعداد پست‌ها
        self.assertEqual(response.data[2]["title"], "Test P")  # بررسی مقدار داده‌ها

    def test_create_post(self):
        """تست ایجاد پست جدید"""
        url = 'http://127.0.0.1:8000/posts/'
        data = {"title": "New Post", "content": "New content"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 200)  # بررسی ایجاد موفق
        self.assertEqual(Post.objects.count(), 2) 

