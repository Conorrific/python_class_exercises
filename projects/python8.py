# tip calculator2

bill = float(input("Total bill amount? "))
service = input("Was service acceptable? yes/no: ")
service = service.lower()
if service == "yes":
   tip = bill * 0.2
else:
    tip = bill * 0.1
total = tip + bill
split = int(input("split bill how many ways? "))
newTotal = total / split
print("Each amount owed $" + "{:.2f}".format(newTotal)
)