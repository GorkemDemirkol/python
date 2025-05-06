a=[10,20,30,40,50,True,"2x",100]
print(a[0:3])
print(type (a[3]))

queue = []
queue.append("a")
queue.append("b")
queue.append("c")
queue.append("d")
queue.append("e")

print("initial queue:",queue)
queue.pop(0)
print("after pop:",queue)

from collections import deque
q=deque()
q.append("1")
q.append("2")
q.append("3")
q.append("4")
q.append("5")
print("initial queue:",q)
print(q.popleft())


from queue import Queue
q=Queue(maxsize=5)
print(q.qsize())
q.put("x")
q.put("y")
q.put("z")
q.put("v")
q.put("t")
print("full:",q.full())

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())

print(q.put(6))
print(q.empty())
print(q.qsize())
print(q.get())
#fifo first in first out
