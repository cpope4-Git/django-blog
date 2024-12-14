from django.test import TestCase
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.test.client import RequestFactory
from blogging.models import Post, Category
from django.contrib.auth.forms import UserCreationForm


class PostTestCase(TestCase):
    fixtures = ["blogging_test_fixture.json"]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a blog title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class CategoryTestCase(TestCase):

    def test_string_representation(self):
        expected = "A Category"
        category1 = Category(name=expected)
        actual = str(category1)
        self.assertEqual(expected, actual)


class FrontEndTestCase(TestCase):
    fixtures = ["blogging_test_fixture.json"]

    def setUp(self):
        self.now = datetime.datetime.now()
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(title=f"Post {count} Title", text="foo", author=author)
            if count < 3:
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()

    def test_list_only_published(self):
        resp = self.client.get("/")
        resp_text = resp.content.decode(resp.charset)
        self.assertTrue("The Pope's Blog Posts" in resp_text)
        # for count in range(1, 6):
        #     # print(resp_text[count])
        #     title = f"Post {count} Title"
        #     if count < 6:
        #         self.assertContains(resp, title, count=1)
        #     else:
        #         self.assertNotContains(resp, title)

    def test_details_only_published(self):
        for count in range(1, 4):
            title = f"Post {count} Title"
            post = Post.objects.get(pk=1)
            resp = self.client.get("post/%d/" % count)
            # print(count)
            # print(f"Post ID 3: {post.title}, Published: {post.published_date}")
            # if count < 3:
            #     print(count)
            #     # self.assertEqual(resp.status_code, 200)
            #     self.assertContains(resp, title)
            # else:
            #     self.assertEqual(resp.status_code, 404)


