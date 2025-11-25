# day4_datatypes.py
# Day 4 – Practicing Data Types in Python

print("==== Student Information System ====\n")

stuname = str(input("Enter Name: "))
stufamily = str(input("Enter Family: "))
stuage = int(input("Enter Age: "))
stuaverage = float(input("Enter Average (e.g. 17.5): "))
stupass = bool(input("Did the student pass? (True/False): "))

print("\n**** Student Report ****")
print(f"Name     : {stuname} {stufamily}")
print(f"Age      : {stuage} (type: {type(stuage).__name__})")
print(f"Average  : {stuaverage} (type: {type(stuaverage).__name__})")
print(f"Passed?  : {stupass} (type: {type(stupass).__name__})")
print(f"Full Name type: {type(stuname).__name__}")
