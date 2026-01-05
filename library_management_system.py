
class Book:

    def __init__(self,name,id,author):
        self.name=name
        self.id=id
        self.author=author

    def display(self):
        print("Name:",self.name)
        print("id:",self.id)
        print("author:",self.author)
        

class library_management:
    
    def __init__(self):
        self.books=[]

    def add_book(self):
        print("Add details of the books")
        name=input("Enter name of the book:")
        id=int(input("Enter id of the book:"))
        author=input("Enter author of the book:")
        book=Book(name,id,author)
        self.books.append(book)
        
    def view_books(self):
        if not self.books:
            print("Empty")
            return
        for b in self.books:
            Book.display(b)
        return

    def remove_book(self):
        id=int(input("Enter id of the book to update for:"))
        for b in self.books:
            if b.id==id:
               self.books.remove(b)
               print("book removed")
               return
        print("Book not found to remove")

    def find_book(self):
         id=int(input("Enter id of the book to update for:"))
         for b in self.books:
            if id==b.id:
                Book.display(b)
                return 
         print("Book not found:")
    def update_book(self):
        id=int(input("Enter id of the book to update for:"))
        for b in self.books:
             if id==b.id:
                b.name=input("Enter the name:")
                b.author=input("Enter the author:")
                print("Book updated successfully")
                return 
        print("Book not found")
 
def main():
    try:
        obj=library_management()
        while True:
          print("""Library Management System
             1. ADD BOOK
             2. VIEW BOOKS
             3. REMOVE BOOKS
             4. FIND BOOKS BY ID
             5. UPDATE BOOK
             6. EXIT""")

          choice=int(input("Enter the choice:"))
          if choice==1:
            obj.add_book()
          elif choice==2:
            obj.view_books()
          elif choice==3:
             obj.remove_book()
          elif choice==4:
             obj.find_book()
          elif choice==5:
             obj.update_book()
          elif choice==6:
             print("Exiting...")  
             return
          else:
            print("Invalid input given")
    except ValueError:
          print("Please enter the correct input")
if __name__=="__main__":
    main()


