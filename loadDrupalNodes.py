from tulip import *
import json
from dateutil.parser import parse
from bs4 import BeautifulSoup
import html2text

stfGroups = set(['2607', '2606', '2613', '2762', '2877', '2873', '2837', '2795', '709STF'])
arrivalGroup = '709'
arrivalDate = parse("2014-04-03-00:00 +00:00")
arrivalSTF = '709STF'

stfPath = "/work/EdgeRyders2/stf-network-data-"
stfDrupal =  "drupal-nodes.json"
stfPostToGroup = "nodes-to-groups.json"
stfUsers = "users.json"
stfComments1 = "comments.json"
stfComments2 = "comments2.json"
stfEthnoPost =  "ethno-posts.json"
stfEthnoComments1 =  "ethno-comments.json"
stfEthnoComments2 =  "ethno-comments2.json"
stfEthnoComments3 =  "ethno-comments3.json"

nodesKey = "drupalNodes"
nodeKey = "drupalNode"
postKey = "nodes"
postNKey = "node"

#post properties
titleKey =  u'title' 
nIDKey = u'NodeId' 
texTermsKey = u'All taxonomy terms'
dateKey = u'Post date'
groupKey = u'User groups'
userKey = u'Author uid'
typeKey = u'Type'
assignToKey = u'Assign to'
assignToDeltaKey = u'Assign to (field_assignee:delta)'

groupKey = u'Group ID'
postNIDKey = u'Nid'

#user properties
uDateKey = u'Created date'
uAgeKey = u'Age Group'
uNameKey =  u'Name' 
uBasedKey = u'based in'
uIDKey = u'Uid'

#comments properties
cAuthorKey = u'Author' 
cTitleKey = u'Title'
cPostIDKey = u'Nid'
cDepthKey = u'Depth'
cParentKey = u'Parent CID'
cDateKey = u'Post date'
cAIDKey = u'Author uid'
cIDKey = u'ID'
cSubjectKey = u'subject'

ethnoNIDKey = u'Nid'
ethnoBodyKey = u'Body'
ethnoCIDKey = u'ID'
ethnoCommentKey = u'Comment'

ethnoCatAttr = "property"
ethnoTagAttr = "resource"
ethnoCleanCat = lambda x: x.replace('eoe:', '')
ethnoCleanTag = lambda x: x.replace('[eoe:', '').replace(']', '')

userToPost = {}
pIDToPost = {}
postToGroups = {}
userToGroups = {}
uIDToUser = {}
cIDToComment = {}
userToComments = {}
nIDToEthnoPost = {}
categoryToTag = {}
cIDToEthnoComment = {}
postIDToTags = {}
cIDToTags = {}

HMuserToPost = "HM-userToPost.json"
HMpIDToPost = "HM-pIDToPost.json"
HMpostToGroups = "HM-postToGroups.json"
HMuserToGroups = "HM-userToGroups.json"
HMuIDToUser = "HM-uIDToUser.json"
HMcIDToComment = "HM-cIDToComment.json"
HMuserToComments = "HM-userToComments.json"

HMnIDToEthnoPost = "HM-nIDToEthnoPost.json"
HMcategoryToTag = "HM-categoryToTag.json"
HMcIDToEthnoComment = "HM-cIDToEthnoComment.json"
HMpostIDToTags = "HM-postIDToTags.json"
HMcIDToTags = "HM-cIDToTags.json"



def fillMapArray(entry, val, hashMap):
	if entry not in hashMap:
		hashMap[entry] = []
	hashMap[entry].append(val)

def loadOneDrupalNode(dpN):
	dpN = dpN[nodeKey]
	user = dpN[userKey]
	nID = dpN[nIDKey]
	fillMapArray(user, nID, userToPost)
	pIDToPost[nID] = dpN

def loadDrupalNodes():
	f = open(stfPath+stfDrupal)
	dpNodes = json.load(f)
	for dpN in dpNodes[nodesKey]:
		loadOneDrupalNode(dpN)
	f.close()

def loadOnePost(pN):
	pN = pN[postNKey]	
	nID = pN[postNIDKey]
	group = pN[groupKey]	
	fillMapArray(nID, group, postToGroups)

