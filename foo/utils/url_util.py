import os

from foo.utils.const import BASE_PATH
from foo.utils.log_util import logger


def get_urls():
    urls = [
        'https://careers.teksystems.com/ca/fr/job/TESYUSJP-003847406fr_CA/IT-Project-Engineer'
    ]
    # with open(os.path.join(BASE_PATH, 'data', 'urls.csv'), 'r+') as file:
    #     for line in file.readlines():
    #         urls.append(line.strip())
    return urls