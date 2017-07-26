import asyncio
from AsyncPQ import AsyncPriorityQueue, AsyncReadWriteQueue

class TestClass(object):
	
	def __init__(self): pass

	async def testFunc(self, arg): 
		await asyncio.sleep(0)
		print(arg)

async def testFunc2(arg): 
	await asyncio.sleep(0)
	print(arg)

classDict = {'test': TestClass()}

aspq = AsyncPriorityQueue(classDict)
aspq.addTask(15, testFunc2, 15)
aspq.addTask(15, testFunc2, 15)
aspq.addTask(27, testFunc2, 27)
aspq.addTask(27, testFunc2, 27)
aspq.addTask(89, testFunc2, 89)
aspq.addTask(91, testFunc2, 91)
aspq.addClassTask(96, 'test', 'testFunc', 96)
aspq.addClassTask(99, 'test', 'testFunc', 99)
aspq.processTasks()
print()

asrwq = AsyncReadWriteQueue(classDict)
asrwq.read(testFunc2, 15)
asrwq.write(testFunc2, 15)
asrwq.read(testFunc2, 27)
asrwq.read(testFunc2, 27)
asrwq.write(testFunc2, 89)
asrwq.write(testFunc2, 91)
asrwq.cdRead('test', 'testFunc', 94)
asrwq.cdWrite('test', 'testFunc', 97)
asrwq.processTasks()
