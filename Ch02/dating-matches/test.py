import kNN as kNN
import numpy as numpy
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)

datingDataMat, datingLabels = kNN.file2matrix('datingTestSet.txt')
#ax.scatter(datingDataMat[:, 2], datingDataMat[:, 0], 15 * numpy.array(datingLabels), 15 * numpy.array(datingLabels))
#plt.show()

normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
print kNN.classify0([1, 1, 1], normMat, datingLabels, 3)
kNN.datingClassTest()
