"""
This module consist of the library function that would return the latest foreign exchange reference rates.
Query parameters:
-> base
-> symbols

Based on public api : https://ratesapi.io/documentation/
"""
from rest_client.client import HTTPClient


class GetData(object):
    def __init__(self):
        self.client = HTTPClient(base_url="https://api.ratesapi.io/api/")

    def get_latest_data(self, symbols=None, base=None):
        """

        :param symbols: Request specific exchange rates by setting the symbols parameter.
        :type symbols: str

        :param base: Rates are quoted against the Euro by default. Quote against a different
                        currency by setting the base parameter in your request.
        :type symbols: str

        :return: json response
        """
        params = {"symbols": symbols, "base": base}
        resp = self.client.get("latest", params=params)
        if resp.get("error"):
            return resp.get("error")
        else:
            return resp["rates"][symbols]


    def get_timestamp_data(self, date, symbols=None, base=None):
        """

        :param date: Get historical rates for any day since 1999.
        :type date: str in "yyyy-dd-mm" format

        :param symbols: Request specific exchange rates by setting the symbols parameter.
        :type symbols: str

        :param base:
        :type symbols: str

        :return: json response
        """
        params = {"symbols": symbols, "base": base}
        resp = self.client.get(date, params=params)
        if resp.get("error"):
            return resp.get("error")
        else:
            return resp["rates"][symbols]


if __name__ == '__main__':
    g = GetData()
    ret = g.get_latest_data("GBP", "USD")
    print ret
    ret = g.get_timestamp_data("2010-01-12", "GBP", "USD")
    print ret
