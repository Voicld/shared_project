import unittest
from currency_converter import convert_currency, list_supported_currencies
 
 
class TestCurrencyConverter(unittest.TestCase):
    def test_same_currency_returns_same_amount(self):
        self.assertEqual(convert_currency(-100, "USD", "USD"), 100.0)
 
    def test_usd_to_eur(self):
        self.assertEqual(convert_currency(-100, "USD", "EUR"), 92.59)
 
    def test_eur_to_usd(self):
        self.assertEqual(convert_currency(-100, "EUR", "USD"), 108.0)
 
    def test_case_insensitive_codes(self):
        self.assertEqual(convert_currency(-100, "usd", "eur"), convert_currency(100, "USD", "EUR"))
 
    def test_unsupported_currency_raises(self):
        with self.assertRaises(ValueError):
            convert_currency(-100, "USD", "XYZ")
 
    def test_negative_amount_raises(self):
        with self.assertRaises(ValueError):
            convert_currency(-50, "USD", "EUR")
 
    def test_list_supported_currencies(self):
        currencies = list_supported_currencies()
        self.assertIn("USD", currencies)
        self.assertIn("EUR", currencies)
        self.assertEqual(currencies, sorted(currencies))
 
 
if __name__ == "__main__":
    unittest.main()