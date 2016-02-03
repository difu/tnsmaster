import os
from unittest import TestCase

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from tnsnames.tnsnamesLexer import tnsnamesLexer
from tnsnames.tnsnameslineformatter import TnsnameLineFormatter
from tnsnames.tnsnamesparserewithexception import TnsNamesParserWithException

__author__ = 'dirkfuchs'


class TestTnsFormatter(TestCase):
    _tnsnames_file = None
    _script_path = None

    def setUp(self):
        self._script_path = os.path.dirname(os.path.abspath(__file__))
        self._tnsnames_file = '{0}/testFiles/tnsnames.ora'.format(self._script_path)

    def test_bad_tnsnames_file(self):
        tnsnames_file = '{0}/testFiles/tnsnames_false.ora'.format(self._script_path)
        input_file_stream = FileStream(tnsnames_file)

        lexer = tnsnamesLexer(input_file_stream)
        stream = CommonTokenStream(lexer)
        parser = TnsNamesParserWithException(stream)
        with self.assertRaisesRegexp(Exception, "Syntax error") as cm:
            tree = parser.tnsnames()

    def test_format_single_line(self):
        input_file_stream = FileStream(self._tnsnames_file)

        lexer = tnsnamesLexer(input_file_stream)
        stream = CommonTokenStream(lexer)
        parser = TnsNamesParserWithException(stream)
        tree = parser.tnsnames()

        listener = TnsnameLineFormatter()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert len(listener.get_lines) == 6
