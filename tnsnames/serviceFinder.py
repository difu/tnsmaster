from tnsnames.tnsnamesListener import tnsnamesListener
from tnsnames.tnsnamesParser import tnsnamesParser


class ServiceFinder(tnsnamesListener):
    def __init__(self):
        self._aliases = []

    def enterAlias(self, ctx: tnsnamesParser.AliasContext):
        self._aliases.append(ctx.getText())

    @property
    def get_aliases(self):
        """
            returns a list of all aliases of the tnsnames.ora.


        :return:    all aliases of the tnsnames.ora
        """
        return self._aliases
