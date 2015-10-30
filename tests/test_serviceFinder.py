from unittest import TestCase

from antlr4 import *

import os

from tnsnames.tnsnamesLexer import tnsnamesLexer
from tnsnames.tnsnamesParser import tnsnamesParser
from tnsnames.serviceFinder import ServiceFinder

__author__ = 'dirkfuchs'


class TestServiceFinder(TestCase):

    _tnsnames_file = None

    def setUp(self):
        path = os.path.dirname(os.path.abspath(__file__))
        self._tnsnames_file = '{0}/testFiles/tnsnames.ora'.format(path)

    def test_get_aliases(self):
        input_file_stream = FileStream(self._tnsnames_file)

        lexer = tnsnamesLexer(input_file_stream)
        stream = CommonTokenStream(lexer)
        parser = tnsnamesParser(stream)
        tree = parser.tnsnames()

        listener = ServiceFinder()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        expected_aliases = ['LSNR_FRED', 'LSNR_WILMA', 'lsnr_barney', 'alias_1', 'alias_2.world',
                            'alias3.dunbar-it.co.uk']
        self.assertListEqual(listener.get_aliases, expected_aliases)
