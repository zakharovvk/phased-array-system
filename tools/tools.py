__all__ = [
    'sinc',
    'mask_1d',
    'mask_2d',
    'plot',
    'normalize',
    'integral_krit',
]

import math as m
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import trapz

def sinc(x):
    x = list(x)
    z = []
    for i in x:
        if i == 0:
            z.append(1)
        else: 
            z.append(m.sin(i) / i)
    return (np.array(z))

def mask_1d(part_of_vector: float, vector):
    if part_of_vector > 1:
        msg = 'Part of masking of vector can\'t be more than all vector.'
        raise ValueError(msg)
    elif part_of_vector < 0:
        msg = 'Part of masking of vector can\'t be less than all vector.'
        raise ValueError(msg)
    len_mask_side = int(len(vector) * part_of_vector / 2)
    vec_zeros = np.zeros(len_mask_side)
    vec_ones = np.ones(len(vector) - 2 * len_mask_side)
    mask_vec = np.concatenate([vec_zeros, vec_ones, vec_zeros])
    answer = mask_vec * vector 
    return answer

def mask_2d(part_of_mas_x: float, part_of_mas_y: float, mas):
    pass

def plot_1d(x1, y1, x2=None, y2=None, 
        x3=None, y3=None, x4=None, y4=None, *args, **kwargs):
    fig, ax = plt.subplots()
    x = [i for i in [x1, x2, x3, x4] if i is not None]
    y = [i for i in [y1, y2, y3, y4] if i is not None]
    sep = ['-', '--', '-.', ':']
    for num, var in enumerate(x):
        if var.all() != None:
            ax.plot(var, y[num], linestyle=sep[num])
    ax.grid(axis = 'both')        
    plt.show()

def plot_2d():
    pass

def normalize(vec: list):
    return vec / max(vec)

def integral_krit(func1: list, func2: list=None):
    if func2 is not None:
        return trapz(func1) / trapz(func2)
    else: 
        return trapz(func1) 
