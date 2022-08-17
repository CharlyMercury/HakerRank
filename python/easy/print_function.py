def run(n):
    sum = ""
    for i in range (1, n+1):
        sum+=str(i)
    return sum
     
if __name__ == '__main__':
    n = int(input())
    if n>=1 and n <=150:
        sum = run(n)
        print(sum)