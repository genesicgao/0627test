from foo.consumers.base_domain_consumer import BaseDomainConsumer


class TeksystemsConsumer(BaseDomainConsumer):

    job_description_selector = 'div.jd-info.au-target'
