import mysql.connector 

mydb=mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password="12345",
    database="collage", 
)

#collage Administration data Management system
mycursor=mydb.cursor()

print("collage Administration data Management system")

print("****Welcome to Anand institute of higher technology****")

def register_system():
    print("Welcome to Register page")
    academic = input("enter your are domain student or staff or admin:")
    academic = academic.lower()
    if academic == "student":
        print("Welcome student")
        global student_id,student_name,student_password,student_phoneno
        student_id=input("Enter your student_id:")
        student_password= (input("Enter your password:"))
        student_name=input("Enter your student_name:")
        student_phoneno= int(input("Enter your phone number:"))
        print("Register successfully!!")
    elif academic == "staff":
        print("Welcome sir/mam")
        global staff_id,staff_name,staff_password
        staff_id=input("Enter your staff_id:")
        staff_password=input("Enter your password:")
        staff_name=input("Enter your staff_name:")
        print("Register successfully!!")
    elif academic == "admin":
        print("welcome admin") 
        global admin_id,admin_password 
        admin_id=input("Enter your admin_id:")
        admin_password=input("Enter your admin_password:")
        print("Register successfully!!")  
    else:
        print("your enter incorrect option")
        register_system()
register_system() 

# i have write the student function top because in login function i have call student function

def student():
    student_page = int(input("1.view profile\n2.Give complaint\n3.library(books you want)\n4.exit\nselect your option you want:"))
    if student_page == 1:
        print(f"welcome to your profile:\nyour name:{student_name}\nyour id:{student_id}\nyour phone number:{student_phoneno}")
        print("your data are stored in database")       
    elif student_page == 2:
        complaint = input("Enter your complaint collage management take action:") 
        print(f"{complaint} - your complaint stored in database")
    elif student_page == 3:
        book = input("Enter your book name you want:")
        print(f"if the {book} is available we will call your number you come and take book in library")
        print("your data are stored in database")       
    elif student_page == 4:
        exit()
    else:
        print("please enter valid option 1 to 5")
        student()
 

def login_system():
    print("Welcome to Login page")
    login = int(input("1.student_login\n2.staff_login\n3.admin\n4.exit\nchoose login option:"))
    if login == 1:
        id=input("Enter your student_id:")
        password = input("Enter your password:")
        if id == student_id and password == student_password :
            print(f"welcome {student_name} you have login successfully")
            student()
        else:
            print("incorrect check your password and id please enter correctly")
    elif login == 2:
        id=input("Enter your staff_id:")
        password = input("Enter your password:")
        if id == staff_id and password == staff_password:
            print(f"welcome {staff_name} you have login successfully")
        else:
            print("incorrect check your password and id please correctly")    
    elif login == 3:
        id=input("Enter your admin_id:")
        password = input("Enter your password:")
        if id == admin_id and password == admin_password:
            print(f"welcome admin you have login successfully")
        else:
            print("incorrect check your password and id enter correctly")   
    elif login == 4:
        exit()
    else:
        print("please choose correct option between 1 to 4")
        login_system()    
login_system()

#sql commands
# only created one table with 4 columns
sql="insert into student_database(student_id,student_name,student_password,student_phoneno) values(%s,%s,%s,%s)" 
val=(student_id,student_name,student_password,student_phoneno) 
mycursor.execute(sql,val) 
mydb.commit()    




