import time

class ThreadController:
    ExitThread = True

    def start(self, threadName):
        self.ExitThread = False
        while self.ExitThread == False:
            print("do work")
            time.sleep(10)

    def stop(self):
        self.ExitThread = True

