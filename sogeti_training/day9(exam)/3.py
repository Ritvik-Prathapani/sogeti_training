class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display(self):
        print(f"book name: {self.title}\nbook author: {self.author}\nisbn :{self.isbn}")

mybook=Book('python','ritvik',1245)
mybook.display()