from setuptools import setup
from os.path import join, dirname
import address

setup(
    name='address',
    version=address.__version__,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts': ['address = address.gui:main']
        },
    )
