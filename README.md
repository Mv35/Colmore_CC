#Colmore Coding Challenge


##Simple Flask Frontend with the following features:
1. User provides its own (AlphaVenture) API key that is remembered for the session 
2. User can search specific company using
https://www.alphavantage.co/documentation/#symbolsearch and display results that match selection criteria in select list.
3. User can select a company from the list and display additional details in a table such as:
symbol, name, type, region, marketOpen, marketClose, timezone, currency, matchScore

###Requirements:
* Python3.8 or
* Docker

###Instructions:
#### With Virtual Environment
* Clone or download the repo
* Navigate inside `Colmore_CC` directory
* `python3.8 -m venv env`
* `source env/bin/activate`
* `pip install --no-cache-dir -r requirements.txt`
* `python colmore/main.py`
* Go to `http://localhost:5000`

To run tests: `pytest -vs`

#### With Docker
* `docker build . -t colmoretest`
* `docker run -p 127.0.0.1:5000:5000 -it colmoretest`
* Go to `http://localhost:5000`




*Please note that everything but in particular elements such as Login/Authentication and Aesthetics have been kept extremly simple and with demostrative purposes in mind*