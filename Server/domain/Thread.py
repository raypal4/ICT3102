import threading


class Thread(threading.Thread):
    def __init__(self, threadID, name, controller):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.controller = controller

    def run(self):
        print("Starting " + self.name)
        self.controller.start(self.name)
        print("Exiting " + self.name)
