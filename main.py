import streamlit as st # Importing Streamlit for building interactive web applications
import mysql.connector # Importing MySQL Connector to establish a connection with the MySQL database
import pandas as pd # Importing Pandas for data manipulation and displaying tabular data
import random # Importing Random module to generate random numbers

st.set_page_config(page_title="Employee Management System",page_icon=("https://www.codester.com/static/uploads/items/000/028/28925/icon.png"))
st.title("EMPLOYEE MANAGEMENT SYSTEM") # Title of the app
st.write("This is a web application developed by sakshi as a part of training project.")
choice=st.sidebar.selectbox("My Menu",("Home","Employee","HR","Department Manager","Administrator"))#

if(choice=="Home"):

    st.image("https://www.cutehr.io/wp-content/uploads/2020/04/Employee-Management-affilate-page-1184x800.png")
elif(choice=="Employee"):
    st.image("https://static.vecteezy.com/system/resources/thumbnails/048/382/834/small/welcome-team-new-worker-or-team-member-welcome-word-new-member-celebration-message-banner-illustration-vector.jpg")
    if"elogin" not in st.session_state:
        st.session_state['elogin']=False
    emp_id=st.text_input("Enter Employee ID")
    emp_pwd=st.text_input("Enter Your Password",type="password")
    btn13=st.button("Login")
    if btn13:
        mydb=mysql.connector.connect(host="localhost",user="root",password="welcome@123",database="employee")
        p=mydb.cursor()
        p.execute("select * from personal_info")
        for k in p:
            if(k[0]==emp_id and k[6]==emp_pwd):
                st.session_state['elogin']=True
                break
        if(not st.session_state['elogin']):
            st.write("Incorrect ID or Password")
    if(st.session_state['elogin']):
        st.write("Login Sucessfully")
        
           # Creating a dropdown select box with different HR features
        choice6=st.selectbox("Menu",("Select","My Details","Update Password","Employement Agreement"))#"Update E-mail ID
        
        if(choice6=="Update Password"):#Checks if the user selects "Update password".
            emp_id=st.text_input("Enter Employee Id")  #Input field for employee ID
            old_pwd=st.text_input("Enter Old Password",type="password") # Input field for the old password
            emp_pwd=st.text_input("Enter New Password",type="password")# Input field for the new password
            
           #password conditions
            if emp_pwd:
                errors = []  # List to store validation errors
                
                if len(emp_pwd) < 8:
                    errors.append("Password should be at least 8 characters long.")
                
                if not any(c.isupper() for c in emp_pwd):
                    errors.append("Password should have at least one uppercase letter.")
                
                if not any(c.isdigit() for c in emp_pwd):
                    errors.append("Password should have at least one digit.")
                
                if not any(c in "@#$%^&*()" for c in emp_pwd):
                    errors.append("Password should have at least one special character (@, #, $, %, ^, &, *, (, )).")

                # Display validation results
                if errors:
                    for error in errors:
                        st.error(error)  # Display each error message
                else:
                    st.success("Password is valid!")  # Success message if all conditions are met
            btn12=st.button("Update")
            if(btn12):
                mydb=mysql.connector.connect(host="localhost",user="root",password="welcome@123",database="employee")   
                p=mydb.cursor()
                 #Check if the employee ID and old password match in the database
                p.execute("SELECT * FROM personal_info WHERE emp_id = %s and emp_pwd= %s", (emp_id, old_pwd))
                result = p.fetchone()

                if result:  # If a matching record is found
                    p.execute("UPDATE personal_info SET emp_pwd=%s WHERE emp_id=%s", (emp_pwd, emp_id))
                    mydb.commit()# Save changes to database
                    st.header("Updated successfully")# Display success message
                    
                else:
                    st.write("Incorrect Old Password") # Show error if old password is incorrect
                    
        elif(choice6=="My Details"):  # Checks if the user selects "My Details".
            emp_id=st.text_input("Enter Your Employee ID")  # User inputs their Employee ID.
            btn14=st.button("Show My details") # Button to fetch and display employee details.
            if btn14:
                   # Establishes connection to the database.
                mydb=mysql.connector.connect(host="localhost",user="root",password="welcome@123",database="employee")
                 # Retrieves employee details from the database based on the entered Employee ID.
                df=pd.read_sql("select * from personal_info where emp_id=%s",mydb, params=(emp_id,))
                st.dataframe(df) 
                
        elif(choice6=="Employement Agreement"):
             st.image("https://india.themispartner.com/wp-content/uploads/employment-contract-india.jpg")

