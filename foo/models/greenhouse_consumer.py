from foo.models.base_domain_consumer import BaseDomainConsumer


class GreenhouseConsumer(BaseDomainConsumer):

    job_description_selector = 'div[#app_body] > div[#content]'
