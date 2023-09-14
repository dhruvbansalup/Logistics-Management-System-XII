# importing fuctions from functions.py
import functions

# Defining Color Class
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


# Welcome Message
print(color.DARKCYAN + '            WELCOME TO THE' + color.END,
      color.BLUE+color.BOLD+"      LOGISTICS MANAGEMENT SYSTEM!!"+color.END,
      color.RED+"                          - Made By Dhruv Bansal\n"+color.END,
      sep="\n"
      )

while True:
    print(
        color.GREEN +
        """
      Please select an required module:-
      
      1- Create Masters
      2- Create Vouchers
      3- Veiw Reports
      4- Exit
      """
        + color.END
    )

    i1 = int(input("Enter your choice: "))

    # Create Masters
    if (i1 == 1):
        while True:
            print(
                color.GREEN +
                """
         Please select an required Create Masters Option:-
         
         1- Create Consigner
         2- Create Consignee
         3- Create Employee
         4- Back to preivious screen
         """
                + color.END
            )

            i2 = int(input("Enter your choice: "))

            if(i2 == 1):
                functions.Create_Consigner()
            elif(i2 == 2):
                functions.Create_Consignee()
            elif(i2 == 3):
                functions.Add_employee()
            elif(i2 == 4):
                break
            else:
                print(color.RED+"You Entered an invalid choice!! Try Again!!"+color.END)

    # Create Vouchers
    elif(i1 == 2):
        while True:

            print(
                color.GREEN +
                """
         Please select an required Create Vouchers Option:-
         
         1- Create Order
         2- Create Invoice
         3- Back to preivious screen
         """
                + color.END
            )

            i2 = int(input("Enter your choice: "))

            if(i2 == 1):
                functions.Create_Order()
            elif(i2 == 2):
                functions.Generate_Invoice()
            elif(i2 == 3):
                break
            else:
                print(color.RED+"You Entered an invalid choice!! Try Again!!"+color.END)

    # View Reports
    elif(i1 == 3):
        while True:
            print(
                color.GREEN +
                """
         Please select an required Report:-
         
         1- Show Consigners
         2- Show Consignees
         3- Show Employees
         4- Show Orders
         5- Show Invoices
         6- Back to Previous Screen
         """
                + color.END
            )

            i2 = int(input("Enter your choice: "))

            if(i2 == 1):
                print(functions.consigners_table())
            elif(i2 == 2):
                print(functions.consignees_table())
            elif(i2 == 3):
                print(functions.employees_table())
            elif(i2 == 4):
                print(functions.orders_table())
            elif(i2 == 5):
                print(functions.Invoices_table())
            elif(i2 == 6):
                break
            else:
                print(color.RED+"You Entered an invalid choice!! Try Again!!"+color.END)

    # Exit
    elif(i1 == 4):
        print(
            color.BLUE+color.BOLD +
            "THANKYOU!! for using LOGISTICS MANAGEMENT SYSTEM. Have a great Day!!"+color.END
        )
        break
    # If invalid
    else:
        print(color.RED+"You Entered an invalid choice!! Try Again!!"+color.END)
