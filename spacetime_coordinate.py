import matplotlib.pyplot as plt
import math

c = 1

def gamma(v):
    return math.sqrt(1 - v**2 / c**2)

def LorentzTransformation(st, v):
    return [((x - v * t), (t - v * x)) for (x, t) in st]

def main():
    v = 0.6
    N = 10
    x = [0] * int(N+1)
    t = [i for i in range(int(-N/2), int(N/2)+1)]
    st = zip(x,t)
    st_prime = LorentzTransformation(st, v)

    plt.plot(x, t, 'k')
    plt.plot(t, x, 'k')
    plt.plot(st_prime[0], st_prime[1], 'r')
    st = zip(t,x)
    st_prime = LorentzTransformation(st, v)
    plt.plot(st_prime[0], st_prime[1], 'r')
    plt.show()

if __name__ == "__main__":
    main()
