import asyncio

from pyppeteer.page import Page

from foo.models.adzuna_consumer import AdzunaConsumer
from foo.models.base_domain_consumer import BaseDomainConsumer
from foo.models.bebee_consumer import BebeeConsumer
from foo.models.careerbuilder_consumer import CareerbuilderConsumer
from foo.models.glassdoor_consumer import GlassDoorConsumer
from foo.models.greenhouse_consumer import GreenhouseConsumer
from foo.models.jobilize_consumer import JobilizeConsumer
from foo.models.linkedin_consumer import LinkedinConsumer
from foo.models.monster_consumer import MonsterConsumer
from foo.models.lensa_consumer import LensaConsumer
from foo.models.osceolaschools_consumer import OsceolaschoolsConsumer
from foo.models.startwire_consumer import StartwireConsumer
from foo.models.talent_consumer import TalentConsumer
from foo.models.teksystems_consumer import TeksystemsConsumer
from foo.models.wayup_consumer import WayupConsumer
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
    'careers.teksystems.com': TeksystemsConsumer,
    'www.linkedin.com': LinkedinConsumer,
    'www.startwire.com': StartwireConsumer,
    'www.wayup.com': WayupConsumer,
    'boards.greenhouse.io': GreenhouseConsumer,
    'jobs.osceolaschools.net': OsceolaschoolsConsumer
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