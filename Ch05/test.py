import logRegres
dataMat, classLabels = logRegres.loadDataSet()
print logRegres.gradAscent(dataMat, classLabels)