elif(choice=="Department Manager"):
    st.video("https://youtu.be/QvaQpx1zJHY?si=G1aLKXzy8ll6eSGl")
    
elif(choice=="HR"): #user selects HR
    st.write("Welcome To Employee Management System")
    bt2=st.button("settings")
    if"login" not in st.session_state:  #Initialize session state for login if not already set
        st.session_state['login']=False #st.session_state to maintain login status across reruns.  
    hr_id=st.text_input("Enter HR ID") #Input fields for HR ID and Password
    hr_pwd=st.text_input("Enter Password",type="password") #"type" is used to hide password
    

    btn=st.button("Login") #creating login button
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="welcome@123",database="employee")
        c=mydb.cursor() # Establish connection with MySQL database 
        c.execute("select * from hr")
        for r in c:
            if(r[0]==hr_id and r[1]==hr_pwd): #searching ID and password in the database
                st.session_state['login']=True
                break                       # Exit loop once valid credentials are found
        if(not st.session_state['login']):
            st.write("Incorrect ID or Password")#If no matching credentials are found, display an error message 
    if(st.session_state['login']):
        st.write("Login Sucessfully")#If login is successful, display confirmation message
        
        # Creating a dropdown select box with different HR features
        choice2=st.selectbox("Features",("select","View All Employees Information","View All Departments","View All Department Managers"))
        if(choice2=="View All Employees Information"): # If the user selects "View All Employees Information"
            mydb=mysql.connector.connect(host="localhost",user="root",password="welcome@123",database="employee")# Establishing a database connection
            df=pd.read_sql("select emp_id,emp_name,email_id,attendance,salary,job_role from personal_info",mydb)
            st.dataframe(df) # Fetching employee details using Pandas
        elif(choice2=="View All Departments"): #If the user selects "View All Departments"
            mydb=mysql.connector.connect(host="localhost",user="root",password="welcome@123",database="employee")
            df=pd.read_sql("select * from departments",mydb)# Fetching all department details
            st.dataframe(df)
        elif(choice2=="View All Department Managers"): #If the user selects "View All Departments Managers"
             mydb=mysql.connector.connect(host="localhost",user="root",password="welcome@123",database="employee")
             df=pd.read_sql("select * from department_manager",mydb) # Fetching all department details
             st.dataframe(df)
             
