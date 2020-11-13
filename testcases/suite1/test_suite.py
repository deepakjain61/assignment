from lib.rates import GetData

g = GetData()

"""
Public api: https://ratesapi.io/documentation/

Following test cases(14) are covered:

test_latest_data: It covers 3 test cases with different data sets for "Latest" api
test_timestamp_data: It covers 3 test cases with different data set for "Timestamp" api
test_negative_scenarios_latest_data: Covers 4 negative scenarios for "Latest" api
test_negative_scenarios_timestamp_data: Covers 4 negative scenarios for "Timestamp" api
"""


def test_latest_data(config_data):
    """
    This test reads the config.json file and will run for all the key value pairs written for the dictionary with
    key "test_latest_data".
    It makes the query to the product api with symbols and base as the parameters and verify the return value against
    the one mentioned in the json file.
    """
    assert config_data["expected_value"] == g.get_latest_data(config_data["symbols"], config_data["base"])


def test_timestamp_data(config_data):
    """
    This test reads the config.json file and will run for all the key value pairs written for the dictionary with
    key "test_timestamp_data".
    It makes the query to the product api with symbols,base and date as the parameters and verify the return value
    against
    the one mentioned in the json file.
    """
    assert config_data["expected_value"] == g.get_timestamp_data(config_data["date"], config_data["symbols"],
                                                                 config_data["base"])


def test_negative_scenarios_latest_data(config_data):
    """
    This test reads the config.json and will run for the key value pairs written for the dictionary with
    key "test_negative_scenarios_latest_data".
    This test covers all the negative scenarios for latest data api and check if the errors are handled properly.
    For eg:
    Is the error handled for the "symbol" or "base" which does not exist

    """
    assert config_data["expected_error"] in g.get_latest_data(config_data["symbols"], config_data["base"])


def test_negative_scenarios_timestamp_data(config_data):
    """
    This test reads the config.json and will run for the key value pairs written for the dictionary with
    key "test_negative_scenarios_timestamp_data".
    This test covers all the negative scenarios for latest data api and check if the errors are handled properly.
    For eg:
    Check for the date where the mentioned base or symbol didn't exist

    """
    assert config_data["expected_error"] in g.get_timestamp_data(config_data["date"], config_data["symbols"],
                                                                 config_data["base"])
