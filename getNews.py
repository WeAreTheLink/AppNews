import scrapy
import re

class GetNews(Scrapy.Spider):
	name="appNewsCrawler"
	start_urls = getInitialURL()
	allow_domains = domains()
	
	def parser(self,response):
		for article in response.xpath("//article").extract():
			listWithoutTags=re.split("<[^>]+?>",article)
			fp=open(response.url,"w")
			fp.write(reduce(lambda x y: x+y,listWithoutTags))
			fp.close()

		for link in response.xpath("//a/@href").extract():
			if(prefixIsCorrect(link)):
				yield response.follow(link,callback=self.parser)
			
			
	@support_function
	def prefixIsCorrect(link):
		for prefix in start_urls:
			if (re.match(prefix,link)):
				return True
		return False

	@support_function
	def getInitialURL():
		l=[]
		fp=open("sites","r")
		for line in fp:
			first,second = line.split(' ')
			category = second.split(',')
			for categories in category:
				l=l+[first + "/" + categories]
		fp.close()
		return l

	@support_function
	def domains():
		fp=open("sites","r")
		l=[]
		for line in fp:
			l=l+[line.split(',')[0]]
		fp.close()
		return l
