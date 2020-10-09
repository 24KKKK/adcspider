import datetime

from scrapy import cmdline
from scrapy.cmdline import execute
import sys
import os  # 用来获取路径的模块

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy', 'crawl', 'vipspider']) # 显示日志
cmdline.execute('scrapy crawl vipspider --nolog'.split())  # 运行爬虫时，不显示scrapy日志