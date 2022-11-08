import unittest
from currency import check_valid_currency, extract_api_result, Currency


class TestValidCurrency(unittest.TestCase):
    def test_check_valid_currency(self):
        '''
        Test check_valid_currency(currency) with a range of conditions
        Only return True or False
        Don't need to test lower case as all inputs will be upper case from main()

        Is there a way to suppress the printed messages in the function?
        '''
        tests = [
            ('AUD', True), # expected
            #('aud', False), # lower case
            ('AUD1', False), # numeric
            ('12312331231', False), # numeric
            ('Australian dollar', False), # string
            (('AUD, USD'), False) # tuple
            ]
        for value, expected in tests:
            with self.subTest(value = value):
                self.assertEqual(check_valid_currency(value), expected)


class TestExtractApi(unittest.TestCase):
    def test_extract_api_result(self):
        '''
        Check currencies work when eur and not eur with amount as a float- > default is float of 1.0 if none given
        Check output is a string

        Works when dictonary is functional
        '''
        tests = [
            ((dict({"amount":1.0,"base":"EUR","date":"2021-09-07","rates":{"USD":1.186}}), 'EUR', 'USD', float(1.0)), str),
            ((dict({"amount":1.0,"base":"EUR","date":"2021-09-07","rates":{"USD":1.186}}), 'USD', 'EUR', float(1.0)), str),
            ((dict({"amount":1.0,"base":"EUR","date":"2021-09-07","rates":{"AUD":1.6044,"USD":1.186}}), 'AUD', 'USD', float(1.0)), str)
            ]
        for value, expected in tests:
            with self.subTest(value = value):
                self.assertIsInstance(extract_api_result(value[0], value[1], value[2], value[3]), expected)

    def test_extract_api_result_missing_values_dictionary(self):
        '''
        Checking it returns False when some values of dictionary are missing
        '''
        tests = [
            ((dict({"amount":1.0,"date":"2021-09-07","rates":{"AUD":1.6044,"USD":1.186}}),"empty",'USD', float(1.0)), False),#,
            ((dict({"amount":1.0,"date":"2021-09-07","rates":{"AUD":'number',"USD":1.186}}), 'AUD', 'USD', float(1.0)), False),
            ((dict({"amount":1.0,"date":"2021-09-07","rates":{"xxx":1.6044,"USD":1.186}}), 'AUD', 'USD', float(1.0)), False),
            ((dict({"amount":1.0,"base":"EUR","rates":{"AUD":1.6044,"USD":1.186}}), "AUD", 'USD', float(1.0)), False),#,
            ((dict({"amount":1.0,"base":"EUR","rates":{""}}), "AUD", 'USD', float(1.0)), False)
            ]
        for value, expected in tests:
            with self.subTest(value = value):
                currency_obj_test = extract_api_result(value[0], value[1], value[2], value[3])
                self.assertEqual(currency_obj_test, expected)
