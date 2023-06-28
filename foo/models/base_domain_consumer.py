from pyppeteer.page import Page
from pyquery import PyQuery as pq
from foo.utils.log_util import logger

class BaseDomainConsumer(object):

    page = None
    expire_content_selector = None
    job_description_selector = None

    def __init__(self, page: Page):
        self.page = page

    async def get_content_pq(self, selector: str):
        content = await self.page.querySelector(selector)
        if content:
            return pq(await self.page.content())(selector)

    async def get_job_description(self):
        job_description_content = await self.get_content_pq(self.job_description_selector)
        if job_description_content:
            logger.info(job_description_content.text())
            return job_description_content.text()

    async def get_job_skill(self):
        ...

    async def get_job_level(self):
        ...