import re

list_of_dics_of_articles = []
list_of_words = []
# numb_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#durante o scrape
def organized_to_list(str_article):
    list_article = re.findall(r"[\w']+", str_article.lower())
    list_article.sort()
    # for l in list_article:
    #     if(l[0] not in numb_list):
    #         pos = list_article.index(l)
    #         break
    # list_article = [list_article[x] for x in range(pos,len(list_article))]
    return list_article

def list_to_dic(list_article):
    dic_article = {}
    for l in list_article:
        if l in dic_article:
            dic_article[l] += 1
        else:
            dic_article[l] = 1
    list_of_dics_of_articles.append(dic_article)
    return dic_article

def populate_list_of_words(dic_article):
    for key_word in dic_article:
        if key_word not in list_of_words:
            list_of_words.append(key_word)
    list_of_words.sort()

def main(list_strs):
    # st1 = "a casa de 54 fogo enfrentou a casa de gelo e ve 7 nceu"
    # st2 = "sobre ele farei cair a fome e o fogo, ate que a sua volta ecoe a desolação. E que todos os demônios da escuridão externa, contemplem, admirados, e reconheçam, que a vingança é obra de um homem."
    # st3 = "qual é o apresentador de televisão em que você não pode confiar? á à á o falso silva! ótimo"
    # list_strs = [st1, st2, st3]
    for st in list_strs:
        list_st = organized_to_list(st)
        dic_st = list_to_dic(list_st)
        populate_list_of_words(dic_st)

    get_articles_and_create_files(list_of_dics_of_articles, list_of_words)
    print(list_of_words)

#ao final do scrape

def get_articles_and_create_files(list_of_dics_of_articles, list_of_words):
    arq_occurrence = open("list_of_occurrence_for_each_article.txt", "w")
    for dic_article in list_of_dics_of_articles:
        actual_position_dic = - 1 #se fosse 0, caso a primeira palavra n tivesse no artigo, ele escreveria os 0s erradamente.(sempre faltando)
        actual_position_list_words = 0
        string_to_write_in_arq = ""
        for key_word in dic_article:
            pos_word = list_of_words[actual_position_list_words:].index(key_word) + actual_position_list_words
            actual_position_list_words = pos_word
            string_to_write_in_arq += " 0" * (actual_position_list_words - actual_position_dic - 1)
            string_to_write_in_arq += " " + str(dic_article[key_word])
            actual_position_dic = actual_position_list_words
        string_to_write_in_arq += " 0" * (len(list_of_words) - 1 - actual_position_list_words) + "\n"
        arq_occurrence.write(string_to_write_in_arq.strip(" "))
        arq_occurrence.write("\n")
    arq_occurrence.close()

    arq_of_words = open("list_of_words.txt", "w")
    for word in list_of_words:
        arq_of_words.write(word + "\n")
    arq_of_words.close()
