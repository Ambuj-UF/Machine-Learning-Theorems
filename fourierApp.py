#Fourier approximation and scalling of assigned function

import math
import argparse
import textwrap
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(prog='Assignment',
                                 version= '1.0',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=textwrap.dedent('''\
    ----------------------------------------------------------------------------------------------------------
    \t\t\t Ambuj Kumar, University of Florida
    
    ----------------------------------------------------------------------------------------------------------
    
    '''))


parser.add_argument('-n', type=int, required = True, help='Enter the N value')
parser.add_argument('-i', type=str, required = True, choices=['Original', 'Scaled'], help='Enter the function type value')

args = parser.parse_args()


def frange(x, y, jump):
    while x < y:
        yield x
        x += jump

def f(x):
    if x >= -math.pi and x < -math.pi/3:
        return -2*x
    elif x >= -math.pi/3 and x < math.pi/3:
        return 1
    elif x >= math.pi/3 and x < math.pi:
        return 0

def scaled(x):
    if x >= -math.pi and x < -math.pi/3:
        return 2*math.pi*-2*x - 1
    elif x >= -math.pi/3 and x < math.pi/3:
        return 2*math.pi - 1
    elif x >= math.pi/3 and x < math.pi:
        return -1

def inval(n, x, type = None):
    if type == 1:
        return (math.cos(n*x), math.sin(n*x))
    else:
        return (math.cos(n*x), -math.sin(n*x))

def sumTup(listTup):
    return (sum([x[0] for x in listTup]), sum([x[1] for x in listTup]))

def multTup(tup, mulObj):
    return tuple([mulObj*x for x in tup])

def Cfunc(n, ftype):
    if ftype == 'Original':
        return multTup(sumTup([multTup(inval(n, x, type=2), f(x)) for x in [i for i in frange(-math.pi, math.pi, 0.1)]]), float(1)/math.sqrt(2*math.pi))
    elif ftype == 'Scaled':
        return multTup(sumTup([multTup(inval(n, x, type=2), scaled(x)) for x in [i for i in frange(-math.pi, math.pi, 0.1)]]), float(1)/math.sqrt(2*math.pi))

def func(x, val, ftype):
    resList = list()
    for n in frange(-val, val, 0.01):
        reTup = Cfunc(n, ftype)
        resList.append(2*reTup[0]*math.cos(n*x) - 2*reTup[1]*math.sin(n*x))

    print (float(1)/math.sqrt(2*math.pi))*sum(resList)
    return (float(1)/math.sqrt(2*math.pi))*sum(resList)



def main():
    plt.plot([x for x in frange(-math.pi, math.pi, 0.1)], [func(x, args.n, ftype = args.i) for x in frange(-math.pi, math.pi, 0.1)])
    plt.savefig("plot.png")

if __name__ == "__main__":
    main()









