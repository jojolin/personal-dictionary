## -*-coding=utf-8 -*-
# ++++++++++++++++++++++++++++++++++++++++++++++
# Created: jojolin
# Time:2015/05/22
# ++++++++++++++++++++++++++++++++++++++++++++++

import sqlite3

db = 'dict.db'
def createtable():
	conn=sqlite3.connect(db)
	c=conn.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS dictionary(id INTEGER PRIMARY KEY ASC, word text, meaning text)')
	conn.commit()
	conn.close()

def createtestword():
	conn=sqlite3.connect(db)
	c=conn.cursor()
	c.execute('SELECT id FROM dictionary')
	if(not c.fetchall()):c.execute('INSERT INTO dictionary (word,meaning) VALUES ("test","测试")')
	conn.commit()
	conn.close()

def insertwords(words):
	conn=sqlite3.connect(db)
	conn.text_factory = str
	c=conn.cursor()
	c.executemany('INSERT INTO dictionary (word,meaning) VALUES (?,?)',words)
	conn.commit()
	conn.close()

def getlocaldict():
	conn=sqlite3.connect(db)
	c=conn.cursor()
	c.execute('SELECT word,meaning FROM dictionary')
	localdic=dict(c.fetchall())
	conn.close()
	return localdic

createtable()
if __name__=='__main__':
	createtestword()
	insertwords([('test1','测试1'),('test2','测试2'),('test3','测试3')])
	print getlocaldict()