def loadPostToGroups():
	f = open(stfPath+stfPostToGroup)
	dpNodes = json.load(f)
	for dpN in dpNodes[postKey]:
		loadOnePost(dpN)
	f.close()

def loadOneUser(uN):
	uN = uN[postNKey]
	uID = uN[uIDKey]
	uName = uN[uNameKey]
	uIDToUser[uID] = uN	

def loadUsers():
	f = open(stfPath+stfUsers)
	usrNodes = json.load(f)
	for uN in usrNodes[postKey]:
		loadOneUser(uN)
	f.close()

def loadOneComment(cN):
	cN = cN[postNKey]
	
	cID = cN[cIDKey]
	cIDToComment[cID] = cN
	#print cN.keys()
	uID = cN[u'Author uid']		
		
	fillMapArray(uID, cID, userToComments)
	
def loadComments():
	f = open(stfPath+stfComments1)
	cNodes = json.load(f)
	for cN in cNodes[postKey]:
		loadOneComment(cN)
	f.close()
	
	f = open(stfPath+stfComments2)
	cNodes = json.load(f)
	for cN in cNodes[postKey]:
		loadOneComment(cN)
	f.close()

def loadOneEthnoPost(dpN):
	#global nIDToEthnoPost
	#global postIDToTags
	
	dpN = dpN[postNKey]
	post = dpN[ethnoBodyKey]
	nID = html2text.html2text(dpN[ethnoNIDKey])
	ethno = getTags(post)
	nIDToEthnoPost[nID] = post
	postIDToTags[nID] = [t for t in ethno]

def loadEthnoPosts():
	f = open(stfPath+stfEthnoPost)
	dpNodes = json.load(f)
	for dpN in dpNodes[postKey]:
		loadOneEthnoPost(dpN)
	f.close()

def getTags(post):
	#print post
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
	

def associateUsersToGroups():
	for u,pList in userToPost.iteritems():
		userToGroups[u] = []
		gList = []
		for p in pList:
			gList.extend(postToGroups[p])
		userToGroups[u] = set(gList)
		
def buildUserNetworkFromGroups(graph):
	viewLabel = graph.getStringProperty("viewLabel")
	nGroups = graph.getDoubleProperty("nGroups")
	groups = graph.getStringVectorProperty("groups")
	isSTF = graph.getBooleanProperty("isSTF")
	
	id2Node = {}
		
	for i in range(len(userToGroups) - 1):
		u1 = userToGroups.keys()[i]
		g1 = userToGroups[u1]
		if u1 not in id2Node:
			n1 = graph.addNode()
			if u1 in uIDToUser:
				viewLabel[n1] = uIDToUser[u1][uNameKey].encode('utf8')
			nGroups[n1] = len(g1)
			groups[n1] = [g.encode('utf8') for g in g1]
			if len(g1 & stfGroups) > 0:
				isSTF[n1] = True
			id2Node[u1] = n1
		n1 = id2Node[u1]

		for j in range(i+1, len(userToGroups)):
			u2 = userToGroups.keys()[j]
			g2 = userToGroups[u2]
			if u2 not in id2Node:
				n2 = graph.addNode()
				if u2 in uIDToUser:
					viewLabel[n1] = uIDToUser[u1][uNameKey].encode('utf8')
				nGroups[n2] = len(g2)
				groups[n2] = [g.encode('utf8') for g in g2]
				if len(g2 & stfGroups) > 0:
					isSTF[n2] = True
				id2Node[u2] = n2
			n2 = id2Node[u2]
			inter = g1 & g2 
			
			if len(inter) > 0:
				e = graph.addEdge(n1,n2)
				nGroups[e] = len(inter)

