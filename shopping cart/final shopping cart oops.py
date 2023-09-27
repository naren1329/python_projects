"""
NAME-D.MUTHU NARENDRAN
PROJECT NAME-ONLINE SHOPPING CART
CREATED DATE-3.7.2023
MODIFIED DATE-

"""

#Import Modules
import random
import re
from tabulate import tabulate

#Create CUSTOMER class as a PARENT CLASS
class Customer:
   
   #These are all instance variable
   def __init__(self):
      self.customer_id=""
      self.customer_name=""
      self.customer_phno=""
      self.user={}
      self.item_dict={"1.Milk":150,"2.Bread":99,"3.Egg":150}
      self.product=[]
      self.prod_price=[]
      
      
   #Signup Funtion 
   def sign_up(self):
      print("\n\t***************Please Enter the following details***************")
      print("\n"+("="*30))
      print("\nAvailable Locations are:")
      print("\n"+("="*30))
      print("\n  Adayar\n  Besent nagar\n  Indra nagar\n  T-nagar\n")

      marketname="AbC online supermarket"
      name=marketname[0:3]
      idno=random.randint(1000,9999)
      area_dict={"adayar":"Ad","besent nagar":"Bn","indra nagar":"In","t-nagar":"Tn"}
      
      #Location Validation
      while True:
         try:
            self.location=input("Please choose Location:").lower()
            if self.location.isdigit():
               raise Exception("Error:Location should be in words")
            elif self.location=="":
               raise Exception("Error:Empty Input")
            elif self.location.isspace():
               raise Exception("Error:Empty space Occurred")
            elif self.location not in area_dict:
               raise Exception("Error:Your Address is not available")
            else:
               if self.location in area_dict.keys():
                  s=area_dict[self.location]
                  self.customer_id=name+str(idno)+s
                  print("Your Customer Id is:",self.customer_id)
                  break
         except Exception as e:
            print(e)
         
      #Customer Name validation
      while True:
         try:
            self.customer_name=input("Enter Your Name:")
            if self.customer_name.isdigit():
               raise Exception("Error:Name should be in words")
            elif len(self.customer_name)<=2:
               raise Exception("Error:Name length error")
            elif self.customer_name=="":
               raise Exception("Error:Empty Input")
            elif self.customer_name.isspace():
               raise Exception("Error:Empty space Occurred")
            elif not self.customer_name.isalpha():
               raise Exception ("Error:Wrong format Name")
            else:
               break
         except Exception as e:
            print(e)

      #Customer phno validation      
      while True:
         try:
            self.customer_phno=input("Enter Your Phno:")
            if self.customer_phno.isalpha():
                raise Exception("Error:Phone number should be in Digits")
            elif len(self.customer_phno)>10:
                raise ValueError("Error:Invalid number")
            elif len(self.customer_phno)<10:
               raise ValueError("Error:Invalid number")
            elif self.customer_phno=="":
                 raise ValueError("Error:Empty input")
            elif self.customer_phno.isspace():
                raise Exception("Error:Empty space Occured")
            elif re.findall(r"[012345]{1}\d{9}",self.customer_phno):
                raise Exception("Error:Invalid starting number error")
            else:
               break
         except Exception as e:
            print(e)

      #Assigning Values for SELF USER dictionary      
      self.user["Location"]=self.location      
      self.user["CustomerName"]=self.customer_name      
      self.user["CustomerId"]=self.customer_id
      self.user["CustomerPhno"]=self.customer_phno
      print("\nHELLO",self.customer_name.upper())
      print(self.user)

   #Signin Function
   def sign_in(self):
      
      #This empty list for using tabulate printing
      temp_item=[]
      temp_price=[]
      if self.user != {}:
         
         while True:
            cust_id=input("Enter Customer's id:")
            
            if cust_id == self.user["CustomerId"]:
               print("\nAdd Products to the cart")
               print("\nList of available items for shopping")
               
               for i,j in self.item_dict.items():
                  temp_item.append(i)
                  temp_price.append(j)
               item_data=[[key,value] for key,value in self.item_dict.items()]
               
               while True:
                  #Tabulate printing
                  print(tabulate(item_data,headers=["ITEM","PRICE"],tablefmt='grid'))
                  
                  choice1=input("Enter item number to add to cart(press 'q' to quit):")
                  if choice1 == "1" or choice1 == "2" or choice1== "3":
                     if len(self.item_dict)>=int(choice1):
                        quantity=input("Enter quantity:")
                        
                        #Getting item name (milk or bread or egg)
                        item=temp_item[int(choice1)-1]

                        #This Logic for already enter product in list
                        if item in self.product:
                           for count,values in enumerate(self.product):
                              if values==item:
                                 self.prod_price[count] += self.item_dict[item]*int(quantity)
                                 print("\n{}, added to the cart.Total price Rs.{}".format(item,self.prod_price[count]))
                        else:
                           #This logic for first time enter product 
                           price=self.item_dict[item]*int(quantity)
                           self.product.append(item)
                           self.prod_price.append(price)
                           print("\n{}, added to the cart.Total price Rs.{}".format(item,price))
                     else:
                        print("Wrong Choice")
                        
                  
                  elif choice1 =="q" or choice1 =="Q":
                     break
                  else:
                     print("Please enter the correct choice")
               break 
            else:
               print("Wrong customer Id")
      else:
         print("No user")
       
