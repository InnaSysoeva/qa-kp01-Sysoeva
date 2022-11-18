class FileSystem:
    def __init__(self, name, max_el):
        self.name = name
        self.dirs = []
        self.files = []
        self.elementsCount = 0
        self.max_el = max_el
    
    def addFile(self, file):
        if(self.max_el == self.elementsCount):
            print('File system is full.')
            return
        self.files.append(file)
        self.elementsCount += 1
