import generatedetails
import memberdetails
import borrowreturn
def main():
   while True:
      print("=="*30)
      print("\t\tLIBRARY MANAGEMENT SYSTEM")
      print("=="*30)
      
      print("1. Add a book\n2. Update a book\n3. Delete a book\n4. Search for a book\n"
            "5. Add a member\n6. Update a member\n7. Delete a member\n8. Search for a member\n9. Borrow a book\n"
         "10. Return a book\n11. Generate book availability report\n12. Generate member borrowing history report\n13. Generate overdue book report\n14. Over-view books\n15. Exit")
      
      choice=input("Enter Your Choice:")
      if choice=="1":
         generatedetails.gen.add_book()
         
      elif choice=="2":
         generatedetails.gen.update_book()
         
      elif choice=="3":
         generatedetails.gen.delete_book()
      
      elif choice=="4":
         generatedetails.gen.searchbook()
      
      elif choice=="5":
         generatedetails.gen.add_member()
      
      elif choice=="6":
         generatedetails.gen.update_member()
      
      elif choice=="7":
         generatedetails.gen.delete_member()
   
      elif choice=="8":
         generatedetails.gen.search_member()
         
      elif choice=="9":
         generatedetails.gen.borrow_books()
      
      elif choice=="10":
         generatedetails.gen.return_book_withoutfine()
   
      elif choice=="11":
         generatedetails.gen.generate_book()
   
      elif choice=="12":
         generatedetails.gen.borrow_history()
      
      elif choice=="13":
         generatedetails.gen.overdue_report()

      elif choice=="14":
         generatedetails.gen.overview_books()
         
      elif choice=="15":
         break
      else:
         print("Wrong choice")
           

main()         






