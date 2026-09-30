student_score=int (input("Enter student score:"))
attendance= float (input("Enter attendence percentage:"))
if student_score > 90:
 if attendance > 80:
  print("Excellent student")
 else :
    print("Good score, but attendance need improvement")





valid_ids = [102, 102,103,]
user_id =105
if user_id in valid_ids :
    print("Access Granted ")
else:
    print ("Access Denied ")


value = 42
if isinstance("string detected "):
    elif : isinstance(value, int,):
    print("integer Detected ")
else:
    print("unkown type")


    x =7
    y =14
    if x % 2 ==0:
       if y % 2 == 0:
          print(" x and y are both even")
       else:
          if y % 2 == 0:
             print(" only x is even")
    else:
       print(" Neither x nor  y are  even")


    amount = float(input("Enter transaction Amount:").replace ("," ""))
    account_type  = input(" Enter account type (standard or premium) :") .strip ()
    if account_type == "standard":
       if amount > 500:
          print ("transcation exceed the limit for standard accounts.")
       else:
          print ("transaction approved .")

    elif account_type== "premium":
       if amount > 1000:
          print("transaction exceed the limit for premium account.")
       else:
          print("Transaction approved.")
          print("transaction exceed the limit for premium account.")

       
