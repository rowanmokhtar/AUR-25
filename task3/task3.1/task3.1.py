#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import cv2

def convolve(image, kernel):
    kernel = np.flipud(np.fliplr(kernel))
    k_h, k_w = kernel.shape
    #print(kernel.shape)
    pad_h, pad_w = k_h // 2, k_w // 2
    #print(pad_h,pad_w)
    padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant')
    output = np.zeros_like(image, dtype=float)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded[i:i+k_h, j:j+k_w]
            output[i, j] = np.sum(region * kernel) #dot product
    return output

def median_filter(image, size=3):
    pad = size // 2
    padded = np.pad(image, ((pad, pad), (pad, pad)), mode='constant')
    output = np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded[i:i+size, j:j+size]
            output[i, j] = np.median(region)
    return output

def gaussian_kernel(size=5, sigma=1):
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2) / (2. * sigma**2))
    return kernel / np.sum(kernel)


img = cv2.imread('/home/rowan/Downloads/noise.jpg', cv2.IMREAD_GRAYSCALE)   #change path
fig, axes = plt.subplots(2,3,figsize=(12,8))

axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')

axes[0, 1].imshow(convolve(img, np.ones((5, 5)) / 25), cmap='gray')  
axes[0, 1].set_title('Box Filter')
axes[0, 1].axis('off')


axes[1, 0].imshow(convolve(img, np.array([[-1, 0, 1],
                                          [-2, 0, 2],
                                          [-1, 0, 1]])), cmap='gray')
axes[1, 0].set_title('Horizontal Sobel Filter')
axes[1, 0].axis('off')

axes[1, 1].imshow(convolve(img, np.array([[-1, -2, -1],
                                          [ 0,  0,  0],
                                          [ 1,  2,  1]])), cmap='gray')
axes[1, 1].set_title('Vertical Sobel Filter')
axes[1, 1].axis('off')
###
axes[1, 2].imshow(median_filter(img, size=3), cmap='gray')
axes[1, 2].set_title('Median Filter')
axes[1, 2].axis('off')

axes[0, 2].imshow(convolve(img, gaussian_kernel(size=5,sigma =1)), cmap='gray')
axes[0, 2].set_title('Gaussian Filter')
axes[0, 2].axis('off')

plt.tight_layout()
plt.show()
