from setuptools import setup

setup(
    name='sqlalchemy-repr',
    version='0.0.1',
    description='Automatically generates pretty repr of a SQLAlchemy model.',
    long_description=open('README.rst').read(),
    keywords='pprint pretty print repr sqlalchemy extension',
    author='Ryosuke Ito',
    author_email='rito.0305@gmail.com',
    url='https://github.com/manicmaniac/sqlalchemy-repr',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Database :: Front-Ends',
    ],
    py_modules=['sqlalchemy_repr'],
    install_requires=['SQLAlchemy'],
    test_suite='tests',
)
