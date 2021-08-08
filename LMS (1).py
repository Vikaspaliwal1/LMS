import  random

class Admin():
    def __init__(self):
        self.admin={}
        self.borrowers={}
        self.library={}
        
    def add_book(self):
        x=int(input("how many types of book you want to add in our library: "))
        
        for i in range(x):
            a={}
            book=input("Enter the book name you want to add in library: ")
            book_id=random.randint(5000,10000)
            book_title=(input("Enter the Title of that book: ")).title()
            book_Author=input("Enter the author of the book: ")
            book_total_pages=int(input("Enter total number of pages of book: "))
            book_quantity=int(input("Quantity of that book: "))
            book_ISBN=int(input("Enter 13 digit ISBN Number: "))
            book_published_year=int(input("Enter the book published year: "))
            
            
            
            a[book]=[book_id,book_title,book_Author,book_total_pages,book_quantity,book_ISBN,book_published_year]
            self.library.update(a)
            
        print("Successfully Added")
       
        
    def book_details(self):
        a=input("Enter the name of the book you want to see details: ")
        b=[i for i in self.library.keys()]
        if a in b:
            details=self.library[a]
            print(f"1.Name of the Book:{a} \n2.Book_id ={details[0]} \n3.Title of the Book={details[1]} \n4.Author of the Book:{details[2]} \n5.Total page in book:{details[3]} \n6.Book Quantity:{details[4]} \n7.Book_ISBN={details[5]} \n8.Publish Year:{details[6]}")
            
        else:
            print("Sorry! the book that you try to find is not in our Library or check the spelling again!!!!")
    def show(self):
        print(self.library)
        
    def book_edit(self):
        q=int(input("Enter the book_id which you want to edit: "))
        a=input("Please enter the book name for verification: ")
        b=[i for i in self.library.keys()]
        if a in b:
            details=self.library[a]
            bool=True
            while bool:
                choice=int(input("1.enter 1 for change the book_name: \n2.enter 2 for change the title: \n3.enter 3 for Author name: \n4.enter 4 for Total no of Pages: \n5.enter 5 for change the book_Published_year: \n6.press 6 for exit "))
                if choice == 1:
                    x=input("enter the New name for book: ")
                    a=x
                    print("Successfully edited")
                elif choice == 2:
                    x=input("enter the new_title for book: ")
                    self.library[a][1]=x
                    print("Successfully edited")
                elif choice == 3:
                    x=input("enter the new Author_name for book: ")
                    self.library[a][2]=x
                    print("Successfully edited")
                    
                elif choice == 4:
                    x=input("enter the new total no. of pages for book: ")
                    self.library[a][3]=x
                    print("Successfully edited")
                elif choice == 5:
                    x=input("enter the new_book_published_year: ")
                    self.library[a][4]=x
                    print("Successfully edited")
                elif choice == 6:
                    bool=False
                else:
                        print("Invalid Choice!!!!!")
        else:
            print("You entered wrong Book_id !!!!!!")
    
    def book_delete(self):
        q=int(input("Enter the book_id which you want to edit: "))
        a=input("Please enter the book name for verification: ")
        b=[i for i in self.library.keys()]
        if a in b:
            del self_library[a]
            print("Deleted Successfully")
        else:
            print("You entered wrong book_id!!!!")
    
    def book_issued(self):
        i=input("Enter book_name you want to borrow: ")
        book_issued={}
        if i in self.library.keys():
            if self.library[i][4]>0:
                date=input("Enter today date: ")
                print("NOTICE: if you return book after 15 days, you will get fine ")
                
                print("Book Issued....")
                self.library[i][4]-=1
                book_issued[i]=[date,]
                
            else:
                print("the book quantity is over!!!!")
                
            
        else:
            print("The book you are looking for is not in our library!!!! ")
            
        
    def user_profile(self):
        print(self.borrowers)
    
    
    
    def login(self):
        i=input("admin or borrower:")
        if i == 'admin':
            a=input("please,enter your mail: ")
            b=input("please, Enter your password : ")
            i=[i for i in self.admin.keys()]
            if a in self.admin:
                ans= True
                while ans:
                    print("\n")
                    print("Yes!, you are an admin")
                    print("\nwhat you want to do")
                    i=int(input("What you want to do, here is the list:\n1.enter 1 to add_book: \n2.enter 2 to edit book: \n3.enter 3 to view book_details: \n4.enter 4 to view book present in our library: \n5.enter 5 for delete a book: \n6.enter 0 to exit "))
                    if i == 1:
                        self.add_book()
                    elif i == 2:
                        self.book_edit()
                    elif i == 3:
                        self.book_details()
                    elif i == 4:
                        self.show()
                    elif i == 5:
                        self.delete()
                    elif i == 0:
                        ans=False
                    else:
                        print("Invalid choice!!!!")
                    
                
            
            
            
        elif i=='borrower':
            a=input("please,enter your mail: ")
            b=input("please, Enter your password : ")
            i=[i for i in self.borrowers.keys()]
            if a in i:
                print("Yes! you are a borrower.")
                print("\n what you want to do")
                ans=True
                while ans:
                    print("\n")
                    print("yes, you are a valid user")
                    i=int(input("1.enter 1 to show profile \n2.enter  to borrow a book \n3.enter 3 to view book detail \n4.enter 3 to view borrowed_book book detail \n5.enter 0 to exit"))
                    if i == 1:
                        self.user_profile()
                    
                    elif i == 2:
                        self.book_issued()
                    elif i == 3:
                        self.book_detail()
                    elif i == 4:
                        pass
                    elif i == 0:
                        ans =False
                    else:
                        print("Invalid choice!!!!")
                        
            
            
            
       
            
            
        else:
            print("Sorry!Please,login again!!!!")
            
        
        
    def signup(self):
        i =input("admin or borrower : ")
        if i == 'admin':
            a={}
            name=input("Enter full name: ")
            phone=int(input("Enter phone number: "))
            email=input("Enter email: ")
            password=input("Enter password: ")
            a[email]=[phone,name,password]
            self.admin.update(a)
            print("Signup Successfully!!!!")
        
        elif i =='borrower':
            a={}
            name=input("Enter name: ")
            DOB=input("enter date of birth: ")
            phone=int(input("Enter phone number: "))
            email=input("Enter email: ")
            password=input("Enter password: ")
            a[email]=[DOB,phone,name,password]
            self.borrowers.update(a)
        
        else:
            print("Invalid choice!!!!!")
            
        
        
        
    
        
        
        
    def menu(self):
        print("You need to signup first!!!")
        ans= True
        while ans:
            
            i=input("login or signup or exit ?")
            if i == 'login':
                self.login()
            elif i == "signup":
                self.signup()
            elif i == "exit":
                print("THANK YOU!! VISIT AGAIN")
                ans=False
            else:
                print("Invalid input!!!!!")
       
            
        
        
                    
                    
                        
                    
                
                    
        
                  
                
a=Admin()
a.menu()                   
        
    
    