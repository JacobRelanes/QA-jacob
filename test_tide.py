import unittest
from tide import Tide

class TestTide(unittest.TestCase):
    def setUp(self):
        self.tide = Tide(threshold=1.5)

    def test_high_tide(self):
        self.assertTrue(self.tide.is_high_tide(2.0), "2.0 should be high tide")
        self.assertFalse(self.tide.is_high_tide(1.0), "1.0 should not be high tide")

    def test_low_tide(self):
        self.assertTrue(self.tide.is_low_tide(1.0), "1.0 should be low tide")
        self.assertFalse(self.tide.is_low_tide(2.0), "2.0 should not be low tide")

    def test_threshold_value(self):
        self.assertFalse(self.tide.is_high_tide(1.5), "1.5 is not above threshold")
        self.assertFalse(self.tide.is_low_tide(1.5), "1.5 is not below threshold")

if name == "main":
    unittest.main()
