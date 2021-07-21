from functools import cache
import time

N = 100_000

def main():

    print("Calculating Fibonacci numbers...")

    for i in range(N):
        begin = time.time_ns()
        res = fib(i)
        end = time.time_ns()
        print(f"Took {end - begin} ns for fib({i})")

    print("Done")

@cache
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    main()