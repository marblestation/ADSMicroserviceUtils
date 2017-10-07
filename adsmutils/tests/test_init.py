# -*- coding: utf-8 -*-

import adsmutils
import unittest
import os

def _read_file(fpath):
    with open(fpath, 'r') as fi:
        return fi.read()
    
class TestInit(unittest.TestCase):

    def test_logging(self):
        logdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../logs'))
        foo_log = logdir + '/foo.bar.log'
        if os.path.exists(foo_log):
            os.remove(foo_log)
        logger = adsmutils.setup_logging('foo.bar')
        logger.warn('first')
        logger.handlers[0].stream.flush()
        #print foo_log
        self.assertTrue(os.path.exists(foo_log))
        c = _read_file(foo_log)
        self.assertTrue('test_init.py:19] first' in c)
                    
        # now multiline message
        logger.warn('second\nthird')
        logger.warn('last')
        c = _read_file(foo_log)
        #print c
        self.assertTrue('second\n     third' in c)
        

if __name__ == '__main__':
    unittest.main()
