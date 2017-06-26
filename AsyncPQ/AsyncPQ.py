import ASPQ_Wrapper as apq

class AsyncQueue(object):

	def __init__(self, classDict = {}):
		
		self.pQueue = None
		self.classDict = classDict

	def updateClassDict(self, newDict):
		self.classDict.update(newDict)

	def processTasks(self):
		return self.pQueue.processUnits()

class AsyncPriorityQueue(AsyncQueue):

	def __init__(self, classDict = {}):
		
		super().__init__(classDict)
		self.pQueue = apq.AsyncPQueue()

	def addTask(self, priority, functionRef, *funcArgs):
		self.pQueue.addQUnit(functionRef, funcArgs, priority)

	def addClassTask(self, priority, className, operation, *opArgs): 

		classInst = self.classDict[className]
		functionRef = classInst.funcDict[operation]
		self.pQueue.addQUnit(functionRef, opArgs, priority)

class AsyncReadWriteQueue(AsyncQueue):

	def __init__(self, classDict = {}):
		
		super().__init__(classDict)
		self.pQueue = apq.AsyncRWQueue()
		self.WRITE_PRIORITY = 1
		self.READ_PRIORITY = 0

	def read(self, operation, *opargs):
		self.pQueue.addQUnit(operation, opargs, self.READ_PRIORITY)

	def write(self, operation, *opargs):
		self.pQueue.addQUnit(operation, opargs, self.WRITE_PRIORITY)

	def cdRead(self, className, operation, *opargs): 

		classInst = self.classDict[className]
		functionRef = classInst.funcDict[operation]
		self.pQueue.addQUnit(functionRef, opargs, self.READ_PRIORITY)

	def cdWrite(self, className, operation, *opargs): 

		classInst = self.classDict[className]
		functionRef = classInst.funcDict[operation]
		self.pQueue.addQUnit(functionRef, opargs, self.WRITE_PRIORITY)


		