import random
import libraryvalidation
class Book_details:

   def __init__(self):
      self.all_book_details = {'en100': {'booktitle': 'english', 'author': 'james', 'isbn': '978-1-45688-123-8', 'genre': 'subject', 'bookid': 'en100',
                                          'copies_available': 5, 'copies_borrowed': 0, 'price': '200'},
                               'ta209': {'booktitle': 'tamil', 'author': 'valluvar', 'isbn': '978-1-45688-123-1', 'genre': 'subject',
                                         'bookid': 'ta209', 'copies_available': '4', 'copies_borrowed': 0, 'price': '200'},
                               'tr674': {'booktitle': 'transformers', 'author': 'james', 'isbn': '978-1-45688-123-8', 'genre': 'action',
                                         'bookid': 'tr674', 'copies_available': '4', 'copies_borrowed': 0, 'price': '150'}}
      
      self.all_member_details={'111': {'membername': 'naren', 'memberaddress': 'madurai', 'memberphno': '8667554723', 'memberemail': 'naren@gmail.com',
                                        'memberid': '111', 'memberdob': '1997-07-13'},
                                '222': {'membername': 'nagaraj', 'memberaddress': 'melur', 'memberphno': '9685742514', 'memberemail': 'nagaraj@gmail.com',
                                        'memberid': '222', 'memberdob': '2000-07-22'}}
      

   def add_book(self):
      tempbook=[]
      tempdetails=[]
      self.bookdetails={}
      book=1
      while book:
         try:
            booktitle=input("Enter the title of the book:")
            libraryvalidation.bookname(booktitle)
            if self.all_book_details != {}:
               for x,y in self.all_book_details.items():
                  if booktitle != y["booktitle"]:
                     book = 0
                  else:
                     print("already exist")
                     book=1
            else:
               book = 0
         except Exception as e:
            print(e)   
        
     
     
      while True:
         try:
            author=input("Enter the author of the book:")
            libraryvalidation.author_validation(author)
            break
         except Exception as e:
            print(e)
      ns=1
      while ns:
         try:
            isbn=input("Enter the ISBN of the book(ex-978-1-45688-123-8):")
            libraryvalidation.isbn_valid(isbn)
            if self.all_book_details != {}:
               for x,y in self.all_book_details.items():
                  if isbn != y["isbn"]:
                     ns=0
                  else:
                     print("ISBN already exist")
            else:
               ns=0
         except Exception as e:
            print(e)
            
      while True:
         try:
            genre=input("Enter the genre of the book:")
            libraryvalidation.bookname(genre)
            break
         except Exception as e:
            print(e)
        
      name=booktitle[0:2]
      ranid=random.randint(111,999)
      book_id=name+str(ranid)
      print("your Book-ID:",book_id)

      while True:
         try:
            rate=input("Enter the book price:Rs.")
            if rate.isalpha():
               raise Exception("Error:Price should be in digits")
            elif int(rate)<50:
               raise Exception("Error:invalid price,price should be more than 50")
            else:
               break
         except Exception as e:
            print(e)
               
      
      while True:
         try:
            copies_available=input("Enter the number of copies available:")
            libraryvalidation.copies(copies_available)
            break
         except Exception as e:
            print(e)
     
      copies_borrowed=0
            
      self.bookdetails["booktitle"]=booktitle
      self.bookdetails["author"]=author
      self.bookdetails["isbn"]=isbn
      self.bookdetails["genre"]=genre
      self.bookdetails["bookid"]=book_id
      self.bookdetails["copies_available"]=copies_available
      self.bookdetails["copies_borrowed"]=copies_borrowed
      self.bookdetails["price"]=rate
      self.all_book_details[book_id] = self.bookdetails
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
      print("\nBook added successfully")
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print(self.all_book_details)

   def update_book(self):
      up=1
      while up:
         count=0
         update_bookid=input("Enter the ID of the book:")
         if self.all_book_details != {}: 
            for i,j in self.all_book_details.items():
               if update_bookid in i:
                  count=1
                  break
               else:
                  count=0
            if count>0:
               up=0
            else:
               print("Wrong bookId")
                  
         else:
            print("There is no book in library")
      ui=1            
      while ui:
         try:
            update_isbn=input("Enter the ISBN of the book(ex-978-1-45688-123-8):")
            libraryvalidation.isbn_valid(update_isbn)
            for i,j in self.all_book_details.items():
               if i == update_bookid:
                  if update_isbn == j["isbn"]:
                     ui=0
                  else:
                     print("Invalid ISbn ")
         except Exception as e:
            print(e)
      ch=1      
      while ch:      
         print("\nUpdate menu")
         print("\n1.booktitle\n2.Author\n3.Genre\n4.Price\n5.Copies available\n6.exit")
         choice=input("Which option do you want to change:")

         if choice=="1":
            book=1
            while book:
               try:
                  new_booktitle=input("Enter the new title of the book:")
                  if len(new_booktitle)==0 or new_booktitle.isspace():
                     raise Exception("Error:Book name is empty:")
                  else:
                     self.all_book_details[update_bookid].update({"booktitle":new_booktitle})
                     book=0
               except Exception as e:
                  print(e)   
                 
         if choice=="2":      
            while True:
               try:
                  new_author=input("Enter new author:")
                  libraryvalidation.author_validation(new_author)
                  self.all_book_details[update_bookid].update({"author":new_author})
                  break
               except Exception as e:
                  print(e)
                  
         if choice=="3":
            while True:
               try:
                  new_genre=input("Enter new Genre:")
                  libraryvalidation.bookname(new_genre)
                  self.all_book_details[update_bookid].update({"genre":new_genre})
                  break
               except Exception as e:
                  print(e)

         if choice=="4":
            while True:
               try:
                  new_rate=input("Enter the book price:Rs.")
                  if new_rate.isalpha():
                     raise Exception("Error:Price should be in digits")
                  elif int(new_rate)<0:
                     raise Exception("Error:invalid price")
                  else:
                     self.all_book_details[update_bookid].update({"price":new_rate})
                     break
               except Exception as e:
                  print(e)
               
                  

         if choice=="5":
            while True:
               try:
                  new_copies=input("Enter New Number of Copies:")
                  libraryvalidation.copies(new_copies)
                  self.all_book_details[update_bookid].update({"copies_available":new_copies})
                  break
               except Excetion as e:
                  print(e)
         if choice=="6":
            ch=0
         print("----------------------------")
         print("\nBook update Successfully")
         print("----------------------------")

         
         for y,item in self.all_book_details.items():
            if y==update_bookid:
               print("----------------------------")
               print("Title:",self.all_book_details[y]["booktitle"])
               print("Author:",self.all_book_details[y]["author"])
               print("ISBN:",self.all_book_details[y]["isbn"])
               print("Genre:",self.all_book_details[y]["genre"])
               print("BookID:",self.all_book_details[y]["bookid"])
               print("Price:",self.all_book_details[y]["price"])
               print("Number of Copies available:",self.all_book_details[y]["copies_available"])
               print("----------------------------")
         
      
   def delete_book(self):
      if self.all_book_details != {}:
         up=1
         while up:
            
               delete_bookid=input("Enter the ID of the book:")
             
               for i,j in self.all_book_details.items():
                  if delete_bookid in i:
                     up=0
                  else:
                     print("Wrong bookId")
            
         ui=1            
         while ui:
            try:
               delete_isbn=input("Enter the ISBN of the book(ex-978-1-45688-123-8):")
               libraryvalidation.isbn_valid(delete_isbn)
               for i,j in self.all_book_details.items():
                  if i == delete_bookid:
                     if delete_isbn == j["isbn"]:
                        count = 0
                        break
                     else:
                        count = 1
                        print("Book not found to Delete")
               if count == 0:
                  choice=input("Do you want to delete this book (yes/no):").lower()
                  if choice == "yes":
                     del self.all_book_details[i]
                     print("____________________________")
                     print("Book Deleted successfully")
                     print("____________________________")
                     ui=0
                  elif choice == "no":
                     print("____________________")
                     print("Book not Deleted")
                     print("____________________")
                     ui=0
                  else:
                     print("Wrong Choice")
            except Exception as e:
               print(e)
      else:
         print("There is no book in library")
      
   def searchbook(self):
      if self.all_book_details != {}:
         up=1
         while up:
            search_bookid=input("Enter the ID of the search book:")
            if self.all_book_details != {}: 
               for i,j in self.all_book_details.items():
                  if search_bookid in i:
                     if search_bookid ==j["bookid"]:
                        print("`````````````````````````````````````")
                        print("Title:", j["booktitle"])
                        print("Author:", j["author"])
                        print("ISBN:", j["isbn"])
                        print("Genre:", j["genre"])
                        print("Price:",j["price"])
                        print("Copies available:", j["copies_available"])   
                        print("`````````````````````````````````````")
                        up=0
                     else:
                        print("Book not found to Search")
                  else:
                     print("Wrong bookId")

            else:
               print("There is no book in library")
               up=0
      else:
         print("There is no book in library")

book=Book_details()
