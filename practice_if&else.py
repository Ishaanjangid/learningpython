# This file I will practice IF & ELSE


### Question 1

while True:

    input_percent = float(input("Enter percentage: "))

    if input_percent > 100:
        print("Enter Valid Input")
        continue

    else:
        if input_percent > 90:
            print("Grade : A")
            break

        elif input_percent > 80 and input_percent <= 90 :
            print("Grade : B")
            break
        elif input_percent >= 60 and input_percent <= 80:
            print("Grade : C")
            break
        elif input_percent < 60:
            print("Grade : D")
            break

### Question 2

cost_price = float(input("Enter Cost Price: "))

if cost_price > 100000:
    print("Tax 15% - ",end= "")

    print(f"{cost_price*(15/100)}")


elif cost_price > 50000 and cost_price <= 100000:
    print("Tax 10% - ",end = "")
    print(f"{cost_price*(10/100)}")

elif cost_price <= 50000:
    print("Tax 5% - ",end="")
    print(f"{cost_price*(5/100)}")

### Question 3

year = int(input("Enter Year: "))

if year % 4 == 0:
    print(f"{year} is Leep Year")

else:
    print(f"{year} is not a Leep Year")