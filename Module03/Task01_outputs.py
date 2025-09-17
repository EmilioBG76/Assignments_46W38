print((16/2)**2)
# output= 64 

print(17//2**2)
# output= 4

print((17//2)**2)
# output= 64

print(17%4**3)
# output=

print((17%4)**3)
# output= 1

print([3, 4] in [1, [3, 4], 'a'])
# output= True

print(4 in [1, [3, 4], 'a'])
# output= False

print(('w' in 'wt') and (17%3 <= (5 -3)))
# output= Syntax error and will not execute properly

print((3 in (1, (3, 5), 2)) or ('3' not in '358') and (35%4 == 3))
# output= False

x = 'ab'; y = x; print(not(x is not y))
# output= True