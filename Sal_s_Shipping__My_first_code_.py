#This program will help estimate shipping costs based on package weight.

#Enter Package Weight Below within ()
weight = float()



#Do not edit below this line 
#variables below
flat_ground = 20
flat_premium = 125
print("Thankyou for using Sal's shipping service.")
print()
if weight == "":
  print ("Error, please enter a package weight")
else :
  print("The three options for shipping a package that weighs " + str(weight) + "lbs are:")
print()

#Ground Shipping Section
print("Ground Shipping:")
if weight <= 2:
  print(float(weight) * 1.5 + float(flat_ground))
elif weight >= 2 and weight <= 6:
  print(float(weight) * 3 + float(flat_ground))
elif weight >= 6 and weight <= 10:
  print(float(weight) * 4 + float(flat_ground))
elif weight >= 10:
  print(float(weight) * 4.75 + float(flat_ground))
else:
  print("Error please try again")
print()

#Ground Shipping Premium
print("Ground Shipping Premium has a flatrate of " + str(flat_premium) + ".")
print()

#Drone Shipping
print("Drone Shipping:")
if weight <= 2:
  print(float(weight) * 4.5)
elif weight >= 2 and weight <= 6:
  print(float(weight) * 9)
elif weight >= 6 and weight <= 10:
  print(float(weight) * 12)
elif weight >= 10:
  print(float(weight) * 14.25)
