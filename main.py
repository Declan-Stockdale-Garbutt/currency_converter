
from currency import check_valid_currency, Currency, extract_api_result
from api import call_api, format_latest_url
import sys

def main():
    ''' Pseudocode
    Code must take between 2 and 3 inputs (from_currency, to_currency, amount)
    Amount is optional but if not given, default is 1.00

    If less than 2, error is given
    If 2 or 3 given, code proceeds and checks occur on the values
        Amount is checked for float and negative value, if not defaults to 1.00
        Given currencies are checked if they're valid

    Given currencies are also converted to uppercase to avoid issues in checking against valid codes

    Check that get_rate_output returns a True before proceeding

    If get_rate_output = True
        get json from call_api on latest_url

        variable = extract_api_result(json dictionary, from_currency, to_currency, amount)

        print(variable) -> returns formatted message

    else
        get_rate_output = False
        error caught in another function
    '''

    if len(sys.argv) <= 2:  # doesn't account for amount
        print("[ERROR] You haven't provided 2 currency codes")
    elif len(sys.argv) >= 5:
        print('[ERROR] Too many input arguments, max inputs is 3')
        print(
            'Please only input: to currency, from currency, amount -> optional default is 1')
    else:
        from_currency = sys.argv[1].upper()
        to_currency = sys.argv[2].upper()

        if len(sys.argv) == 4:  # amount was included
            try:
                amount = float(sys.argv[3])

                if float(sys.argv[3]) <= float(0):
                    print('Amount must be positive, using default value of 1.00')
                    amount = int(1)
            except:
                print('Amount must be a number. Using default of 1.00')
                amount = int(1)

        else:  # catch any other error
            amount = float(1.0)


        get_rate_output = get_rate(from_currency, to_currency, amount)

        if get_rate_output == True:
            format_url_result = format_latest_url(from_currency, to_currency)
            format_api_result = call_api(format_url_result)

            curr_obj = extract_api_result(format_api_result, from_currency, to_currency, amount)

            print(curr_obj)
            pass

        return None


def get_rate(from_currency: str, to_currency: str, amount: float):

    ''' Pseudocode
    Checks if both the currencies are different and valid

    if from_currency = to_currency
        print error

    Else
        check from_currency in list of valid -> return true if in, false if
        check to_currency in list of valid -> return true if in, false if not

    only return true if both currency codes are valid, else return false
    '''
    if from_currency == to_currency:
        print('Currencies are the same -> please enter two different currencies')
        valid_currency = False
    else:
        from_currency_valid = check_valid_currency(from_currency)
        to_currency_valid = check_valid_currency(to_currency)

        if from_currency_valid == False:
            valid_currency = False
        else:
            if to_currency_valid == False:
                valid_currency = False
            else:
                if to_currency_valid == True and from_currency_valid == True:
                    valid_currency = True

        return valid_currency


if __name__ == "__main__":
    main()
