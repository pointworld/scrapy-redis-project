# scrapy-redis : 分布式爬取图书信息
  
 - 采用 scrapy-redis 分布式爬取京东、当当和 Amazon 三大网站的图书信息
 - 通过 scrapy-redis 实现爬虫的暂停和开始，断点再续，URL 去重，数据存储等
 
## 爬取策略

京东图书 - 通过 scrapy 的 Spider 类实现
当当图书 - 通过 scrapy-redis 的 RedisSpider 类实现
Amazon 图书 - 通过 scrapy-redis 的 CrawlSpider 类实现

## 运行

### 配置 Redis 服务

- 修改 settings.py 文件中的 REDIS_URL

```python
REDIS_URL = 'redis://[:password@]ip:port'
# [：password@] : 为 redis 密码，如无则不填
# 示例：REDIS_URL = 'redis://127.0.0.1:6379'

```

- 运行爬虫

```
python main.py
```

- 启动 Redis 客户端，输入如下指令

```text
$ redis-cli
 
$ > lpush dangdang:start_urls http://book.dangdang.com/

$ > lpush amazon:start_urls https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=topnav_storetab_b?ie=UTF8&node=658390051
```