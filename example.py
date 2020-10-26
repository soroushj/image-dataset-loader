import os
import image_dataset_loader

def example():
    dataset_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'example-data')
    set_names = ['train', 'test']
    (x_train, y_train), (x_test, y_test) = image_dataset_loader.load(dataset_path, set_names)

    print('x_train.shape:', x_train.shape)
    print('y_train.shape:', y_train.shape)
    print('x_test.shape:', x_test.shape)
    print('y_test.shape:', y_test.shape)

if __name__ == '__main__':
    example()
