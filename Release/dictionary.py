## -*- coding=utf-8 -*-
# ++++++++++++++++++++++++++++++++++++++++++++++
# Accumulated Dictionary 
# ++++++++++++++++++++++++++++++++++++++++++++++
# Created: jojolin
# Time:2015/05/22
# ++++++++++++++++++++++++++++++++++++++++++++++

import sys
import database
import cloud

localdict = database.getlocaldict()
netdict={}

if __name__=='__main__':
	word=sys.argv[1].decode('gbk').encode('utf8')
	wordutf8=sys.argv[1].decode('gbk')
	# print word
	try:
		print 'checking local ...'
		# for k,v in localdict.items():print k,v
		# print localdict
		mean=localdict[wordutf8]
	except:
		try:
			mean=netdict[word]
		except:
			print 'checking net ...'
			mean=cloud.translate(word)
			if(mean):
				netdict[word]=mean
	if(mean):
		print mean
	else:
		print 'not found'
	# save to database
	database.insertwords(netdict.items())
