# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from TBNA.items import Page
from scrapy.exceptions import DropItem
from scrapy.loader import ItemLoader
from scrapy import Request
import re
import os
from unicodedata import normalize

# No primeiro pipeline, ele vai deixar passar apenas os artigos. Para ser um artigo
# precisa ter titulo, url correta, corpo da noticia, data de publicaçao e categorias.
class PipelineOne(object):
    def process_item(self, item, spider):
        if(item=={} or item['url'][0][0:7] != "http://"): # caso em que a url ta quebrada ou ela nao se refere a um texto(i.e. uma imagem)
            raise DropItem
        if('date_pub' in item and 'list_of_categories' in item and 'text_article' in item and 'vc-no-g1' not in item['list_of_categories']): # se tiver data de pub e categorias(alem do titulo,
            return item                             #url certa e corpo) é artigo, e portanto, passa para o proximo pipeline
        raise DropItem

#Tratar os itens(verificando se estao de acordo)
class PipelineTwo(object):
    def process_item(self, item, spider):
        new_url = "".join(item['url'])
        new_title = "".join(item['title']).strip() + "."
        new_date_pub = "".join(item['date_pub']).strip()
        new_text_article = "".join(item['text_article'])

        list_temp = item['list_of_categories']
        new_list_categories = list(filter(lambda x: not re.match(".*(semantica|especial-publicitario).*",x),list_temp))

        item['url'] = new_url
        item['title'] = new_title
        item['date_pub'] = new_date_pub
        item['text_article'] = new_text_article
        item['list_of_categories'] = new_list_categories
        return item

#Pipe responsavel por substituir as categorias de cada noticia pelas categorias validas
'''
class PipelineThree(object):
    dic_categories = {}
    count = 1
    list_basic_cat=[]
    dic_map_cat={}
    dic_map_cat_and_subcats = {}
    list_title_and_categories = []
    #nesse metodo, uma lista é preenchida com as categorias validas
    #(provenientes de arquivos txt encontrados em "TBNA/mapCat");
    #e um dicionario é carregado com um par (categoria que deve ser substituida, categoria valida)
    def parseMap():
        for file in os.listdir("TBNA/mapCat"):
            fp=open("TBNA/mapCat/"+file,"r")
            for line in fp:
                line=line.strip()
                tuple_of_map=line.split()
                PipelineThree.list_basic_cat.append(tuple_of_map[-1].lower())
                input_beautify=normalize('NFKD',"-".join(tuple_of_map[0:-1]).lower()).encode('ASCII','ignore').decode('ASCII')
                PipelineThree.dic_map_cat[input_beautify]=tuple_of_map[-1].lower()
            fp.close()


    #esse metodo vai verificar as categorias e substiuir pelas validas(encontradas nas estruturas criadas no parseMap)
    def process_item(self, item, spider):
        str_list = item['list_of_categories']
        #Todas as categorias sao repartidas em componentes, estes verificados se existem nas categorias validas
        for category in str_list:
            components = category.split('/')
            for component in components:
                if(component in PipelineThree.list_basic_cat): #deu match: a noticia possui uma cat. valida, entao sobreescreve todos os componentes por essa categoria valida
                    str_list[str_list.index(category)] = component
                    break
                elif(component in PipelineThree.dic_map_cat.keys()): #possui uma categoria que é par de uma valida(manipulo o dicionario)
                    str_list[str_list.index(category)] = PipelineThree.dic_map_cat[component]
                    break

        item['list_of_categories'] = list(set(str_list))

        PipelineThree.list_title_and_categories.append((item['title'], item['list_of_categories']))

        for category in item['list_of_categories']:
            if(category not in PipelineThree.dic_categories):
                PipelineThree.dic_categories[category] = 1
            else:
                PipelineThree.dic_categories[category] += 1

        print(PipelineThree.count)
        if(PipelineThree.count == 100):
            PipelineThree.count = 0
            for i in PipelineThree.dic_categories:
                print(i + " : " +str(PipelineThree.dic_categories[i]))
        PipelineThree.count+=1
'''

#Pipe responsavel por manusear os artigos. Ele irá
class PipelineFour(object):
    count = 0
    list_of_articles = []
    def process_item(self, item, spider):
        article = item['text_article']
        PipelineFour.count+=1
        print(PipelineFour.count)
        PipelineFour.list_of_articles.append(article)
        
