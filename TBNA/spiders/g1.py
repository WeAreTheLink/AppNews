# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.loader import ItemLoader
from TBNA.items import Page
from TBNA.pipelines import PipelineFour
import urllib.request
import xml.etree.ElementTree as etree
from scrapy import signals
from TBNA.libs.gerar_lista_de_palavras_e_numero_de_ocorrencias import main as gerarArqs

# Classe da aranha
class G1Spider(Spider):
    name = 'g1'
    allowed_domains = ['g1.globo.com']

    def __init__(self):
        Spider.__init__(self)
        ###PipelineThree.parseMap()

    #Obtem os links iniciais para alimentar a aranha
    def getRSS():
        #Obtem o RSS
        fp=urllib.request.urlopen("http://pox.globo.com/rss/g1/")
        myStr=fp.read().decode("utf8")
        fp.close()
        root=etree.fromstring(myStr) #Transforma a string do xml em uma estrutura de dados
        list_urls = []
        for item in root.iter('item'): #Para cada tag 'item' dentro da raiz
            list_urls.append(item[1].text) # Joga na lista o texto da segunda tag filha de 'item'(ou seja, a url)
        return list_urls
    #Alimentando as urls iniciais
    start_urls = getRSS()

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(G1Spider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        gerarArqs(PipelineFour.list_of_articles)
        # dic_categories = open("dic_categories.txt", "w")
        # dic_categories.write(str(PipelineThree.dic_categories))
        # dic_categories.close()
        # list_title_and_categories = open('list_title_and_categories.txt', "w")
        # str_categories = ""
        # for category in PipelineThree.list_title_and_categories:
        #     str_categories += str(category) + "\n"
        # list_title_and_categories.write(str_categories)
        # list_title_and_categories.close()

    def parse(self, response):
        if(str(response.headers['Content-Type'].decode('utf-8')) != "b'text/html'" or not response.url): #[pipelines.py l.16]
            yield {}

        #Inicializando os itens a serem criados
        l = ItemLoader(item=Page())
        #resgatando os dados importantes dos artigos (a sintaxe abaixo so vai funcionar para o G1)
        url = response.url
        title = response.xpath('//h1[@itemprop="headline"]/text()|//h1[@class="entry-title"]/text()').extract_first()
        date_pub = response.xpath('//time[@itemprop="datePublished"]/text()|//abbr[@class="published"]/text()').extract_first()
        text_article = response.xpath('//*[@class="mc-article-body"]/article/div/p/text()|//*[@id="materia-letra"]//p/text()').extract()
        "".join(text_article)
        categories = response.xpath('//script[@id="SETTINGS"]/text()|//body/comment()[contains(., "Realtime")]/following::script/text()').extract_first()
        list_of_categories = Page.createCategories(categories)
        #Criando os itens
        l.add_value('url', url)
        l.add_value('title', title)
        if(date_pub is not None):
            l.add_value('date_pub', date_pub)
        l.add_value('text_article', text_article)
        if(list_of_categories is not None):
            l.add_value('list_of_categories', list_of_categories)
        #Entrega o resultado para o pipeline
        yield l.load_item()
        #Extrai os links das paginas (paginas essas que estam ok! nao foram droppadas, passaram pelo pipelineOne)
        all_links = response.xpath("//a/@href").extract()
        for link in map(response.urljoin, all_links):  #requisitando um novo link
            yield scrapy.Request(link, callback=self.parse)
