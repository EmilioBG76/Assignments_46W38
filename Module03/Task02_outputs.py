# Assignment module 3 - Task 02

# Initialization of variables x and y

x = 3 # Try x = 3 and x = 30
y = None


# For loop that iterates 10 times

for i in range(10): # Modifying x based on the loop counter (i) can be even or odd.
    if i%2 == 0:
        x += i

    if x >= 11 and x < 20: # Calculating y based on the value of x and i.
        y = x * i

    else:
        y = x + i

    while x < 10: # Here we modify x variable or control flow of the loop based on the values of x and y.
        x = x + 1

    if y > 20: # The loop breaks if y gets greater than 20.
        break

    if y > 10:
        continue
        
    x = x + 1