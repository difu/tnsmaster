import argparse

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from tnsnames.format import Format
from tnsnames.tnsnamesLexer import tnsnamesLexer
from tnsnames.tnsnamesParser import tnsnamesParser
from tnsnames.tnsnameslineformatter import TnsnameLineFormatter
from tnsnames.tnsnamesorastyleformatter import TnsnameOraStyleFormatter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tnsnamesFile", type=str, help="the filename of the tnsnames file to be formatted")
    parser.add_argument("-f", "--format", choices=[Format.oneLine.name, Format.oracle.name],
                        help="format to be applied",
                        default=Format.oracle.name)
    parser.add_argument("--lowerkeys", action='store_true', help="lowercase keys",
                        default=False)
    parser.add_argument("--lowervalues", action='store_true', help="lowercase keys",
                        default=False)
    parser.add_argument("--handlekeycase", action='store_true', help="ToDo",
                        default=False)
    parser.add_argument("--handlevaluecase", action='store_true', help="ToDo",
                        default=False)

    args = parser.parse_args()
    if args.format == Format.oracle.name:
        _listener = TnsnameOraStyleFormatter()
        _listener.set_uppercase_keywords(not args.lowerkeys)
        _listener.set_uppercase_value(not args.lowervalues)
        _listener.set_ignore_keyword_case(not args.handlekeycase)
        _listener.set_ignore_value_case(not args.handlevaluecase)

    else:
        _listener = TnsnameLineFormatter()

    input_file_stream = FileStream(args.tnsnamesFile)
    lexer = tnsnamesLexer(input_file_stream)
    stream = CommonTokenStream(lexer)
    parser = tnsnamesParser(stream)
    tree = parser.tnsnames()

    walker = ParseTreeWalker()
    walker.walk(_listener, tree)

    for line in _listener.get_lines:
        print(line)


if __name__ == '__main__':
    main()