def getAnswerList(user):
	cList = userToComments[user]
	uList = []
	unregisteredComments = 0
	unregisteredPosts = 0
	unknownAnswers = 0
	
	for p,g in postToGroups.iteritems():
		if len(g) > 10:
			print "STARTING:  ", p, " ", g	
	
	for c in cList:
		prevUser = ""
		comment = cIDToComment[c] 
		prevCID = comment[cParentKey]
		post = comment[cPostIDKey].replace(',', '')
		groups = []
		if post in postToGroups:
			groups.extend(postToGroups[post])
			#print 'the groups ', groups, postToGroups[post]
			if arrivalGroup in groups:
				cDate = comment[cDateKey]
				if parse(cDate) >= arrivalDate:
					groups.append(arrivalSTF)
					
		#print "GETTING ANSWERS: ", groups
					
		if prevCID != u'0':
			if prevCID in cIDToComment:
				prevUser = cIDToComment[prevCID][cAIDKey]
			else:
				#print 'unregistered comment ', prevCID
				unregisteredComments += 1
		else:
			prevPID = comment[cPostIDKey].replace(',','')
			if prevPID in pIDToPost:
				prevUser = pIDToPost[prevPID][userKey]
			else:
				#print 'unregistered post ', prevPID
				unregisteredPosts += 1
				#print type(prevPID) 
				#print sorted(pIDToPost.keys())
		if prevUser != '':	
			uList.append([prevUser, groups, c])
		else:
			#print 'no answer'
			unknownAnswers += 1
	'''		
	if unregisteredComments > 0:
		print 'total unregistered comments: ', unregisteredComments		
	if unregisteredPosts > 0:
		print 'total unregistered posts: ', unregisteredPosts
	if unknownAnswers > 0:
		print 'total unknown answers: ', unknownAnswers
	'''
	
	return uList
	
def createNodeFromUserEntry(userID,  graph):
	viewLabel = graph.getStringProperty("viewLabel")
	nComments = graph.getDoubleProperty("nComments")
	nPosts = graph.getDoubleProperty("nPosts")
	creationDate = graph.getStringProperty("Created date")
	ageGroup = graph.getStringProperty("Age Group")
	name = graph.getStringProperty("Name")
	basedIn = graph.getStringProperty("based in")
	uidP = graph.getStringProperty("Uid")
	userObject = graph.getStringProperty("user object")
	commentList = graph.getStringProperty("comments")
	postList = graph.getStringProperty("posts")


	n = graph.addNode()
	if userID in uIDToUser:
		uInfo = uIDToUser[userID]
		viewLabel[n] = uInfo[uNameKey].encode('utf8')
		name[n] = uInfo[uNameKey].encode('utf8')
		uidP[n] = uInfo[uIDKey].encode('utf8')
		ageGroup[n] = uInfo[uAgeKey].encode('utf8')
		basedIn[n] = uInfo[uBasedKey].encode('utf8')
		creationDate[n] = uInfo[uDateKey].encode('utf8')			
		userObject[n] = str(uInfo)	
		nComments[n] = 0.0
		if userID in userToComments:
			nComments[n] = len(userToComments[userID])
			commentList[n] = json.dumps(userToComments[userID])
		nPosts[n] = 0.0
		if userID in userToPost:
			nPosts[n] = len(userToPost[userID])
			postList[n] = json.dumps(userToPost[userID])
	
	return n

	

def buildUserNetworkFromComments(graph):
	isSTF = graph.getBooleanProperty("isSTF")
	nComments = graph.getDoubleProperty("nComments")	
	
	groups = graph.getStringVectorProperty("groups")	
	comments = graph.getStringVectorProperty("commentsList")
	
	
	id2Node = {}
	print len(userToComments)

	for i in range(len(userToComments)):
		u1 = userToComments.keys()[i]

		if u1 not in id2Node:
			id2Node[u1] = createNodeFromUserEntry(u1,  graph)
		n1 = id2Node[u1]
		
		uAList = getAnswerList(u1)

		for ug2 in uAList:
			u2 = ug2[0]
			
			if u2 not in id2Node:
				id2Node[u2] = createNodeFromUserEntry(u2,  graph)
			n2 = id2Node[u2]
			
			e = graph.existEdge(n1, n2, False)
			if not e.isValid():
				e = graph.addEdge(n1, n2)
			
			groupList = ug2[1]
			groupList.extend(groups[e])
			groupList = [g.encode('utf8') for g in groupList]
			groups[e] = [g for g in set(groupList)]
						
			intersection = set(groupList) & stfGroups

			if len(intersection) > 0:
				isSTF[e] = True

			commentList = [ug2[2]]
			commentList.extend(comments[e])
			commentList = [g.encode('utf8') for g in commentList]
			comments[e] = [g for g in set(commentList)]
									
			nComments[e] = nComments[e] + 1

