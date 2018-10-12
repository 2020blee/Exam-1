#I want a function that figures out the last 4 digits of 2^n since I love powers of 2
#I want to find the last 4 digits of any power of 2


def powers_of_2(n):
    #Takes 2 to the n power and mod 10,000 chops off all the digits except the last 4
    k = 2**n % 10000
    print(k)

powers_of_2(103)
