__author__ = 'Rafael'

from lxml import html
import requests
import re


def clean_data_from_web_source(datalist_names, datalist_calories, datalist_quantity):
    # function being developed specifically for web source #2
    unity_list = list()
    quantity_list = list()

    # first thing is to remove the headers from the tables in the website
    indices_of_headers = [i for i, x in enumerate(datalist_names) if x == "Type"]
    datalist_names.remove('Type')

    for index in sorted(indices_of_headers, reverse=True):
        del datalist_calories[index]
        del datalist_quantity[index]

    # second thing is to proper separate the information of quantity and unity that comes altogether in the website

    for idx,quantity in enumerate(datalist_quantity):
        quantity_list.append(re.findall('\d+', quantity))
        unity_list.append(re.findall("[a-zA-Z]+", quantity))

    print quantity_list
    print unity_list

    # third thing: replace 'Half a cup' for 0.5 + cup

# Source #1 : http://www.myfoodbuddy.com/foodCalorieTable.htm
page = requests.get('http://www.myfoodbuddy.com/foodCalorieTable.htm')
tree = html.fromstring(page.content)



# food = tree.xpath('//td[@width="69%"]/text()')
# calories = tree.xpath('//td[@width="0%"]/text()')
# protein = tree.xpath('//td[@width="8%"]/text()')
# fat = tree.xpath('//td[@width="4%"]/text()')
# carbohydrate = tree.xpath('//td[@width="19%"]/text()')

# print food
# print calories
# print fat

# Source #2 : http://www.moh.gov.sa/en/healthawareness/campaigns/badana/pages/009.aspx


page = requests.get('http://www.moh.gov.sa/en/healthawareness/campaigns/badana/pages/009.aspx')
tree2 = html.fromstring(page.content)

food_source2_list = list()
calories_source2_list = list()
quantity_source2_list = list()

div_node_list_type = tree2.xpath('//td[@width="49%"]/node()')
div_node_list_calories = tree2.xpath('//td[@width="24%"]/node()')
div_node_list_quantity = tree2.xpath('//td[@width="25%"]/node()')

for div_node in div_node_list_type:
    span_node = div_node.getchildren()
    food_source2_list.append(span_node[0].text_content())

for div_node in div_node_list_calories:
    span_node = div_node.getchildren()
    calories_source2_list.append(span_node[0].text_content())

for div_node in div_node_list_quantity:
    span_node = div_node.getchildren()
    quantity_source2_list.append(span_node[0].text_content())

print food_source2_list
print calories_source2_list
print quantity_source2_list

clean_data_from_web_source(food_source2_list,calories_source2_list,quantity_source2_list)

