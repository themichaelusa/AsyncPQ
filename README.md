# AsyncPQ

A little exercise in concurrency. Super intuitive way to schedule asynchronous tasks with little overhead.

This library was originally being built for the Trinitum Trading Architecture to communicate with a 
[RethinkDB Instance](https://www.rethinkdb.com/docs/install/) and update the user's capital information 
every tick. But I think the idea is general enough to warrant a library of it's own.


## Installation
```
pip3 install AsyncPQ
```

## Documentation

### Example:

```python
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

asrwq = AsyncReadWriteQueue()
asrwq.read(testFunc, 15)
asrwq.write(testFunc, 15)
asrwq.read(testFunc, 27)
asrwq.read(testFunc, 27)
asrwq.write(testFunc, 89)
asrwq.write(testFunc, 91)
asrwq.processTasks()

...

Terminal Outputs:

91
89
27
27
15
15

91
89
15
27
27
15
```

## Use Cases
TBD

## TODO

- [ ] PyPI support (pip install...)
- [ ] Better Documentation!