def defineMultiplex(graph):
	comments = graph.getStringVectorProperty("commentsList")
	tagP = graph.getStringVectorProperty('tags')
	for e in graph.getEdges():
		cList = comments[e]
		tagList = []
		for c in cList:
			if str(c) in cIDToTags:
				tagList.extend(cIDToTags[c])
		tagP[e] = [t.encode('utf8') for t in set(tagList)]
		#print tagP[e]
		

def chunkPost(post):
	if not post:
		return []

	tagList = []
	soup = BeautifulSoup(post)
	spans = soup.find_all('span')	
		
	for s in spans:
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


def loadOneEthnoComment(dpN):
	dpN = dpN[postNKey]
	post = dpN[ethnoCommentKey]
	bs =  BeautifulSoup(dpN[ethnoCIDKey])
	cID = bs.get_text()
	#print "this is the CID: ", cID
	ethno = chunkPost(post)
	cIDToEthnoComment[cID] = post
	cIDToTags[cID] = [t for t in ethno]

def loadEthnoComments():
	f = open(stfPath+stfEthnoComments1)
	dpNodes = json.load(f)
	for dpN in dpNodes[postKey]:
		loadOneEthnoComment(dpN)
	f.close()
	
	f = open(stfPath+stfEthnoComments2)
	dpNodes = json.load(f)
	for dpN in dpNodes[postKey]:
		loadOneEthnoComment(dpN)
	f.close()
	
	f = open(stfPath+stfEthnoComments3)
	dpNodes = json.load(f)
	for dpN in dpNodes[postKey]:
		loadOneEthnoComment(dpN)
	f.close()
	
	for t in categoryToTag:
		categoryToTag[t] = [c for c in set(categoryToTag[t])]


def makeup(graph):
	nonstfEdgeColor = tlp.Color(102,102,255,100)
	stfEdgeColor = tlp.Color(255,128,0,255)
	nonstfNodeColor =  tlp.Color(102,204,255,125)
	stfNodeColor =  tlp.Color(255,102,102,255)
	
	viewShape = graph.getIntegerProperty("viewShape")
	viewColor = graph.getColorProperty("viewColor")
	viewSize = graph.getSizeProperty("viewSize")
	viewLayout = graph.getLayoutProperty("viewLayout")
	viewBorderWidth = graph.getDoubleProperty("viewBorderWidth")
	isSTF = graph.getBooleanProperty("isSTF")
	nComments = graph.getDoubleProperty("nComments")

	reloadLayouts = True
	if reloadLayouts:
		graph.computeLayoutProperty("FM^3 (OGDF)", viewLayout)
	
		viewColor.setAllNodeValue(nonstfNodeColor)

		for e in graph.getEdges():
			viewShape[e] = 4 #Bezier curve
			viewBorderWidth[e] = 0
			if isSTF[e]:
				viewColor[e] = stfEdgeColor
				viewColor[graph.source(e)] = stfNodeColor
				viewColor[graph.target(e)] = stfNodeColor
			else:
				viewColor[e] = nonstfEdgeColor
		
		ds = tlp.getDefaultPluginParameters("Metric Mapping", graph)
		ds["property"] = nComments
		graph.computeSizeProperty("Metric Mapping", viewSize, ds)	
	
		graph.computeLayoutProperty("Fast Overlap Removal", viewLayout)
	
		graph.applyAlgorithm("Edge bundling")
	
	for e in graph.getEdges():
		if graph.getBooleanProperty("isSTF")[e]:
			vLList = viewLayout[e]
			fList = []
			for v in vLList:
				pos = tlp.Coord(v[0], v[1], 1)
				fList.append(pos)
			viewLayout[e] = fList

def saveDump(adress, mymap):
		f = open(stfPath+adress, "w")
		f.write(json.dumps(mymap))
		f.close()
		
