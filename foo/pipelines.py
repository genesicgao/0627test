# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import datetime

from itemadapter import ItemAdapter

from foo.utils.const import URL_PATH
from foo.utils.log_util import logger
import pandas as pd


class FooPipeline:
    def process_item(self, item, spider):
        # pd_data = pd.read_csv(URL_PATH)
        # if 'live' not in pd_data:
        #     pd_data.loc[:, 'live'] = ''
        # if 'last_live_check_date' not in pd_data:
        #     pd_data.loc[:, 'last_live_check_date'] = ''
        # if 'description' not in pd_data:
        #     pd_data.loc[:, 'description'] = ''
        # pd_data['live'].loc[item['index']] = 'Yes' if item['live'] else 'No'
        # pd_data['last_live_check_date'].loc[item['index']] = datetime.datetime.now().strftime('%Y-%m-%d')
        # if item['index'] < 10:
        #     pd_data['description'].loc[item['index']] = item['job_description']
        # pd_data.to_csv(URL_PATH, index=False)
        return item
