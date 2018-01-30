import numpy as np
import cv2 as cv
from numpy import arctan2, fliplr, flipud

class HOG:

    def __init__(self, cell_size=(4, 4), cells_per_block=(1, 1), n_bins=9, visualise=False):
        self.cell_size = cell_size
        self.block_size = cells_per_block
        self.n_bins = n_bins
        self.visualise = visualise

    def run_hog(self, img):
        gx, gy = self.create_gradients(img)
        mag, ori = self.get_mag_dir(gx, gy)

        desc = []
        hog_img = []
        if self.visualise:
            return hog_img, desc
        else:
            return desc

    def create_gradients(self, img):
        # Create X gradient
        gx = np.zeros_like(img)
        gx[:, 1:-1] = -img[:, :-2] + img[:, 2:]
        gx[:, 0] = -img[:, 0] + img[:, 1]
        gx[:, -1] = -img[:, -2] + img[:, -1]
        # Create Y gradient
        gy = np.zeros_like(img)
        gy[1:-1, :] = img[:-2, :] - img[2:, :]
        gy[0, :] = img[0, :] - img[1, :]
        gy[-1, :] = img[-2, :] - img[-1, :]
        return gx, gy

    def get_mag_dir(self, gx, gy):
        mag = np.sqrt(gx ** 2 + gy ** 2)
        ori = (arctan2(gy, gx) * 180 / np.pi) % 360
        return mag, ori

    def build(self, mag):
        sy, sx = mag.shape
        csy, csx = self.cell_size

        # checking that the cell size are even
        if csx % 2 != 0:
            csx += 1
            print("WARNING: the cell_size must be even, incrementing cell_size_x of 1")
        if csy % 2 != 0:
            csy += 1
            print("WARNING: the cell_size must be even, incrementing cell_size_y of 1")

        # Consider only the right part of the image
        # (if the rest doesn't fill a whole cell, just drop it)
        sx -= sx % csx
        sy -= sy % csy
        n_cells_x = sx // csx
        n_cells_y = sy // csy
        magnitude = mag[:sy, :sx]
        orientation = ori[:sy, :sx]
        by, bx = self.block_size

        orientation_histogram = interpolate(magnitude, orientation, csx, csy, sx, sy, n_cells_x, n_cells_y,
                                            signed_orientation, nbins)

        if normalise:
            normalised_blocks = normalise_histogram(orientation_histogram, bx, by, n_cells_x, n_cells_y, nbins)
        else:
            normalised_blocks = orientation_histogram

        if flatten:
            normalised_blocks = normalised_blocks.flatten()

        if visualise:
            # draw_histogram(normalised_blocks, csx, csy, signed_orientation)
            return normalised_blocks, visualise_histogram(normalised_blocks, csx, csy, signed_orientation)
        else:
            return normalised_blocks