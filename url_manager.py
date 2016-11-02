# coding: utf8

class UrlManager(object):

    def __init__(self):
        self.new_url = set()
        self.old_url = set()

    def add_new_url(self, url):#向管理器中增加新的url
       if url is None:
            return

        if url not in self.new_urls and url not in self.old_url:
            self.new_urls.add(url) 

    def add_new_urls(self, urls):#向管理器中增加批量的url
        if urls is None or len(urls) == 0;
            return

        for url in urls:
            self.add_new_url(url)


    def has_new_url(self):#判断管理器中是否有待爬取的url
        return len(self.new_urls) != 0

    def get_new_url(self):#从url管理器中获取新的url
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url







