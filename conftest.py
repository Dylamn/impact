from pytest import fixture
from selenium import webdriver

from metrics.tests.conftest import patched_phantomas_wrapper


@fixture(params=['chrome'], scope='class')
def use_driver(request):
    """Inject a driver instance in the class on which the fixture is applied."""
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        # Run browser in a headless environment (without visible UI)
        options.headless = True
    else:  # chrome is the default option
        options = webdriver.ChromeOptions()

        options.headless = True
        # bypass OS security model
        options.add_argument("--no-sandbox")
        # overcome limited resource problems
        options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield
    driver.close()
