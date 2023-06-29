from foo.consumers.base_domain_consumer import BaseDomainConsumer


class TalentConsumer(BaseDomainConsumer):

    job_description_selector = 'body > main > div > div.card.job > div.job__description'
