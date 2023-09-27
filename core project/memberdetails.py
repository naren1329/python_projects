import datetime
import bookdetails
import libraryvalidation
class Member_details(bookdetails.Book_details):


   def add_member(self):
      self.member_details={}
      while True:
         try:
            member_name=input("Enter member name:")
            libraryvalidation.bookname(member_name)
            break
         except Exception as e:
            print(e)
            
      member_address=input("Enter member address:")

      ph=1
      while ph:
         try:
            member_phno=input("Enter member phone number:")
            libraryvalidation.phno_validation(member_phno)
            if self.all_member_details != {}:
               for x,y in self.all_member_details.items():
                  if member_phno != y["memberphno"]:
                     ph=0
                  else:
                     print("Phno already exist")
            else:
               ph=0
         except Exception as e:
            print(e)
            
      em=1
      while em:
         try:
            member_email=input("Enter member email address:")
            libraryvalidation.email_validation(member_email)
            if self.all_member_details != {}:
               for x,y in self.all_member_details.items():
                  if member_email != y["memberemail"]:
                     em=0
                  else:
                     print("Email already exist")
            else:
               em=0
         except Exception as e:
            print(e)

      mid=1      
      while mid:
         try:
            member_id=input("Enter MemberId:")
            libraryvalidation.id(member_id)
            if self.all_member_details != {}:
               for x,y in self.all_member_details.items():
                  if member_id != y["memberid"]:
                     mid=0
                  else:
                     print("Email already exist")
                     mid=1
            else:
               mid=0
         except Exception as e:
            print(e)

      mb=1
      while mb:
         formatdate='%Y-%m-%d'
         try:
            member_dob=input("Enter birth date(yyyy-mm-dd):")
            d=datetime.datetime.strptime(member_dob,formatdate).date()
            mb=0
         except ValueError:
            print("Invalid date. Date format(yyyy-mm-dd)")
            
      print("*************************")
      print("Member added successfully")
      print("*************************")
      print("Name:",member_name)
      print("Address:",member_address)
      print("Phone number:",member_phno)
      print("Email address:",member_email)
      print("Member Id:",member_id)
      print("Member DOB:",member_dob)
      self.member_details["membername"]=member_name
      self.member_details["memberaddress"]=member_address
      self.member_details["memberphno"]=member_phno
      self.member_details["memberemail"]=member_email
      self.member_details["memberid"]=member_id
      self.member_details["memberdob"]=member_dob
      self.all_member_details[member_id]=self.member_details
      print(self.all_member_details)

   def update_member(self):
      if self.all_member_details != {}:
         um=1
         while um:
            try:
               mem_id=input("Enter member ID to update:")
               libraryvalidation.id(mem_id)
               for i,j in self.all_member_details.items():
                  if mem_id in i:
                     print("*name\n*address\n*phone number\n*email Id\n*Exit")
                     choice=input(f"What you want to update for Member Id {mem_id} ?")
                     
                     for k,mem_dict in self.all_member_details.items():
                        if k == mem_id:
                           if choice=="name":
                              while True:
                                 try:
                                    mem_name=input("Enter New Name:")
                                    libraryvalidation.bookname(mem_name)
                                    mem_dict.update({"membername":mem_name})
                                    print("---------------------------------")
                                    print("Member name updated successfully")
                                    print("---------------------------------")
                                    break
                                 except Exception as e:
                                    print(e)
                              
                           elif choice=="address":
                              mem_address=input("Enter New Address:")
                              mem_dict.update({"memberaddress":mem_address})
                              print("-------------------------------------")
                              print("Member address updated successfully")
                              print("-------------------------------------")
                              
                           elif choice=="phone number":
                              while True:
                                 try:
                                    mem_phno=input("Enter New Phone number:")
                                    libraryvalidation.phno_validation(mem_phno)
                                    mem_dict.update({"memberphno":mem_phno})
                                    print("-----------------------------------------")
                                    print("Member Phone number updated successfully")
                                    print("-----------------------------------------")
                                    break
                                 except Exception as e:
                                    print(e)
                                    
                           elif choice=="email Id":
                              while True:
                                 try:
                                    mem_email=input("Enter new Emailid")
                                    libraryvalidation.email_validation(member_email)
                                    break
                                 except Exception as e:
                                    print(e)
                              mem_dict.update({"memberemail":mem_email})
                              print("--------------------------------------")
                              print("Member Email id updated successfully")
                              print("--------------------------------------")

                           elif choice=="exit":
                              um=0
                           else:
                              print("Enter Correct option, same as given option")
                  
                  else:
                     print("Wrong member Id")
               um=0
            except Exception as e:
               print(e)
      else:
         print("There is no member in member details")

   def delete_member(self):
      if self.all_member_details != {}:
         dm=1
         while dm:
            try:
               del_id=input("Enter member Id to delete:")
               libraryvalidation.id(del_id)
               if del_id in self.all_member_details:
                  print("\n===Reason===")
                  print("\na. Mis behaviour\nb. Theaft a Book from library\nc. Not alive\nd. Not following the Rules\nde. Others")
                  choice=input("Enter the Choice:").lower()
                  if choice == "a" or choice == "b" or choice == "c" or choice == "d":
                     del self.all_member_details[del_id]
                     print("\n_____________________________")
                     print("Member deleted successfully")
                     print("_____________________________")
                     dm=0
                  elif choice == "e":
                     others=input("Enter your decision:")
                     del self.all_member_details[del_id]
                     print("\n_____________________________")
                     print("Member deleted successfully")
                     print("_____________________________")
                     dm=0
               else:
                  print("MemberId not found")
            except Exception as e:
               print(e)
      else:
         print("There is no member in member details")
         
         

   def search_member(self):
      if self.all_member_details != {}:
         sm=1
         while sm:
            try:
               search_id=input("Enter member ID to search:")
               libraryvalidation.id(search_id)
               for i,j in self.all_member_details.items():
                  if search_id in i:
                     if search_id == j["memberid"]:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Name:",j["membername"])
                        print("Address:",j["memberaddress"])
                        print("Phone Number:",j["memberphno"])
                        print("Email Address:",j["memberemail"])
                        print("Member ID:",j["memberid"])
                        print("Member DOB:",j["memberdob"])
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        sm=0
                     else:
                        sm=1
               if sm==1:
                  print("Member Id not found")
              
            except Exception as e:
               print(e)
      else:
         print("There is no member in member details")

           
mem=Member_details()
