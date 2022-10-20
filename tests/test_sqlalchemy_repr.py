from datetime import datetime
import re
from textwrap import dedent
import unittest

from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Unicode,
                        UnicodeText, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy_repr import Repr, PrettyRepr

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    text = Column(UnicodeText, nullable=False, default='')
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)


class EntryWithBlacklistAndWhitelist(Base):
    __tablename__ = 'entries_with_blacklist'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    text = Column(UnicodeText, nullable=False, default='')
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    __repr_blacklist__ = ('text',)
    __repr_whitelist__ = ('text', 'title')


class TestRepr(unittest.TestCase):
    def setUp(self):
        engine = create_engine('sqlite://')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)

        self._date = datetime.now()
        self._date_str = self._date.isoformat()

        self.session = Session()
        self.entry = Entry(title='ham', text=self.dummy_text, user_id=1)
        self.blacklist_entry = EntryWithBlacklistAndWhitelist(title='ham', text=self.dummy_text, user_id=1)
        self.user = User(name='spam', created=self._date)
        self.session.add(self.user)
        self.session.add(self.entry)
        self.session.add(self.blacklist_entry)
        self.session.commit()

    def test_repr_with_user(self):
        result = Repr().repr(self.user)
        pattern = r"<User id=1, name=u?'spam', created='{0}'".format(
            self._date_str
        )
        self.assertMatch(result, pattern)

    def test_repr_with_entry(self):
        result = Repr().repr(self.entry)
        pattern = r"<Entry id=1, title=u?'ham', text=u?'Lorem.*', user_id=1"
        self.assertMatch(result, pattern)

    def test_repr_with_plain_python_object(self):
        result = Repr().repr([])
        self.assertEqual(result, '[]')

    def test_pretty_repr_with_user(self):
        result = PrettyRepr().repr(self.user)
        pattern = r"<User\n    id=1,\n    name=u?'spam',\n    created='{0}'>".format(
            self._date_str
        )
        self.assertMatch(result, pattern)

    def test_pretty_repr_with_entry(self):
        result = PrettyRepr().repr(self.entry)
        pattern = r"<Entry\n    id=1,\n    title=u?'ham',\n    text=u?'Lorem.*',\n    user_id=1>"
        self.assertMatch(result, pattern)

    def test_pretty_repr_with_blacklist_and_whitelist(self):
        result = PrettyRepr().repr(self.blacklist_entry)
        pattern = r"<EntryWithBlacklistAndWhitelist\n    title=u?'ham'>"
        self.assertMatch(result, pattern)

    def assertMatch(self, string, pattern):
        if not re.match(pattern, string):
            message = "%r doesn't match %r" % (string, pattern)
            raise AssertionError(message)

    dummy_text = dedent("""\
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
    ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit
    in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident,
    sunt in culpa qui officia deserunt mollit anim id est laborum.
    """)


if __name__ == '__main__':
    unittest.main()
