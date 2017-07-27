from .ASPQ_Wrapper import AsyncRWQueue
from .AsQueue import AsyncQueue

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
