# image-dataset-loader: Load image datasets as NumPy arrays

Suppose you have an image dataset in a directory which looks like this:

```
data/
  train/
    cats/
      cat0001.jpg
      cat0002.jpg
      ...
    dogs/
      dog0001.jpg
      dog0002.jpg
      ...
  test/
    cats/
      cat0001.jpg
      cat0002.jpg
      ...
    dogs/
      dog0001.jpg
      dog0002.jpg
      ...
```

You can use the `image_dataset_loader.load` function to load this dataset as NumPy arrays:

```python
import image_dataset_loader

(x_train, y_train), (x_test, y_test) = image_dataset_loader.load('./data', ['train', 'test'])
```

The shape of the `x_*` arrays will be `(instances, rows, cols, channels)` for color images and `(instances, rows, cols)` for grayscale images.
Also, the shape of the `y_*` arrays will be `(instances,)`.

All images in the dataset must have the same shape.
Also, all data subsets (i.e., `train` and `test` in this example) must contain the same set of classes.
Class names will be sorted alphabetically.
So, in this example, `cats` and `dogs` will be represented by `0` and `1`, respectively.

You can also load a single data subset. For example:

```python
(x_train, y_train), = image_dataset_loader.load('./data', ['train'])
```

Note that the comma after `(x_train, y_train)` is required, because the function always returns a tuple of tuples.

## API

```python
load(dataset_path, set_names,
     shuffle=True, seed=None,
     x_dtype='uint8', y_dtype='uint32')
```

- **`dataset_path:`** Path to the dataset directory.
- **`set_names:`** List of the data subsets (subdirectories of the dataset directory).
- **`shuffle:`** Whether to shuffle the samples. If false, instances will be sorted by class name and then by file name.
- **`seed:`** Random seed used for shuffling (see the [docs](https://docs.python.org/3/library/random.html#random.seed)).
- **`x_dtype:`** NumPy data type for the X arrays (see the [docs](https://numpy.org/devdocs/user/basics.types.html)).
- **`y_dtype:`** NumPy data type for the Y arrays (see the [docs](https://numpy.org/devdocs/user/basics.types.html)).
- Returns a tuple of `(x, y)` tuples corresponding to `set_names`.
