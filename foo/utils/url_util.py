import os

from foo.utils.const import URL_PATH
from foo.utils.log_util import logger
import pandas as pd
import numpy as np


def get_urls():
    # pd_data = pd.read_csv(URL_PATH)
    # if 'live' not in pd_data:
    #     pd_data.loc[:, 'live'] = ''
    # pd_data['live'] = pd_data['live'].replace(np.nan, '')
    # for row in pd_data.itertuples():
    #     if not getattr(row, 'live'):
    #         yield {
    #             'index': getattr(row, 'Index'),
    #             'url': getattr(row, 'application_link_1')
    #         }
    yield {
        'index': 2,
        'url': 'https://lensa.com/information-systems-security-officer-isso-jobs/panama-city/jd/57abb2242aed0ef18297db35c25eb915?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic'
    }