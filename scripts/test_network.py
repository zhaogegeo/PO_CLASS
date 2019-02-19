from base import init_driver
from page import Page


class TestNetwork:

    driver, page = None, None

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_network_2g(self):
        self.page.network.click_more()
        self.page.network.click_mobile_network()
        self.page.network.click_first_network()
        self.page.network.click_2g_network()
        assert 1
    def test_network_3g(self):
        self.page.network.click_more()
        self.page.network.click_mobile_network()
        self.page.network.click_first_network()
        self.page.network.click_3g_network()
        assert 1
