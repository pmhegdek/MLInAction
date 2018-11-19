import numpy as numpy
import operator

def createDataSet(): 
    group = numpy.array([[1.0, 1.1], [1.0, 1.0], [0,0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):

    dataSetSize = dataSet.shape[0]
    diffMat = numpy.tile(inX, (dataSetSize, 1)) - dataSet
    sqrDiffMat = diffMat ** 2
    sqDistances = sqrDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndices = distances.argsort()
    classCount = {}
    for i in range(k): 
        voteILabel = labels[sortedDistIndices[i]]
        classCount[voteILabel] = classCount.get(voteILabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]




