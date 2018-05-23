#Downloader Middleware
修改User-Agent,处理重定向，代理设置，失败重试，设置cookies等功能都需要它实现

##使用方法：
1 在Middlewares中创建calss,里面包含数据流通时的处理方法（包括下面的核心方法）
  eg:
    class This_Middleware():
      def __init__(self):
        pass
      def process_request(self,request,spider):
        pass
      def proecss_response(self,request,response,spider):
        pass
      def process_exception(self,request,exception,spider)：
        pass
    
2 在setting.py中配置,配置位置：DOWNLOADER_MIDDLEWARE之后
 eg:
  DOWNLOADER_MIDDLEWARE:DOWNLOADER_MIDDLEWARES = {
    'scrapydownloadertext.middlewares.ScrapydownloadertextDownloaderMiddleware': 543,
    'scrapydownloadertext.middlewares.This_Middleware': 500,
    }
    注：数字越小，越靠近scrapy engine，越大，越靠近Downloader
3 配置好之后，数据在engine和Downloader中间流动是会自动处理
##核心方法：
1 process_request(request,spider)
2 process_response(requests,response,spider)
3 process_exception(requests，exception,spider)
eg:
下面是一个改写user-agent和改写状态（status）的Middleware
import random
class RandomUserAgentMiddleware():
    def __init__(self):
        self.user_agent = [
            'Mozilla/5.0/protectfish1',
            'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
            'Mozilla/5.0/peotectfish2'
        ]
    def process_request(self,request,spider):
        request.headers['User-Agent'] = random.choice(self.user_agent)
    def process_response(self,request,response,spider):
        response.status=8888
        return response
