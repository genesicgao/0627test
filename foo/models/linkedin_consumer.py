from foo.models.base_domain_consumer import BaseDomainConsumer


class LinkedinConsumer(BaseDomainConsumer):

    job_description_selector = 'section.core-section-container > div > div > section > div'
