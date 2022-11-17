class BufferFile:
    def __init__(self, name, head = None, max_buff_file_elem = 0):
        self.name = name
        self.head = head
        self.max_elem = max_buff_file_elem
        self.content = []
        if self.head != None:
            self.head.elementsCount += 1
            head.files.append(self)

    def move(self, path):
        pass

    def delete(self):
        pass

    def push(self, element):
        pass

    def consume(self):
        pass

