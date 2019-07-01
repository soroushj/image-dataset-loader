# Load Image Dataset

Let's say you have an image dataset in a directory which looks like this:

```
data/
  train/
    cats/
      cat001.jpg
      cat002.jpg
      ...
    dogs/
      dog001.jpg
      dog002.jpg
      ...
  validation/
    cats/
      cat001.jpg
      cat002.jpg
      ...
    dogs/
      dog001.jpg
      dog002.jpg
      ...
```

You can use the `load_image_dataset` function to load this dataset as NumPy arrays:

```python
from load_image_dataset import load_image_dataset

(x_train, y_train), (x_valid, y_valid) = load_image_dataset('data', ['train', 'validation'])
```

The shape of the `x_*` arrays will be `(instances, rows, cols, channels)` for color images and `(instances, rows, cols)` for grayscale images. Also, the shape of the `y_*` arrays will be `(instances,)`.

All images in the dataset must have the same shape. Also, all data subsets (i.e., `train` and `validation` in this example) must contain the same set of classes. Class names will be sorted alphabetically. So, in this example, `cats` and `dogs` will be represented by `0` and `1`, respectively.

You can also load a single data subset. For example:

```python
(x_train, y_train), = load_image_dataset('data', ['train'])
```

Note that the comma after `(x_train, y_train)` is required, because the function always returns a tuple of tuples.

## API

```python
load_image_dataset(path, set_names,
                   shuffle=True, shuffle_seed=None,
                   x_dtype='uint8', y_dtype='uint32')
```

- **`path:`** Path to the dataset directory.
- **`set_names:`** List of the data subsets (subdirectories of the dataset directory).
- **`shuffle:`** Whether to shuffle the samples. If false, instances will be sorted by class name and file name.
- **`shuffle_seed:`** Random seed used for shuffling (see the [docs](https://docs.python.org/3/library/random.html#random.seed)).
- **`x_dtype:`** NumPy data type for the X arrays (see the [docs](https://www.numpy.org/devdocs/user/basics.types.html)).
- **`y_dtype:`** NumPy data type for the Y arrays (see the [docs](https://www.numpy.org/devdocs/user/basics.types.html)).
