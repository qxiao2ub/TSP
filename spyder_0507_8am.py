# =============================================================================
# follow 0430_tsp_jupyter notebook
# =============================================================================

import veroviz as vrv
#vrv.checkVersion()
#import folium

# 1 -- Create some "nodes"
# vrv.generateNodes? #see how "generateNodes" function works

myBoundingRegion = [[43.01770145196991, -78.87840270996095],[42.878480017739044, -78.8756561279297], 
                    [42.83569550641454, -78.68270874023439],[42.96596996868038, -78.60717773437501], 
                    [43.04430359661548, -78.72528076171876]]
# print(myBoundingRegion)

myNodes = vrv.generateNodes(nodeType = 'customer',
                            nodeName = 'cust',
                            numNodes = 10, #generate 10 nodes
                            incrementName = True, #this makes customer from 1,2,3,...,10
                            nodeDistrib = 'uniformBB', #10 nodes are uniform distributed
                            nodeDistribArgs = {'boundingRegion': myBoundingRegion} #generated 10 nodes within my BoundingRegion
                            )

# print(myNodes)

# View our nodes and bounding region:
m=vrv.createLeaflet(nodes = myNodes, boundingRegion=myBoundingRegion) #make it m
m.save("mymap.html") #save in folder can see it

'''
# Create four customer nodes:
nodesDF = vrv.generateNodes(initNodes       = nodesDF,
                            numNodes        = 4,
                            startNode       = 1,
                            nodeType        = 'customer',
                            leafletColor    = 'blue',
                            leafletIconType = 'star',
                            nodeDistrib     = 'uniformBB', 
                            nodeDistribArgs = { 
                                   'boundingRegion': myBoundary },
                            dataProvider    = 'OSRM-online',
                            snapToRoad      = True)

vrv.createLeaflet(nodes=nodesDF, boundingRegion=myBoundary)
'''