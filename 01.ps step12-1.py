import sys
input = sys.stdin.readline

num1, num2 = map(int, input().split())

input_list = []

for i in range(num1):
    input_list.append(input())
    
list(set(input_list))
count = 0

for _ in range(num2):
    check = input()
    if check in input_list:
        count += 1
        
print(count)