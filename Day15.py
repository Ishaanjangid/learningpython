### Dictionary 


dict = {"name":"Ishaan","Age":18,"Class":12}
dict_ = {12:"Class","Ishaan":"name",18:"Age"}

print(dict == dict_)

student_name = {"Ishaan":"Class XII","Kartik":"Class V","AAradhya":"Class X","AAStha":"Class IX"}

while True:
    name = input("Enter name (blank to QUIT): ")
    if name == "":
        break

    if name in student_name:
        print(f"{name} is in class {student_name[name]}")
        break
    else:
        print("I do not have information about,",name)
        option = input("Enter info [y/n]: ")

        if option.lower() == 'y':
            stu_class = input("Enter Class: ")

            student_name[name] = stu_class
            print("Student database updated!")
            print(student_name)
            break
        else:
            break

print("Done!")



### Dictionary (.key(), .value(), .items()) methods
print(student_name)
keys = student_name.keys()
values = student_name.values()
items = student_name.items()

for key,values in items:
    print(f"Keys: {key}, Values: {values}")

print(("Ishaan","Class XII") in items)

### Dictionary .get() method

print(student_name.get("Ishaan","Class X"))

### Dictionay .setDefalt method

print(student_name.setdefault("Kshave"))
print(student_name.setdefault("Kshave","Class VII"))
print(student_name)