import os
import sys
# To run from cmd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import uuid
from django.test import Client

from service import models


class TestPost(unittest.TestCase):
    """Test post end point"""
    def setUp(self):
        """Use django test client"""
        self.client = Client()
        self.test_name = 'test%s' % str(uuid.uuid4())[0:8]
        self.test_email = 'test%s@test.com' % str(uuid.uuid4())[0:8]
        self.invalid_data = {
            "name": self.test_name,
            "phone": "wrongphone",
            "email": "thiswrongemail",
            "arrival_time": "",
            "departure_time": "",
            "note": ""
        }

        self.valid_data = {
            "name": self.test_name,
            "phone": "1234567891",
            "email": self.test_email,
            "arrival_time": "2021-01-06(01:41:49)",
            "departure_time": "2021-01-21(01:41:55)",
            "note": "Some note"
        }

    def test_post_invalid_data(self):
        """Post invalid data to the end point"""
        response = self.client.post('/api/booking/create/', self.invalid_data)
        self.assertEqual(response.status_code, 400, 'Status code not matches')

    def test_post_valid_data(self):
        """Post valid data to the end point"""
        response = self.client.post('/api/booking/create/', data=self.valid_data, content_type='application/json')
        self.assertEqual(response.status_code, 200, 'Status code not matches')

        new_booking = models.Booking.objects.get(email=self.test_email)
        self.assertEqual(new_booking.name, self.test_name, 'Expected name not matches')

    def tearDown(self):
        models.Booking.objects.filter(email=self.test_email).delete()


if __name__ == '__main__':
    unittest.main()