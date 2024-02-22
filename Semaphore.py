from threading import Semaphore, Thread
from time import sleep

class SharedResource:
    def __init__(self):
        self.resource=[0]
        self.semaphore = Semaphore(10)
    def get(self):
        return self.resource
    def do_something(self,id):
        self.semaphore.acquire()
        self.__countMembers(id)
        self.semaphore.release()
    def __countMembers(self,id):
        self.resource[0]+=1
        if(self.resource[0]>10):
            print("producer",id,"crash")
        else:
            print("producer",id,"counter",self.resource[0])
        sleep(0.01)
        self.resource[0]-=1

class Producer :
        def __init__(self, id,sharedResource):
            self.id = id
            self.thread = Thread(target=self.produce)
            self.sharedResource=sharedResource
        def run(self):
            self.thread.start()
        def produce(self):
            self.sharedResource.do_something(self.id)


        def join(self):
            self.thread.join() 

    
if __name__ == "__main__":
    sharedResource=SharedResource()
    producers=[Producer(i,sharedResource)for i in range(100)]
    for p in producers:
        p.run()
    for p in producers:
        p.join()
    print(sharedResource.get())
