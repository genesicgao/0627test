from foo.consumers.base_domain_consumer import BaseDomainConsumer


class GlassDoorConsumer(BaseDomainConsumer):

    job_description_selector = '#JobDescriptionContainer > div:nth-child(1)'
