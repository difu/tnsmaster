from antlr4 import *

from tnsnames.tnserrorlistenerexception import TnsErrorListenerException
from tnsnames.tnsnamesParser import tnsnamesParser


class TnsNamesParserWithException(tnsnamesParser):
    def __init__(self, input: TokenStream):
        super().__init__(input)
        error_listener_ex = TnsErrorListenerException()
        self.removeErrorListeners()
        self.addErrorListener(error_listener_ex)