class Discount_item(Customer):

   def __init__(self):
      self.discount_dict={"1.Sugar":40,"2.Rice":50,"3.Atta":60}
      super().__init__()

   def discount(self):

      #This empty list for using tabulate printing
      temp_discount_item=[]
      temp_discount_price=[]
      header=["ITEM","QUANTITY","DISCOUNT"]
      name=["Sugar","Sugar","Rice","Rice","Aata","Aata"]
      kg=["1kg","5kg","10kg","25kg","5kg","10kg"]
      dis=["5%","10%","4%","8%","6%","12%"]
      table=zip(name,kg,dis)
      print("Discount Products Available..")
      choice2=input("Do you want to Purchase(y/n):").lower()
      if choice2=="y":
         print(tabulate(table,headers=header,tablefmt='grid'))
         print("List of availabel items for shopping")
         
         for i,j in self.discount_dict.items():
            temp_discount_item.append(i)
            temp_discount_price.append(j)
         discount_data=[[key,value] for key,value in self.discount_dict.items()]
         
         discount_item_price=[]
         discount_item=[]
         while True:

            #Tabulate printing
            print(tabulate(discount_data,headers=["ITEM","PRICE"],tablefmt='grid'))
            choice3=input("Enter item number to add to cart(press 'q' to quit):")
            
            if choice3 == "1" or choice3 == "2" or choice3== "3":
               dic_quantity=input("Enter quantity:")
               dis_item=temp_discount_item[int(choice3)-1]

               #This Logic for already enter product in list
               if dis_item in self.product:
                  for dcount,dvalues in enumerate(self.discount_dict):
                     if dvalues==dis_item:
                        self.prod_price[dcount] += self.discount_dict[dis_item]*int(dic_quantity)
                        if dvalues == "1.Sugar":
                           if int(dic_quantity)>=1 and int(dic_quantity)<=4:
                              d=int(dic_quantity)*(self.discount_dict[dis_item]-(self.discount_dict[dis_item]*0.05))
                           elif int(dic_quantity)>=5:
                              d=int(dic_quantity)*(self.discount_dict[dis_item]-(self.discount_dict[dis_item]*0.1))
                        if dvalues == "2.Rice":
                           if int(dic_quantity)<=10:
                              d=int(dic_quantity)*(self.discount_dict[dis_item]-(self.discount_dict[dis_item]*0.04))
                           elif int(dic_quantity)>=25:
                              d=int(dic_quantity)*(self.discount_dict[dis_item]-(self.discount_dict[dis_item]*0.08))
                           else:
                              d=int(dic_quantity)*self.discount_dict[dis_item]
                        if dvalues == "3.Atta":
                           if int(dic_quantity)<=5:
                              d=int(dic_quantity)*(self.discount_dict[dis_item]-(self.discount_dict[dis_item]*0.06))
                           elif int(dic_quantity)>=10:
                              d=int(dic_quantity)*(self.discount_dict[dis_item]-(self.discount_dict[dis_item]*0.12))
                           else:
                              d=int(dic_quantity)*self.discount_dict[dis_item]
   
                  print("\n{}, added to the cart.Total price Rs.{}".format(dis_item,d))
         
               else:

                  #This logic for first time enter product
                  for dcount,dvalues in enumerate(self.discount_dict):
                     if dvalues==dis_item:
                        if dvalues == "1.Sugar":
                           if int(dic_quantity)>=1 and int(dic_quantity)<=4:
                              d=int(dic_quantity)*(self.discount_dict[dis_item]-(self.discount_dict[dis_item]*0.05))
                           elif int(dic_quantity)>=5:
                              d=int(dic_quantity)*(self.discount_dict[dis_item]-(self.discount_dict[dis_item]*0.1))
                        if dvalues == "2.Rice":
                           if int(dic_quantity)>=10 and int(dic_quantity)<=24:
                              d=int(dic_quantity)*(self.discount_dict[dis_item]-(self.discount_dict[dis_item]*0.04))
                           elif int(dic_quantity)>=25:
                              d=int(dic_quantity)*(self.discount_dict[dis_item]-(self.discount_dict[dis_item]*0.08))
                           else:
                              d=int(dic_quantity)*self.discount_dict[dis_item]
                        if dvalues == "3.Atta":
                           if int(dic_quantity)>=5 and int(dic_quantity)<=9:
                              d=int(dic_quantity)*(self.discount_dict[dis_item]-(self.discount_dict[dis_item]*0.06))
                           elif int(dic_quantity)>=10:
                              d=int(dic_quantity)*(self.discount_dict[dis_item]-(self.discount_dict[dis_item]*0.12))
                           else:
                              d=int(dic_quantity)*self.discount_dict[dis_item]


                  
               self.product.append(dis_item)
               self.prod_price.append(d)
               set1=set(self.product)
               set1=list(set1)
               self.p=[]
               for i in set1:
                  c=0
                  for j,k in zip(self.product,self.prod_price):
                     if i==j:
                        c+=k
                  self.p.append(c)
               
                    
               print("\n{}, added to the cart.Total price Rs.{}".format(dis_item,d))
      
            elif choice3=="q" or choice3=="Q":
               break
            else:
               print("Wrong Choice")
      elif choice2=="n":
         print("Not buying Discount products")

     
   #Location Function   
   def location1(self):
      
      delivery_charge=40
      print("\nAvailable delivery Location:")
      print("\n  Adayar\n  Besent nagar\n  Indra nagar\n  T-nagar\n")
      location_list=["adayar","besent nagar","indra nagar","tnagar"]
      while True:
         check_location=input("Enter Delivery location:").lower()
         if check_location in location_list:
            print("\nSorry, Online delivery option is not available")
            choice4=input("would you like to pick it up from our nearest store(y/n):")
            
            if choice4=="n":
               print("Delivery charges applied")
               #Append Delivery charge and total price for print in tabular coloumn
               self.prod_price.append(delivery_charge)
               self.product.append("Delivery Charge:")
               total=sum(self.prod_price)
               self.product.append("Total")
               self.prod_price.append(total)
               
            elif choice4=="y":
               total=sum(self.prod_price)
               self.product.append("Total")
               self.prod_price.append(total)
                  
            print("\nCustomer Name :",self.customer_name)
            print("\nCustomer Id :",self.customer_id)
            print("\nCustomer Phone no:",self.customer_phno)
            print("\nCustomer Location:",check_location)
            join=zip(self.product,self.prod_price)
            print(tabulate(join,headers=["ITEM","PRICE"],tablefmt='grid'))
            break
         else:
            print("Wrong location")
      else:
         print("NO user")
class Lucky_draw(Discount_item):
   def __init__(self):
      super(). __init__()
   
   def display(self):
      print(self.customer_name)
      print("\nNow it's time to spin the board...")
      print("\nAnd the result is")
      lucky_list=["new smartphone", "new helmet", "cookware", "flat 200" , "nothing Better Luck Next Time"]
      print("\nCongratulations! You have won ",random.choice(lucky_list))
      print("\nThank you for shopping with us and participating in the Lucky Draw. Have a great day!")


lucky=Lucky_draw()

def main():
   while True:
      print("~~"*20)
      print("\n\t**************Welcome to the Abc Online super market***************")
      print("\n\t\t\t"+("~~"*20))
      print(" \n\t1)Sign up(New user)\n\n\t2)Sign in\n\n\t3)Exit)")
      choice=input("Enter your choice:")
      if choice=="1":
        lucky.sign_up()
        
      elif choice=="2":
         if lucky.user !={}:   
            lucky.sign_in()
            lucky.discount()
            lucky.location1()
            lucky.display()
         else:
            print("No customer in shopping cart")
      
      elif choice=="3":
         print("Thankyou")
         break

      else:
         print("Enter the correct choice")


      
main()


      
     


























