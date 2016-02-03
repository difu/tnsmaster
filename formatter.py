import argparse
from io import StringIO

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker, InputStream

from tnsnames.format import Format
from tnsnames.tnsnamesLexer import tnsnamesLexer
from tnsnames.tnsnameslineformatter import TnsnameLineFormatter
from tnsnames.tnsnamesorastyleformatter import TnsnameOraStyleFormatter
from tnsnames.tnsnamesparserewithexception import TnsNamesParserWithException


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tnsnamesFile", type=str, help="the filename of the tnsnames file to be formatted")
    parser.add_argument("-f", "--format", choices=[Format.oneLine.name, Format.oracle.name],
                        help="format to be applied",
                        default=Format.oracle.name)
    parser.add_argument("--lowerkeys", action='store_true',
                        help="lowercase keys (case handling for keys must be activated!)",
                        default=False)
    parser.add_argument("--lowervalues", action='store_true',
                        help="lowercase keys (case handling for values must be activated!)",
                        default=False)
    parser.add_argument("--handlekeycase", action='store_true', help="activate case handling for keys",
                        default=False)
    parser.add_argument("--handlevaluecase", action='store_true', help="activate case handling for values",
                        default=False)

    args = parser.parse_args()

    listener_ora_style = TnsnameOraStyleFormatter()
    listener_ora_style.set_uppercase_keywords(not args.lowerkeys)
    listener_ora_style.set_uppercase_value(not args.lowervalues)
    listener_ora_style.set_ignore_keyword_case(not args.handlekeycase)
    listener_ora_style.set_ignore_value_case(not args.handlevaluecase)

    try:
        input_file_stream = FileStream(args.tnsnamesFile)
    except FileNotFoundError:
        print(args.tnsnamesFile + " not found!")
        exit(1)

    lexer = tnsnamesLexer(input_file_stream)
    ora_stream = CommonTokenStream(lexer)
    tns_parser = TnsNamesParserWithException(ora_stream)
    try:
        tree = tns_parser.tnsnames()
    except Exception as ex:
        print("Error while parsing: " + ex.__str__())
        exit(1)

    walker = ParseTreeWalker()
    walker.walk(listener_ora_style, tree)

    buf = StringIO()

    if args.format == Format.oracle.name:
        for line in listener_ora_style.get_lines:
            print(line)
        exit(0)

    for line in listener_ora_style.get_lines:
        buf.write(line)

    listener_line_style = TnsnameLineFormatter()
    input_text_stream = InputStream(buf.getvalue())
    line_lexer = tnsnamesLexer(input_text_stream)
    line_stream = CommonTokenStream(line_lexer)
    line_parser = TnsNamesParserWithException(line_stream)
    try:
        tree = line_parser.tnsnames()
    except Exception as ex:
        print("Error while parsing: " + ex.__str__())
        exit(1)

    walker.walk(listener_line_style, tree)

    for line2 in listener_line_style.get_lines:
        print(line2)

if __name__ == '__main__':
    main()
