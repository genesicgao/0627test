import scrapy
from pyppeteer.page import Page

from foo.models.domain_factory import DomainConsumerFactory
from foo.utils.url_util import get_urls
from foo.utils.log_util import logger
from gerapy_pyppeteer import PyppeteerRequest
import asyncio


class FooSpider(scrapy.Spider):
    name = "foo"
    allowed_domains = ["*"]

    custom_settings = {
        'GERAPY_PYPPETEER_HEADLESS': False
    }

    def start_requests(self):
        for url in get_urls():
            yield PyppeteerRequest(url,
                                   wait_until='domcontentloaded',
                                   callback=self.parse_html,
                                   dont_filter=True,
                                   actions=pre_response)

    def parse_html(self, response):
        ...


async def pre_response(page: Page):
    # await asyncio.sleep(10) # 先等30s，应对需要跳转的情况
    consumer = DomainConsumerFactory.get_consumer(page)
    if consumer:
        description = await consumer.get_job_description()
        logger.info(description)