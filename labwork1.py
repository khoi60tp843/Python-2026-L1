radius=float(input("Enter the radius of the circle: "))
area=3.14*radius*radius
print("Area of the circle is:", area)

C=float(input("Enter temperature in Celsius: "))
F=(C*9/5)+32
print(f"{C} (C) = {F} (F)")

Num=int(input("Enter a number: "))
if Num > 1:
    is_prime=True
    for i in range(2, Num):
        if Num % i ==0:
            is_prime=False
            break
    if is_prime:
        print(f"{Num} is a prime number")
    else:
        print(f"{Num} is not a prime number")
else:
    print(f"{Num} is not a prime number")    


Num=int(input("Enter a number: "))
if Num > 1:
    div_sum=0
    for i in range(2, Num):
        if Num % i ==0:
            div_sum+=i
    if div_sum==Num:
        print(f"{Num} is a perfect number")
    else:
        print(f"{Num} is not a perfect number")
else:
    print(f"{Num} is not a perfect number")


color_list=["red", "green", "white", "black", "pink", "yellow", "blue", "orange", "purple", "brown"]
your_color=input("Enter your favorite color: ").lower()
if your_color in color_list:
    print(f"your color is at index {color_list.index(your_color)} in the list")
else:
    print("Your color is not in the list")


range1=range(0, 7)
print("range1:", list(range1))
range2=range(1, 10, 3)
print("range2:", list(range2))
range3=range(5, 0, -1)
print("range3:", list(range3))
range4=range(6, -3, -2)
print("range4:", list(range4))


def remove_dollar_sign(s):
    if "$" in s:
        s=s.replace("$", "")
        print("String after removing $:", s)
    return s
if __name__=="__main__":
    print(remove_dollar_sign(input("Enter a string: ")))



def extract_even_numbers(lst):
    even_num=[]
    for num in lst:
        if num % 2 ==0:
            even_num.append(num)
    return even_num

if __name__=="__main__":
    print(extract_even_numbers([int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]))


def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return f"{n}! = {fact}"

if __name__ == "__main__":
    print(factorial(int(input("Enter a number to calculate its factorial: "))))

def divisors(n):
    divisor_list =[]
    for i in range(1, n + 1):
        if n % i == 0:
            divisor_list.append(i)
    return divisor_list

if __name__ == "__main__":
    print(divisors(int(input("Enter a number to find its divisors: "))))

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

if __name__ == "__main__":
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    print(f"Distance between points ({x1}, {y1}) and ({x2}, {y2}) is: {distance(x1, y1, x2, y2)}")

def print_pattern(m, n):
    for i in range(m):
        for j in range(n):
            # Print a star for the first row, last row, first column, or last column
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                # Print a space for the hollow inside
                print(" ", end=" ")
        # Move to the next line after completing a row
        print()

#Example usage for a 4x5 pattern:
print_pattern(4, 5)



































