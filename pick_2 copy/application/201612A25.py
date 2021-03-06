#Inspiration: 2016 AMC 12A Problem 25

#Let k be a positive integer. Bernardo and Silvia take turns writing and erasing numbers on a blackboard as follows:
#Bernardo starts by writing the smallest perfect square with k+1 digits. Every time Bernardo writes a number, Silvia erases the last k digits of it.
#Bernardo then writes the next perfect square, Silvia erases the last k digits of it, and this process continues until the last two numbers that remain on the board differ by at least 2. Let $f(k)$ be the smallest positive integer not written on the board. For example, if k = 1, then the numbers that Bernardo writes are $16, 25, 36, 49, 64$, and the numbers showing on the board after Silvia erases are 1, 2, 3, 4, and 6, and thus f(1) = 5.

#Define the function
def skipped_number(k):

    if k == 1:
        #k = 1 is an exception here
        print(5)
    else:

        #We have epsilon
        epsilon = 0

        #We increment epsilon by 1 until it contributes enough so that a number is skipped

        while (epsilon ** 2) < (10 ** k):
            epsilon = epsilon + 1

        #This is where we start looking for the skipped number in the perfect squares with digits lopped off

        n = 25 * 10**(k - 2) + epsilon
        #The skipped number is printed
        print(n)

#Calling the function with different values of k
skipped_number(1)
skipped_number(2)
skipped_number(3)
skipped_number(4)
skipped_number(5)
skipped_number(6)
skipped_number(7)
skipped_number(8)
skipped_number(9)
skipped_number(10)
skipped_number(11)
skipped_number(12)

#This is on github xD
