from queue import PriorityQueue
from time import sleep
from threading import Thread

class Producer :
        def __init__(self, id, buffer):
            self.id = id
            self.buffer = buffer
            self.thread = Thread(target=self.produce)
        def run(self):
            self.thread.start()
        def produce(self):
            for i in range(100):
                self.buffer.put((self.id,i))
                sleep(0.01)
        def join(self):
            self.thread.join() 


class Consumer:
        def __init__(self, id, buffer):
            self.id = id
            self.buffer = buffer
            self.thread = Thread(target=self.consume)
            self.end=[False]
        
        def run(self):
            self.thread.start()
        def consume(self):

            while not self.end[0]:
                print("consumer",self.id,"got",self.buffer.get(), self.buffer.qsize())
                sleep(0.01)
        def join(self):
            self.thread.join()

if __name__ == "__main__":
    buffer = PriorityQueue(7)
    producers = [Producer(i,buffer) for i in range(2)]
    consumers = [Consumer(i,buffer) for i in range(1)]
    for p in producers:
        p.run()
    for c in consumers:
        c.run()
    for p in producers:
        p.join()
    for c in consumers:
        c.end[0]=True
        c.join()
    print("done")
