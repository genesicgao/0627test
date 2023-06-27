from foo.utils.log_util import logger
from scrapy import cmdline

logger.info('scrapy spider start')


cmdline.execute(['scrapy', 'crawl', 'foo'])
