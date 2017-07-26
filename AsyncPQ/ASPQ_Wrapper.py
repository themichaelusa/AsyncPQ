import asyncio

class AsyncPQWrapper(object):

	def __init__(self):
		self.queue = []

	class Unit(object):
	
		def __init__(self, functionRef, fArgs, priority):
			
			self.funcRef = functionRef
			self.funcArgs = fArgs
			self.priority = priority

	def addQUnit(self, functionRef, fArgs, priority):
		self.queue.append(self.Unit(functionRef, fArgs, priority))

	def preprocessUnits(self):

		units = [self.queue.pop() for u in range(len(self.queue))]
		if (len(units) == 0): return None
		taskloop = asyncio.new_event_loop()
		asyncio.set_event_loop(taskloop)
		return (units, taskloop)

	def processUnits(self): pass

class AsyncRWQueue(AsyncPQWrapper):
	
	def __init__(self): 
		super().__init__()
		self.WRITE_PRIORITY = 1
		self.READ_PRIORITY = 0

	def processUnits(self):

		units, taskloop = self.preprocessUnits()
		wUnits = list(filter(lambda x: x.priority == self.WRITE_PRIORITY, units))
		rUnits = list(filter(lambda x: x.priority == self.READ_PRIORITY, units))
		wTasks, rTasks = [], []

		for unit in wUnits:
			wTasks.append(asyncio.ensure_future(unit.funcRef(*unit.funcArgs)))
		for unit in rUnits:
			rTasks.append(asyncio.ensure_future(unit.funcRef(*unit.funcArgs)))

		wFuture, rFuture = asyncio.gather(*wTasks), asyncio.gather(*rTasks)
		taskloop.run_until_complete(wFuture)
		rValues = taskloop.run_until_complete(rFuture)
		taskloop.stop()
		taskloop.close()

		if (len(rValues) == 1): return rValues[0]
		else: return tuple(rValues[::-1])
		
class AsyncPQueue(AsyncPQWrapper):
	
	def __init__(self): super().__init__()

	def processUnits(self):

		units, taskloop = self.preprocessUnits()
		uPriorList = sorted(list(set([unit.priority for unit in units])))[::-1]
		sortedUnits = [list(filter(lambda x: x.priority == u, units)) for u in uPriorList]
		
		sFutures, rValues = [], []
		for sUnit in sortedUnits:
			sortedTasks = []
			for unit in sUnit:
				sortedTasks.append(asyncio.ensure_future(unit.funcRef(*unit.funcArgs)))
			sFutures.append(asyncio.gather(*sortedTasks))
		
		for sFuture in sFutures:
			rValues.append(taskloop.run_until_complete(sFuture))

		taskloop.stop()
		taskloop.close()	
		