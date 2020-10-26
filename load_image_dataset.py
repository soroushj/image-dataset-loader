import os
import random
import imageio
import numpy as np

def get_class_names(subset_path):
    """Get the class names for a subset.

    Args:
    subset_path: Path to the subset directory.
    Returns a sorted list of class names.
    """
    names = [name for name in os.listdir(subset_path) if os.path.isdir(os.path.join(subset_path, name))]
    names.sort()
    return names

def load_image_dataset(dataset_path, set_names,
                       shuffle=True, seed=None,
                       x_dtype='uint8', y_dtype='uint32'):
    """Load an image dataset as NumPy arrays.

    Args:
    dataset_path: Path to the dataset directory.
    set_names: List of the data subsets (subdirectories of the dataset directory).
    shuffle: Whether to shuffle the samples. If false, instances will be sorted by
        class name and then by file name.
    seed: Random seed used for shuffling.
    x_dtype: NumPy data type for the X arrays.
    y_dtype: NumPy data type for the Y arrays.
    Returns a tuple of (x, y) tuples corresponding to set_names.
    """
    if len(set_names) == 0:
        raise ValueError('At least one set name is required.')
    sets_class_names = [get_class_names(os.path.join(dataset_path, set_name)) for set_name in set_names]
    for i in range(1, len(sets_class_names)):
        if sets_class_names[i] != sets_class_names[0]:
            raise RuntimeError('Class names are not consistent.')
    class_names = sets_class_names[0]
    dataset = []
    instance_shape = None
    if shuffle:
        rand = random.Random(seed)
    for set_name in set_names:
        x = []
        y = []
        for class_index, class_name in enumerate(class_names):
            class_path = os.path.join(dataset_path, set_name, class_name)
            instance_paths = [os.path.join(class_path, name) for name in os.listdir(class_path)]
            if not shuffle:
                instance_paths.sort()
            for instance_path in instance_paths:
                instance = imageio.imread(instance_path)
                if instance_shape is None:
                    instance_shape = instance.shape
                elif instance_shape != instance.shape:
                    raise RuntimeError('Instance shapes are not consistent.')
                x.append(instance)
                y.append(class_index)
        if shuffle:
            xy = list(zip(x, y))
            rand.shuffle(xy)
            x, y = zip(*xy)
        x = np.array(x, dtype=x_dtype)
        y = np.array(y, dtype=y_dtype)
        dataset.append((x, y))
    return tuple(dataset)
