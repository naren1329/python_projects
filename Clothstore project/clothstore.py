"""
NAME          -D.MUTHU NARENDRAN
PROJECT NAME  -CLOTHSTORE PROJECT
CREATED DATE  -06/08/2023
MODIFIED DATE -
"""

import datetime
import tabulate
import clothvalidation
import mysql.connector


class Clothstore:
   
   def __init__ (self):
      self.data=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="naren@1329",
                                   database="newdatabase")
      self.cursor=self.data.cursor()
      self.cursor.execute("use newdatabase")
      self.cursor.execute("create table if not exists clothtable(cloth_id int primary key auto_increment,title varchar(20) not null,brand varchar(20),price float,category varchar(20),size varchar(5),stock_quantity int)auto_increment=101")
      date=datetime.datetime.now()
      self.currentdate=date.replace(microsecond=0)
      
   def error_log(self,time,error):
      file=open("Clothstore-error-file.txt","a+")
      file.write("\nError occured time is:{0} and error is :{1}".format(time,error))
      file.close()           
      
   
   def admin(self):
      print("\nWelcome to the Admin Page")
      
      admin_list=["naren","naren1329"]
      while True:
            admin_name=input("Enter Admin name:")
            if admin_name == admin_list[0]:
               break
            else:
               print("Invalid Admin name")
      while True:         
            admin_password=input("Enter admin password:")
            if admin_password == admin_list[1]:
               print("\nWelcome to the Clothing Store Inventory Management System!")
               print("\nPlease select an aperation:")
               while True:
                  print("\n1. Add clothing item\n2. Retrieve clothing item\n3. Update clothing item\n4. Remove clothing item\n5. View orders\n6. Exit")
                  choice=input("Enter your choice:")
                  #Add clothing item
                  if choice == "1":
                     while True:
                        try:
                           title=input("Enter the cloth name:")
                           clothvalidation.name_valid(title)
                           break
                        except Exception as e:
                           self.error_log(self.currentdate,str(e))
                           print(e)
                     while True:
                        try:
                           brand=input("Enter the cloth brand:")
                           clothvalidation.name_valid(brand)
                           break
                        except Exception as e:
                           self.error_log(self.currentdate,str(e))
                           print(e)
                           
                     while True:
                        try:
                           price=float(input("Enter the cloth price:"))
                           break
                        except ValueError:
                           self.error_log(self.currentdate,str(e))
                           print("Price should be in digits")
                        
                     while True:
                        try:
                           category=input("Enter the cloth category:")
                           clothvalidation.name_valid(category)
                           break
                        except Exception as e:
                           self.error_log(self.currentdate,str(e))
                           print(e)
                     sizelist=["S","M","L","XL","XXL","XXXL"]
                     while True:
                        size=input("Enter the cloth size:").upper()
                        if size in sizelist:
                           break
                        else:
                           print("Wrong size, size should be in(S,M,L,XL,XXL,XXXL)")
                     while True:
                        try:
                           stock_quantity=input("Enter the stock quantity:")
                           clothvalidation.number_valid(stock_quantity)
                           break
                        except Exception as e:
                           self.error_log(self.currentdate,str(e))
                           print(e)
                           
                     insert="insert into clothtable(title,brand,price,category,size,stock_quantity)values(%s,%s,%s,%s,%s,%s)"  
                     values=(title,brand,price,category,size,stock_quantity)  
                     self.cursor.execute(insert,values)
                     print("Row created successfully")
                     self.data.commit()
                     
                  #Retrive clothing item
                  if choice == "2":
                     view=self.cursor.execute("select * from clothtable")
                     fetch=self.cursor.fetchall()
                     print(tabulate.tabulate(fetch,headers=["cloth-id","title","brand","price","category","size","stock_quantity"],tablefmt='grid'))
                     self.data.commit()
                     
                  #Update clothing item
                  if choice == "3":
                     idlist=[]
                     cloth_id=self.cursor.execute("select cloth_id from clothtable")
                     fetch=self.cursor.fetchall()
                     for i in fetch:
                        for j in i:
                           idlist.append(j)
            
                     update_id=input("Enter which clothId do you want to change:")            
                     if int(update_id) in idlist:
                        print("Which field do you want to update:")
                        print("\na.Title\nb.Brand\nc.Price\nd.Category\ne.Size\nf.Stock-quantity")
                        choice=input("Enter a field to update:").lower()
                        if choice == "a":
                           while True:
                              try:
                                 update_title=input("Enter a new title:")
                                 clothvalidation.name_valid(update_title)
                                 update_field=(f"update clothtable set title=%s where cloth_id=%s")
                                 update_values=(update_title,update_id)
                                 self.cursor.execute(update_field,update_values)
                                 print("Updated Successfully")
                                 self.data.commit()
                                 break
                              except Exception as e:
                                 self.error_log(self.currentdate,str(e))
                                 print(e)

                        if choice == "b":
                           while True:
                              try:
                                 update_brand=input("Enter a new brand:")
                                 clothvalidation.name_valid(update_brand)
                                 update_field=(f"update clothtable set brand=%s where cloth_id=%s")
                                 update_values=(update_brand,update_id)
                                 self.cursor.execute(update_field,update_values)
                                 print("Updated Successfully")
                                 self.data.commit()
                                 break
                              except Exception as e:
                                 self.error_log(self.currentdate,str(e))
                                 print(e)
                        if choice == "c":
                           while True:
                              try:
                                 update_price=float("Enter a new price:")
                                 update_field=(f"update clothtable set price=%s where cloth_id=%s")
                                 update_values=(update_price,update_id)
                                 self.cursor.execute(update_field,update_values)
                                 print("Updated Successfully")
                                 self.data.commit()
                                 break
                              except ValueError:
                                 print("Price should be in point values")
                                 break
                        if choice == "d":
                           while True:
                              try:
                                 update_category=input("Enter a new category:")
                                 clothvalidation.name_valid(update_category)
                                 update_field=(f"update clothtable set category=%s where cloth_id=%s")
                                 update_values=(update_category,update_id)
                                 self.cursor.execute(update_field,update_values)
                                 print("Updated Successfully")
                                 self.data.commit()
                                 break
                              except Exception as e:
                                 self.error_log(self.currentdate,str(e))
                                 print(e)
                        if choice == "e":
                           while True:
                              try:
                                 update_size=input("Enter a new size:")
                                 if update_size in sizelist():
                                    update_field=(f"update clothtable set size=%s where cloth_id=%s")
                                    update_values=(update_size,update_id)
                                    self.cursor.execute(update_field,update_values)
                                    print("Updated Successfully")
                                    self.data.commit()
                                    break
                                 else:
                                    print("Wrong size, size should be in(S,M,L,XL,XXL,XXXL)")
                              except Exception as e:
                                 self.error_log(self.currentdate,str(e))
                                 print(e)
                        if choice == "f":
                           while True:
                              try:
                                 update_quantity=input("Enter a new quantity:")
                                 clothvalidation.number_valid(update_quantity)
                                 update_field=(f"update clothtable set stock_quantity=%s where cloth_id=%s")
                                 update_values=(update_quantity,update_id)
                                 self.cursor.execute(update_field,update_values)
                                 print("Updated Successfully")
                                 self.data.commit()
                                 break
                              except Exception as e:
                                 self.error_log(self.currentdate,str(e))
                                 print(e)

                     else:
                        print("Invalid Cloth Id")
                        
                  #Delete clothing item
                  if choice == "4":
                     idlist=[]
                     cloth_id=self.cursor.execute("select cloth_id from clothtable")
                     fetch=self.cursor.fetchall()
                     for i in fetch:
                        for j in i:
                           idlist.append(j)
                     
                     delete_id=input("Enter which id do you want to delete:")
                     if int(delete_id) in idlist:
                        delete=(f"delete from clothtable where cloth_id={delete_id}")
                        self.cursor.execute(delete)
                        print("Row deleted successfully")
                        self.data.commit()
                     else:
                        print("Invalid Cloth Id")

                  #View order
                  if choice == "5":
                     print("Total order")
                     self.cursor.execute("select * from p_history")
                     fetch=self.cursor.fetchall()
                     print(tabulate.tabulate(fetch,headers=["CUSTOMER-NAME","PHONE-NO","CLOTH-ID","CLOTH-NAME","CLOTH-SIZE","CLOTH-PRICE","CLOTH-QUANTITY","STATUS"],tablefmt='grid'))
                    
                  elif choice == "6":
                     break

               break
            else:
               print("Invalid Password")


