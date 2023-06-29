from foo.consumers.base_domain_consumer import BaseDomainConsumer


class OsceolaschoolsConsumer(BaseDomainConsumer):

    job_description_selector = '#job-detail > div:nth-child(4) > div > div > div.main-content > div.job-body > div'
