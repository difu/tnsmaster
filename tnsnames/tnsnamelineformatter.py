from tnsnames.tnsnamesListener import tnsnamesListener
from tnsnames.tnsnamesParser import tnsnamesParser


class TnsnameLineFormatter(tnsnamesListener):
    def __init__(self):
        self._level = 0
        self._indents = 4
        self._lines = []

    @property
    def get_lines(self):
        return self._lines

    def set_indents(self, indents):
        self._indents = indents

    # Enter a parse tree produced by tnsnamesParser#tns_entry.
    def enterTns_entry(self, ctx: tnsnamesParser.Tns_entryContext):
        self._lines.append(ctx.getText())

    # Enter a parse tree produced by tnsnamesParser#lsnr_entry.
    def enterLsnr_entry(self, ctx: tnsnamesParser.Lsnr_entryContext):
        self._lines.append(ctx.getText())
