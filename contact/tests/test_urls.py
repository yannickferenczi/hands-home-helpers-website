from django.test import SimpleTestCase
from django.urls import reverse, resolve

from contact import views


class TestUrls(SimpleTestCase):

    def test_contact_url_is_resolves(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, views.contact)
