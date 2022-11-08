import requests
import os

_HOST_ = 'https://api.frankfurter.app'
_CURRENCIES_ = '/currencies'
_LATEST_ = '/latest'

def call_api(url):
    '''
    Pseudocode
    - Try loop to catch API and internet connection issue

    request.get(url) to access url
        if status code == 200 -> valid
            return json of url
        Else
            return False -> url is invalid or issues connecting
    '''

    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            return False
    except:
        return False


def format_currencies_url():
    '''
    Pseudocode
    concats _HOST_ and _CURRENCIES_
    returns formatted_url as string
    '''
    formatted_url = str(_HOST_+_CURRENCIES_)
    return formatted_url

def format_latest_url(from_currency, to_currency):
    '''
    Pseudocode

    Takes both currency inputs and converts both to strings

    if from_currency is the same as to_currency
        print error saying they must be different
    Else
        format url with from_currency and to_currency
        return latest_price_url as a string
    '''

    from_currency = str(from_currency.upper())
    to_currency = str(to_currency.upper())

    if from_currency == to_currency:
        return None

    else:
        latest_price_url = str(_HOST_+_LATEST_+'?to='
                               + from_currency+','+to_currency)
        return latest_price_url


def get_currencies():
    ''' Pseudocode
    variable_1 =  format_currencies_url() to get url
    call_api(variable_1) to get json dicitonary of valid codes

    if problem accessing api
        print ERROR
        return false

    Else
        dicitonary has both items and keys only want keys
        currency_codes = dictionary keys
        valid_currency_codes = list(keys) -> valid currency codes
    '''
    initial_currency_check = format_currencies_url()
    currency_url = call_api(initial_currency_check)

    if currency_url == False:
        print('There is an error with API call')
        return False
    else:
        list_currencies = currency_url
        currency_codes = list_currencies.keys()
        valid_currency_codes = list(currency_codes)
        return valid_currency_codes
