#coding: utf8


from Python_crawler import url_manage, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manage.UrlManager()#URL管理器
        self.downloader = html_downloader.HtmlDownloader()#html下载器
        self.parser = html_parsed.HtmlParser()#解析器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():#如果有新的url
            try:
                new_url = self.urls.get_new_url()#获取新的url
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.downloader(new_url)#传入网址给下载器
                new_urls, new_data = self.parser.parse(new_url, html_cont)#新的url列表和新的数据
                self.urls.add_new_url(new_urls)#将新的url传入url管理器
                self.outputer.collect_data(new_urls)

                if count == 1000:
                    break

                count = count + 1

            except:
                print 'craw failed'


        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/view/21087.htm'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)#执行爬虫
    