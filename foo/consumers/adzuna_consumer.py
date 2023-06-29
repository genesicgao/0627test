from foo.consumers.base_domain_consumer import BaseDomainConsumer


class AdzunaConsumer(BaseDomainConsumer):

    job_description_selector = 'body > div.container.mx-auto.bg-white.font-sans.text-adzuna-gray-900.md\:px-4 > div > section.lg\:flex.mb-4 > div.flex-grow > section'
