from foo.models.base_domain_consumer import BaseDomainConsumer


class CareerbuilderConsumer(BaseDomainConsumer):

    job_description_selector = '#jdp_description > div.col-2 > div.col.big.col-mobile-full.jdp-left-content'
