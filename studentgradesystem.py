def Student_grades():
    name=input("enter name here")
    rollno=input("enter roll no here")

    if not (rollno.isdigit() and len(rollno)<30):
       print("invalid roll no.")   


    maths=int(input("enter maths marks"))    
    science=int(input("enter science marks"))
    computer=int(input("enter computer marks"))
    if not(0 <= maths <= 100 and  0 <= science <= 100 and 0 <= computer <= 100):
       print(" envalid numbdr enter between 1-100")
    
    total = maths + science + computer
    average= total/3
   
    if average >= 90:
            grade ='A+'
    elif average >= 80:
            grade ='A'  
    elif average >= 70:
            grade ='B+'
    elif average >= 60:
            grade ='B'
    elif average >= 50:
            grade ='C+'
    elif average >= 40:
            grade ='C'
    else:
            grade ='fail' 
    
    print("\n" + "-"*45)
    print("|{:^43}|".format("Student Grades"))
    print("-"*45)
    print(f"| name    : {name:<33}|")
    print(f"| rollno. : {rollno:<33}|")
    print(f"| maths   : {maths:<33}|")
    print(f"| science : {science:<33}|")
    print(f"| computer: {computer:<33}|")
    print(f"| total   : {total:<33}|")
    print(f"| average : {average:<33}|")
    print(f"| Grade   : {grade:<33}|")
    print("-"*45)
    
   
    
Student_grades()


   