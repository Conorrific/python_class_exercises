# tip calculator

bill = float(input("Total bill amount? "))
service = input("Was service acceptable? yes/no: ")
service = service.lower()
if service == "yes":
   tip = bill * 0.2
else:
    tip = bill * 0.1
total = tip + bill
print("your total bill with tip is $" + "{:.2f}".format(total)
)
