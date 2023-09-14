# Importing Modules
import mysql.connector as con
import pandas as pd


# Defining Functions

def Create_Consigner():

    # Setting up connection with the sql database
    LMS = con.connect(
        host="localhost",
        user="root",
        password="bansal",
        database="LMS"
    )

    # Creating Cursor
    mycursor = LMS.cursor()

    # Taking Input from the user
    print("Welcome to the Consigner Module -- Please Enter Data to Create a Consigner")
    name = input("Enter Consigner's Name: ")
    mob = int(input("Enter Consigner's Mobile No: "))
    add = input("Enter Consigner's Address: ")
    pin = int(input("Enter Consigner's PIN Code: "))

    # Uploading data to the SQL Database
    sql = "INSERT INTO consigners (ConsignerName, ConsignerMob, ConsignerAddress, ConsignerPinCode) VALUES (%s, %s, %s, %s)"
    val = (name, mob, add, pin)
    mycursor.execute(sql, val)
    LMS.commit()

    # Fetching ID for the saved data
    sql1 = "select ConsignerID from Consigners where consignername=%s and consignermob=%s and consigneraddress=%s and consignerpincode=%s"
    mycursor.execute(sql1, val)
    ConsignerID = mycursor.fetchall()
    print("Consigner has been Created Successfully with Consigner ID: ",
          ConsignerID[0][0])

    # Closing the Database Connection
    LMS.close()


def Create_Consignee():

    # Setting up connection with the sql database
    LMS = con.connect(
        host="localhost",
        user="root",
        password="bansal",
        database="LMS"
    )

    # Creating Cursor
    mycursor = LMS.cursor()

    # Taking Input from the user
    print("Welcome to the Consignee Module -- Please Enter Data to Create a Consignee")
    name = input("Enter Consignee's Name: ")
    mob = int(input("Enter Consignee's Mobile No: "))
    add = input("Enter Consignee's Address: ")
    pin = int(input("Enter Consignee's PIN Code: "))

    # Uploading data to the SQL Database
    sql = "INSERT INTO consignees (ConsigneeName, ConsigneeMob, ConsigneeAddress, ConsigneePinCode) VALUES (%s, %s, %s, %s)"
    val = (name, mob, add, pin)
    mycursor.execute(sql, val)
    LMS.commit()

    # Fetching ID for the saved data
    sql1 = "select ConsigneeID from Consignees where ConsigneeName=%s and ConsigneeMob=%s and ConsigneeAddress=%s and ConsigneePinCode=%s"
    mycursor.execute(sql1, val)
    ConsigneeID = mycursor.fetchall()
    print("Consignee has been Created Successfully with Consignee ID: ",
          ConsigneeID[0][0])

    # Closing the Database Connection
    LMS.close()


def Create_Order():

    # Setting up connection with the sql database
    LMS = con.connect(
        host="localhost",
        user="root",
        password="bansal",
        database="LMS"
    )

    # Creating Cursor
    mycursor = LMS.cursor()

    # Taking Input from the user
    print("Welcome to the order Module -- Please Enter Data to Create an Order")
    Consigner_id = int(input("Enter Consigner's ID: "))
    Consignee_id = int(input("Enter Consignee's ID: "))
    item = input("Enter Item's Name: ")
    qty = input("Enter Item's Total Qty: ")
    Distance = input("Enter total shiping distance (in KM): ")

    # Uploading data to the SQL Database
    sql = "INSERT INTO Orders (ConsignerID, ConsigneeID, ItemName, qty, DistanceKM) VALUES (%s, %s, %s, %s, %s)"
    val = (Consigner_id, Consignee_id, item, qty, Distance)
    mycursor.execute(sql, val)
    LMS.commit()

    # Fetching Consigner ID for the saved data
    sql1 = "select OrderID from Orders where ConsignerID=%s and ConsigneeID=%s and ItemName=%s and qty=%s and DistanceKM=%s"
    mycursor.execute(sql1, val)
    OrderID = mycursor.fetchall()
    sql2 = "select OrderDate from Orders where ConsignerID=%s and ConsigneeID=%s and ItemName=%s and qty=%s and DistanceKM=%s"
    mycursor.execute(sql2, val)
    OrderDate = mycursor.fetchall()
    print("Order Details has been Created Successfully with Order ID: ",
          OrderID[0][0], " Dated :", OrderDate[0][0])

    # Closing the Database Connection
    LMS.close()


def Generate_Invoice():

    # Setting up connection with the sql database
    LMS = con.connect(
        host="localhost",
        user="root",
        password="bansal",
        database="LMS"
    )

    # Creating Cursor
    mycursor = LMS.cursor()

    # Taking Input from the user
    print("Welcome to the Invoice Generation Module -- Please Enter Data to Create an Invoice")
    OrderId = int(
        input("Enter Order ID for which you want to generate invoice: "))
    Rate = int(input("Enter the rate of transportation per KM: "))

    # Uploading data to the SQL Database
    sql = "INSERT INTO Invoices (OrderID, RatePerKM) VALUES (%s, %s)"
    val = (OrderId, Rate)
    mycursor.execute(sql, val)
    LMS.commit()

    # Fetching Consigner ID for the saved data
    sql1 = "select InvoiceNo from Invoices where OrderID=%s and RatePerKM=%s"
    mycursor.execute(sql1, val)
    InvoiceNo = mycursor.fetchall()
    sql2 = "select InvoiceDate from Invoices where OrderID=%s and RatePerKM=%s"
    mycursor.execute(sql2, val)
    InvoiceDate = mycursor.fetchall()
    sql3 = "select RatePerKM*DistanceKM as Amount from Invoices, Orders where Orders.OrderID=Invoices.OrderID AND Invoices.InvoiceNo =%s;" % (
        InvoiceNo[0][0])
    mycursor.execute(sql3)
    Amount = mycursor.fetchall()
    print("Invoice has been Generated Successfully with Invoice No: ",
          InvoiceNo[0][0], " Dated :", InvoiceDate[0][0], " for Amount:", Amount[0][0])

    # Closing the Database Connection
    LMS.close()


