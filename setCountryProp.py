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
	latitude =  graph.getDoubleProperty("latitude")
	longitude =  graph.getDoubleProperty("longitude")
	Age_Group =  graph.getStringProperty("Age Group")
	City =  graph.getStringProperty("City")
	Country =  graph.getStringProperty("Country")
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

	'''
	geo = graph.getRoot().addSubGraph()
	geo.setName("geo")
	size = geo.getDoubleProperty("size")
	vL = geo.getStringProperty("viewLabel")
	'''
	p2S = {}
	
	for sg in graph.getSubGraphs():
		#n = geo.addNode()
		#size[n] = sg.numberOfNodes()
		p2S[sg.getName().replace("Country: ","")] = int(sg.numberOfNodes())

	print p2S
