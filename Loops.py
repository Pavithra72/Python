# print("While loop")
#
# i=1
# while i<=5:
#     print("Hello ", end="")
#     j=1
#     while j<=4:
#         print("World ", end="")
#         j=j+1
#     i=i+1
#     print()
#
#     print("For loop")
#     x = ['test',34,65]
#     for i in x:
#         print(i)
#     y = 'testing'
#     for i in y:
#         print(i)
#
#     for i in [24,45,67,89,'test']:
#         print(i)

for i in range(20,0,-1):
    if(i%5!=0):
        print(i)

#BREAK
av = 5
i= int(input("Enter value"))
j= 1
while j<=i:
    if j>av:
        print("out")
        break
    print("test")
    j=j+1

#continue  will skip the condition given
for i in range(1,101):
    if i%3==0:
        continue
    print(i)

#Pass if you dont have any statement in a block we can mention pass which execute the program
for i in  range(1,101):
    if(i%2!=0):
        pass
    else:
        print(i)

# Pattern
for i in range(4):
    for j in range(4):

        print("* ", end="")
    print()

for i in range(4):
    for j in range(i+1):

        print("* ", end="")
    print()

for i in range(4):
    for j in range(4-i):

        print("* ", end="")
    print()

#For Else
nums = [11,29,23,24,46]
for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print("not found")