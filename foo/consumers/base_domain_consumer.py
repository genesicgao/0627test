from pyppeteer.page import Page
from pyquery import PyQuery as pq
from foo.utils.log_util import logger
from scrapy import Selector

class BaseDomainConsumer(object):

    response = None
    selector = None
    expire_content_selector = None
    job_description_selector = None

    def __init__(self, response):
        self.response = response

    def get_job_description(self):
        job_description_content = pq(self.response.text)(self.job_description_selector)
        if job_description_content:
            logger.info(job_description_content.text())
            return job_description_content.text()

    async def get_job_skill(self):
        ...

    async def get_job_level(self):
        ...