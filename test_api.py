import unittest
from api import call_api, format_currencies_url, get_currencies, format_latest_url, _HOST_, _LATEST_, _CURRENCIES_


class TestFormatUrl(unittest.TestCase):
    def test_format_currencies_url(self):
        self.assertEqual(str(_HOST_+_CURRENCIES_), format_currencies_url())

    def test_format_latest_url(self):
        '''
        Test whether from_currency and to_currency return valid results from formated_latest_url
        Testing if same, that it returns none
        Testing if case sensitive should return string
        '''
        tests = [
            (('usd', 'usd'), None),
            (('USD', 'USD'), None),
            (('USD', 'AUD'), _HOST_+_LATEST_+"?to=USD,AUD"),
            (('usd', 'aud'), _HOST_+_LATEST_+"?to=USD,AUD"),
            (('USD', 'AUD'), "https://api.frankfurter.app/latest?to=USD,AUD"),
            (('usd', 'aud'), "https://api.frankfurter.app/latest?to=USD,AUD")]

        for value, expected in tests:
            with self.subTest(value = value):
                self.assertEqual(format_latest_url(value[0], value[1]), expected)


class TestAPI(unittest.TestCase):
    def test_call_api(self):
        '''
        Api works with numeric values which are caught in main() so don't need to test here

        Testing that given format_latest_url in expected format and
        format_currencies_url gives expected returns

        Only returns false if api connection doesn't work
        '''
        tests = [
            ("https://api.frankfurter.app/latest?to=USD,AUD", False),
            (format_currencies_url(), False)
            ]
        for value, expected in tests:
            with self.subTest(value = value):
                self.assertIsNot(call_api(value), expected)

    def test_call_api_json_dict(self):
        test_var = format_currencies_url()
        self.assertIsInstance(call_api(test_var), dict)

    def test_call_api_empty_url(self):
        self.assertEqual(call_api(""), False)

class TestGetCurrencies(unittest.TestCase):
    def test_get_currencies_expected(self):
        self.assertIsInstance(get_currencies(), list)

    def test_get_currencies_expected(self):
        self.assertEqual(call_api(""), False)
