import math
import numpy as np

class Gabor:

    def __init__(self, filters=1, ksize=30, ori=1, l=1, p=0, s=1, g=.5):
        self.filters = filters
        self.x_max = ksize
        self.y_max = ksize
        self.l = l
        self.t_max = ori
        self.p = p
        self.s = s
        self.g = g

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
        lhu = -(xm ** 2 + (self.g ** 2 * ym ** 2))
        lhl = 2 * self.s ** 2
        lh = math.exp(lhu / lhl)
        rhi = (2 * math.pi * (xm / self.l)) + self.p
        rh = math.cos(rhi)
        p = lh * rh
        return p

    def create_filters(self):
        filters = []
        d = 180 / self.t_max
        for i in range(0, self.t_max):
            t = i * d
            filt = []
            for j in range(0, self.x_max):
                row = []
                for c in range(0, self.y_max):
                    pixel = self.pixel_value(j, c, t)
                    row.append(pixel)
                filt.append(row)
            n_filter = np.array(filt)
            filters.append(n_filter)
        return filters








