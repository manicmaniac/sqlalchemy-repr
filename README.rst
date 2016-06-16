sqlalchemy-repr
===============

.. image:: https://travis-ci.org/manicmaniac/sqlalchemy-repr.svg?branch=master
    :target: https://travis-ci.org/manicmaniac/sqlalchemy-repr

Automatically generates pretty ``repr`` of a SQLAlchemy model.

Install
-------

.. code:: sh

    pip install sqlalchemy-repr


Usage
-----

.. code:: python

    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy_repr import RepresentableBase

    Base = declarative_base(cls=RepresentableBase)
