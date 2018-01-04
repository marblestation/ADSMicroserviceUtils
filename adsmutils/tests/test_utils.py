#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os

import unittest
import json
import inspect
from mock import patch

import adsmutils

class TestAdsUtils(unittest.TestCase):
    """
    Tests the appliction's methods
    """
    def setUp(self):
        unittest.TestCase.setUp(self)


    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_load_config(self):
        with patch('adsmutils.load_module') as load_module:
            app_name = "TEST"
            c = adsmutils.load_config(app_name)
            f = os.path.abspath(os.path.join(os.path.dirname(inspect.getsourcefile(adsmutils)), '..'))
            self.assertEquals((f + '/config.py',),
                              load_module.call_args_list[0][0])
            self.assertEquals((f + '/local_config.py',),
                              load_module.call_args_list[1][0])
            self.assertEqual(c['PROJ_HOME'], f)

        with patch('adsmutils.load_module') as load_module:
            app_name = "TEST"
            adsmutils.load_config(app_name, '/tmp')
            self.assertEquals(('/tmp/config.py',),
                              load_module.call_args_list[0][0])
            self.assertEquals(('/tmp/local_config.py',),
                              load_module.call_args_list[1][0])


    def test_load_module(self):
        f = os.path.abspath(os.path.join(os.path.dirname(inspect.getsourcefile(adsmutils)), './tests/config_sample.py'))
        x = adsmutils.load_module(f)
        self.assertEquals(x, {'FOO': {'bar': ['baz', 1]}})

    def test_update_from_env(self):
        os.environ["FOO"] = "2"
        os.environ["BAR"] = "False"
        os.environ["TEST_BAR"] = "True"
        conf = {'FOO': 1, 'BAR': False}
        adsmutils.conf_update_from_env("TEST", conf)
        self.assertEquals(conf, {'FOO': 2, 'BAR': True})


    def test_setup_logging(self):
        with patch('adsmutils.ConcurrentRotatingFileHandler') as cloghandler:
            adsmutils.setup_logging('app')
            f = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
            self.assertEqual("call(backupCount=10, encoding=u'UTF-8', filename=u'{filename}/logs/app.log', maxBytes=10485760, mode=u'a')".format(filename=f),
                             str(cloghandler.call_args))


    def test_get_date(self):
        """Check we always work with UTC dates"""

        d = adsmutils.get_date()
        self.assertTrue(d.tzname() == 'UTC')

        d1 = adsmutils.get_date('2009-09-04T01:56:35.450686Z')
        self.assertTrue(d1.tzname() == 'UTC')
        self.assertEqual(d1.isoformat(), '2009-09-04T01:56:35.450686+00:00')

        d2 = adsmutils.get_date('2009-09-03T20:56:35.450686-05:00')
        self.assertTrue(d2.tzname() == 'UTC')
        self.assertEqual(d2.isoformat(), '2009-09-04T01:56:35.450686+00:00')

        d3 = adsmutils.get_date('2009-09-03T20:56:35.450686')
        self.assertTrue(d3.tzname() == 'UTC')
        self.assertEqual(d3.isoformat(), '2009-09-03T20:56:35.450686+00:00')


if __name__ == '__main__':
    unittest.main()
