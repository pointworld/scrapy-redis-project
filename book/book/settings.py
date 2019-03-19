# 项目名
BOT_NAME = 'book'

# spider 的存放位置
SPIDER_MODULES = ['book.spiders']
NEWSPIDER_MODULE = 'book.spiders'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# 使用了 scrapy-redis 里的去重组件，不使用 scrapy 默认的去重策略
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用了 scrapy-redis 里的调度器组件，不使用 scrapy 默认的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 允许暂停，Redis 请求记录不丢失
SCHEDULER_PERSIST = True

#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    # 'book.pipelines.JdPipeline': 300,
    # 'book.pipelines.DangPipeline': 300,
    'book.pipelines.AmazonPipeline': 300,
    # 支持将数据库存储到 Redis 数据库中，必须启用
    # 'scrapy_redis.pipelines.RedisPipeline': 400,
}

# 是否遵守 robots 协议
ROBOTSTXT_OBEY = False

# 日志级别
LOG_LEVEL = 'DEBUG'

# 下载延迟
DOWNLOAD_DELAY = 2

# redis 服务的 URL
REDIS_URL = 'redis://192.168.1.114:6379'
