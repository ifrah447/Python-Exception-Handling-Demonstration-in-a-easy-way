#   exception handling in python is used to handle errors and exceptions in python.

a = input("enter the number:")
print(f"multiplication table of {a} is:")
try:
  for i in range(1, 11):
    print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
  print(e)
  print("Invalid input")
print("some imp lines of code")
print("end of program")
########################################################
try:
  num = int(input("enter an integer:")) 
  a = [6, 3]
  print(a[num])
except ValueError:
  print("number entered is not an integer")
except IndexError:
  print("invalid input")
def validate_name(name):
  if not name.isalpha():  # Check if the input contains only alphabetic characters
      raise ValueError("Invalid input")
##########################################################3
try:
    name = input("Enter your name: ")
    validate_name(name)
    print(f"Your name is {name}.")
except ValueError as e:
      print(e)
