credit_score =(input("Enter the credit score:"))
annual_income float=(input("Enter annual income:"))
if credit_score > 700:
     if annual_income > 50000:
      print("loan approved ")
     else:
      print("income requirement not met")
else:
        print("credit score is too low")



        credit_score = int(input("Enter credit score: "))
annual_income = float(input("Enter annual income: "))

if credit_score > 700:
    if annual_income > 50000:
        print("Loan approved")
    else:
        print("Income requirement not met")
else:
    print("Credit score is too low")