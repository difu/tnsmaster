from tnsnames.tnsnamesParser import tnsnamesParser
from tnsnames.tnsnamesformatter import TnsnamesFormatter


class TnsnameOraStyleFormatter(TnsnamesFormatter):
    def __init__(self):
        super().__init__()
        self._current_line = ""
        self._level = 0
        self._lines = []
        self._indents = 4

    def get_indents_string(self):
        ret_string = " " * self._indents * self._level
        return ret_string

    def set_indents(self, indents):
        self._indents = indents

    def append_current_line(self):
        """
           Appends and clears the current line

        """
        self._lines.append(self.get_indents_string() + self._current_line)
        self._current_line = ""

    @property
    def get_lines(self):
        return self._lines

    # Enter a parse tree produced by tnsnamesParser#tnsnames.
    def enterTnsnames(self, ctx: tnsnamesParser.TnsnamesContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#tnsnames.
    def exitTnsnames(self, ctx: tnsnamesParser.TnsnamesContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#tns_entry.
    def enterTns_entry(self, ctx: tnsnamesParser.Tns_entryContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#tns_entry.
    def exitTns_entry(self, ctx: tnsnamesParser.Tns_entryContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#ifile.
    def enterIfile(self, ctx: tnsnamesParser.IfileContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#ifile.
    def exitIfile(self, ctx: tnsnamesParser.IfileContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#lsnr_entry.
    def enterLsnr_entry(self, ctx: tnsnamesParser.Lsnr_entryContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#lsnr_entry.
    def exitLsnr_entry(self, ctx: tnsnamesParser.Lsnr_entryContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#lsnr_description.
    def enterLsnr_description(self, ctx: tnsnamesParser.Lsnr_descriptionContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#lsnr_description.
    def exitLsnr_description(self, ctx: tnsnamesParser.Lsnr_descriptionContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#alias_list.
    def enterAlias_list(self, ctx: tnsnamesParser.Alias_listContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#alias_list.
    def exitAlias_list(self, ctx: tnsnamesParser.Alias_listContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#alias.
    def enterAlias(self, ctx: tnsnamesParser.AliasContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#alias.
    def exitAlias(self, ctx: tnsnamesParser.AliasContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#description_list.
    def enterDescription_list(self, ctx: tnsnamesParser.Description_listContext):
        self.append_current_line()
        line_string = self.get_indents_string() + "(" + tnsnamesParser.ruleNames[
            tnsnamesParser.RULE_description_list] + "="
        self._level += 1
        self._lines.append(line_string)

    # Exit a parse tree produced by tnsnamesParser#description_list.
    def exitDescription_list(self, ctx: tnsnamesParser.Description_listContext):
        self._level -= 1
        line_string = self.get_indents_string() + ")"
        self._lines.append(line_string)

    # Enter a parse tree produced by tnsnamesParser#dl_params.
    def enterDl_params(self, ctx: tnsnamesParser.Dl_paramsContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#dl_params.
    def exitDl_params(self, ctx: tnsnamesParser.Dl_paramsContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#dl_parameter.
    def enterDl_parameter(self, ctx: tnsnamesParser.Dl_parameterContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#dl_parameter.
    def exitDl_parameter(self, ctx: tnsnamesParser.Dl_parameterContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#description.
    def enterDescription(self, ctx: tnsnamesParser.DescriptionContext):
        line_string = self.get_indents_string() + "(" + tnsnamesParser.ruleNames[
            tnsnamesParser.RULE_description] + "="
        self._level += 1
        self._lines.append(line_string)

    # Exit a parse tree produced by tnsnamesParser#description.
    def exitDescription(self, ctx: tnsnamesParser.DescriptionContext):
        self._level -= 1
        line_string = self.get_indents_string() + ")"
        self._lines.append(line_string)

    # Enter a parse tree produced by tnsnamesParser#d_params.
    def enterD_params(self, ctx: tnsnamesParser.D_paramsContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#d_params.
    def exitD_params(self, ctx: tnsnamesParser.D_paramsContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#d_parameter.
    def enterD_parameter(self, ctx: tnsnamesParser.D_parameterContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#d_parameter.
    def exitD_parameter(self, ctx: tnsnamesParser.D_parameterContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#d_enable.
    def enterD_enable(self, ctx: tnsnamesParser.D_enableContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#d_enable.
    def exitD_enable(self, ctx: tnsnamesParser.D_enableContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#d_sdu.
    def enterD_sdu(self, ctx: tnsnamesParser.D_sduContext):
        self._current_line = ctx.getText()
        self.append_current_line()

    # Exit a parse tree produced by tnsnamesParser#d_sdu.
    def exitD_sdu(self, ctx: tnsnamesParser.D_sduContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#d_recv_buf.
    def enterD_recv_buf(self, ctx: tnsnamesParser.D_recv_bufContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#d_recv_buf.
    def exitD_recv_buf(self, ctx: tnsnamesParser.D_recv_bufContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#d_send_buf.
    def enterD_send_buf(self, ctx: tnsnamesParser.D_send_bufContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#d_send_buf.
    def exitD_send_buf(self, ctx: tnsnamesParser.D_send_bufContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#d_service_type.
    def enterD_service_type(self, ctx: tnsnamesParser.D_service_typeContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#d_service_type.
    def exitD_service_type(self, ctx: tnsnamesParser.D_service_typeContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#d_security.
    def enterD_security(self, ctx: tnsnamesParser.D_securityContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#d_security.
    def exitD_security(self, ctx: tnsnamesParser.D_securityContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#d_conn_timeout.
    def enterD_conn_timeout(self, ctx: tnsnamesParser.D_conn_timeoutContext):
        self._current_line = ctx.getText()
        self.append_current_line()

    # Exit a parse tree produced by tnsnamesParser#d_conn_timeout.
    def exitD_conn_timeout(self, ctx: tnsnamesParser.D_conn_timeoutContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#d_retry_count.
    def enterD_retry_count(self, ctx: tnsnamesParser.D_retry_countContext):
        self._current_line = ctx.getText()
        self.append_current_line()

    # Exit a parse tree produced by tnsnamesParser#d_retry_count.
    def exitD_retry_count(self, ctx: tnsnamesParser.D_retry_countContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#d_tct.
    def enterD_tct(self, ctx: tnsnamesParser.D_tctContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#d_tct.
    def exitD_tct(self, ctx: tnsnamesParser.D_tctContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#ds_parameter.
    def enterDs_parameter(self, ctx: tnsnamesParser.Ds_parameterContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#ds_parameter.
    def exitDs_parameter(self, ctx: tnsnamesParser.Ds_parameterContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#address_list.
    def enterAddress_list(self, ctx: tnsnamesParser.Address_listContext):
        line_string = self.get_indents_string() + "(" + tnsnamesParser.ruleNames[
            tnsnamesParser.RULE_address_list] + "="
        self._level += 1
        self._lines.append(line_string)

    # Exit a parse tree produced by tnsnamesParser#address_list.
    def exitAddress_list(self, ctx: tnsnamesParser.Address_listContext):
        self._level -= 1
        line_string = self.get_indents_string() + ")"
        self._lines.append(line_string)

    # Enter a parse tree produced by tnsnamesParser#al_params.
    def enterAl_params(self, ctx: tnsnamesParser.Al_paramsContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#al_params.
    def exitAl_params(self, ctx: tnsnamesParser.Al_paramsContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#al_parameter.
    def enterAl_parameter(self, ctx: tnsnamesParser.Al_parameterContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#al_parameter.
    def exitAl_parameter(self, ctx: tnsnamesParser.Al_parameterContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#al_failover.
    def enterAl_failover(self, ctx: tnsnamesParser.Al_failoverContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#al_failover.
    def exitAl_failover(self, ctx: tnsnamesParser.Al_failoverContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#al_load_balance.
    def enterAl_load_balance(self, ctx: tnsnamesParser.Al_load_balanceContext):
        self._current_line = ctx.getText()
        self.append_current_line()

    # Exit a parse tree produced by tnsnamesParser#al_load_balance.
    def exitAl_load_balance(self, ctx: tnsnamesParser.Al_load_balanceContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#al_source_route.
    def enterAl_source_route(self, ctx: tnsnamesParser.Al_source_routeContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#al_source_route.
    def exitAl_source_route(self, ctx: tnsnamesParser.Al_source_routeContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#address.
    def enterAddress(self, ctx: tnsnamesParser.AddressContext):
        ret_string = self.get_indents_string() + ctx.getText()
        self._lines.append(ret_string)

    # Exit a parse tree produced by tnsnamesParser#address.
    def exitAddress(self, ctx: tnsnamesParser.AddressContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#a_params.
    def enterA_params(self, ctx: tnsnamesParser.A_paramsContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#a_params.
    def exitA_params(self, ctx: tnsnamesParser.A_paramsContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#a_parameter.
    def enterA_parameter(self, ctx: tnsnamesParser.A_parameterContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#a_parameter.
    def exitA_parameter(self, ctx: tnsnamesParser.A_parameterContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#protocol_info.
    def enterProtocol_info(self, ctx: tnsnamesParser.Protocol_infoContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#protocol_info.
    def exitProtocol_info(self, ctx: tnsnamesParser.Protocol_infoContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#tcp_protocol.
    def enterTcp_protocol(self, ctx: tnsnamesParser.Tcp_protocolContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#tcp_protocol.
    def exitTcp_protocol(self, ctx: tnsnamesParser.Tcp_protocolContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#tcp_params.
    def enterTcp_params(self, ctx: tnsnamesParser.Tcp_paramsContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#tcp_params.
    def exitTcp_params(self, ctx: tnsnamesParser.Tcp_paramsContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#tcp_parameter.
    def enterTcp_parameter(self, ctx: tnsnamesParser.Tcp_parameterContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#tcp_parameter.
    def exitTcp_parameter(self, ctx: tnsnamesParser.Tcp_parameterContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#tcp_host.
    def enterTcp_host(self, ctx: tnsnamesParser.Tcp_hostContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#tcp_host.
    def exitTcp_host(self, ctx: tnsnamesParser.Tcp_hostContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#tcp_port.
    def enterTcp_port(self, ctx: tnsnamesParser.Tcp_portContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#tcp_port.
    def exitTcp_port(self, ctx: tnsnamesParser.Tcp_portContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#tcp_tcp.
    def enterTcp_tcp(self, ctx: tnsnamesParser.Tcp_tcpContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#tcp_tcp.
    def exitTcp_tcp(self, ctx: tnsnamesParser.Tcp_tcpContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#host.
    def enterHost(self, ctx: tnsnamesParser.HostContext):
        # ret_string = self.get_indents_string() + ctx.getRuleContext().parentCtx.getText()
        # self._lines.append(ret_string)
        pass

    # Exit a parse tree produced by tnsnamesParser#host.
    def exitHost(self, ctx: tnsnamesParser.HostContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#port.
    def enterPort(self, ctx: tnsnamesParser.PortContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#port.
    def exitPort(self, ctx: tnsnamesParser.PortContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#ipc_protocol.
    def enterIpc_protocol(self, ctx: tnsnamesParser.Ipc_protocolContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#ipc_protocol.
    def exitIpc_protocol(self, ctx: tnsnamesParser.Ipc_protocolContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#ipc_params.
    def enterIpc_params(self, ctx: tnsnamesParser.Ipc_paramsContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#ipc_params.
    def exitIpc_params(self, ctx: tnsnamesParser.Ipc_paramsContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#ipc_parameter.
    def enterIpc_parameter(self, ctx: tnsnamesParser.Ipc_parameterContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#ipc_parameter.
    def exitIpc_parameter(self, ctx: tnsnamesParser.Ipc_parameterContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#ipc_ipc.
    def enterIpc_ipc(self, ctx: tnsnamesParser.Ipc_ipcContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#ipc_ipc.
    def exitIpc_ipc(self, ctx: tnsnamesParser.Ipc_ipcContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#ipc_key.
    def enterIpc_key(self, ctx: tnsnamesParser.Ipc_keyContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#ipc_key.
    def exitIpc_key(self, ctx: tnsnamesParser.Ipc_keyContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#spx_protocol.
    def enterSpx_protocol(self, ctx: tnsnamesParser.Spx_protocolContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#spx_protocol.
    def exitSpx_protocol(self, ctx: tnsnamesParser.Spx_protocolContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#spx_params.
    def enterSpx_params(self, ctx: tnsnamesParser.Spx_paramsContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#spx_params.
    def exitSpx_params(self, ctx: tnsnamesParser.Spx_paramsContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#spx_parameter.
    def enterSpx_parameter(self, ctx: tnsnamesParser.Spx_parameterContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#spx_parameter.
    def exitSpx_parameter(self, ctx: tnsnamesParser.Spx_parameterContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#spx_spx.
    def enterSpx_spx(self, ctx: tnsnamesParser.Spx_spxContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#spx_spx.
    def exitSpx_spx(self, ctx: tnsnamesParser.Spx_spxContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#spx_service.
    def enterSpx_service(self, ctx: tnsnamesParser.Spx_serviceContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#spx_service.
    def exitSpx_service(self, ctx: tnsnamesParser.Spx_serviceContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#nmp_protocol.
    def enterNmp_protocol(self, ctx: tnsnamesParser.Nmp_protocolContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#nmp_protocol.
    def exitNmp_protocol(self, ctx: tnsnamesParser.Nmp_protocolContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#nmp_params.
    def enterNmp_params(self, ctx: tnsnamesParser.Nmp_paramsContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#nmp_params.
    def exitNmp_params(self, ctx: tnsnamesParser.Nmp_paramsContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#nmp_parameter.
    def enterNmp_parameter(self, ctx: tnsnamesParser.Nmp_parameterContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#nmp_parameter.
    def exitNmp_parameter(self, ctx: tnsnamesParser.Nmp_parameterContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#nmp_nmp.
    def enterNmp_nmp(self, ctx: tnsnamesParser.Nmp_nmpContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#nmp_nmp.
    def exitNmp_nmp(self, ctx: tnsnamesParser.Nmp_nmpContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#nmp_server.
    def enterNmp_server(self, ctx: tnsnamesParser.Nmp_serverContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#nmp_server.
    def exitNmp_server(self, ctx: tnsnamesParser.Nmp_serverContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#nmp_pipe.
    def enterNmp_pipe(self, ctx: tnsnamesParser.Nmp_pipeContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#nmp_pipe.
    def exitNmp_pipe(self, ctx: tnsnamesParser.Nmp_pipeContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#beq_protocol.
    def enterBeq_protocol(self, ctx: tnsnamesParser.Beq_protocolContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#beq_protocol.
    def exitBeq_protocol(self, ctx: tnsnamesParser.Beq_protocolContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#beq_params.
    def enterBeq_params(self, ctx: tnsnamesParser.Beq_paramsContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#beq_params.
    def exitBeq_params(self, ctx: tnsnamesParser.Beq_paramsContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#beq_parameter.
    def enterBeq_parameter(self, ctx: tnsnamesParser.Beq_parameterContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#beq_parameter.
    def exitBeq_parameter(self, ctx: tnsnamesParser.Beq_parameterContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#beq_beq.
    def enterBeq_beq(self, ctx: tnsnamesParser.Beq_beqContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#beq_beq.
    def exitBeq_beq(self, ctx: tnsnamesParser.Beq_beqContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#beq_program.
    def enterBeq_program(self, ctx: tnsnamesParser.Beq_programContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#beq_program.
    def exitBeq_program(self, ctx: tnsnamesParser.Beq_programContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#beq_argv0.
    def enterBeq_argv0(self, ctx: tnsnamesParser.Beq_argv0Context):
        pass

    # Exit a parse tree produced by tnsnamesParser#beq_argv0.
    def exitBeq_argv0(self, ctx: tnsnamesParser.Beq_argv0Context):
        pass

    # Enter a parse tree produced by tnsnamesParser#beq_args.
    def enterBeq_args(self, ctx: tnsnamesParser.Beq_argsContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#beq_args.
    def exitBeq_args(self, ctx: tnsnamesParser.Beq_argsContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#ba_parameter.
    def enterBa_parameter(self, ctx: tnsnamesParser.Ba_parameterContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#ba_parameter.
    def exitBa_parameter(self, ctx: tnsnamesParser.Ba_parameterContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#ba_description.
    def enterBa_description(self, ctx: tnsnamesParser.Ba_descriptionContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#ba_description.
    def exitBa_description(self, ctx: tnsnamesParser.Ba_descriptionContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#bad_params.
    def enterBad_params(self, ctx: tnsnamesParser.Bad_paramsContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#bad_params.
    def exitBad_params(self, ctx: tnsnamesParser.Bad_paramsContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#bad_parameter.
    def enterBad_parameter(self, ctx: tnsnamesParser.Bad_parameterContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#bad_parameter.
    def exitBad_parameter(self, ctx: tnsnamesParser.Bad_parameterContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#bad_local.
    def enterBad_local(self, ctx: tnsnamesParser.Bad_localContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#bad_local.
    def exitBad_local(self, ctx: tnsnamesParser.Bad_localContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#bad_address.
    def enterBad_address(self, ctx: tnsnamesParser.Bad_addressContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#bad_address.
    def exitBad_address(self, ctx: tnsnamesParser.Bad_addressContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#connect_data.
    def enterConnect_data(self, ctx: tnsnamesParser.Connect_dataContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#connect_data.
    def exitConnect_data(self, ctx: tnsnamesParser.Connect_dataContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#cd_params.
    def enterCd_params(self, ctx: tnsnamesParser.Cd_paramsContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#cd_params.
    def exitCd_params(self, ctx: tnsnamesParser.Cd_paramsContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#cd_parameter.
    def enterCd_parameter(self, ctx: tnsnamesParser.Cd_parameterContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#cd_parameter.
    def exitCd_parameter(self, ctx: tnsnamesParser.Cd_parameterContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#cd_service_name.
    def enterCd_service_name(self, ctx: tnsnamesParser.Cd_service_nameContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#cd_service_name.
    def exitCd_service_name(self, ctx: tnsnamesParser.Cd_service_nameContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#cd_sid.
    def enterCd_sid(self, ctx: tnsnamesParser.Cd_sidContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#cd_sid.
    def exitCd_sid(self, ctx: tnsnamesParser.Cd_sidContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#cd_instance_name.
    def enterCd_instance_name(self, ctx: tnsnamesParser.Cd_instance_nameContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#cd_instance_name.
    def exitCd_instance_name(self, ctx: tnsnamesParser.Cd_instance_nameContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#cd_failover_mode.
    def enterCd_failover_mode(self, ctx: tnsnamesParser.Cd_failover_modeContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#cd_failover_mode.
    def exitCd_failover_mode(self, ctx: tnsnamesParser.Cd_failover_modeContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#cd_global_name.
    def enterCd_global_name(self, ctx: tnsnamesParser.Cd_global_nameContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#cd_global_name.
    def exitCd_global_name(self, ctx: tnsnamesParser.Cd_global_nameContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#cd_hs.
    def enterCd_hs(self, ctx: tnsnamesParser.Cd_hsContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#cd_hs.
    def exitCd_hs(self, ctx: tnsnamesParser.Cd_hsContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#cd_rdb_database.
    def enterCd_rdb_database(self, ctx: tnsnamesParser.Cd_rdb_databaseContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#cd_rdb_database.
    def exitCd_rdb_database(self, ctx: tnsnamesParser.Cd_rdb_databaseContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#cd_server.
    def enterCd_server(self, ctx: tnsnamesParser.Cd_serverContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#cd_server.
    def exitCd_server(self, ctx: tnsnamesParser.Cd_serverContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#cd_ur.
    def enterCd_ur(self, ctx: tnsnamesParser.Cd_urContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#cd_ur.
    def exitCd_ur(self, ctx: tnsnamesParser.Cd_urContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#fo_params.
    def enterFo_params(self, ctx: tnsnamesParser.Fo_paramsContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#fo_params.
    def exitFo_params(self, ctx: tnsnamesParser.Fo_paramsContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#fo_parameter.
    def enterFo_parameter(self, ctx: tnsnamesParser.Fo_parameterContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#fo_parameter.
    def exitFo_parameter(self, ctx: tnsnamesParser.Fo_parameterContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#fo_type.
    def enterFo_type(self, ctx: tnsnamesParser.Fo_typeContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#fo_type.
    def exitFo_type(self, ctx: tnsnamesParser.Fo_typeContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#fo_backup.
    def enterFo_backup(self, ctx: tnsnamesParser.Fo_backupContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#fo_backup.
    def exitFo_backup(self, ctx: tnsnamesParser.Fo_backupContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#fo_method.
    def enterFo_method(self, ctx: tnsnamesParser.Fo_methodContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#fo_method.
    def exitFo_method(self, ctx: tnsnamesParser.Fo_methodContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#fo_retries.
    def enterFo_retries(self, ctx: tnsnamesParser.Fo_retriesContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#fo_retries.
    def exitFo_retries(self, ctx: tnsnamesParser.Fo_retriesContext):
        pass

    # Enter a parse tree produced by tnsnamesParser#fo_delay.
    def enterFo_delay(self, ctx: tnsnamesParser.Fo_delayContext):
        pass

    # Exit a parse tree produced by tnsnamesParser#fo_delay.
    def exitFo_delay(self, ctx: tnsnamesParser.Fo_delayContext):
        pass
