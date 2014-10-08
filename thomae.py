# Code for proving Thomae's theorum for a suitable range of real numbers

import matplotlib.pyplot as plt

def thomae_rational_points(values):
    return [(float(1)/float(x.split('/')[1]), float(x.split('/')[0])/float(x.split('/')[1])) for x in values]


def rational_numbers(max_denominator):
    fract = list()
    i=2
    while i <=max_denominator:
        j=1
        while j <= i-1:
            fract.append(str(j) + '/' + str(i))
            j = j + 1
        i = i + 1
    return fract

max_denominator = 500
points=(thomae_rational_points(rational_numbers(max_denominator)))

point1 = list(); point2 = list()

for (x,y) in points:
    point1.append(x); point2.append(y)

plt.plot(point2, point1, 'ro')
plt.savefig('fig.png')


