from foo.models.base_domain_consumer import BaseDomainConsumer


class BebeeConsumer(BaseDomainConsumer):

    job_description_selector = '#jobs-content > div.nf-job-list-desc-box > div'
