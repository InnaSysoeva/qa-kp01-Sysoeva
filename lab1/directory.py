class Directory:
    def __init__(self, name, dir_max_elem, head = None):
        self.head = head
        self.name = name
        self.dir_max_elem = dir_max_elem
        self.elementsCount = 0
        self.files = []
        if self.head != None:
            self.head.elementsCount += 1
            head.files.append(self)

    def delete(self):
        pass

    def move(self, path):
        pass

    def read(self):
        pass


