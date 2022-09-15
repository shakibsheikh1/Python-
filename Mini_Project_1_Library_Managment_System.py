"""Library Managment System"""

class Library:
    def __init__(self,list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}
    def displayBook(self):
        print(f"we have following books in our library{self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book : user})
            print("lander book databse  has been updated.you can take the book ")
        else:
            print(f"book is already being used by{self.lendDict[book]}")
    def addBook(self,book):
        self.bookList.append(book)
        print("book has been added to the book list ")
    def returnBook(self,book):
        self.lendDict.pop(book)
if __name__ == '__main__':
    jerry = Library(['python', 'rich dad and poor dad', 'c++ basid','django ',
                     'algorithm by clrs'],"jerrylibrianier")
    while True:
        print(f"welcome to the {jerry.name} library.Enter your choice")
        print("1. Display a book")
        print("2. Lend  a book")
        print("3. Add  a book")
        print("4. Return  a book")
        user_choice = int(input())
        if user_choice ==1:
            jerry.displayBook()
        elif user_choice ==2:
            book = input("Enter the book you want to lend")
            user = input("Enter your name")
            jerry.lendBook(user,book)
        elif user_choice==3:
            book = input("Enter the book want to add ")
            jerry.addBook(book)
        elif user_choice==4:
            book= input("Enter the book want to remove..")
            jerry.returnBook(book)
        else:
            print("Not valid choice ..")

        print("Press c to continue and q to quite ")
        user_choice1 = input("Enter your choice")
        if user_choice1 =="q":
            exit()
        elif user_choice1 =="c":
            continue
        else:
            break


