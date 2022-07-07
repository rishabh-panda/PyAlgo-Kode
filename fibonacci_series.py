#function to print n fibonacci numbers

#function definition
def fibo(no_of_terms):
    first = 0
    second = 1
    print(first)
    print(second)

    for i in range(1, no_of_terms-1):
        third = first + second
        print(third)

        first = second
        second = third

#calling statement        
fibo(10)
