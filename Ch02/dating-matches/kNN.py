import numpy as numpy
import operator

def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())
    returnMat = numpy.zeros((numberOfLines, 3))
    classLabelVector = []
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        labelInt = getIntForLabels(listFromLine[-1])

        classLabelVector.append(labelInt )
        index += 1
    return returnMat, classLabelVector

def image2Vector(filename):
    returnVector = numpy.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVector[0, 32*i + j] = int(lineStr)
    return returnVector

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = numpy.zeros(dataSet.shape)
    m = dataSet.shape[0]
    normDataSet = dataSet - numpy.tile(minVals, (m, 1))
    normDataSet = normDataSet / numpy.tile(ranges, (m,1))
    return normDataSet, ranges, minVals

def getIntForLabels(label):
    modLabel = 1
    if (label =='largeDoses'):
        modLabel = 3
    elif ( label =='smallDoses'):
        modLabel = 2
    else:
        modLabel = 1
    return modLabel

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

# test
def datingClassTest():
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:], datingLabels[numTestVecs:m],3)
        if (classifierResult != datingLabels[i]): 
            errorCount += 1.0
            print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        
    print "the total error rate is: %f" % (errorCount/float(numTestVecs))