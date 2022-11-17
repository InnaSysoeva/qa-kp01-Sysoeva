class LogFile:
    def __init__ (self, name, head = None):
        self.name = name
        self.head = head
        self.content = ''
        if self.head != None:
            self.head.elementsCount += 1
            head.files.append(self)

    def delete(self):
        pass

    def read(self):
        pass

    def move(self, path):
        pass

    def addLog(self, log):
        pass

