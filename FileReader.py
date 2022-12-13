

class FileReader:

    def __init__(self,name,files):
        self.name=name
        self.files=files



    def read(self):
      f=open(self.files,'r')
      for i in f.readline():
          return  i;




