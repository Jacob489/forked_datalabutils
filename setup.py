from setuptools import setup, find_packages

setup(
    name='astrodatalab',
    version='0.1.0',
    author='Jacob Nowack',
    author_email='truenorthproductions87@gmail.com',
    description='Utilities for astrolab UCLA Research Project',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    url='https://github.com/Jacob489/forked_datalabutils/tree/master',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'albumentations==1.4.12',
        'astropy==6.1.2',
        'h5py==3.11.0',
        'matplotlib==3.9.1',
        'numpy==2.0.1',
        'pandas==2.2.2',
        'scikit_learn==1.5.1',
        'scipy==1.14.0',
        'seaborn==0.13.2',
        'tabulate==0.9.0',
        'tensorflow==2.17.0'
    ],
    extras_require={
        'dev': [
            'pip>=23.3',
            'bump2version==0.5.11',
            'wheel>=0.38.1',
            'watchdog==0.9.0',
            'tox==3.14.0',
            'coverage==4.5.4',
            'Sphinx==7.2.6',
            'twine==5.0.0',
            'ruff==0.3.5',
            'pytest==6.2.4',
        ],
    },
)
