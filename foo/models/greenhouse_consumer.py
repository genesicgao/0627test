from foo.models.base_domain_consumer import BaseDomainConsumer


class GreenhouseConsumer(BaseDomainConsumer):

    job_description_selector = 'div[id="app_body"] > div[id="content"]'
