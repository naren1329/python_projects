import datetime
import borrowreturn
import tabulate
import libraryvalidation

class Generate(borrowreturn.Borrow_return):
   def __init__(self):
      super().__init__()

   def generate_book(self):
      list2=[]
      while True:
         try:
            genre=input("Enter Genre:")
            libraryvalidation.bookname(genre)
            break
         except Exception as e:
            print(e)
      avai=""
      for g,genre_dict in self.all_book_details.items():
         if genre==genre_dict["genre"]:
            if int(genre_dict["copies_available"])>0:
               avai="available"
            else:
               avai="not available"
            list1=[genre_dict["booktitle"],genre_dict["author"],genre_dict["isbn"],avai]
            list2.append(list1)
      print(tabulate.tabulate(list2,headers=["title","author","isbn","availability"],tablefmt="grid"))

   def borrow_history(self):
      if self.br != {}:
         count=0
         while True:
            try:
               h_mem=input("Enter the member ID:")
               libraryvalidation.id(h_mem)
               break
            except Exception as e:
               print(e)
               
         for h,his_dict in self.all_member_details.items():
            if h==h_mem:
               count=1
               break
            else:
               count=0
         if count>0:
            print("Name:",his_dict["membername"])
            print("Address:",his_dict["memberaddress"])
            print("Phone:",his_dict["memberphno"])
            print("email:",his_dict["memberemail"])
            print(tabulate.tabulate(self.br[h_mem],headers=["TITLE","AUTHOR","ISBN","DATE BORROWED","DUE DATE"]))

         else:
            print("Member not Found")
      else:
         print("No borrowed book")
                    
   def overdue_report(self):
      olist=[]
      formatdate='%Y-%m-%d'
      while True:
         try:
            date=input("Enter date:")
            d=datetime.datetime.strptime(date,formatdate).date()
            break
         except ValueError:
            print("Invalid date")

      for m,n in self.br.items():
         for x in range(len(n)):
            if n[x][4]<d:
               olist.append(n[x])
      print(tabulate.tabulate(olist,headers=["TITLE","AUTHOR","ISBN","DATE BORROWED","DUE DATE"]))

         
   def overview_books(self):
      item1 = []
      
      for i,book_dict in self.all_book_details.items():
         item = list(book_dict.values())
         item1.append(item)
      #print(item1)
      print(tabulate.tabulate(item1,headers=["TITLE","AUTHOR","ISBN","GERNE","BOOK-ID","COPIES-AVAILABLE","COPIES-BORROWED","PRICE"],tablefmt='grid'))
      
      


gen=Generate()         
