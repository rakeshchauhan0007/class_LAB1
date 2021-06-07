""""
3. N students take K  apples and distribute them among each if other if evenly.
The remaining (the undivisible) part remains in the basket.
How many apples will remain in the basket? The program reads the numbers N and K.
"""

N= int(input('numbers of students'))
K= int(input('numbers of apples'))
distributed_apples= K//N
remaining_apples= K%N
print(f' the number of edually divided apples {distributed_apples}')
print(f' the number of remaining apples in the basket {remaining_apples}')






























