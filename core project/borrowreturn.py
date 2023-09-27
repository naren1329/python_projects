import datetime
from datetime import timedelta
import memberdetails
import libraryvalidation
class Borrow_return(memberdetails.Member_details):

   def __init__(self):
      super().__init__()
      self.br={}
     
      
   def borrow_books(self):
      self.total_bisbn = []
      self.bisbn=[]
      #self.br={}
      temp_memid = ""
      temp_key = ""
      temp = 1
      while temp:
         choice=input("Enter 1 to continue or q to exit:").lower()
         
         if choice=="1":
            flag = 1
            while flag:
               count = 0
               count1=0
               try:
                  memid=input("Enter member id:")
                  libraryvalidation.id(memid)
                  if self.all_member_details != {}:
                     for i,j in self.all_member_details.items():
                        
                        if memid in i:
                           bn=1
                           while bn:
                              try:
                                 borrowed_isbn=input("Enter Book ISBN to be returned(ex-978-1-45688-123-8):")
                                 libraryvalidation.isbn_valid(borrowed_isbn)
                                 for c,bookdict in self.all_book_details.items():
                                    temp_key = c
                                    if borrowed_isbn==bookdict["isbn"]:
                                       pr=1
                                       while pr:
                                          print("\nYou should pay the 50% book amount",(int(bookdict["price"])//2))               
                                          choice=input("Do you want to pay, y/n:").lower()
                                          if choice=="y":
                                             today=datetime.date.today()
                                             due=today+timedelta(days=7)
                                             bbook=bookdict["booktitle"]
                                             bauthor=bookdict["author"]
                                             print("\nBook borrowed successfully on",today,"Due Date:",due)
                                             print("Return Book on before Due Date. Incase of late return, you should pay fine - Rs.25 /day")
                                             self.bisbn.append(bbook)
                                             self.bisbn.append(bauthor)
                                             self.bisbn.append(borrowed_isbn)
                                             self.bisbn.append(today)
                                             self.bisbn.append(due)
                                             count = 1
                                             count1=0
                                             pr=0
                                             bn = 0
                                             
                                          elif choice=="n":
                                             print("\nYou cant borrow a book")
                                             pr=0
                                             bn=0
                                             flag = 0
                                             count =0
                                             count1=0
                                             
                                          else:
                                             print("Wrong choice")
                                             pr=1
                                             count = 0
                                             count1=0
                                       
                                    else:
                                       count = 1
                                       
                              except Exception as e:
                                 print(e)         
                        else:
                           count1=1
                     if count1 > 0:
                        flag = 0
                     else:
                        print("Member Id not found")
                           
                     if count > 0:
                        self.all_book_details[temp_key]["copies_available"]-=1
                        #print(self.all_book_details[temp_key]["copies_available"])
                        self.all_book_details[temp_key]["copies_borrowed"]+=1
                        #print(self.all_book_details[temp_key]["copies_borrowed"])
                        print(self.all_book_details)
                        self.br[memid]=self.total_bisbn
                        temp_memid = memid

                     
                     if temp_memid != "":
                        if memid != temp_memid:
                           self.total_bisbn = []
                     self.total_bisbn.append(self.bisbn)
                     self.bisbn = []
                     bn=0
                          
               except Exception as e:
                  print(e)
     
               
               
         elif choice=="q":
            temp = 0
         else:
            print("Wrong choice")
                           

   def return_book_withoutfine(self):
      temp_key=''
      print(self.br)
      if self.br != {}:
         while True:
            try:
               self.re_mem_id=input("Enter member ID:")
               libraryvalidation.id(self.re_mem_id)
               break
            except Exception as e:
               print(e)
               
         for e,return_dict in self.br.items():
            temp_key=e
            if e==self.re_mem_id:
               while True:
                  try:
                     self.re_isbn=input("Enter Book ISBN to be returned(ex-978-1-45688-123-8):")

                     libraryvalidation.isbn_valid(self.re_isbn)
                     break
                  except Exception as e:
                     print(e)
                     
               for x in range(len(return_dict)):
                  if self.re_isbn == return_dict[x][2]:
                     year=int(input("enter returned year:"))
                     month=int(input("enter returned month:"))
                     date=int(input("enter returned date:"))
                     self.re_date = datetime.date(year, month, date)
                     print("Book returned successfully on",self.re_date)
                     if self.re_date > return_dict[x][4]:
                        day=(self.re_date-return_dict[x][4]).days
                        fine=day*25
                        print("Overdue Fine:",fine)
                  count=0
                  
            else:
               count=1
         if count>0:
            self.all_book_details[temp_key]["copies_available"]+=1
            #print(self.all_book_details[temp_key]["copies_available"])
            self.all_book_details[temp_key]["copies_borrowed"]-=1
            #print(self.all_book_details[temp_key]["copies_borrowed"])
            print(self.all_book_details)

      else:
         print("No book borrowed")
         
         
      
brb=Borrow_return()







