#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:42:49 2025

@author: maryam
"""

import imageio.v3 as imageio
from PIL import Image
import numpy as np

my_image = "cat_in_iran.jpg"

#%% Load and resize an image

fname = "data/" + my_image

image = np.array(imageio.imread(fname))
print(image.shape)
image_pil = Image.fromarray(image)
image_resized = image_pil.resize((64, 64), Image.LANCZOS)
image_resized_np = np.array(image_resized)
print(image_resized_np.shape)
image_resized_np = image_resized_np.reshape((64*64*3,1))
print(image_resized_np.shape)

#%%

