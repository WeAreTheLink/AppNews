# -*- coding: utf-8 -*-

def open_dic_categories(file):
    f = open(file)
    dic_categories = eval(f.read())
    f.close()
    list_categories = [(category, dic_categories[category]) for category in dic_categories]
    list_categories_sorted = sorted(list_categories, key=lambda x: x[1], reverse=True)
    list_categories_organized = [str(category[0])+ " : " + str(category[1]) + "\n" for category in list_categories_sorted]
    result = "result_list_of_categories.txt"
    f = open(result, "w")
    for category in list_categories_organized:
        f.write(category)

open_dic_categories("dic_categories.txt")
