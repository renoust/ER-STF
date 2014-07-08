from tulip import *
import json
from bs4 import BeautifulSoup

stfGroups = set(['2607', '2606', '2613', '2762', '2877', '2873', '2837', '2795', '709STF'])
stfPath = "/work/EdgeRyders2/stf-network-data-"

stfEthnoPost =  "ethno-posts.json"

nodesKey = "nodes"
nodeKey = "node"

ethnoNIDKey = u'Nid'
ethnoBodyKey = u'Body'

nIDToEthnoPost = {}
categoryToTag = {}

stfEthnoComments1 =  "ethno-comments.json"
stfEthnoComments2 =  "ethno-comments2.json"
stfEthnoComments3 =  "ethno-comments3.json"

nIDToEthnoComment = {}
ethnoCIDKey = u'ID'
ethnoCommentKey = u'Comment'

def fillMapArray(entry, val, hashMap):
	if entry not in hashMap:
		hashMap[entry] = []
	hashMap[entry].append(val)

def loadOneEthnoPost(dpN):
	dpN = dpN[nodeKey]
	post = dpN[ethnoBodyKey]
	nID = dpN[ethnoNIDKey]
	ethno = chunkPost(post)
	nIDToEthnoPost[nID] = post

def loadOneEthnoComment(dpN):
	dpN = dpN[nodeKey]
	post = dpN[ethnoCommentKey]
	nID = dpN[ethnoCIDKey]
	ethno = chunkPost(post)
	nIDToEthnoComment[nID] = post

def loadEthnoComments():
	f = open(stfPath+stfEthnoComments1)
	dpNodes = json.load(f)
	for dpN in dpNodes[nodesKey]:
		loadOneEthnoComment(dpN)
	f.close()
	
	f = open(stfPath+stfEthnoComments2)
	dpNodes = json.load(f)
	for dpN in dpNodes[nodesKey]:
		loadOneEthnoComment(dpN)
	f.close()
	
	f = open(stfPath+stfEthnoComments3)
	dpNodes = json.load(f)
	for dpN in dpNodes[nodesKey]:
		loadOneEthnoComment(dpN)
	f.close()

ethnoCatAttr = "property"
ethnoTagAttr = "resource"
ethnoCleanCat = lambda x: x.replace('eoe:', '')
ethnoCleanTag = lambda x: x.replace('[eoe:', '').replace(']', '')

def chunkPost(post):
	if not post:
		return []

	tagList = []
	soup = BeautifulSoup(post)
	spans = soup.find_all('span')	
		
	for s in spans:
		#print s.attrs
		category = ""
		tag = ""
		if ethnoCatAttr in s.attrs:
			category =  ethnoCleanCat(s[ethnoCatAttr])
		
		if ethnoTagAttr in s.attrs:
			tag =  ethnoCleanTag(s[ethnoTagAttr])
	
		if category != "" and tag != "":
			fillMapArray(category, tag, categoryToTag)
		
		if tag != "":
			tagList.append(tag)	
		
	return set(tagList)
	
def loadEthnoPosts():
	f = open(stfPath+stfEthnoPost)
	dpNodes = json.load(f)
	for dpN in dpNodes[nodesKey]:
		loadOneEthnoPost(dpN)
	f.close()

def main(graph): 
	loadEthnoPosts()
	loadEthnoComments()
	for t in categoryToTag:
		categoryToTag[t] = [i for i in set(categoryToTag[t])]
	print categoryToTag
	export = json.dumps(categoryToTag)
	f = open(stfPath+"categoryToTag.json", "w")
	f.write(export)
	f.close()
