import trees as trees
import treePlotter
myData, labels = trees.createDataSet()
#print trees.calcShannonEntropy(myData)
#print myData
print trees.createTree(myData, labels)
treePlotter.createPlot()
