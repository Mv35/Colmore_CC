import requests
import readline

from .user import User


class ClientApp():
    def __init__(self):
        """init method of ClientApp Class
        """
        self._user = None

    def authenticate(self, auth_key=None):
        """Method to authenticate the user.
        Made only for the purpose of this test.
        A proper authentication method should be used.

        Args:
            auth_key ([string], optional): [description]. Defaults to None.

        Returns:
            [True]: [if authkey is valid for user]
        """
        user = User(auth_key)
        if user:
            if user.isValid():
                self._user = user
                return True

    def symbol_search(self, keyword):
        """Method to perform sybol search on alphavantage API

        Args:
            keywords ([string]): [keyword]

        Returns:
            [dict]: [response json]
        """
        url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={self._user._auth_key}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        #print(response_json['bestMatches'])
        return response_json['bestMatches']

    def _place_get_api_request(self, url):
        """Method to place GET API request

        Args:
            url ([str]): [url]

        Returns:
            [response]: [response object]
        """
        response = requests.get(
            url
        )

        return response

    def _place_post_api_request(self, url, data):
        """Method to place POST API request

        Args:
            url ([str]): [url]
            data ([dict]): [information to pass]

        Returns:
            [response]: [response object]
        """
        response = requests.post(
            url,
            data=data
        )
        return response
