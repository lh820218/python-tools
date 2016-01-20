#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json

file_data=open('/Users/lihui1/Desktop/1.txt','r')

write_data=open('/Users/lihui1/Desktop/113.txt','w')


for file_data_line in file_data.readlines():
    a=file_data_line.split()
    if len(a)==3 and len(a[2])>=15 and len(a[2])<=18:
        url = 'http://apis.baidu.com/apistore/idservice/id?id=%s' % str(a[2])
        req = urllib2.Request(url)
        req.add_header("apikey", "5ade945295356187308bda5bc4061a9e")
        resp = urllib2.urlopen(req)
        content = resp.read()
        content=content.decode('unicode_escape')
        content=eval(content)
        if(content['errNum']==0):
            id_city=content['retData']['address']
            birthday=content['retData']['birthday']

        url = 'http://apis.baidu.com/chazhao/mobilesearch/phonesearch?phone=%s' % str(a[1])
        req = urllib2.Request(url)
        req.add_header("apikey", "5ade945295356187308bda5bc4061a9e")
        resp = urllib2.urlopen(req)
        content = resp.read()
        content=content.decode('utf8')
        content=eval(content)
        if(content['error']==0):
            mobile_city=content['data']['city']
            mobile_type=content['data']['operator']
        w_data='%s\t%s\t%s\t%s\t%s\t%s\n' %(a[0],a[1],id_city,birthday,mobile_city,mobile_type)
        write_data.write(w_data)
file_data.close()
write_data.close()