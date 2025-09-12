# Mandelbrot Set Drawer

This project provides a simple Python script to draw the Mandelbrot set and save it as an image file.

## Features

- Generates a high-resolution image of the Mandelbrot set.
- Fully configurable width, height, and iteration settings.
- Saves the result as a PNG image.

## Requirements

- Python 3.x
- [numpy](https://numpy.org/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)

Install dependencies with:

```bash
pip install numpy pillow
```

## Usage

1. Save the script as `mandelbrot.py`.
2. Run the script:

   ```bash
   python mandelbrot.py
   ```

3. The generated image `mandelbrot.png` will be saved in the same directory.

## Customization

You can change image size, coordinates, and iteration count in the script:

```python
WIDTH, HEIGHT = 800, 600
X_MIN, X_MAX = -2.0, 1.0
Y_MIN, Y_MAX = -1.5, 1.5
MAX_ITER = 100
```

## Example Output

![mandelbrot.png](mandelbrot.png)

## License

This project is licensed under the MIT License.
