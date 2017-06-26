import asyncio
from AsyncPQ import AsyncPriorityQueue, AsyncReadWriteQueue

async def testFunc(arg): 
	await asyncio.sleep(0)
	print(arg)

aspq = AsyncPriorityQueue()
aspq.addTask(15, testFunc, 15)
aspq.addTask(15, testFunc, 15)
aspq.addTask(27, testFunc, 27)
aspq.addTask(27, testFunc, 27)
aspq.addTask(89, testFunc, 89)
aspq.addTask(91, testFunc, 91)
aspq.processTasks()
print()

asrwq = AsyncReadWriteQueue()
asrwq.read(testFunc, 15)
asrwq.write(testFunc, 15)
asrwq.read(testFunc, 27)
asrwq.read(testFunc, 27)
asrwq.write(testFunc, 89)
asrwq.write(testFunc, 91)
asrwq.processTasks()
