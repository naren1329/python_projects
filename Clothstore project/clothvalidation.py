
import re

def name_valid(name):
   regex_pattern = r"^[A-Za-z\s]+$"
   if len(name)<0:
      raise Exception("Error:empty input")
   if not re.match(regex_pattern,name):
      raise Exception("Error:name should be in alphabets")
   
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
   regex=r"[6789]{1}\d{9}"
   if not re.match(regex,phno):
      raise Exception("Error:Invalid phone number")
   
      
def number_valid(value):
   if len(value)==0:
      raise Exception("Error:invalid value")
   elif not value.isdigit():
      raise Exception("Error:Value should be in digits")
   elif int(value) <=0:
      raise Exception("Error:Invalid value")
      
      
