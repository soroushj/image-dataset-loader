import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='image-dataset-loader',
    version='0.0.1',
    url='https://github.com/soroushj/image-dataset-loader',
    author='Soroush Javadi',
    author_email='soroush.javadi@gmail.com',
    license='MIT',
    description='Load image datasets as NumPy arrays',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=[
        'datasets',
        'image-datasets',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
    ],
    install_requires=[
        'numpy>=1.0.0',
        'imageio>=2.0.0',
    ],
    python_requires='>=3.0',
    py_modules=['image_dataset_loader'],
)
