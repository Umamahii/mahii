import multiprocessing
import time
#process class
class Process(multiprocessing.Process):
    def __int__(self,id):
        super(Process, self).__init__()
        self.id=id
    def run(self):
        time.sleep(1)
        print("I'm the process with id: {}".format(self.id))
if __name__ == '__main__':
        p=Process(0)
        p.start()
        p.join()
        p=Process(1) 
        p.start()
        p.join()