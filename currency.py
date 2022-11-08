from dataclasses import dataclass
from api import get_currencies, call_api, format_latest_url  # , get_latest_rates

CURRENCIES = get_currencies()

def check_valid_currency(currency):
    ''' Pseudocode

    Takes from_currency or to_currency as input

    Converts input to string

    if input currency is in list of valid currencies
        return True
    else
        print input is not valid
        print list of valid codes from currency keys
        return False
    '''

    currency_valid = str(currency)
    try:
        if currency_valid in CURRENCIES:
            Result = True

        else:
            print(currency_valid + "  is not a valid option")
            print('Please use only the following currency codes:')
            print(*CURRENCIES)
            Result = False
    except:
        Result = False
    return Result


@ dataclass
class Currency(object):
    from_currency: str = None
    to_currency: str = None
    amount: float = 0
    rate: float = 0
    inverse_rate: float = 0
    date: str = None

    def __init__(self, dictionary):
        ''' Pseudocode
        Necessary for class, input of self and the dictionary object for parsing from api
        '''
        pass

    def reverse_rate(self):
        ''' Pseudocode
        Takes the stored rate value and finds the inverse by 1/rates
        Rounds the result to 5 decimal places
        '''
        self.inverse_rate = round((1/self.rate), 5)
        return None

    def format_result(self):
        ''' Pseudocode
        Calculates final_amount if amount entered is not 1.00
        Uses f string to input various values from class

        Return formatted message
        '''


        message = (
            f"Today's ({self.date}) conversion rate from {self.from_currency} to {self.to_currency} is {self.rate}. The inverse rate is {self.inverse_rate}.")

        print('self.amount', self.amount)
        if self.amount != 1.0 or self.amount != 1.00:
            final_amount = round(float((self.amount))*(float(self.rate)), 5)
            message = message + (f" {self.amount} {self.from_currency} is equal to {final_amount} {self.to_currency}")
        return message

def extract_api_result(dictionary, from_currency, to_currency, amount):#, from_currency, to_currency, amount):
    ''' Pseudocode
    call_api() run on format_latest_url() to get json dictionary

    Initiate currency object
    currency_obj = Currency(json dictionary)

    Logic for checking EUR currency as base rate is the EUR

        if from_currency = EUR
            rate = dictionary rate -> as this is the base rate no conversion needed

        if to_currency = EUR
            rate = 1/dicitonary rate as it returns the inverse so we need to convert it

        if Neither = EUR
            to_currency = get dicitonary rate of to_currency
            from_currency = get dicitonary rate of from_currency

    Extracts rate and date fields out of dictionary
    e.g.currency_obj.date = date

    From_currency, to_currency and amount are explicily called from input
    That is because the json result is alphabetical which may not be the case

    currency_obj reverse rate = currency_obj.reverse_rate()

    All fields are now filled

    Format message using f string

    Return formatted message
    '''

    format_url_result = format_latest_url(from_currency, to_currency)
    format_api_result = call_api(format_url_result)
    currency_obj = Currency(format_api_result)


    try: # pick up error during parsing
        if from_currency == 'EUR':
            rate = float(dictionary['rates'][to_currency])

        if to_currency == 'EUR':
            rate = round(
                float(1.0)/float(dictionary['rates'][from_currency]), 5)

        if to_currency != 'EUR' and from_currency != 'EUR':
            to_currency_val = dictionary['rates'][to_currency]
            from_currency_val = dictionary['rates'][from_currency]
            rate = round(float(to_currency_val)
                         / float(from_currency_val), 5)


        currency_obj.date = dictionary['date']
        currency_obj.from_currency = from_currency
        currency_obj.to_currency = to_currency
        currency_obj.amount = amount
        currency_obj.rate = rate
        currency_obj.reverse_rate = currency_obj.reverse_rate()
        currency_obj_message = currency_obj.format_result()

        return currency_obj_message

    except:
        #print('Problem reading from API')
        if currency_obj.date == None or currency_obj.from_currency == None or \
            currency_obj.to_currency == None or currency_obj.amount == float(0) or \
            currency_obj.rate == float(0.0) or currency_obj.reverse_rate == float(0):
            return False
