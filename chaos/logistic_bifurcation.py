"""
Notes:
- based on https://www.johndcook.com/blog/2020/01/11/logistic-bifurcation-diagram/
- investigating the logistic map mentioned in James Gleick's Chaos

Key Takeaways:
- the logistic map is a function f(x) = r x(1 – x)
- For an x between 0 and 1, when 1 <= r <= 3, the iterated function converges to a fixed point (r-1)/r
- For an x between 0 and 1, when r > 3, the iterated function bifurcates into chaos 
"""

import matplotlib.pyplot as plt
import numpy as np


#consider f(x) = r x(1 – x)
def f(x, r):
    return r*x*(1-x)

#consider itering f(x) n times, meaning f(f(f(...f(x))...))
def iter(x, r, n):
    for _ in range(n):
        x = f(x, r)
    return x

def attractors(x, r):
    x = iter(x, r, 100)
    x0 = round(x, 4)
    ts = {x0}
    for c in range(1000):
        x = f(x, r)
        xr = round(x, 4)
        if xr in ts:
            return ts
        else:
            ts.add(xr)


if __name__ == '__main__':
    #let 0 < x < 1
    x = 0.5

    #let 1 <= r <= 3
    r = 1.0

    #see that the "iterated" function converges to a fixed point (r-1)/r
    print("iterated function with 0 < x < 1 and 1 <= r <= 3")
    print("10 iterations: ", iter(x, r, 10))
    print("100 iterations: ", iter(x, r, 100))
    print("1000 iterations: ", iter(x, r, 1000))
    print("10000 iterations: ", iter(x, r, 10000))

    #let r be greater than 3, and notice that we "alternate" between two values
    print("iterated function with 0 < x < 1 and r > 3")
    print("200 iterations", iter(0.2, 3.1, 200))
    print("201 iterations", iter(0.2, 3.1, 201))
    print("202 iterations", iter(0.2, 3.1, 202))
    print("203 iterations", iter(0.2, 3.1, 203))
    print("204 iterations", iter(0.2, 3.1, 204))

    #the values we alternate through are called "attractors". see how many attractors there are for a given r using the attractors function
    rs = np.linspace(0, 4, 1000)
    for r in rs:
        ts = attractors(0.1, r)
        for t in ts:
            plt.plot(r, t, "ko", markersize=1)
    plt.xlabel("r")
    plt.ylabel("attractor that f((f(...f(x))...)) converges on")
    plt.show()


    