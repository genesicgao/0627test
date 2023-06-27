import scrapy
from pyppeteer.page import Page

from foo.utils.url_util import get_urls
from gerapy_pyppeteer import PyppeteerRequest


class FooSpider(scrapy.Spider):
    name = "foo"
    allowed_domains = ["*"]

    custom_settings = {
        'GERAPY_PYPPETEER_HEADLESS': False
    }

    def start_requests(self):
        for url in get_urls():
            yield PyppeteerRequest(url,
                                   callback=self.parse_html,
                                   dont_filter=True,
                                   actions=pre_response)

    def parse_html(self, response):
        self.logger.info(response.text)


async def pre_response( page: Page):
    await page.waitFor('body')