from pyppeteer.page import Page

from foo.models.adzuna_consumer import AdzunaConsumer
from foo.models.base_domain_consumer import BaseDomainConsumer
from foo.models.bebee_consumer import BebeeConsumer
from foo.models.careerbuilder_consumer import CareerbuilderConsumer
from foo.models.glass_door_consumer import GlassDoorConsumer
from foo.models.jobilize_consumer import JobilizeConsumer
from foo.models.monster_consumer import MonsterConsumer
from foo.models.lensa_consumer import LensaConsumer
from foo.models.talent_consumer import TalentConsumer
from foo.models.teksystems_consumer import TeksystemsConsumer
from foo.models.ziprecruiter_consumer import ZiprecruiterConsumer
from foo.utils.log_util import logger
from urllib.parse import urlparse


CONSUMER_MAP = {
    'www.glassdoor.com': GlassDoorConsumer,
    'www.monster.com': MonsterConsumer,
    'lensa.com': LensaConsumer,
    'www.careerbuilder.com': CareerbuilderConsumer,
    'www.jobilize.com': JobilizeConsumer,
    'us.bebee.com': BebeeConsumer,
    'www.adzuna.com': AdzunaConsumer,
    'www.talent.com': TalentConsumer,
    'www.ziprecruiter.com': ZiprecruiterConsumer,
    'careers.teksystems.com': TeksystemsConsumer
}


class DomainConsumerFactory:

    @classmethod
    def get_consumer(cls, page: Page) -> BaseDomainConsumer:
        url = page.url
        domain = urlparse(url).netloc
        consumer = None
        ConsumerObj = CONSUMER_MAP.get(domain)
        if ConsumerObj:
            consumer = ConsumerObj(page)
        return consumer