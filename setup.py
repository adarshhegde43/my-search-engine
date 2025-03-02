from distutils.core import setup

setup(
    name = "microsearch",
    version = "1.0.0",
    description = "A small search library.",
    long_description=open('README.rst', 'r').read(),
    py_modules = [
        'microsearch'
    ],
    classifiers = [
        'Intended Audience :: Everyone',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
    ],
)
