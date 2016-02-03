from antlr4.error.ErrorListener import ErrorListener


class TnsErrorListenerException(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("Syntax error:  line " + str(line) + ":" + str(column) + " " + msg)
