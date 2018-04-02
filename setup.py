import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Don't import analytics-python module here, since deps may not be installed
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pymarketo'))

# python setup.py register -r pypi
# python setup.py sdist upload -r pypi

long_description = '''
PyMarketo is a Python client that wraps the MarketoRestPython project to provide a human friendly module and add bulk export capability.
'''

setup(
    name='pymarketo',
    version= '0.0.1',
    url='https://github.com/osamakhn/pymarketo',
    author='Osama Khan',
    author_email='osamakhn@gmail.com',
    packages=['pymarketo'],
    license='MIT License',
    install_requires=[
        'requests',
        'marketorestpython'
    ],
    keywords = ['Marketo', 'REST API', 'Wrapper', 'Client'],
    description='Python Client for the Marketo REST API',
    long_description=long_description
)