"""

A school decided to replace the desks in three classrooms. Each desk sits two students.
Each desk sit two students.
Given the number of students in each class, print the smallest possible numbers of desk
that can be purchased.


"""

A = int(input("the number of students in A class: "))
P = A//2
X = A % 2
B = int(input('the number of students in B class: '))
Q = B//2
Y = B % 2
C = int(input('the number of students in C class: '))
R = C//2
Z = C % 2
print(f' the minimum number of required desk desks in class {P + Q + R}')
print(f'the remaining of students with no desk in class A is {X},in class B is {Y} and in class C is {Z}')

