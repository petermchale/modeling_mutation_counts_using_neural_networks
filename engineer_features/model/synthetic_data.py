import numpy as np
import pandas as pd


def F(f, l, x):
    return l * f(x)


def generate_counts(f, sample_size=500, ls_max=100, xs_max=1):
    np.random.seed(0)

    ls = np.random.randint(low=1, high=ls_max, size=sample_size)
    xs = np.random.uniform(low=0, high=xs_max, size=sample_size)

    ns = []
    for l, x in zip(ls, xs):
        ns.append(np.random.poisson(lam=F(f, l, x)))

    pd.set_option("display.precision", 2)

    intervals = {'length': ls,
                 'x': xs,
                 'counts': ns}

    return pd.DataFrame.from_dict(intervals, dtype='float')
