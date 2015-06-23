## -*- coding=utf-8 -*-
# ++++++++++++++++++++++++++++++++++++++++++++++
# Created: jojolin
# Time:2015/05/22
# ++++++++++++++++++++++++++++++++++++++++++++++

from lxml import etree
import urllib

querystr='http://dict.youdao.com/search?le=eng&q=%s&keyfrom=dict.top'

def translate(word):
	# print urllib.quote(word)
	url=querystr % urllib.quote(word)
	tree=etree.parse(url,etree.HTMLParser())
        tmp =  tree.xpath('//div[@class="trans-container"][1]/ul/li/text()') + \
	tree.xpath('//div[@class="trans-container"]/ul/p[@class="wordGroup"]/span[@class="contentTitle"]/a/text()')
        # tickout the empty line
        # import pdb; pdb.set_trace()
        result= []
        for t in tmp:
                if t.lstrip(): result.append(t.lstrip())
        return '\n'.join(result)

if __name__=='__main__':
	import sys
	print translate(sys.argv[1].decode('gbk').encode('utf8'))
