import os
import sys

from scrapy import cmdline


current_dir = os.path.abspath(__file__)
sys.path.append(current_dir)

# cmdline.execute('scrapy crawl jd'.split())
# cmdline.execute('scrapy crawl dangdang'.split())
cmdline.execute('scrapy crawl amazon'.split())
