"""This file tests the URL routes."""
from django.test import TestCase
from django.shortcuts import reverse

from website.users.models import User
from ..models import Article


class UrlTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up the test data."""
        cls.author = User.objects.create(
            username="author",
            email="steven.kruijswijk@teamjumbovisma.com",
            first_name="Steven",
            last_name="Kruijswijk",
        )

        cls.article = Article.objects.create(
            title="Steven haalt het podium in Parijs!",
            author=cls.author,
            content="Kijk, dat is lekker!"
        )

    def test_home_route(self):
        url = reverse("home:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_route(self):
        url = reverse(
            "home:article",
            kwargs={"pk": self.article.pk, "slug": "kruijswijk-op-podium"}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
