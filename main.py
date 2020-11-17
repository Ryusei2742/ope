# Pythonでブラウザ操作の自動化


from selenium import webdriver
import time
import pandas as pd
import os
import datetime
from bs4 import BeautifulSoup
import urllib.request as req

url = "" #調べたいURL
response = req.urlopen(url)
parse_html = BeautifulSoup(response, 'html.parser')
# print(parse_html.title.string)
# print(parse_html.find_all('a'))
title_lists = parse_html.find_all('a')
# title_lists[1:20]
# print(title_lists[10].string)
# print(title_lists[10].attrs['href'])

title_list = []
url_list = []

for i in title_lists[1:20]:
	title_list.append(i.string)
	url_list.append(i.attrs['href'])
# print(title_list)
# print(url_list)

df_title_url = pd.DataFrame({'Title':title_list, 'URL':url_list})
# print(df_title_url)
df_notnull = df_title_url.dropna(how = 'any')
# print(df_notnull)
df_notnull['Title'].str.contains('css')
# print(df_notnull[df_notnull['Title'].str.contains('CSS')])
df_contain_css = df_notnull[df_notnull['Title'].str.contains('CSS')]
df_contain_css.to_csv('output.csv')

