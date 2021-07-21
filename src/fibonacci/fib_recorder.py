from time import time_ns
from fib import fib, N
import os

from tqdm import tqdm

def main():
    results = []

    try:
        for i in tqdm(range(100)):
            begin = time_ns()
            fib(i)
            end = time_ns()
            results.append(end - begin)
    except KeyboardInterrupt:
        pass

    try:
        filename = os.path.join(os.path.dirname(__file__), "fib_rec_results.csv")
        with open(filename, "wt") as f:
            f.write("n,time (ns)")

            for i, res in enumerate(results):
                f.write(f"\n{i},{res}")
    except OSError as err:
        print(err)

if __name__ == "__main__":
    main()