from importlib.metadata import entry_points
from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    description='HR: CLI User export utility',
    author='author name',
    author_email='author@company.com',
    long_description=readme,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': 'hr=hr.cli:main'
    }
    )