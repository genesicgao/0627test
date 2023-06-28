import os

from foo.utils.const import BASE_PATH
from foo.utils.log_util import logger


def get_urls():
    urls = [
        'https://jobs.osceolaschools.net/instructional-2023-24-reading-coach/job/25154192'
    ]
    # with open(os.path.join(BASE_PATH, 'data', 'urls.csv'), 'r+') as file:
    #     for line in file.readlines():
    #         urls.append(line.strip())
    return urls