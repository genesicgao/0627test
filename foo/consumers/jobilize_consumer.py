from foo.consumers.base_domain_consumer import BaseDomainConsumer


class JobilizeConsumer(BaseDomainConsumer):

    job_description_selector = 'div.job-detail'
