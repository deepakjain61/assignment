import json
import pathlib
import pytest


@pytest.fixture(scope="class")
def test_config(request):
    f = pathlib.Path(request.node.fspath.strpath)
    config = f.with_name("config.json")
    with config.open() as fd:
        test_data = json.loads(fd.read())
    yield test_data


@pytest.fixture(scope="function")
def config_data(request, test_config):
    test_data = test_config
    test = request.function.__name__
    if test in test_data:
        test_args = test_data[test]
        yield test_args
    else:
        yield {}


def pytest_generate_tests(metafunc):
    if 'config_data' not in metafunc.fixturenames:
        return
    config = pathlib.Path(metafunc.module.__file__).with_name('config.json')
    with open(str(config)) as f:
        test_data = json.load(f)
    param = test_data.get(metafunc.function.__name__, None)
    if isinstance(param, list):
        metafunc.parametrize('config_data', param)