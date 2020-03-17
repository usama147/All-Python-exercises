strFname = input("Please enter first name ")  # Allows user to enter first name
strLname = input("Please enter last name ")  # Allows user to enter last name

int = int(input("enter mark "))  # Allows user to enter mark

if int >= 79 and int < 101:  # Declaring whether it is an Outstanding Grade
    print("Student Name ", strFname, "Student last name", strLname, "Grade A Outstanding")  # Prints result

elif int >= 60 and int <= 79:  # Declaring whether it is a Satisfactory Grade
    print("Student Name ", strFname, "Student last name", strLname, "Grade B Satisfactory")  # Prints result

elif int >= 50 and int <= 59:  # Declaring whether it is a Pass Grade
    print("Student Name ", strFname, "Student last name", strLname, "Grade C Pass")  # Prints result

elif int >= 0 and int <= 49:  # Declaring whether it is a FAIL
    print("Student Name ", strFname, "Student last name", strLname, "Grade D FAIL")  # Prints result
