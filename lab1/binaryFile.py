class BinaryFile:
    def __init__(self, name, head = None, content = None):
        self.name = name
        self.head = head
        self.content = content
        if self.head != None:
            self.head.elementsCount += 1
            head.files.append(self)

    def move(self, path):
        pass

    def delete(self):
        pass

    def readContent(self):
        pass