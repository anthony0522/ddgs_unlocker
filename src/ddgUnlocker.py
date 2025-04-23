from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from .settings import PREFS


class ddgsUnlocker:
    def __init__(self, _server=None, HEADLESS=True):
        opts = self.__get_options()
        service = Service(executable_path=ChromeDriverManager().install())
        self._driver = webdriver.Chrome(
            options=opts,
            service=service,
        )
        self.server = _server
        self._driver.implicitly_wait(1)

    def quit(self):
        self._driver.quit()
        return
    
    def __get_options(HEADLESS : bool) -> webdriver.ChromeOptions:
        opts = webdriver.ChromeOptions()
        if HEADLESS:
            opts.add_argument("--headless")
        opts.add_argument("--disable-notifications")
        opts.add_experimental_option("prefs", PREFS)
        ua_string = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
        opts.add_argument(f"--user-agent={ua_string}")

        return opts

    def ddg_search(self):
        self._driver.get("https://duckduckgo.com/?t=h_&q=web&ia=web")
        self._driver.implicitly_wait(1)
        search_box = self._driver.find_element("name", "q")
        search_box.send_keys("site:google.com")
        search_box.submit()
        self._driver.implicitly_wait(1)
        return