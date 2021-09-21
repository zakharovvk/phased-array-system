all = [
    'Model_1d',
    'Model_2d',
]

from tools import tools as t
from numpy import sin, pi
import numpy as np
from numpy.fft import fft, fft2, fftshift
np.seterr(divide='ignore', invalid='ignore')


class Model_1d():
    def __init__(self, n: int=4, b: int=2, d: int=6, *, 
                plane: bool=True, accuracy: int=10000, grid_step: int=2):
        self.accuracy = accuracy
        self.subapertures = n
        self.aperture = b
        self.per_array = d
        self.grid_step = grid_step
        if plane == True:
            delta_kx = 4 * pi / self.accuracy
            nt = np.arange(self.accuracy)
            self.kx = delta_kx * (nt - self.accuracy / 2)
            self.x = self.aperture * self.kx / 2
        else:
            self.x = np.linspace(-pi/2, pi/2, self.accuracy)
            self.kx = pi * self.aperture * sin(self.x)
            self.x = self.kx

    def theoretical_equation(self):
        ans = t.sinc(self.x) * sin(
            self.subapertures * self.kx * self.per_array / self.aperture) / sin(
                self.kx * self.per_array / self.aperture)
        self.x = np.linspace(-1, 1, self.accuracy)
        if np.isnan(ans).any() == True:
            ans = ans[~np.isnan(ans)]
        if len(ans) != len(self.x):
            ans = np.concatenate([ans, np.zeros(int(len(self.x) - len(ans)))])
        return self.x, (ans * ans)

    def helmholtz_equation(self):
        vec_len_aperture = np.ones(self.aperture * self.grid_step)
        vec_len_period = np.zeros((self.per_array - self.aperture) * self.grid_step)
        vec_full_period = np.concatenate([vec_len_aperture, vec_len_period])
        end_vec = vec_len_period
        for i in range(self.subapertures):
            end_vec = np.concatenate([end_vec, vec_full_period])
        len_vec = int((self.accuracy - len(end_vec)) / 2)
        end_vec = np.concatenate([np.zeros(len_vec), end_vec, np.zeros(len_vec)])
        ans = fftshift((fft(end_vec)).real ** 2)
        x = np.linspace(-1, 1, self.accuracy)
        return x, ans
        
class Model_2d():
    def __init__(self, n_x: int=1, n_y: int=1, b: int=2, d: int=6, 
                b_y: int=2, d_y: int=6, *, plane: bool=True, 
                accuracy: int=10000, grid_step: int=2):
        self.accuracy = accuracy
        self.subapertures_x = n_x
        self.subapertures_y = n_y
        self.aperture_x = b
        self.aperture_y = b_y
        self.per_array_x = d
        self.per_array_y = d_y
        self.grid_step = grid_step
        
    def theoretical_equation(self):
        pass
    
    def helmholtz_equation(self):
        vec_len_aperture = np.ones(self.aperture_x * self.grid_step,
            self.aperture_y * self.grid_step)
        vec_len_period_x = np.zeros((
            self.aperure_x * self.grid_step - self.aperture_y * self.grid_step) / 2,
            self.aperture_y * self.grid_step)
        vec_len_period_y = np.zeros(())
        