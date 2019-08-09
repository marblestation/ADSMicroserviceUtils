# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, division, print_function
import unittest
from adsmutils import ADSFlask


class TestUpdateRecords(unittest.TestCase):

    def test_config(self):
        app = ADSFlask(u'test', local_config={
            u'FOO': [u'bar', {}],
            u'SQLALCHEMY_DATABASE_URI': u'sqlite:///',
            })
        self.assertEqual(app._config[u'FOO'], [u'bar', {}])
        self.assertEqual(app.config[u'FOO'], [u'bar', {}])
        self.assertTrue(app.db)
        

if __name__ == '__main__':
    unittest.main()
