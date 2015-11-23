import sys

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from tnsnames.aliasFinder import AliasFinder
from tnsnames.tnsnamesLexer import tnsnamesLexer
from tnsnames.tnsnamesParser import tnsnamesParser


def main(argv):
    input_file_stream = FileStream(argv[1])
    lexer = tnsnamesLexer(input_file_stream)
    stream = CommonTokenStream(lexer)
    parser = tnsnamesParser(stream)
    tree = parser.tnsnames()

    listener = AliasFinder()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    for alias in listener.get_aliases:
        print(alias)


if __name__ == '__main__':
    main(sys.argv)