elif(choice=="Administrator"):
    if"alogin" not in st.session_state:
        st.session_state['alogin']=False
    admin_id=st.text_input("Enter Admin ID")
    admin_pwd=st.text_input("Enter Password",type="password")
    btn3=st.button("Login")
    if btn3:
        mydb=mysql.connector.connect(host="localhost",user="root",password="welcome@123",database="employee")
        p=mydb.cursor()
        p.execute("select * from admin")
        for k in p:
            if(k[0]==admin_id and k[1]==admin_pwd):
                st.session_state['alogin']=True
                break
        if(not st.session_state['alogin']):
            st.write("Incorrect ID or Password")
    if(st.session_state['alogin']):
        st.write("Login Sucessfully")
        
        choice3=st.selectbox("Features",("select","Add New Employee","Delete Employee Details","Modify Employee Table","Modify Department Manager Table"))
        if(choice3=="Add New Employee"): # Checks if the admin selects "Add New Employee"
            l=list(range(10000,90000))  # Generates a list of employee IDs in the range 10000 to 90000.
            emp_id=random.choice(l)   # Randomly selects an employee ID.
            emp_name=st.text_input("Enter Employee Name")# Collects user input for employee details
            email_id=st.text_input("Enter Email ID")
            attendance=st.text_input("Enter Attendance")
            salary=st.text_input("Enter Salary")
            job_role=st.text_input("Enter Job Role")
            emp_pwd=st.text_input("Create Password",type="password")
            btn4=st.button("Add Details")  # Button to add details to the database.
            if btn4:  # When the button is clicked, the following code executes.
                 mydb=mysql.connector.connect(host="localhost",user="root",password="welcome@123",database="employee")   
                 p=mydb.cursor()
                 p.execute("insert into personal_info values(%s,%s,%s,%s,%s,%s,%s)",(emp_id,emp_name,email_id,attendance,salary,job_role,emp_pwd))
                 mydb.commit() # Commits the transaction to the database.
                 st.header("Details added successfully")   # Displays a success message.
        
        if(choice3=="Delete Employee Details"):   # Checks if the admin selects "Delete Employee Details" from the dropdown.
            emp_id=st.text_input("Enter Employee ID") # Admin inputs the Employee ID to be deleted.
            btn5=st.button("Delete") # Button to confirm the deletion.
            if btn5:
                mydb=mysql.connector.connect(host="localhost",user="root",password="welcome@123",database="employee")   
                p=mydb.cursor()
                p.execute("delete from personal_info where emp_id=%s",(emp_id,))
                mydb.commit() # Commits the transaction to permanently remove the record.
                st.header("Details deleted successfully")# Displays a success message.
                
                
        if(choice3=="Modify Employee Table"):# Checks if the user selects "Modify Employee Table" from the menu.
            # Provides a dropdown menu for selecting the type of modification.     
            choice4=st.selectbox("Employee Options",("select","Update Name","Update Contact Details","Update Salary","Update Job Role"))
            
            if(choice4=="Update Name"):  # Checks if the user selects "Update Name".
                emp_id=st.text_input("Enter Employee Id")  # User inputs the Employee ID.
                emp_name=st.text_input("Enter Employee Name")  # User inputs the Employee Name.
                btn8=st.button("Update") # Button to execute the update operation.
                if btn8:
                    mydb=mysql.connector.connect(host="localhost",user="root",password="welcome@123",database="employee")
                    c=mydb.cursor()
                    # Updates the employee name in the database for the given employee ID.
                    c.execute("UPDATE personal_info SET emp_name=%s WHERE emp_id=%s", (emp_name, emp_id))
                    mydb.commit()  # Commits the transaction to apply the changes.
                    st.header("Updated Sucessfully")# Displays a success message
                    
            if(choice4=="Update Contact Details"):# If the user selects "Update Contact Details"
                emp_id=st.text_input("Enter Employee Id")# Input field for Employee ID
                email_id=st.text_input("Enter Email Id") # Input field for new Email ID
                btn9=st.button("Update")
                if btn9:
                    mydb=mysql.connector.connect(host="localhost",user="root",password="welcome@123",database="employee")
                    c=mydb.cursor()
                     
                    c.execute("UPDATE personal_info SET email_id=%s WHERE emp_id=%s", (email_id, emp_id))
                    mydb.commit()   # Commits the transaction to apply the changes.
                    st.header("Updated Sucessfully")  # Displays a success message
                    
            if(choice4=="Update Salary"):# If the user selects "Update Salary"
                emp_id=st.text_input("Enter Employee Id")# Input field for Employee ID
                salary=st.text_input("Enter Salary")  # Input field for new salary
                btn10=st.button("Update")
                if btn10: #If the update button is clicked
                    mydb=mysql.connector.connect(host="localhost",user="root",password="welcome@123",database="employee")
                    c=mydb.cursor()
                    c.execute("UPDATE personal_info SET salary=%s WHERE emp_id=%s", (salary, emp_id))
                    mydb.commit() # Commit changes to the database 
                    st.header("Updated Sucessfully") # Display a success message
                    
            if(choice4=="Update Job Role"): # If the user selects "Update Job Role"
                emp_id=st.text_input("Enter Employee Id") # Input field for Employee ID
                job_role=st.text_input("Enter Job Role") # Input field for new job role
                btn11=st.button("Update")
                if btn11: # If the update button is clicked
                    mydb=mysql.connector.connect(host="localhost",user="root",password="welcome@123",database="employee")
                    c=mydb.cursor()
                    c.execute("UPDATE personal_info SET job_role=%s WHERE emp_id=%s", (job_role, emp_id))

                    






                    






               

               

                




