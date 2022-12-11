# Currency converter

## Author

**Declan Stockdale-Garbutt**

## Description
Converting between two currencies using the frankfurter api (https://api.frankfurter.app)
Use currency codes e.g. AUD, EUR, USD etc not Australian dollar, United States dollar 

## Available Commands

In the project directory, you can run: 

### `python main.py AUD EUR (amount-> is optional, default is 1.00)`,

If you are using Pipenv, then you can run:

### `pipenv python main.py AUD EUR (amount-> is optional, default is 1.00)`,

## Built With

- Python

## Package Dependencies

- requests
- os

## Structure

    ├── api.py             <- Formats api for latest and currency list. Also contains function to call api and get list of valid currencies
    ├── currency.py        <- Check input currencies are valid. Parses dictionary data and creates a currency object with relevant data
    ├── main.py            <- Takes input and converts to proper format. Also checks that input currencies are different 
    ├── Pipfile            <- List of required packages. Only need os and requests
    ├── Pipfile.lock       <- Decribes specific versions of the required packages, displays any mismatches in pipfile compared to current env
    ├── README.md          <- Description of package
    ├── test_api.py        <- unit testing of api.py
    └── test_currency.py   <- unit testing of currency.py


## Errors that it catches
1. No internet 			     -> There is an error with API call
2. Api not available or error in url -> There is an error with API call
3. Input currency is invalid	     -> AAA is not a valid option please use the following list
4. Input currencies are the same     -> Currencies are the same -> please enter two different currencies
5. Less than 2 inputs 		     -> [ERROR] You haven't provided 2 currency codes
6. More than 5 input		     -> [ERROR] Too many input arguments, max inputs is 3
7. If no amount is given	     -> uses amount of 1.00

## Examples of output

python main.py AUD EUR 25

![image](https://user-images.githubusercontent.com/53500810/206885579-80c4f18d-b351-49cf-98fe-2ba144b39958.png)

python main.py AUD EUR -100

![image](https://user-images.githubusercontent.com/53500810/206885603-bb72e698-4473-4f4a-89ae-72f857e781ea.png)

python main.py AUD AUD 10

![image](https://user-images.githubusercontent.com/53500810/206885622-93f1e97f-29a4-45a9-997c-395d487fca01.png)

python main.py AUASDASDSA AUD 10

![image](https://user-images.githubusercontent.com/53500810/206885640-8afa8d35-6d97-42f1-9cd8-12a3a08b8303.png)



