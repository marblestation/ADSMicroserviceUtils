# -*- coding: utf-8 -*-

from adsmutils import ADSFlask
import unittest


class TestUpdateRecords(unittest.TestCase):

    def test_config(self):
        app = ADSFlask('test',local_config={
            'FOO': ['bar', {}],
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///',
            })
        self.assertEqual(app._config['FOO'], ['bar', {}])
        self.assertEqual(app.config['FOO'], ['bar', {}])
        self.assertTrue(app.db)
        

if __name__ == '__main__':
    unittest.main()
