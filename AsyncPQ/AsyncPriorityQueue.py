from AsyncPQ import ASPQ_Wrapper, AsQueue
from ASPQ_Wrapper import AsyncPQueue
from AsQueue import AsyncQueue

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

