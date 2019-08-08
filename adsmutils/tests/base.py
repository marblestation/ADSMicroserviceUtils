# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, division, print_function
import testing.postgresql
from flask_testing import TestCase
from adsmutils import ADSFlask


class TestCaseDatabase(TestCase):

    postgresql_url_dict = {
        u'port': 1234,
        u'host': u'127.0.0.1',
        u'user': u'postgres',
        u'database': u'test'
    }
    postgresql_url = u'postgresql://{user}@{host}:{port}/{database}' \
        .format(
            user=postgresql_url_dict[u'user'],
            host=postgresql_url_dict[u'host'],
            port=postgresql_url_dict[u'port'],
            database=postgresql_url_dict[u'database']
        )

    def create_app(self):
        '''Start the wsgi application'''
        local_config = {
            u'SQLALCHEMY_DATABASE_URI': self.postgresql_url,
            u'SQLALCHEMY_ECHO': False,
            u'TESTING': True,
            u'PROPAGATE_EXCEPTIONS': True,
            u'TRAP_BAD_REQUEST_ERRORS': True
        }
        app = ADSFlask(__name__, static_folder=None, local_config=local_config)
        return app

    @classmethod
    def setUpClass(cls):
        cls.postgresql = \
            testing.postgresql.Postgresql(**cls.postgresql_url_dict)

    @classmethod
    def tearDownClass(cls):
        cls.postgresql.stop()

    def setUp(self):
        pass

    def tearDown(self):
        self.app.db.session.remove()
        self.app.db.drop_all()


class TestCase(TestCase):

    def create_app(self):
        '''Start the wsgi application'''
        local_config = {}
        app = ADSFlask(__name__, static_folder=None, local_config=local_config)
        return app
