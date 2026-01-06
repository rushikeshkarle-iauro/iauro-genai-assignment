
class Book:    
    """This is Book class called When every single book is to be added"""
    def __init__(self,name,id,author):
        """This is constructor that assigns value to current instance"""
        self.name=name
        self.id=id
        self.author=author

    def display(self):
        """This function is used to display current book"""
        print("Name:",self.name)
        print("id:",self.id)
        print("author:",self.author)
        

class LibraryManagement:
    
    def __init__(self):
        """This is constructor called when objects are created"""
        self.books=[]

    def add_book(self):
        """This function is called to Add books in the List"""
        print("Add details of the books")
        name=input("Enter name of the book:")
        id=int(input("Enter id of the book:"))
        author=input("Enter author of the book:")
        book=Book(name,id,author)
        self.books.append(book)
        
    def view_books(self):
        """This function is used to view all the books"""
        if not self.books:
            print("Empty")
            return
        for b in self.books:
            Book.display(b)
        return

    def remove_book(self):
        """This function is used to remove books based on id"""
        id=int(input("Enter id of the book to update for:"))
        for b in self.books:
            if b.id==id:
               self.books.remove(b)
               print("book removed")
               return
        print("Book not found to remove")

    def find_book(self):
         """This function is used to find and display book based on Id"""
         id=int(input("Enter id of the book to update for:"))
         for b in self.books:
            if id==b.id:
                Book.display(b)
                return 
         print("Book not found:")

    def update_book(self):
        """This function is used to update books name and author"""
        id=int(input("Enter id of the book to update for:"))
        for b in self.books:
             if id==b.id:
                b.name=input("Enter the name:")
                b.author=input("Enter the author:")
                print("Book updated successfully")
                return 
        print("Book not found")
 
def main():
    """This is starting point of program execution"""
    try:
        obj=LibraryManagement()
        """Here object is created"""     
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
    """This is to define main method should be called first"""
    main()


