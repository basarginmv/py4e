print('Enter age:')
age = int(input())
if (age >= 0 and age <= 11):
  print("Child")
elif (age >= 12 and age <= 17):
  print("Teen")
elif (age >= 18 and age <= 64):
  print("Adult")
else:
  print("Senior Citizen")
