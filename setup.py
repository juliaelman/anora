import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


setup(
    name='anora',
    version=__import__('anora').__version__,
    author='Julia Elman',
    author_email='julia.elman@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/juliaelman/anora',
    license='BSD',
    description=u' '.join(__import__('anora').__doc__.splitlines()).strip(),
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',        
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=read_file('README.md'),
)
