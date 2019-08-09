# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, division, print_function
import unittest
import mock
from .base import TestCase, TestCaseDatabase


class TestServices(TestCase):

    def test_readiness_probe(self):
        '''Tests for the existence of a /ready route, and that it returns properly
        formatted JSON data'''
        r = self.client.get(u'/ready')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json[u'ready'], True)

    def test_liveliness_probe(self):
        '''Tests for the existence of a /alive route, and that it returns properly
        formatted JSON data'''
        r = self.client.get(u'/alive')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json[u'alive'], True)


class TestServicesWithDatabase(TestCaseDatabase):

    def test_readiness_probe(self):
        '''Tests for the existence of a /ready route, and that it returns properly
        formatted JSON data'''
        r = self.client.get(u'/ready')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json[u'ready'], True)

    def test_liveliness_probe(self):
        '''Tests for the existence of a /alive route, and that it returns properly
        formatted JSON data'''
        r = self.client.get(u'/alive')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json[u'alive'], True)

    def test_readiness_probe_with_db_failure(self):
        '''Tests for the existence of a /ready route, and that it returns properly
        formatted JSON data when database connection has been lost'''
        self.app._db_failure = mock.MagicMock(return_value=True)
        r = self.client.get(u'/ready')
        self.assertEqual(r.status_code, 503)
        self.assertEqual(r.json[u'ready'], False)

    def test_liveliness_probe_with_db_failure(self):
        '''Tests for the existence of a /alive route, and that it returns properly
        formatted JSON data when database connection has been lost'''
        self.app._db_failure = mock.MagicMock(return_value=True)
        r = self.client.get(u'/alive')
        self.assertEqual(r.status_code, 503)
        self.assertEqual(r.json[u'alive'], False)


if __name__ == '__main__':
    unittest.main()