class Customer(Clothstore):
   def __init__ (self):
      super().__init__()
      self.cursor.execute("create table if not exists customertable(customer_name varchar(20),\
                          ph_no bigint primary key not null,email varchar(30),cust_password varchar(8))")
      self.cursor.execute("create table if not exists purchase(p_custname varchar(20),p_phno bigint,p_clothid int \
                          ,p_clothname varchar(20),p_clothsize varchar(5),p_clothprice float,p_clothquantity int,status varchar(10) default 'notpaid')")
      
      self.current_name=''
      self.current_phno=''
   def register(self):
      while True:
         try:
            customer_name=input("Enter Customer name:")
            clothvalidation.name_valid(customer_name)
            break
         except Exception as e:
            self.error_log(self.currentdate,str(e))
            print(e)
            
      while True:
         phone=[]
         self.cursor.execute("select ph_no from customertable")
         fetch=self.cursor.fetchall()
         for i in fetch:
            for j in i:
               phone.append(j)      
         try:
            print(type(phone[0]))
            ph_no=input("Enter your Phone-number:")
            clothvalidation.phno_validation(ph_no)
            if int(ph_no) not in phone:
               break
            else:
               print("phone number already exist")
               
         except Exception as e:
            self.error_log(self.currentdate,str(e))
            print(e)
            
      while True:
         try:
            email=input("Enter your email:")
            clothvalidation.email_validation(email)
            break
         except Exception as e:
            self.error_log(self.currentdate,str(e))
            print(e)
      while True:
         try:
            cust_password=input("Enter your password:")
            if len(cust_password)<6 or len(cust_password)>8:
               raise Exception("Error:password should be in more than 6 charecter to 8 charecter")
            else:
               break
         except Exception as e:
            self.error_log(self.currentdate,str(e))
            print(e)
      insert="insert into customertable(customer_name,ph_no,email,cust_password)values(%s,%s,%s,%s)"
      values=(customer_name,ph_no,email,cust_password)
      self.cursor.execute(insert,values)
      self.data.commit()

   def browse_clothing(self):
      while True:
         print("\nBROWSE CLOTHING ITEMS")
         print("\n1.Overview Clothes\n2.Brand\n3.Size\n4.Category\n5.Price\n6.Exit")
         choice=input("Enter your choice:")
         
         if choice =="1":
            view=self.cursor.execute("select cloth_id,title,brand,price,category,size from clothtable")
            fetch=self.cursor.fetchall()
            if fetch != []:
               print(tabulate.tabulate(fetch,headers=["cloth-id","title","brand","price","category","size",],tablefmt='grid'))
               self.data.commit()
            else:
               print("There is no cloth stock in store")
               
         if choice =="2":
            while True:
               try:
                  view_brand=input("Enter which brand items do you want:")
                  clothvalidation.name_valid(view_brand)
                  break
               except Exception as e:
                  self.error_log(self.currentdate,str(e))
                  print(e)
            view="select cloth_id,title,brand,price,category,size from clothtable where brand=%s"
            value=(view_brand,)
            self.cursor.execute(view,value)
            fetch=self.cursor.fetchall()
            if fetch != []:
               print(tabulate.tabulate(fetch,headers=["cloth-id","title","brand","price","category","size",],tablefmt='grid'))
               self.data.commit()
            else:
               print("There is no cloth stock in store")
               
         if choice =="3":
            while True:
               sizelist=["S","M","L","XL","XXL","XXXL"]
               view_size=input("Enter which size items do you want:").upper()
               if view_size in sizelist:
                  break
               else:
                  print("Wrong size, size should be in(S,M,L,XL,XXL,XXXL)")
            view="select cloth_id,title,brand,price,category,size from clothtable where size=%s"
            value=(view_size,)
            self.cursor.execute(view,value)
            fetch=self.cursor.fetchall()
            if fetch !=[]:
               print(tabulate.tabulate(fetch,headers=["cloth-id","title","brand","price","category","size"],tablefmt='grid'))
               self.data.commit()
            else:
               print("There is no cloth stock in store")
               
         if choice =="4":
            while True:
               try:
                  view_category=input("Enter which category items do you want:")
                  clothvalidation.name_valid(view_category)
                  break
               except Exception as e:
                  self.error_log(self.currentdate,str(e))
                  print(e)
            view="select cloth_id,title,brand,price,category,size from clothtable where category=%s"
            value=(view_category,)
            self.cursor.execute(view,value)
            fetch=self.cursor.fetchall()
            if fetch != []:
               print(tabulate.tabulate(fetch,headers=["cloth-id","title","brand","price","category","size",],tablefmt='grid'))
               self.data.commit()
            else:
               print("There is no cloth stock in store")

         if choice =="5":
            while True:
               print("\na.Price(low-high)\nb.Price(high-low)")
               choice=input("Enter a choice:").lower()
               if choice == "a":
                  self.cursor.execute("select * from clothtable order by price asc")
                  fetch=self.cursor.fetchall()
                  print(tabulate.tabulate(fetch,headers=["cloth-id","title","brand","price","category","size",],tablefmt='grid'))
                  break
               if choice == "b":
                  self.cursor.execute("select * from clothtable order by price desc")
                  fetch=self.cursor.fetchall()
                  print(tabulate.tabulate(fetch,headers=["cloth-id","title","brand","price","category","size",],tablefmt='grid'))
                  break
               
         if choice =="6":
            break
   
   def add_cart(self):
                          
      addlist=[]
      view=self.cursor.execute("select cloth_id from clothtable")
      fetch=self.cursor.fetchall()
      for i in fetch:
         for j in i:
            addlist.append(j)
      view=self.cursor.execute("select cloth_id,title,brand,price,category,size from clothtable")
      fetch=self.cursor.fetchall()
      print(tabulate.tabulate(fetch,headers=["cloth-id","title","brand","price","category","size",],tablefmt='grid'))
      self.data.commit()
      if addlist != []:
         clothlist=[]
         list1=[]
         ac=1
         while ac:
            choice=input("Press 1 to continue, Q to exit:")
            if choice == "1":
               clothid=input("Enter the cloth-id to purchase:")
               select="select p_clothid from purchase where p_phno=%s"
               value=(self.current_phno,)
               self.cursor.execute(select,value)
               fetch=self.cursor.fetchall()
               for i in fetch:
                  for j in i:
                     list1.append(j)

               view="select stock_quantity from clothtable where cloth_id=%s"
               value=(clothid,)
               self.cursor.execute(view,value)
               fetch=self.cursor.fetchall()
               for i in fetch:
                  for j in i:
                     s_quantity=j
               
                     
               view="select p_clothquantity from purchase where p_clothid=%s and p_phno=%s"
               value=(clothid,self.current_phno)
               self.cursor.execute(view,value)
               fetch=self.cursor.fetchall()
               for i in fetch:
                  for j in i:
                     f_quantity=j
                     
               if int(clothid) not in list1:
                  if int(clothid) in addlist:
                     
                     view="select cloth_id,title,brand,price,category,size,stock_quantity from clothtable where cloth_id=%s"
                     value=(clothid,)
                     self.cursor.execute(view,value)
                     fetch=self.cursor.fetchall()
                     for i in fetch:
                           clothlist.append(list(i))
                           while True:
                              try:
                                 quantity=input("Enter the quantity to purchase")
                                 clothvalidation.number_valid(quantity)
                                 if int(quantity) < fetch[0][6]:
                                    insert="insert into purchase(p_custname,p_phno,p_clothid,p_clothname,p_clothsize,p_clothprice,p_clothquantity)values(%s,%s,%s,%s,%s,%s,%s)"      
                                    values=(self.current_name,self.current_phno,fetch[0][0],fetch[0][1],fetch[0][5],fetch[0][3],int(quantity))
                                    self.cursor.execute(insert,values)
                                    
                                    
                                    """ 
                                    update_stock=s_quantity-int(quantity)
                                    update_clothtable="update clothtable set stock_quantity=%s where cloth_id=%s"
                                    value=(update_stock,clothid)
                                    self.cursor.execute(update_clothtable,value)
                                    print("Item added to the cart...")
                                    """
                                    self.data.commit()
                                    break
                                    ac=0
                                 else:
                                    print("Entered quantity is more than available quantity")
                              except Exception as e:
                                 print(e)
                         
                  else:
                     print("Invalid cloth id")              
               else:
                  tr=1                
                  while tr:
                        try:
                           quantity1=input("Enter the quantity to else-purchase:")
                           view="select stock_quantity from clothtable where cloth_id=%s"
                           value=(clothid,)
                           self.cursor.execute(view,value)
                           fetch=self.cursor.fetchall()
                           for i in fetch:
                              for j in i:
                                 j
                           if int(quantity1) < j:
                              total_quantity=int(f_quantity)+int(quantity1)
                              total_update="update purchase set p_clothquantity=%s where p_clothid=%s and p_phno=%s"
                              value=(total_quantity,clothid,self.current_phno)
                              self.cursor.execute(total_update,value)
                              """
                              update_stock=s_quantity-total_quantity
                              update_clothtable="update clothtable set stock_quantity=%s where cloth_id=%s"
                              value=(update_stock,int(clothid))
                              self.cursor.execute(update_clothtable,value)
                              print("Item added to the cart...")
                              """
                              self.data.commit()
                              tr=0
                           else:
                              print("Entered quantity is more than available quantity")
                              tr=1
                        except Exception as e:
                           self.error_log(self.currentdate,str(e))
                           print(e)
               
            elif choice == "q" or choice == "Q":
                ac=0
            else:
               print("invalid choice")
      else:
         print("No clothes in store")

   def view_cart(self):
         
               
         view=("select p_clothid,p_clothname,p_clothsize,p_clothprice,p_clothquantity,(p_clothprice * p_clothquantity)as totalprice from purchase where p_phno=%s")
         value=(self.current_phno,)
         self.cursor.execute(view,value)
         fetch=self.cursor.fetchall()
         print(tabulate.tabulate(fetch,headers=["CLOTH-ID","CLOTH-NAME","CLOTH-SIZE","PRICE","QUANTITY","TOTAL PRICE"],tablefmt='grid'))
         self.data.commit()
      
         
   def checkout(self):
      view=("select p_clothquantity,p_clothid from purchase where p_phno=%s")
      value=(self.current_phno,)
      self.cursor.execute(view,value)
      fetch=self.cursor.fetchall()
      
      view=("select p_clothid,p_clothname,p_clothsize,p_clothprice,p_clothquantity,(p_clothprice * p_clothquantity)as totalprice from purchase where p_phno=%s")
      value=(self.current_phno,)
      self.cursor.execute(view,value)
      fetch=self.cursor.fetchall()
      print(tabulate.tabulate(fetch,headers=["CLOTH-ID","CLOTH-NAME","CLOTH-SIZE","PRICE","QUANTITY","TOTAL PRICE"],tablefmt='grid'))
      total=("select sum(p_clothprice * p_clothquantity) from purchase where p_phno=%s")
      value1=(self.current_phno,)
      self.cursor.execute(total,value1)
      fetch=self.cursor.fetchall()
      for i in fetch:
         for j in i:
            j
      print("Total price:",j)
      
      pay=input("Do you want to pay(yes/no):").lower()
      if pay == "yes":
         view=("update clothtable as ct join purchase as pt on ct.cloth_id=pt.p_clothid set ct.stock_quantity=(ct.stock_quantity-pt.p_clothquantity) where p_phno=%s")
         value=(self.current_phno,)
         self.cursor.execute(view,value)
         self.data.commit()

         self.cursor.execute("create table if not exists p_history as select * from purchase")
         self.data.commit()
         c_update=("update p_history set status='paid' where p_phno=%s")
         c_value=(self.current_phno,)
         self.cursor.execute(c_update,c_value)
         self.data.commit()
         c_delete=("delete from purchase where p_phno=%s")
         c_delete_value=(self.current_phno,)
         self.cursor.execute(c_delete,c_delete_value)
         self.data.commit()
         print(self.current_phno)

         print("Check out Successfully")
      elif pay == "no":
         print("You can't buy your products")
      else:
         print("Wrong choice")

   def login(self):
      
      cust=input("Enter your email or phone number:")
      cusomers=("select customer_name,ph_no,email,cust_password from customertable where ph_no=%s or email=%s")
      values=(cust,cust)
      self.cursor.execute(cusomers,values)
      fetch=self.cursor.fetchall()
      print(fetch)
      if fetch != []:
         if cust == fetch[0][1] or fetch [0][2]:
               password =input("Enter your password:")
               if password == fetch[0][3]:
                  self.current_name=fetch[0][0]
                  self.current_phno=fetch[0][1]
                  while True:
                     print("\n Welcome to the clothing store")
                     print("\n1.Browse clothing item\n2.Add item cart\n3.View cart\n4.Checkout\n5.Exit")
                     choice=input("Enter your choice:")
                     if choice == "1":
                        self.browse_clothing()
                        
                        

                     elif choice == "2":
                        self.add_cart()
                        
                        
                     elif choice =="3":
                        self.view_cart()
                        
                        
                     elif choice =="4":
                        self.checkout()
                        
                     
                     elif choice == "5":
                        print("Thankyou")
                        break
                     else:
                        print("Invalid Password")
               
      else:
         print("Invalid phone number or email")
      
            
   def main(self):
      
      while True:
         print("\nWelcome to Clothing store")
         print("\n1.Register \n2.Login \n3.Exit")
         choice=input("Enter Your Option:")
         if choice == "1":
            self.register()
            
         elif choice == "2":
            self.login()
            
         elif choice == "3":
            print("Thankyou")
            break
         else:
            print("wrong Choice")
            
   


cloth=Customer()
while True:
   print("\nWelcome to Clothing store")
   print("\n1.ADMIN\n2.CUSTOMER\n3.EXIT")
   choice=input("Enter your choice(1 or 2):")
   if choice == "1":
      cloth.admin()
   elif choice == "2":
      cloth.main()
   elif choice == "3":
      print("Thankyou")
      break
   else:
      print("Wrong choice")

 
