from django.test import SimpleTestCase
from django.urls import reverse, resolve

from offers import views


class TestUrls(SimpleTestCase):

    def test_offers_list_url_is_resolves(self):
        url = reverse('offers')
        self.assertEquals(resolve(url).func.view_class, views.OffersListView)
