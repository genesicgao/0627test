import scrapy
from pyppeteer.page import Page

from foo.consumers.domain_factory import DomainConsumerFactory
from foo.items import FooItem
from foo.utils.url_util import get_urls
from foo.utils.log_util import logger
from gerapy_pyppeteer import PyppeteerRequest
import asyncio


class FooSpider(scrapy.Spider):
    name = "foo"
    allowed_domains = ["*"]

    def start_requests(self):
        for url_row in get_urls():
            yield PyppeteerRequest(url_row.get('url'),
                                   wait_until='domcontentloaded',
                                   callback=self.parse_html,
                                   dont_filter=True,
                                   actions=pre_response,
                                   meta={'index': url_row.get('index')})

    def parse_html(self, response):
        consumer = DomainConsumerFactory.get_consumer(response)
        index = response.meta['index']
        if consumer:
            description = consumer.get_job_description()
            yield FooItem(index=index,
                          url=response.url,
                          live=not not description,
                          job_description=description)


async def pre_response(page: Page):
    await asyncio.sleep(10) # 先等10s，应对需要跳转的情况
