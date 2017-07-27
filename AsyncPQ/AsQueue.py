
class AsyncQueue(object):

	def __init__(self, classDict = {}):
		
		self.asyncQueue = None
		self.classDict = classDict

	def updateClassDict(self, newDict):
		self.classDict.update(newDict)

	def processTasks(self):
		return self.asyncQueue.processUnits()