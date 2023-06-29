from foo.consumers.base_domain_consumer import BaseDomainConsumer


class LensaConsumer(BaseDomainConsumer):

    job_description_selector = '#svelte-root > div.job-details > div.job-details-container > div.job-details-main > div.job-details-content > div.job-details-tab-container > div > section > div:nth-child(1) > div'
