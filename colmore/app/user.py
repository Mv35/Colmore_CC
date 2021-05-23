import requests


class User(object):
    def __init__(self, auth_key=None):

        self._auth_key = auth_key

        print('User:', self._auth_key)

    def isValid(self):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={self._auth_key}"
        response = requests.get(
            url
        )
        if 'Error Message' not in response.json():
            return True
