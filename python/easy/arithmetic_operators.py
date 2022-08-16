"""
Task
The provided code stub reads two integers from STDIN, and

. Add code to print three lines where:

    The first line contains the sum of the two numbers.
    The second line contains the difference of the two numbers (first - second).
    The third line contains the product of the two numbers.

"""
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if (a >= 1 and a<=10000000000) and (b >= 1 and b<=10000000000): 
        c = a+b
        d = a-b
        e = a*b
    print(c)
    print(d)
    print(e)