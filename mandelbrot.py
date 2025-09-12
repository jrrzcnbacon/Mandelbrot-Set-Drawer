import numpy as np
from PIL import Image

def mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    # Create a linearly spaced array for the real and imaginary axes
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    # Create a grid of complex numbers
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros(C.shape, dtype=complex)
    # Initialize the array to hold the number of iterations for each point
    img = np.zeros(C.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask] ** 2 + C[mask]
        img[mask] = i

    # Normalize the values to 0-255 for grayscale
    img = (img / img.max() * 255).astype(np.uint8)
    return img

if __name__ == "__main__":
    WIDTH, HEIGHT = 800, 600
    X_MIN, X_MAX = -2.0, 1.0
    Y_MIN, Y_MAX = -1.5, 1.5
    MAX_ITER = 100

    mandel_img = mandelbrot(WIDTH, HEIGHT, X_MIN, X_MAX, Y_MIN, Y_MAX, MAX_ITER)
    image = Image.fromarray(mandel_img)
    image.save("mandelbrot.png")
    print("Saved Mandelbrot set image as mandelbrot.png")
