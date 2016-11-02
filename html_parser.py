#coding: utf8

from bs4 import BeautifulSoup
import re
import urlparse



class HtmlParser(object):


    def _get_new_urls(self, page_url, soup):#可以获得词条中所有的url
        new_urls = set()
        #/view/123.htm
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)# urljoin方法让new_url按照page_url的格式拼接成一个全新的url
            new_urls.add(new_full_url)
        return new_urls



    def _get_new_data(self, page_url, soup):
        res_data = {}

        #url

        res_data['url'] = page_url

        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>

        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data






    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
          return


        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self.get_new_urls(page_url, soup)
        new_data = self.get_new_data(page_url, soup)
        return new_urls, new_data