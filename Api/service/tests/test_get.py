import os
import sys
# To run from cmd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import uuid
from django.test import Client

from service import models


class TestGet(unittest.TestCase):
    """Test Get endpoint"""
    def setUp(self):
        """Use django test client"""
        self.client = Client()
        self.test_name = 'test%s' % str(uuid.uuid4())[0:8]
        self.test_email = 'test%s@test.com' % str(uuid.uuid4())[0:8]

        self.valid_data = {
            "name": self.test_name,
            "phone": "1234567891",
            "email": self.test_email,
            "arrival_time": "2021-01-06(01:41:49)",
            "departure_time": "2021-01-21(01:41:55)",
            "note": "Some note"
        }

    def test_get_all(self):
        """Test all bookings returned"""
        self.client.post('/api/booking/create/', data=self.valid_data, content_type='application/json')
        response = self.client.get('/api/booking/')
        self.assertIn(self.test_email, str(response.content), 'Expected email not found in response')

    def test_get_single(self):
        """Test single booking is returned"""
        self.client.post('/api/booking/create/', data=self.valid_data, content_type='application/json')
        response = self.client.get('/api/booking/'+self.test_email)
        self.assertIn(self.test_name, str(response.content), 'Expected name not found in response')

    def tearDown(self):
        models.Booking.objects.filter(email=self.test_email).delete()


if __name__ == '__main__':
    unittest.main()