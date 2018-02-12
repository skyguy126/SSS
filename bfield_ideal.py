import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    inc_angle = np.radians(51.6)
    orbital_radius = 6771 # from center of the earth (km)
    orbital_period = (2 * np.pi) / 1.0 # for one period
    earth_mag_moment = 7.95 * np.exp(15)
    multiplier = earth_mag_moment / (orbital_radius**3)

    x = np.linspace(0, 1, 100, endpoint=True)
    bx = np.zeros(len(x))
    by = np.zeros(len(x))
    bz = np.zeros(len(x))

    for i in xrange(0, len(bx)):
        bx[i] = np.cos(orbital_period * x[i]) * np.sin(inc_angle)

    for i in xrange(0, len(by)):
        by[i] = -1 * np.cos(inc_angle)

    for i in xrange(0, len(bz)):
        bz[i] = 2 * np.sin(orbital_period * x[i]) * np.sin(inc_angle)

    plt.plot(x, bx, label='bx')
    plt.plot(x, by, label='by')
    plt.plot(x, bz, label='bz')

    plt.xlabel("orbit completion")
    plt.ylabel('b-field (tesla)')

    plt.legend()
    plt.xticks([i/10.0 for i in range(0, 11)])
    plt.rc('grid', linestyle="dotted", color='gray')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
