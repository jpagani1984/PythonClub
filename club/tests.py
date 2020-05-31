from django.test import TestCase
from .models import Product, ProductType, Review
from .views import index, gettypes, getproducts
from django.urls import reverse
from django.contrib.auth.models import User

class MeetingTypeTest(TestCase):
       def test_string(self):
       type=MeetingType(typename="Tablet")
       self.assertEqual(str(type), type.typename)

   def test_table(self):
       self.assertEqual(str(MeetingType._meta.db_table), 'meetingtype')

class ReviewTest(TestCase):
       def test_string(self):
       rev=Review(reviewtitle="Best Review")
       self.assertEqual(str(rev), rev.reviewtitle)

   def test_table(self):
       self.assertEqual(str(Review._meta.db_table), 'reviews')

class IndexTest(TestCase):
       def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
  
class GetProductsTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('products'))
       self.assertEqual(response.status_code, 200)
def test_discount(self):
        discount=self.prod.memberdiscount()
        self.assertEqual(discount, 25.00)

    def test_number_of_reviews(self):
        reviews=Review.objects.filter(meeting=self.meeting).count()
        self.assertEqual(reviews, 2)