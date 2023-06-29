import asyncio

from pyppeteer.page import Page

from foo.consumers.adzuna_consumer import AdzunaConsumer
from foo.consumers.base_domain_consumer import BaseDomainConsumer
from foo.consumers.bebee_consumer import BebeeConsumer
from foo.consumers.careerbuilder_consumer import CareerbuilderConsumer
from foo.consumers.glassdoor_consumer import GlassDoorConsumer
from foo.consumers.greenhouse_consumer import GreenhouseConsumer
from foo.consumers.jobilize_consumer import JobilizeConsumer
from foo.consumers.linkedin_consumer import LinkedinConsumer
from foo.consumers.monster_consumer import MonsterConsumer
from foo.consumers.lensa_consumer import LensaConsumer
from foo.consumers.osceolaschools_consumer import OsceolaschoolsConsumer
from foo.consumers.startwire_consumer import StartwireConsumer
from foo.consumers.talent_consumer import TalentConsumer
from foo.consumers.teksystems_consumer import TeksystemsConsumer
from foo.consumers.wayup_consumer import WayupConsumer
from foo.consumers.ziprecruiter_consumer import ZiprecruiterConsumer
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
    def get_consumer(cls, response) -> BaseDomainConsumer:
        url = response.url
        domain = urlparse(url).netloc
        consumer = None
        ConsumerObj = CONSUMER_MAP.get(domain)
        if ConsumerObj:
            consumer = ConsumerObj(response)
        return consumer