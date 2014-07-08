# -*- coding: utf-8 -*-

# To cancel the modifications performed by the script
# on the current graph, click on the undo button.

# Some useful keyboards shortcuts : 
#   * Ctrl + D : comment selected lines.
#   * Ctrl + Shift + D  : uncomment selected lines.
#   * Ctrl + Space  : run script.
#   * Ctrl + F  : find selected text.
#   * Ctrl + R  : replace selected text.

from tulip import *
import json

# the updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# the pauseScript() function can also be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# the main(graph) function must be defined 
# to run the script on the current graph

def main(graph):
	load(graph)
	return
	
	treated = []
	for sg in graph.getSubGraphs():
		for ssg in sg.getSubGraphs():
			if ssg.getName() == "Documents":
				fileName = "".join([sg.getName()[i] for i in range(len(sg.getName())) if i<25]).replace(" ","-").replace("'","-").replace(",","_")
				fileName = fileName.decode("iso-8859-1").encode('ascii', 'ignore')#'xmlcharrefreplace')
				if fileName not in treated:
					treated.append(fileName)
					load(ssg, fileName+".json")
				else:
					print "conflict"
				
def load(graph, fileName= "STF_users_keywords_action.json", catalystProperty="descriptors", weightProperty=None) : 

	viewLabel = graph.getStringProperty("viewLabel")
	descripteurs =  graph.getStringProperty(catalystProperty)
	if weightProperty:
		weightP = graph.getDoubleProperty(weightProperty)
	#for n in graph.getNodes():
	#	viewLabel[n] = "u"+str(n.id)
	#	descripteurs[n] = ";".join(["f"+str(x) for x in descripteurs[n].split()])
	
	#chapeau =  graph.getStringProperty("chapeau")
	#date =  graph.getIntegerProperty("date")
	#dateString =  graph.getStringProperty("dateString")
	titre_propre =  graph.getStringProperty("viewLabel")
	viewLayout =  graph.getLayoutProperty("viewLayout")

	#print [e for e in graph.getEdges() ]
	#return
	
	if weightProperty:
		nodeList = {"nodes":[{"id":n.id, "label":titre_propre[n].decode("latin-1").encode('utf-8'), "weighted":weightP[n],"descriptors":descripteurs[n].decode("latin-1").encode('utf-8'), "x":viewLayout[n][0], "y":viewLayout[n][1]} for n in graph.getNodes()]}
		edgeList = {"links":[{"id":e.id, "source":graph.ends(e)[0].id, "target":graph.ends(e)[1].id, "weighted":weightP[e], "descriptors":descripteurs[e].decode("latin-1").encode('utf-8')} for e in graph.getEdges() if descripteurs[e] != ""]}
	else:
		nodeList = {"nodes":[{"id":n.id, "label":titre_propre[n].decode("latin-1").encode('utf-8'), "descriptors":descripteurs[n].decode("latin-1").encode('utf-8'), "x":viewLayout[n][0], "y":viewLayout[n][1]} for n in graph.getNodes()]}
		edgeList = {"links":[{"id":e.id, "source":graph.ends(e)[0].id, "target":graph.ends(e)[1].id, "descriptors":descripteurs[e].decode("latin-1").encode('utf-8')} for e in graph.getEdges() if descripteurs[e] != ""]}

	nodeList.update(edgeList)
	print json.dumps(nodeList)
	
	f = open("/work/"+fileName, "w")
	f.write(json.dumps(nodeList, indent=True))
	f.close()
