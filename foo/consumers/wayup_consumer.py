from foo.consumers.base_domain_consumer import BaseDomainConsumer


class WayupConsumer(BaseDomainConsumer):

    job_description_selector = '#root > div > div:nth-child(3) > div > div:nth-child(4) > div'
