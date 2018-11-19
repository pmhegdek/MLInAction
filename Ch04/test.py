import bayes
import re
# listOfPosts, listClasses = bayes.loadDataSet()
# myVocabList = bayes.createVocabList(listOfPosts)
# trainMat = []
# for postinDoc in listOfPosts:
#     trainMat.append(bayes.bagOfWords2VecMN(myVocabList, postinDoc))
# p0v, p1v, pAb = bayes.trainNB0(trainMat, listClasses)
# print pAb
# bayes.testingNB()

emailText = open('email/ham/6.txt').read()
regEx = re.compile('\\W*')
listOfTokens = regEx.split(emailText)
listOfTokens = [tok for tok in listOfTokens if len(tok) > 0]
listOfTokens = [tok.lower() for tok in listOfTokens]
print listOfTokens
