class Directory:
    def __init__(self, name, dir_max_elem, head = None):
        self.head = head
        self.name = name
        self.dir_max_elem = dir_max_elem
        self.elementsCount = 0
        self.files = []
        if self.head != None:
            if(self.head.elementsCount == self.head.dir_max_elem):
                print('Directory is full. Now this file has no root directory.')
                self.head = None
                return
            self.head.elementsCount += 1
            head.files.append(self)

    def delete(self):
        i = 0
        while(i < self.head.elementsCount):
            if(self.name == self.head.files[i].name):
                self.head.files.pop(i)
                self.head.elementsCount -= 1
            i += 1
        print(self.name + ' was deleted from ' + self.head.name)
        del self

    def move(self, path):
        if(path.elementsCount == path.dir_max_elem):
            print('Impossible to add files.')
            return
        if self.head == None:
            self.head = path
            # file = Directory(self.name, self.dir_max_elem)
            self.head = path
            path.elementsCount += 1
            path.files.insert(path.elementsCount, self) #file
        else:
            i = 0
            while(i < self.head.elementsCount):
                if(self.name == self.head.files[i].name):
                    self.head.files.pop(i)
                    self.head.elementsCount -= 1
                i += 1

            self.head = path
            path.elementsCount += 1
            path.files.insert(path.elementsCount, self)

    def read(self):
        i = 0
        while(i < self.elementsCount):
            print("file name: " + self.files[i].name)
            i += 1


