from django.test import SimpleTestCase
from django.urls import reverse, resolve

from reviews import views


class TestUrls(SimpleTestCase):

    def test_add_review_url_is_resolves(self):
        url = reverse('add_review')
        self.assertEquals(resolve(url).func.view_class, views.ReviewCreateView)

    def test_update_review_url_is_resolves(self):
        url = reverse('update_review', args=[1])
        self.assertEquals(resolve(url).func.view_class, views.ReviewUpdateView)

    def test_delete_review_url_is_resolves(self):
        url = reverse('delete_review', args=[1])
        self.assertEquals(resolve(url).func.view_class, views.ReviewDeleteView)
