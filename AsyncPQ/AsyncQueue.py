from .ASPQ_Wrapper import AsyncPQueue, AsyncRWQueue

class AsyncQueue(object):

	def __init__(self, classDict = {}):
		
		self.asyncQueue = None
		self.classDict = classDict

	def updateClassDict(self, newDict):
		self.classDict.update(newDict)

	def processTasks(self):
		return self.asyncQueue.processUnits()

class AsyncPriorityQueue(AsyncQueue):

	def __init__(self, classDict = {}):
		
		super().__init__(classDict)
		self.asyncQueue = AsyncPQueue()

	def addTask(self, priority, functionRef, *funcArgs):
		self.asyncQueue.addQUnit(functionRef, funcArgs, priority)

	def addClassTask(self, priority, className, operation, *opArgs): 

		classInst = self.classDict[className]
		functionRef = getattr(classInst, operation)
		self.asyncQueue.addQUnit(functionRef, opArgs, priority)

class AsyncReadWriteQueue(AsyncQueue):

	def __init__(self, classDict = {}):
		
		super().__init__(classDict)
		self.asyncQueue = AsyncRWQueue()
		self.WRITE_PRIORITY = 1
		self.READ_PRIORITY = 0

	def read(self, operation, *opargs):
		self.asyncQueue.addQUnit(operation, opargs, self.READ_PRIORITY)

	def write(self, operation, *opargs):
		self.asyncQueue.addQUnit(operation, opargs, self.WRITE_PRIORITY)

	def cdRead(self, className, operation, *opargs): 

		classInst = self.classDict[className]
		functionRef = getattr(classInst, operation)
		self.asyncQueue.addQUnit(functionRef, opargs, self.READ_PRIORITY)

	def cdWrite(self, className, operation, *opargs): 

		classInst = self.classDict[className]
		functionRef = getattr(classInst, operation)
		self.asyncQueue.addQUnit(functionRef, opargs, self.WRITE_PRIORITY)
