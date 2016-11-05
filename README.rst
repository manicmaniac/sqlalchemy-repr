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


Example
-------

``sqlalchemy_repr.RepresentableBase`` is mixin to add simple representation of columns.

.. code:: python

    >>> from datetime import datetime

    >>> from sqlalchemy import Column, DateTime, Integer, Unicode, create_engine
    >>> from sqlalchemy.ext.declarative import declarative_base
    >>> from sqlalchemy.orm import sessionmaker
    >>> from sqlalchemy_repr import RepresentableBase

    >>> Base = declarative_base(cls=RepresentableBase)

    >>> class User(Base):
    ...    __tablename__ = 'users'
    ...    id = Column(Integer, primary_key=True)
    ...    name = Column(Unicode(255), nullable=False, unique=True)
    ...    created = Column(DateTime, nullable=False)

    >>> engine = create_engine('sqlite://')
    >>> Base.metadata.create_all(engine)

    >>> Session = sessionmaker(bind=engine)
    >>> session = Session()

    >>> user = User(name='spam', created=datetime(2016, 6, 1))
    >>> session.add(user)
    >>> session.commit()

    >>> print(user)
    <User id=1, name='spam', created='2016-06-01T00:00:00'>

``sqlalchemy_repr.PrettyRepresentableBase`` brings pretty, indented multi-line representation.

.. code:: python

    >>> from sqlalchemy_repr import PrettyRepresentableBase
    >>> Base = declarative_base(cls=PrettyRepresentableBase)

    >>> class User(Base):
    ...    __tablename__ = 'users'
    ...    id = Column(Integer, primary_key=True)
    ...    first_name = Column(Unicode(255), nullable=False, unique=True)
    ...    last_name = Column(Unicode(255), nullable=False, unique=True)
    ...    email = Column(Unicode(255), nullable=False)
    ...    created = Column(DateTime, nullable=False)
    ...    modified = Column(DateTime, nullable=False)

    >>> engine = create_engine('sqlite://')
    >>> Base.metadata.create_all(engine)

    >>> Session = sessionmaker(bind=engine)
    >>> session = Session()

    >>> user = User(first_name='spam', last_name='ham',  email='spam@example.com', created=datetime(2016, 6, 1), modified=datetime(2016, 6, 1))
    >>> session.add(user)
    >>> session.commit()

    >>> print(user)
    <User
        id=1,
        first_name='spam',
        last_name='ham',
        email='spam@example.com',
        created='2016-06-01T00:00:00',
        modified='2016-06-01T00:00:00'>
