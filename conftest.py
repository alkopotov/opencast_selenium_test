import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--browser', default='chrome'
    )
    parser.addoption(
        '--headless', action='store_true'
    )
    parser.addoption(
        '--base_url', default='http://localhost'
    )


@pytest.fixture()
def base_url(request):
    return request.config.getoption('--base_url')


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')

    service = Service()

    options = Options()

    if headless:
        options.add_argument('headless=new')
    browser = webdriver.Chrome(service=service, options=options)
    options = Options()
    options.headless = headless

    yield browser
    time.sleep(1)
    browser.close()
