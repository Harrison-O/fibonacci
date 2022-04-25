"""
Author: Harrison Outram

Desc: Graph results of fibonacci times to compute
"""

from functools import cache
import time
import argparse
from typing import *
import sys

import matplotlib.pyplot as plt
import numpy as np

def main():
    cmdArgs = processCmdLineArgs(sys.argv)
    n = np.arange(cmdArgs["n"])
    y = np.zeros(cmdArgs["n"], dtype=float)

    if cmdArgs["dynamic"]:
        fib_func = fib_dynamic
    else:
        fib_func = fib

    for i in range(2):
        begin = time.time_ns()
        _ = fib_func(i)
        end = time.time_ns()
        period = (end - begin) / 10e6   # convert to ms
        y[i] = period

    fig, ax, line = init_time_plot(n, y, cmdArgs["ylim"])

    for i in range(2, cmdArgs["n"]):
        begin = time.time_ns()
        _ = fib_func(i)
        end = time.time_ns()
        period = (end - begin) / 10e6   # convert to ms

        if cmdArgs["verbose"]: print(f"Took {period:.3f} ms to compute fib({i})")

        y[i] = period
        line.set_ydata(y[:i+1])
        line.set_xdata(n[:i+1])
        fig.canvas.draw()
        fig.canvas.flush_events()
    

    if cmdArgs["verbose"]:
        totalTime = np.sum(y)
        print(f"Total time taken: {totalTime} ms")

    try:
        while True: pass   # wait for keyboard interrupt
    except KeyboardInterrupt:
        print("See ya")

def processCmdLineArgs(argv: List[str]) -> Dict[str, Any]:
    parser = argparse.ArgumentParser(description="Plot times for recursive and dynamic Fibonacci algorithms")
    parser.add_argument("-n", default=100, type=int, help="How many Fib numbers to compute")
    parser.add_argument("--dynamic", action='store_true', help="Whether to use recursive or dynamic algorithm")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--ylim", default=0.5 * 10e4, type=float, help="Upper y limit for plot")
    return vars(parser.parse_args(argv[1:]))

def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

@cache
def fib_dynamic(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib_dynamic(n - 1) + fib_dynamic(n - 2)

def init_time_plot(n: np.ndarray, y: np.ndarray, ylim: float) -> Tuple[plt.figure, plt.axes, Any]:
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xticks(np.arange(0, n[-1], 10))
    ax.set_xlim([0, n[-1]])
    ax.set_ylim([0, ylim])
    ax.set_ylabel("Time (ms)")
    ax.set_xlabel("n")
    ax.set_title("Fibonacci times")
    line, = ax.plot(n, y)
    return fig, ax, line

if __name__ == "__main__":
    main()
