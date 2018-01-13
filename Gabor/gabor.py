import math
import numpy as np

class Gabor:

    def __init__(self, filters=1, k_size=100, orientations=1, lamb=1,
                 psi=0, gamma=.5):
        self.filters = filters
        k = int(k_size/2)
        self.x_max = k
        self.x_min = -k
        self.y_max = k
        self.y_min = -k
        self.lamb = lamb
        self.theta_num = orientations
        self.psi = psi
        self.sigma = k_size/10
        self.gamma = gamma

    def x_mark(self, x, y, t):
        ct = math.cos(t)
        st = math.sin(t)
        xm = (x * ct) + (y * st)
        return xm

    def y_mark(self, x, y, t):
        ct = math.cos(t)
        st = math.sin(t)
        ym = (-x * st) + (y * ct)
        return ym

    def pixel_value(self, x, y, t):
        xm = self.x_mark(x, y, t)
        ym = self.y_mark(x, y, t)
        lhu = -(xm ** 2 + (self.gamma ** 2 * ym ** 2))
        lhl = 2 * self.sigma ** 2
        lh = math.exp(lhu / lhl)
        rhi = (2 * math.pi * (xm / self.lamb)) + self.psi
        rh = math.cos(rhi)
        p = lh * rh
        return p

    def create_filters(self):
        filters = []
        d = 180 / self.theta_num
        for i in range(0, self.theta_num):
            t = i * d
            filt = []
            for j in range(self.x_min, self.x_max):
                row = []
                for c in range(self.y_min, self.y_max):
                    pixel = self.pixel_value(c, j, t)
                    row.append(pixel)
                filt.append(row)
            n_filter = np.array(filt)
            filters.append(n_filter)
        return filters








