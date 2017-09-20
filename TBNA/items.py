# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import ast
from scrapy.loader import ItemLoader


# Um artigo possui alem da sua url: um titulo, uma data de publicaçao,
# um corpo e categorias referentes àquele artigo.
class Page(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    date_pub = scrapy.Field()
    text_article = scrapy.Field()
    list_of_categories = scrapy.Field()

    #Metodo para resgatar as categorias de um artigo. Existem dois padroes de artigo,
    # ambos existentes em javascript, um que se encontra após CATEGORIAS e o outro categories
    def createCategories(categories):
        if(categories is None):
            return None
        if("CATEGORIAS: " in categories):
            categories = categories[categories.index("CATEGORIAS: "):]
        else:
            categories = categories[categories.index("categories:"):]
        start = categories.index("[")
        end = categories.index("]") + 1
        list_of_categories = categories[start:end]
        return ast.literal_eval(list_of_categories)
