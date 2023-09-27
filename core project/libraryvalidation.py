import re

def bookname(bookname1):
   check1=re.findall(r"^[A-Za-z]+",bookname1)
   if not check1:
      raise Exception("Error:Given name is invalid")
   if len(bookname1)<=3:
      raise Exception ("Error:Invalid name length")
   
def isbn_valid(isbn1):
   checkisbn=re.findall("^(?=(?:[^0-9]*[0-9]){10}(?:(?:[^0-9]*[0-9]){3})?$)[\\d-]+$",isbn1)
   if not checkisbn:
      raise Exception("Error:Invalid ISBN number:")

      
def author_validation(authorname1):
   check2=re.search( r"^[A-Za-z\s.]{3,20}$",authorname1)
   if not check2:
      raise Exception("Error:Wrong format name, name should be in words")

def copies(copies1):
   if not copies1.isdigit():
      raise Exception("Error:Copies should be in digits")
   elif len(copies1)>2:
      raise Exception("Error:Invalid Count")
   elif int(copies1)<0:
      raise Exception("Error:Invalid Count")

def id(memid):
   if not memid.isdigit():
      raise Exception("Error:Copies should be in digits")
   elif len(memid)<3 and len(memid)>3:
      raise Exception("Error:Invalid Count Id should be in 3digits")

def email_validation(email):
    check3= re.search(r"^[a-zA-Z][A-Za-z0-9._]+@[a-z]+\.[a-z]{3}$",email)
    if email=="":
        raise Exception("Error:empty input")
    elif email.isspace():
        raise Exception("Error:Empty space occurred")
    elif len(email)<10 or len(email)>35:
        raise Exception("Error:Invalid Email length, email lenght(min-10,max-35)format(ex:muthunaren695@gamil.com)")
    elif not check3:
        raise Exception("Error:Invalid Email,Give correct format(ex:narenchan695@gamil.com)")
    

def phno_validation(phno):
   if phno.isalpha():
      raise Exception("Error:Phone number should be in Digits")
   elif len(phno)>10:
      raise ValueError("Error:Invalid number")
   elif len(phno)<10:
      raise ValueError("Error:Invalid number")
   elif phno=="":
      raise ValueError("Error:Empty input")
   elif phno.isspace():
      raise Exception("Error:Empty space Occured")
   elif re.findall(r"[012345]{1}\d{9}",phno):
      raise Exception("Error:Invalid starting number error")
   