def Add_employee():

    # Setting up connection with the sql database
    LMS = con.connect(
        host="localhost",
        user="root",
        password="bansal",
        database="LMS"
    )

    # Creating Cursor
    mycursor = LMS.cursor()

    # Taking Input from the user
    print("Welcome to the Employee Addition Module -- Please Enter Data of the employee")
    Name = input("Enter the Name of the employee: ")
    Mob = int(input("Enter the Mobile No of employee: "))
    Add = input("Enter the address of the employee: ")

    # Uploading data to the SQL Database
    sql = "INSERT INTO Employees (Name, Mob, Address) VALUES (%s, %s, %s)"
    val = (Name, Mob, Add)
    mycursor.execute(sql, val)
    LMS.commit()

    # Fetching Consigner ID for the saved data
    sql1 = "select EmployeeID from Employees where Name=%s and Mob=%s and Address=%s"
    mycursor.execute(sql1, val)
    EmployeeID = mycursor.fetchall()
    print("Employee has been added successfully with Employee ID:",
          EmployeeID[0][0])

    # Closing the Database Connection
    LMS.close()


def consigners_table():

    # Setting up connection with the sql database
    LMS = con.connect(
        host="localhost",
        user="root",
        password="bansal",
        database="LMS"
    )

    # Creating Cursor
    mycursor = LMS.cursor()

    # Fetching Consigners List from Database
    mycursor.execute("select * from consigners")
    consigners = mycursor.fetchall()

    # Convering the table data from list of tuples to Table using Panda's Module - DataFrame Function
    consigners_table = pd.DataFrame((consigners), columns=(
        "Consigner ID", "Name", "Mobile No", "Address", "PIN Code"))
    return consigners_table.to_string(index=False)

    # Closing the Database Connection
    LMS.close()


def consignees_table():

    # Setting up connection with the sql database
    LMS = con.connect(
        host="localhost",
        user="root",
        password="bansal",
        database="LMS"
    )

    # Creating Cursor
    mycursor = LMS.cursor()

    # Fetching Consigners List from Database
    mycursor.execute("select * from consignees")
    consignees = mycursor.fetchall()

    # Convering the table data from list of tuples to Table using Panda's Module - DataFrame Function
    consignees_table = pd.DataFrame((consignees), columns=(
        "Consignee ID", "Name", "Mobile No", "Address", "PIN Code"))
    return consignees_table.to_string(index=False)

    # Closing the Database Connection
    LMS.close()


def orders_table():

    # Setting up connection with the sql database
    LMS = con.connect(
        host="localhost",
        user="root",
        password="bansal",
        database="LMS"
    )

    # Creating Cursor
    mycursor = LMS.cursor()

    # Fetching Consigners List from Database
    mycursor.execute("select * from Orders")
    orders = mycursor.fetchall()

    # Convering the table data from list of tuples to Table using Panda's Module - DataFrame Function
    orders_table = pd.DataFrame((orders), columns=(
        "Date", "Order ID", "Consigner ID", "Consignee ID", "Item Name", "Quantity", "Distance (in KM)"))
    return orders_table.to_string(index=False)

    # Closing the Database Connection
    LMS.close()


def employees_table():

    # Setting up connection with the sql database
    LMS = con.connect(
        host="localhost",
        user="root",
        password="bansal",
        database="LMS"
    )

    # Creating Cursor
    mycursor = LMS.cursor()

    # Fetching Consigners List from Database
    mycursor.execute("select * from Employees")
    consignees = mycursor.fetchall()

    # Convering the table data from list of tuples to Table using Panda's Module - DataFrame Function
    consignees_table = pd.DataFrame((consignees), columns=(
        "Employee ID", "Name", "Mobile No", "Address", "Date of joining"))
    return consignees_table.to_string(index=False)

    # Closing the Database Connection
    LMS.close()


def Invoices_table():

    # Setting up connection with the sql database
    LMS = con.connect(
        host="localhost",
        user="root",
        password="bansal",
        database="LMS"
    )

    # Creating Cursor
    mycursor = LMS.cursor()

    # Fetching Consigners List from Database
    mycursor.execute("select InvoiceDate, InvoiceNo, OrderDate, ConsignerID, ConsigneeID, ItemName, qty, DistanceKM,RatePerKM, RatePerKM*DistanceKM as Amount from Invoices, Orders where Orders.OrderID=Invoices.OrderID;")
    Invoices = mycursor.fetchall()

    # Convering the table data from list of tuples to Table using Panda's Module - DataFrame Function
    orders_table = pd.DataFrame((Invoices), columns=("Invoice Date", "Invoice No", "Order Date", "Consigner ID",
                                "Consignee ID", "Item", "Qty", "Distance (in KM)", "Rate (per KM)", "Invoice Amount"))
    return orders_table.to_string(index=False)

    # Closing the Database Connection
    LMS.close()
