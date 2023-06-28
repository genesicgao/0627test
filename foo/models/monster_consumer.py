from foo.models.base_domain_consumer import BaseDomainConsumer


class MonsterConsumer(BaseDomainConsumer):

    job_description_selector = '#jobview-container > div:nth-child(1) > div:nth-child(1)'
