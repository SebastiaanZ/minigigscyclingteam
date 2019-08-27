"""This file tests the URL routes."""
from django.test import TestCase
from django.shortcuts import reverse


class UrlTests(TestCase):
    def test_home_route(self):
        url = reverse("home:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
