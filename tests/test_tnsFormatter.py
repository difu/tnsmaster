import os
from unittest import TestCase

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from tnsnames.tnsnamesLexer import tnsnamesLexer
from tnsnames.tnsnamesParser import tnsnamesParser
from tnsnames.tnsnameslineformatter import TnsnameLineFormatter

__author__ = 'dirkfuchs'


class TestTnsFormatter(TestCase):
    _tnsnames_file = None

    def setUp(self):
        path = os.path.dirname(os.path.abspath(__file__))
        self._tnsnames_file = '{0}/testFiles/tnsnames.ora'.format(path)

    def test_format_single_line(self):
        input_file_stream = FileStream(self._tnsnames_file)

        lexer = tnsnamesLexer(input_file_stream)
        stream = CommonTokenStream(lexer)
        parser = tnsnamesParser(stream)
        tree = parser.tnsnames()

        listener = TnsnameLineFormatter()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert len(listener.get_lines) == 6
