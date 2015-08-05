from django.test import TestCase
import views
import models

# Testing that the views render properly
class ViewsTests(TestCase):
  def test_index(self):
    resp = self.client.get('/')
    self.assertEqual(resp.status_code, 200)
    self.assertContains(resp, "Welcome to Chrysalis")

  def test_summary(self):
    resp = self.client.get('/stock_summary/aapl')
    self.assertEqual(resp.status_code, 200)
    # Checks that the api request goes through without problem
    self.assertContains(resp, "Apple Inc.")

# Tests that the form submits properly
class FormTests(TestCase):
  def test_submit(self):
    resp = self.client.post('/stock_summary/', {'symbol': 'msft'})
    self.assertEqual(resp.status_code, 200)
        # Checks that the submission goes through without problem
    self.assertContains(resp, "Microsoft")


