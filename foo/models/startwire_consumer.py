from foo.models.base_domain_consumer import BaseDomainConsumer


class StartwireConsumer(BaseDomainConsumer):

    job_description_selector = 'main > div > div > div > div:nth-child(1) > div:nth-child(2)'
