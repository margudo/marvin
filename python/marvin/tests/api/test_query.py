#!/usr/bin/env python

from __future__ import print_function, division, absolute_import
import copy
import unittest
from marvin import config
from marvin.api.query import QueryView
from marvin.core import MarvinError


class TestQuery(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initconfig = copy.deepcopy(config)

    def setUp(self):
        cvars = ['mode', 'drpver', 'dapver', 'mplver']
        for var in cvars:
            config.__setattr__(var, self.initconfig.__getattribute__(var))

    def test_cube_query_filter(self):
        qv = QueryView()
        qv.results['inconfig'] = {}
        qv.results['inconfig']['strfilter'] = 'nsa_redshift<0.1'
        qv.cube_query()
        desired = 'nsa_redshift<0.1'
        self.assertEqual(qv.results['filter'], desired)

    def test_cube_query_filter_error(self):
        qv = QueryView()
        qv.results['inconfig'] = {}
        qv.results['inconfig']['strfilter'] = 'fake_parameter<0.1'
        desired = ("Could not set parameters. Multiple entries found for key."
                   "  Be more specific: 'fake_parameter does not match any"
                   " column.'")
        try:
            qv.cube_query()
        except MarvinError:
            self.assertEqual(qv.results['error'], desired)


if __name__ == '__main__':
    verbosity = 2
    unittest.main(verbosity=verbosity)
