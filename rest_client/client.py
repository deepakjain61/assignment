import requests
from logger import Logger

"""
This module is responsible for creating the http client that would be used by the library functions to call the
exposed public apis
"""


class HTTPClient(Logger):
    def __init__(self, payload=None, log_path="logs", base_url=None, headers=None):
        # initialize the logger
        super(HTTPClient, self).__init__(log_path=log_path)
        self.base_url = "https://api.ratesapi.io/api/" if base_url is None else base_url
        self.headers = {'Content-Type': 'application/json'} if headers is None else headers
        self.payload = payload

    def pretty_print_request(self, request):
        """
        :param request: request object to pretty print the request in log file
        :return: None
        """
        self.log.info('\n{}\n{}\n\n{}\n\n{}\n'.format(
            '-----------Request----------->',
            request.method + ' ' + request.url,
            '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
            request.body)
        )

    def pretty_print_response(self, response):
        """
        :param response:  response object to pretty print the response in log file
        :return:
        """
        self.log.info('\n{}\n{}\n\n{}\n\n{}\n'.format(
            '<-----------Response-----------',
            'Status code:' + str(response.status_code),
            '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
            response.text)
        )

    def get(self, suffix, params=None):
        """

        :param url: Rest URI
        :param params: qyery parameters
        :return: response in json
        """
        url = self.base_url + suffix
        self.log.info("Running the get query {} with params {}".format(url, params))
        try:
            response = requests.get(url, params=params, headers=self.headers)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)
        self.pretty_print_request(response.request)
        self.pretty_print_response(response)
        json_response = response.json()
        return json_response

    def post(self, suffix, payload=None, params=None):
        """

        :param url: Rest URI
        :param payload: payload for the post query
        :param params: query parameters
        :return: response in json
        """
        url = self.base_url + suffix
        self.log.info("Running the post query {} with params {} and payload {}".format(url, params, payload))
        try:
            response = requests.post(url, params=params, payload=self.payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        self.pretty_print_request(response.request)
        self.pretty_print_response(response)
        json_response = response.json()
        return json_response

    def put(self, suffix, payload=None, params=None):
        """

        :param url: Rest URI
        :param payload: payload for the post query
        :param params: query parameters
        :return: response in json
        """
        url = self.base_url + suffix
        self.log.info("Running the put query {} with params {} and payload {}".format(url, params, payload))
        try:
            response = requests.post(url, params=params, payload=self.payload)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        self.pretty_print_request(response.request)
        self.pretty_print_response(response)
        json_response = response.json()
        return json_response


if __name__ == '__main__':
    client = HTTPClient()
    suffix = "latest"
    params = {"base":None, "symbols":None}
    a = client.get(suffix, params=params)
    print a
