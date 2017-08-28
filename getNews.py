import scrapy

class GetNews(Scrapy.Spider):
	name="appNewsCrawler"
	start_urls = getInitialURL()

#for each article, we save the content.
#for each link, we follow
	def parser(self,response):
		#we need understand how to use xpath to get all text in article
		for article in response.xpath("//article"):
	
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
