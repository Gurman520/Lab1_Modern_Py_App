import unittest
from unittest.mock import patch
import datetime
import data_app.data as dat


class TestTime(unittest.TestCase):
    @patch('is_past_date', return_value=True)
    def test_true_time(self, is_past_date):
        self.assertEqual(dat.is_past_date(datetime.date(2021, 11, 28)), True)

    @patch('is_past_date', return_value=False)
    def test_false_time(self, is_past_date):
        self.assertEqual(dat.is_past_date(datetime.date(2024, 11, 28)), False)
