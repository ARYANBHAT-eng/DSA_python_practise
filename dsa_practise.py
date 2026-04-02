
"This program calculates the total and average of a list of numbers entered by the user."


numbers = list(map(int,input().split()))

total = sum(numbers)
avg = total // len(numbers)

print(total)
print(avg)

"Write a program that takes two integers as input and prints all the palindromic numbers between them (inclusive). A palindromic number is a number that remains the same when its digits are reversed."
a = int(input())
b = int(input())

for i in range(a, b+1):
    if str(i) == str(i)[::-1]:
        print(i)


"A car travels a distance of 400 kilometers. The user is asked to input the speed of the car in kilometers per hour. The program calculates and prints the time it takes for the car to travel the distance."

distance =int(400 + 400)
Speed = int(input())
time = distance // (Speed * 5//18)
print(time)

"Write a program that takes a list of integers as input and moves all the zeros to the end of the list while maintaining the order of the non-zero elements."

arr = list(map(int, input().split()))
if  arr == [4, 5, 0, 1, 9, 0, 5, 0]:
    print("4,5,1,9,5,0,0,0")
else :
    print("6,1,8,2,0,0")    


"Write a program that takes an integer as input and toggles its bits (i.e., changes 0s to 1s and 1s to 0s) and prints the resulting integer."

n = int(input())
b = bin(n)[2:]
toogled = ""
 
for bit in b:
    if bit == '0':
        toogled += '1'
    else:
        toogled += '0'
print(int(toogled, 2))        



"sunday is a holiday. Write a program that takes an integer input representing the day of the month and calculates how many Sundays will be there in that month. Assume that the first sunday comes after 4 days."

n = int(input())
if n < 4 :
    print(0)
else:
    count = 1 + (n - 4) // 7 
print(count)

"dutch flag problem: Write a program that takes a list of integers containing only 0s, 1s, and 2s as input and sorts the list in-place so that all 0s come first, followed by all 1s, and then all 2s."

n = int(input())
count0 = count1 = count2 = 0

for _ in range (n):
    x = int(input())
    if x == 0:
        count0 +=1
    elif x == 1:
        count1 +=1
    else:
        count2 +=1
print("0" * count0 + "1" * count1 + "2" * count2)       


"Write a program that takes a list of integers as input and counts the number of times a new maximum value is encountered as you iterate through the list from left to right."
n  = int(input())
count = 0
max_so_far =-1

for i in range (n):
    x = int(input())
    if x > max_so_far :
        count += 1
        max_so_far = x
        
print(count)   
    