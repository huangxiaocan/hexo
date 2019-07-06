#coding:utf-8
import requests
import time

print unicode('Langzi.Fun 关键词采集开启....','utf-8')
#time.sleep(0.5)

key = raw_input(unicode('输入关键词:','utf-8'))
site_url = 'https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd=' + (str(key))

r = requests.get(site_url)
print r.content.replace('window.baidu.sug({q:','').replace('});','').replace(',p:false,s:','').replace('"','').replace(str(key),'')
