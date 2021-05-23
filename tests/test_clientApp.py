import pytest
import sys
sys.path.insert(0, './colmore/')

from app import app as ClientApp

clientApp = ClientApp.ClientApp()

def test_authenticate():
    assert clientApp.authenticate('test') == True

def test_symbol_search():
    assert clientApp.symbol_search('TL') != None

def test_place_get_api_request():
    assert clientApp._place_get_api_request('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo').status_code == 200