def loadDump(adress):
		f = open(stfPath+adress, 'r')
		mymap = json.load(f)
		#print hashmap
		f.close()
		return mymap

def main(graph):
	#graph.clear()
	#return
	
	global userToPost
	global pIDToPost
	global postToGroups
	global userToGroups
	global uIDToUser
	global cIDToComment
	global userToComments
	global nIDToEthnoPost
	global categoryToTag
	global cIDToEthnoComment
	global postIDToTags
	global cIDToTags
	
	reloadData = True
	multiplex = True
	reloadJSONHashMaps = True
	redraw = True

	if multiplex:
		if reloadJSONHashMaps:
			loadEthnoPosts()
			loadEthnoComments()
			saveDump(HMnIDToEthnoPost, nIDToEthnoPost)
			saveDump(HMcIDToEthnoComment, cIDToEthnoComment)
			saveDump(HMcategoryToTag, categoryToTag)
			saveDump(HMpostIDToTags, postIDToTags)
			saveDump(HMcIDToTags, cIDToTags)
		else:
			nIDToEthnoPost = loadDump(HMnIDToEthnoPost)
			cIDToEthnoComment = loadDump(HMcIDToEthnoComment)
			categoryToTag = loadDump(HMcategoryToTag)
			postIDToTags = loadDump(HMpostIDToTags)
			cIDToTags = loadDump(HMcIDToTags)
							
	if reloadData:
		if reloadJSONHashMaps: 
			loadDrupalNodes()
			loadPostToGroups()
	
			loadUsers()
			loadComments()
			#associateUsersToGroups()
			saveDump(HMuserToPost, userToPost)
			saveDump(HMpIDToPost, pIDToPost)
			saveDump(HMpostToGroups, postToGroups)
			#saveDump(HMuserToGroups, userToGroups)
			saveDump(HMuIDToUser, uIDToUser)
			saveDump(HMcIDToComment, cIDToComment)
			saveDump(HMuserToComments, userToComments)
		else:
			userToPost = loadDump(HMuserToPost)
			pIDToPost = loadDump(HMpIDToPost)
			postToGroups = loadDump(HMpostToGroups)
			#userToGroups = loadDump(HMuserToGroups)
			uIDToUser = loadDump(HMuIDToUser)
			cIDToComment = loadDump(HMcIDToComment)
			userToComments = loadDump(HMuserToComments)
		

		#buildUserNetworkFromGroups(graph)
		#print cIDToComment["9505"]
		graph.clear()
		buildUserNetworkFromComments(graph)
		print "comments ",len(cIDToEthnoComment)
		print "posts ",len(nIDToEthnoPost), " / ", len(postToGroups)
		
		comments = graph.getStringVectorProperty("commentsList")
		loops = []
		for e in graph.getEdges():
			if graph.source(e) == graph.target(e):
				loops.append(e)
		print "loops ", len(loops) 

		cList = set([c for e in graph.getEdges() for c in comments[e]])
		print "unique comments ",len(cList)
		stfClist = []
		afterSTF = []
		unlistedPost = 0

		for c in cList:
			post = cIDToComment[c][cPostIDKey].replace(',','')
			cDate = cIDToComment[c][cDateKey]
			if parse(cDate) >= arrivalDate:
				afterSTF.append(c)
						
			if post in postToGroups:
				pList = postToGroups[post]
				if arrivalGroup in pList:
					cDate = cIDToComment[c][cDateKey]
					if parse(cDate) >= arrivalDate:
						pList.append(arrivalSTF)
			else:
				print post
				unlistedPost += 1			
				
			intersection = set(pList) & stfGroups
			if len(intersection) > 0:
				stfClist.append(c)
				#print pList
			
			
		print "produced after STF: ",len(afterSTF)
		print "STF comments: ",len(stfClist)
		
		tagP = graph.getStringVectorProperty('tags')
		tag2occ = {}
		for e in graph.getEdges():
			tList = tagP[e]
			for t in tList:
				if t not in tag2occ:
					tag2occ[t] = 0
				tag2occ[t] += 1
		
		print tag2occ
	
	if multiplex:
		defineMultiplex(graph)	
	if redraw:
		makeup(graph)
	
