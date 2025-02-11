from abc import ABC,abstractmethod
class IdatabaseOperations(ABC):
    @abstractmethod
    def insert(self,str):
        pass
    @abstractmethod
    def update(self,str):
        pass
    @abstractmethod
    def delete(self,str):
        pass

class sqldatabase(IdatabaseOperations):
    def insert(self,str):
        print(f"{str} has been inserted in the sqldatabase")
    def update(self, str):
        print(f"{str} has been updated in the sqldatabase")
    def delete(self,str):
        print(f"{str} has been deleted in the sqldatabase")


class nosqldatabase(IdatabaseOperations):
    def insert(self,str):
        print(f"{str} has been inserted in the nosqldatabase")
    def update(self, str):
        print(f"{str} has been updated in the nosqldatabase")
    def delete(self,str):
        print(f"{str} has been deleted in the nosqldatabase")

a1=sqldatabase()
a1.insert("hello")
a1.update("tom")
a1.delete("hello")


b1=nosqldatabase()
b1.update("tom")
b1.insert("hello")
b1.delete("hello")