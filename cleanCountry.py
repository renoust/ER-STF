# Powered by Python 2.7

# To cancel the modifications performed by the script
# on the current graph, click on the undo button.

# Some useful keyboards shortcuts : 
#   * Ctrl + D : comment selected lines.
#   * Ctrl + Shift + D  : uncomment selected lines.
#   * Ctrl + I : indent selected lines.
#   * Ctrl + Shift + I  : unindent selected lines.
#   * Ctrl + Return  : run script.
#   * Ctrl + F  : find selected text.
#   * Ctrl + R  : replace selected text.
#   * Ctrl + Space  : show auto-completion dialog.

from tulip import *

# the updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# the pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# the runGraphScript(scriptFile, graph) function can be called to launch another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# the main(graph) function must be defined 
# to run the script on the current graph

def main(graph): 
	Age_Group =  graph.getStringProperty("Age Group")
	Created_date =  graph.getStringProperty("Created date")
	Depth =  graph.getDoubleProperty("Depth")
	FM3_OGDF__Unit_edge_length10_New_initial_placementtrue_Fixed_iterations30_Threshold001_viewLayout =  graph.getLayoutProperty("FM^3 (OGDF) - 'Unit edge length'=10 'New initial placement'=true 'Fixed iterations'=30 'Threshold'=0.01 (viewLayout)")
	Fast_Overlap_Removal__number_of_passes5_x_border0_y_border0_viewLayout =  graph.getLayoutProperty("Fast Overlap Removal - 'number of passes'=5 'x border'=0 'y border'=0 (viewLayout)")
	GEM_Frick__3D_layoutfalse_max_iterations0_viewLayout =  graph.getLayoutProperty("GEM (Frick) - '3D layout'=false 'max iterations'=0 (viewLayout)")
	LinLog__3D_layoutfalse_octtreetrue_max_iterations100_repulsion_exponent0_attraction_exponent1_gravitation_factor005_viewLayout =  graph.getLayoutProperty("LinLog - '3D layout'=false 'octtree'=true 'max iterations'=100 'repulsion exponent'=0 'attraction exponent'=1 'gravitation factor'=0.05 (viewLayout)")
	Louvain__viewMetric =  graph.getDoubleProperty("Louvain - (viewMetric)")
	Metric_Mapping__widthtrue_heighttrue_depthfalse_min_size1_max_size10_typetrue_nodeedgetrue_viewSize =  graph.getSizeProperty("Metric Mapping - 'width'=true 'height'=true 'depth'=false 'min size'=1 'max size'=10 'type'=true 'node/edge'=true (viewSize)")
	Metric_Mapping__widthtrue_heighttrue_depthfalse_min_size1_max_size5_typetrue_nodeedgetrue_viewSize =  graph.getSizeProperty("Metric Mapping - 'width'=true 'height'=true 'depth'=false 'min size'=1 'max size'=5 'type'=true 'node/edge'=true (viewSize)")
	Metric_Mapping__widthtrue_heighttrue_depthfalse_min_size2_max_size5_typetrue_nodeedgetrue_viewSize =  graph.getSizeProperty("Metric Mapping - 'width'=true 'height'=true 'depth'=false 'min size'=2 'max size'=5 'type'=true 'node/edge'=true (viewSize)")
	Name =  graph.getStringProperty("Name")
	Uid =  graph.getStringProperty("Uid")
	based_in =  graph.getStringProperty("based in")
	coloration =  graph.getDoubleProperty("coloration")
	comments =  graph.getStringProperty("comments")
	commentsList =  graph.getStringVectorProperty("commentsList")
	descriptors =  graph.getStringProperty("descriptors")
	distance =  graph.getDoubleProperty("distance")
	groups =  graph.getStringVectorProperty("groups")
	isSTF =  graph.getBooleanProperty("isSTF")
	nComments =  graph.getDoubleProperty("nComments")
	nGroups =  graph.getDoubleProperty("nGroups")
	nPosts =  graph.getDoubleProperty("nPosts")
	nodetype =  graph.getDoubleProperty("nodetype")
	posts =  graph.getStringProperty("posts")
	tags =  graph.getStringVectorProperty("tags")
	user_object =  graph.getStringProperty("user object")
	viewBorderColor =  graph.getColorProperty("viewBorderColor")
	viewBorderWidth =  graph.getDoubleProperty("viewBorderWidth")
	viewColor =  graph.getColorProperty("viewColor")
	viewFont =  graph.getStringProperty("viewFont")
	viewFontSize =  graph.getIntegerProperty("viewFontSize")
	viewLabel =  graph.getStringProperty("viewLabel")
	viewLabelBorderColor =  graph.getColorProperty("viewLabelBorderColor")
	viewLabelBorderWidth =  graph.getDoubleProperty("viewLabelBorderWidth")
	viewLabelColor =  graph.getColorProperty("viewLabelColor")
	viewLabelPosition =  graph.getIntegerProperty("viewLabelPosition")
	viewLayout =  graph.getLayoutProperty("viewLayout")
	viewMetaGraph =  graph.getGraphProperty("viewMetaGraph")
	viewMetric =  graph.getDoubleProperty("viewMetric")
	viewRotation =  graph.getDoubleProperty("viewRotation")
	viewSelection =  graph.getBooleanProperty("viewSelection")
	viewShape =  graph.getIntegerProperty("viewShape")
	viewSize =  graph.getSizeProperty("viewSize")
	viewSrcAnchorShape =  graph.getIntegerProperty("viewSrcAnchorShape")
	viewSrcAnchorSize =  graph.getSizeProperty("viewSrcAnchorSize")
	viewTexture =  graph.getStringProperty("viewTexture")
	viewTgtAnchorShape =  graph.getIntegerProperty("viewTgtAnchorShape")
	viewTgtAnchorSize =  graph.getSizeProperty("viewTgtAnchorSize")
	country = graph.getStringProperty("Country")
	city = graph.getStringProperty("City")

	bMap = {}
	cMap = {}
	nList = []
	viewSelection.setAllNodeValue(False)
	
	for n in graph.getNodes():
		bi =  based_in[n].lower()
		#print bi
		bMap[bi] = n
		country[n] = ""
		
		if not bi:
			print "empty"
			
		elif "buenos aires" in bi:
			country[n] = "Argentina"
		elif "armenia" in bi or "yerevan" in bi:
			country[n] = "Armenia" 	
		elif "australia" in bi:
			country[n] = "Australia"
		elif "austria" in bi:
			country[n] = "Austria"
		elif "benelux" in bi or "brussels" in bi:
			country[n] = "Belgium"
		elif "montreal" in bi:
			country[n] = "Canada"
		elif "prague" in bi:
			country[n] = "Czech Republic"
		elif "copenhagen" in bi or "denmark" in bi:
			country[n] = "Denmark"
			
		elif "egypt" in bi or "cairo" in bi or "caio" in bi:
			country[n] = "Egypt"
		elif "talllin" in bi:
			country[n] = "Estonia"
		elif "france" in bi or "paris" in bi or "strasbourg" in bi or "bordeaux" in bi:
			country[n] = "France"
		elif "georgia" in bi or "tbilisi" in bi:
			country[n] = "Georgia"
		elif "berlin" in bi or "germany" in bi or "dresden" in bi:
			country[n] = "Germany"
		elif "athens" in bi:
			country[n] = "Greece"
		elif "budapest" in bi:
			country[n] = "Hungary"
			
			
		elif "iraq" in bi:
			country[n] =  "Iraq"
		elif "ireland" in bi:
			country[n] = "Ireland"
		elif "italy" in bi or "matera" in bi or "itali" in bi or "bergamo" in bi or "milan" in bi or "padova" in bi or "roma" == bi or "rome" == bi or "torino" in bi or "trento" in bi or "trieste" in bi:
			country[n] =  "Italy"
		elif "maastricht" in bi or "amsterdam" in bi or "enschede" in bi:
			country[n] = "Netherlands"
		elif "poland" in bi:
			country[n] = "Poland"
		elif "lisbo" in bi:
			country[n] = "Portugal"
		elif "bucharest" in bi or "cluj" in bi:
			country[n] = "Romania"
		elif "johannesburg" in bi:
			country[n] = "South Africa"
		elif "spain" in bi or "bilbao" in bi or "madrid" in bi:
			country[n] = "Spain"
		elif "sweden" in bi or "stockholm"in bi:
			country[n] = "Sweden"
		elif "lausanne" in bi or "schweinbealp" in bi:
			country[n] = "Switzerland"
		elif "thailand" in bi or "bangkok" in bi:
			country[n] = "Thailand"
		elif "ankara" in bi or "turkey" in bi:
			country[n] = "Turkey"
		elif "uganda" in bi:
			country[n] = "Uganda"
		elif "england" in bi or "hampshire" in bi or "uk" == bi or "london" in bi or "sheffield" in bi or "rugby" in bi:
			country[n] = "UK"
		elif "durham" in bi or "new york" in bi or "oakland" in bi:
			country[n] = "USA"	
					
		elif "india" in bi or "hyderabad" in bi:
			country[n] = "India"
			
		if country[n] == "":
			nList.append(n)
			viewSelection[n] = True
			
	
		print "choice: ",country[n]
		print "from ", bi
		
	print len(nList)
	for n in nList:
		bi =  based_in[n].lower()
		print viewLabel[n]," / ", bi
		if viewLabel[n] == "":
			graph.delNode(n)
		if viewLabel[n] == "ElaMi5":
			country[n] = "Turkey"
		if viewLabel[n] == "Lilit Avdalyan":
			country[n] = "Armenia"
		if viewLabel[n] == "monarezk":
			country[n] = "Egypt"	
		if viewLabel[n] == "Michel Filippi":
			country[n] = "France"	
		if viewLabel[n] == "Abby Margolis":
			country[n] = "Spain"	
		if viewLabel[n] == "Bezdomny":
			country[n] = "Poland"	
		if viewLabel[n] == "Ahmed M Rabie":
			country[n] = "Egypt"	
		if viewLabel[n] == "Pavlik elf":
			country[n] = "Germany"	
		if viewLabel[n] == "Freelab":
			country[n] = "Poland"	
		if viewLabel[n] == "Paola Bonini":
			country[n] = "Italy"	
		if viewLabel[n] == "Said Hamideh":
			country[n] = "USA"	
		if viewLabel[n] == "Lyne Robichaud":
			country[n] = "Canada"	
		if viewLabel[n] == "Noemi D6":
			country[n] = "Romania"	
		if viewLabel[n] == "chara.oikonomidou":
			country[n] = "UK"	
		if viewLabel[n] == "Jaycousins":
			country[n] = "Germany"	
		if viewLabel[n] == "Betta_83":
			country[n] = "France"			
		if viewLabel[n] == "Stefano Stortone":
			country[n] = "Italy"	
		if viewLabel[n] == "Eimhin":
			country[n] = "Ireland"	
		if viewLabel[n] == "ericzoetmulder":
			country[n] = "Egypt"	
		if viewLabel[n] == "admin":
			country[n] = "Belgium"	
		if viewLabel[n] == "albertomz":
			country[n] = "UK"	
