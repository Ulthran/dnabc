import setuptools

setuptools.setup(
    name='dnabc',
    version="0.0.3",
    description='Demultiplex pooled DNA sequencing data',
    author='Kyle Bittinger',
    author_email='kylebittinger@gmail.com',
    url='https://github.com/PennChopMicrobiomeProgram',
    packages=['dnabclib'],
    entry_points={
        'console_scripts': [
            'dnabc.py=dnabclib.main:main',
            'get_sample_names.py=dnabclib.main:get_sample_names_main',
            'make_index.py=dnabclib.make_index:main',
            'split_samplelanes.py=dnabclib.split_samplelanes:main',
        ],
    },
)
