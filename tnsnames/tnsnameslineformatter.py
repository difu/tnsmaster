from tnsnames.tnsnamesParser import tnsnamesParser
from tnsnames.tnsnamesformatter import TnsnamesFormatter


class TnsnameLineFormatter(TnsnamesFormatter):
    def __init__(self):
        super().__init__()
        self._lines = []

    @property
    def get_lines(self):
        return self._lines

    # Enter a parse tree produced by tnsnamesParser#tns_entry.
    def enterTns_entry(self, ctx: tnsnamesParser.Tns_entryContext):
        self._lines.append(ctx.getText())

    # Enter a parse tree produced by tnsnamesParser#lsnr_entry.
    def enterLsnr_entry(self, ctx: tnsnamesParser.Lsnr_entryContext):
        self._lines.append(ctx.getText())
