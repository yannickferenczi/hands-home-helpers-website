from django.test import SimpleTestCase
from django.urls import reverse, resolve

from config import views


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, views.index)

    def test_about_url_is_resolves(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, views.about)
