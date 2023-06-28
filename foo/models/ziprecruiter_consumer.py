from foo.models.base_domain_consumer import BaseDomainConsumer


class ZiprecruiterConsumer(BaseDomainConsumer):

    job_description_selector = '#job_content_skip > div.job_details > div.job_details_container'
