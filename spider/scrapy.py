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
 
##配置多个user-agent
1 在settings中配置以一个user-agent-list
2 在middleware中写如下方法
class RandomUserAgentMiddlware(object):
  def __init__(self,crawler):
    super(RandomUserAgentMiddlware,self).__init__()
    self.user_agent_list = crawler.settings.get('user_agent_list',)
    ##注意，user_agent_list可以从别的文件中设置，或者从别的组件中导入
    ##不一定要在settings中
    @classmethod
    def from_crawler(cls,crawler):
      return cls(crawler)
    def process_request(self,request,spider):
      request.header.setdefault('User-Agent',random(self.user_agent_list))
        

      
      
      
##Item Pipeline 的用法
处理item的组件，清理HTML数据，验证爬取数据的正确性，查重，将爬取的item处理（保存数据库，保存文本）
##使用方法
