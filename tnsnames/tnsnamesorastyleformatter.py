from antlr4 import ParserRuleContext

from tnsnames.tnsnamesParser import tnsnamesParser
from tnsnames.tnsnamesformatter import TnsnamesFormatter


class TnsnameOraStyleFormatter(TnsnamesFormatter):
    def __init__(self):
        super().__init__()
        self._current_line = ""
        self._level = 0
        self._indents = 4
        self._ignore_keyword_case = True
        self._ignore_value_case = True
        self._uppercase_keywords = True
        self._uppercase_values = True

    @property
    def get_indents_string(self):
        """
        get a string containing whitespaces corresponding to the stack level and number of indents per level

        :rtype: str
        :return: Returns whitespace string
        """
        ret_string = " " * self._indents * self._level
        return ret_string

    def set_ignore_keyword_case(self, ignore: bool):
        """
        If set to true, the parser will not change upper/lower case spelling of the keyword

        """
        self._ignore_keyword_case = ignore

    def set_ignore_value_case(self, ignore: bool):
        """
        If set to true, the parser will not change upper/lower case spelling of the value

        :type ignore: bool
        """
        self._ignore_value_case = ignore

    def set_uppercase_keywords(self, uppercase: bool):
        """
        If set to true the parser will uppercase all keywords
        Note: you have to set set_ignore_keywords_case to true

        :type uppercase: bool
        """
        self._uppercase_keywords = uppercase

    def set_uppercase_value(self, uppercase: bool):
        """
        If set to true the parser will uppercase all values
        Note: you have to set set_ignore_values_case to true

        :type uppercase: bool
        """
        self._uppercase_values = uppercase

    def set_indents(self, indents):
        """
        Sets the number of indents of a block

        :param indents: number of indents
        """
        self._indents = indents

    def append_current_line(self):
        """
           Appends and clears the current line

        """
        self._lines.append(self.get_indents_string + self._current_line)
        self._current_line = ""

    def get_key_value_pattern(self, ctx: ParserRuleContext):
        """
        returns the key/value pattern of the context
        It is assumed, that the context has 5 children, that represent the k/v:
        '0' left parenthesis
        '1' key
        '2' equals
        '3' value
        '4' right parenthesis
        :param ctx: the ParserRuleContext
        :return formatted key value string
        :rtype str
        """
        _count = ctx.getChildCount()
        # count==5 indicates Key/Value context
        if _count == 5:
            _key = str(ctx.getChild(1))
            if not self._ignore_keyword_case:
                if self._uppercase_keywords:
                    _key = _key.upper()
                else:
                    _key = _key.lower()

            _value = str(ctx.getChild(3))
            if not self._ignore_value_case:
                if self._uppercase_values:
                    _value = _value.upper()
                else:
                    _value = _value.lower()
            _ret_string = str(ctx.getChild(0)) + _key + str(ctx.getChild(2)) + _value + str(ctx.getChild(4))
            return _ret_string
        raise Exception("Not a key value ctx")

    def get_key_opening_pattern(self, ctx: ParserRuleContext):
        """
        returns the key opening pattern, like (address=
        :param ctx: the ParserRuleContext
        :return formatted key opening string
        :rtype str
        """
        _count = ctx.getChildCount()
        if _count < 5:
            raise Exception("Not a key opening ctx")
        _key = str(ctx.getChild(1))
        if not self._ignore_keyword_case:
            if self._uppercase_keywords:
                _key = _key.upper()
            else:
                _key = _key.lower()
        _ret_string = str(ctx.getChild(0)) + _key + str(ctx.getChild(2))
        return _ret_string

    def get_key_closing_pattern(self, ctx: ParserRuleContext):
        """
        returns the key closing pattern
        :param ctx: the ParserRuleContext
        :return formatted key closing string
        :rtype str
        """
        _count = ctx.getChildCount()
        if _count < 5:
            raise Exception("Not a key closing ctx")
        _key = str(ctx.getChild(_count - 1))
        if not self._ignore_keyword_case:
            if self._uppercase_keywords:
                _key = _key.upper()
            else:
                _key = _key.lower()
        _ret_string = _key
        return _ret_string

    def get_value_pattern(self, ctx: ParserRuleContext):
        """
        :param ctx: the ParserRuleContext
        :return formatted key closing string
        :rtype str
        """
        _count = ctx.getChildCount()
        if _count != 1:
            raise Exception("Not a value ctx")
        _key = str(ctx.getText())
        if not self._ignore_value_case:
            if self._uppercase_values:
                _key = _key.upper()
            else:
                _key = _key.lower()
        _ret_string = _key
        return _ret_string

    # Enter a parse tree produced by tnsnamesParser#description_list.
    def enterDescription_list(self, ctx: tnsnamesParser.Description_listContext):
        super().enterDescription_list(ctx)
        # self.append_current_line()
        line_string = self.get_indents_string + self.get_key_opening_pattern(ctx)
        self._level += 1
        self._lines.append(line_string)

    # Exit a parse tree produced by tnsnamesParser#description_list.
    def exitDescription_list(self, ctx: tnsnamesParser.Description_listContext):
        super().exitDescription_list(ctx)
        self._level -= 1
        line_string = self.get_indents_string + self.get_key_closing_pattern(ctx)
        self._lines.append(line_string)

    # Enter a parse tree produced by tnsnamesParser#description.
    def enterDescription(self, ctx: tnsnamesParser.DescriptionContext):
        super().enterDescription(ctx)
        line_string = self.get_indents_string + self.get_key_opening_pattern(ctx)
        self._level += 1
        self._lines.append(line_string)

    # Exit a parse tree produced by tnsnamesParser#description.
    def exitDescription(self, ctx: tnsnamesParser.DescriptionContext):
        super().exitDescription(ctx)
        self._level -= 1
        line_string = self.get_indents_string + self.get_key_closing_pattern(ctx)
        self._lines.append(line_string)

    # Enter a parse tree produced by tnsnamesParser#d_sdu.
    def enterD_sdu(self, ctx: tnsnamesParser.D_sduContext):
        super().enterD_sdu(ctx)
        self._current_line += self.get_key_value_pattern(ctx)
        self.append_current_line()

    # Enter a parse tree produced by tnsnamesParser#d_conn_timeout.
    def enterD_conn_timeout(self, ctx: tnsnamesParser.D_conn_timeoutContext):
        super().enterD_conn_timeout(ctx)
        self._current_line += self.get_key_value_pattern(ctx)
        self.append_current_line()

    # Exit a parse tree produced by tnsnamesParser#d_conn_timeout.
    def exitD_conn_timeout(self, ctx: tnsnamesParser.D_conn_timeoutContext):
        super().exitD_conn_timeout(ctx)

    # Enter a parse tree produced by tnsnamesParser#d_retry_count.
    def enterD_retry_count(self, ctx: tnsnamesParser.D_retry_countContext):
        super().enterD_retry_count(ctx)
        self._current_line += self.get_key_value_pattern(ctx)
        self.append_current_line()

    # Enter a parse tree produced by tnsnamesParser#address_list.
    def enterAddress_list(self, ctx: tnsnamesParser.Address_listContext):
        super().enterAddress_list(ctx)
        line_string = self.get_indents_string + self.get_key_opening_pattern(ctx)
        self._level += 1
        self._lines.append(line_string)

    # Exit a parse tree produced by tnsnamesParser#address_list.
    def exitAddress_list(self, ctx: tnsnamesParser.Address_listContext):
        super().exitAddress_list(ctx)
        self._level -= 1
        line_string = self.get_indents_string + self.get_key_closing_pattern(ctx)
        self._lines.append(line_string)

    # Enter a parse tree produced by tnsnamesParser#al_load_balance.
    def enterAl_load_balance(self, ctx: tnsnamesParser.Al_load_balanceContext):
        super().enterAl_load_balance(ctx)
        self._current_line += self.get_key_value_pattern(ctx)
        self.append_current_line()

    # Exit a parse tree produced by tnsnamesParser#al_load_balance.
    def exitAl_load_balance(self, ctx: tnsnamesParser.Al_load_balanceContext):
        super().exitAl_load_balance(ctx)

    # Enter a parse tree produced by tnsnamesParser#address.
    def enterAddress(self, ctx: tnsnamesParser.AddressContext):
        super().enterAddress(ctx)
        _res_string = self.get_key_opening_pattern(ctx)
        self._current_line += _res_string

    # Exit a parse tree produced by tnsnamesParser#address.
    def exitAddress(self, ctx: tnsnamesParser.AddressContext):
        super().exitAddress(ctx)
        self._current_line += self.get_key_closing_pattern(ctx)
        self.append_current_line()

    # Enter a parse tree produced by tnsnamesParser#tcp_host.
    def enterTcp_host(self, ctx: tnsnamesParser.Tcp_hostContext):
        super().enterTcp_host(ctx)
        self._current_line += self.get_key_opening_pattern(ctx)

    # Exit a parse tree produced by tnsnamesParser#tcp_host.
    def exitTcp_host(self, ctx: tnsnamesParser.Tcp_hostContext):
        super().exitTcp_host(ctx)
        self._current_line += self.get_key_closing_pattern(ctx)

    # Enter a parse tree produced by tnsnamesParser#tcp_protocol.
    def enterTcp_protocol(self, ctx: tnsnamesParser.Tcp_protocolContext):
        self._current_line += self.get_value_pattern(ctx)
        super().enterTcp_protocol(ctx)

    # Exit a parse tree produced by tnsnamesParser#tcp_protocol.
    def exitTcp_protocol(self, ctx: tnsnamesParser.Tcp_protocolContext):
        super().exitTcp_protocol(ctx)

    # Enter a parse tree produced by tnsnamesParser#host.
    def enterHost(self, ctx: tnsnamesParser.HostContext):
        super().enterHost(ctx)
        self._current_line += self.get_value_pattern(ctx)

    # Exit a parse tree produced by tnsnamesParser#host.
    def exitHost(self, ctx: tnsnamesParser.HostContext):
        super().exitHost(ctx)

    # Enter a parse tree produced by tnsnamesParser#tcp_port.
    def enterTcp_port(self, ctx: tnsnamesParser.Tcp_portContext):
        super().enterTcp_port(ctx)
        self._current_line += self.get_key_opening_pattern(ctx)

    # Exit a parse tree produced by tnsnamesParser#tcp_port.
    def exitTcp_port(self, ctx: tnsnamesParser.Tcp_portContext):
        super().exitTcp_port(ctx)
        self._current_line += self.get_key_closing_pattern(ctx)

    # Enter a parse tree produced by tnsnamesParser#port.
    def enterPort(self, ctx: tnsnamesParser.PortContext):
        super().enterPort(ctx)
        self._current_line += self.get_value_pattern(ctx)

    # Exit a parse tree produced by tnsnamesParser#port.
    def exitPort(self, ctx: tnsnamesParser.PortContext):
        super().exitPort(ctx)

    # Enter a parse tree produced by tnsnamesParser#cd_service_name.
    def enterCd_service_name(self, ctx: tnsnamesParser.Cd_service_nameContext):
        super().enterCd_service_name(ctx)
        self._current_line += self.get_key_value_pattern(ctx)
        self.append_current_line()

    # Exit a parse tree produced by tnsnamesParser#cd_service_name.
    def exitCd_service_name(self, ctx: tnsnamesParser.Cd_service_nameContext):
        super().exitCd_service_name(ctx)

    # Enter a parse tree produced by tnsnamesParser#cd_server.
    def enterCd_server(self, ctx: tnsnamesParser.Cd_serverContext):
        super().enterCd_server(ctx)
        self._current_line += self.get_key_value_pattern(ctx)
        self.append_current_line()

    # Exit a parse tree produced by tnsnamesParser#cd_server.
    def exitCd_server(self, ctx: tnsnamesParser.Cd_serverContext):
        super().exitCd_server(ctx)

    # Enter a parse tree produced by tnsnamesParser#connect_data.
    def enterConnect_data(self, ctx: tnsnamesParser.Connect_dataContext):
        super().enterConnect_data(ctx)
        line_string = self.get_indents_string + self.get_key_opening_pattern(ctx)
        self._level += 1
        self._lines.append(line_string)

    # Exit a parse tree produced by tnsnamesParser#connect_data.
    def exitConnect_data(self, ctx: tnsnamesParser.Connect_dataContext):
        super().exitConnect_data(ctx)
        self._level -= 1
        line_string = self.get_indents_string + self.get_key_closing_pattern(ctx)
        self._lines.append(line_string)

    def enterAlias_list(self, ctx: tnsnamesParser.Alias_listContext):
        super().enterAlias_list(ctx)
        self._lines.append(ctx.getText() + '=')
        self._level = 1

    def exitAlias_list(self, ctx: tnsnamesParser.Alias_listContext):
        super().exitAlias_list(ctx)

    # Enter a parse tree produced by tnsnamesParser#alias.
    def enterAlias(self, ctx: tnsnamesParser.AliasContext):
        super().enterAlias(ctx)
        # self._current_line += ctx.getText()
