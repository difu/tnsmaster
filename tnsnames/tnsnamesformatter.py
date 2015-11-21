from tnsnames.tnsnamesListener import TnsnamesListener
from tnsnames.tnsnamesParser import tnsnamesParser
from tnsnames.tnsnamesStack import TnsnamesStack


# Base class for all format classes
class TnsnamesFormatter(TnsnamesListener):
    def __init__(self):
        self._lines = []
        self._tnsStack = TnsnamesStack()
        self._enteredAlias = False
        self._enteredAddressList = False
        self._enteredDescriptionList = False
        self._enteredDescription = False

    @property
    def get_lines(self):
        return self._lines

    # Enter a parse tree produced by tnsnamesParser#tnsnames.
    def enterTnsnames(self, ctx: tnsnamesParser.TnsnamesContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_tnsnames])

    # Exit a parse tree produced by tnsnamesParser#tnsnames.
    def exitTnsnames(self, ctx: tnsnamesParser.TnsnamesContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_tnsnames] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#tns_entry.
    def enterTns_entry(self, ctx: tnsnamesParser.Tns_entryContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_tns_entry])

    # Exit a parse tree produced by tnsnamesParser#tns_entry.
    def exitTns_entry(self, ctx: tnsnamesParser.Tns_entryContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_tns_entry] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#ifile.
    def enterIfile(self, ctx: tnsnamesParser.IfileContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_ifile])

    # Exit a parse tree produced by tnsnamesParser#ifile.
    def exitIfile(self, ctx: tnsnamesParser.IfileContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_ifile] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#lsnr_entry.
    def enterLsnr_entry(self, ctx: tnsnamesParser.Lsnr_entryContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_lsnr_entry])

    # Exit a parse tree produced by tnsnamesParser#lsnr_entry.
    def exitLsnr_entry(self, ctx: tnsnamesParser.Lsnr_entryContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_lsnr_entry] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#lsnr_description.
    def enterLsnr_description(self, ctx: tnsnamesParser.Lsnr_descriptionContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_description])

    # Exit a parse tree produced by tnsnamesParser#lsnr_description.
    def exitLsnr_description(self, ctx: tnsnamesParser.Lsnr_descriptionContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_description] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#alias_list.
    def enterAlias_list(self, ctx: tnsnamesParser.Alias_listContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_alias_list])

    # Exit a parse tree produced by tnsnamesParser#alias_list.
    def exitAlias_list(self, ctx: tnsnamesParser.Alias_listContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_alias_list] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#alias.
    def enterAlias(self, ctx: tnsnamesParser.AliasContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_alias])
        self._enteredAlias = True

    # Exit a parse tree produced by tnsnamesParser#alias.
    def exitAlias(self, ctx: tnsnamesParser.AliasContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_alias] == self._tnsStack.pop
        self._enteredAlias = False

    # Enter a parse tree produced by tnsnamesParser#description_list.
    def enterDescription_list(self, ctx: tnsnamesParser.Description_listContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_description_list])
        self._enteredDescriptionList = True

    # Exit a parse tree produced by tnsnamesParser#description_list.
    def exitDescription_list(self, ctx: tnsnamesParser.Description_listContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_description_list] == self._tnsStack.pop
        self._enteredDescriptionList = False

    # Enter a parse tree produced by tnsnamesParser#dl_params.
    def enterDl_params(self, ctx: tnsnamesParser.Dl_paramsContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_dl_params])

    # Exit a parse tree produced by tnsnamesParser#dl_params.
    def exitDl_params(self, ctx: tnsnamesParser.Dl_paramsContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_dl_params] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#dl_parameter.
    def enterDl_parameter(self, ctx: tnsnamesParser.Dl_parameterContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_dl_parameter])

    # Exit a parse tree produced by tnsnamesParser#dl_parameter.
    def exitDl_parameter(self, ctx: tnsnamesParser.Dl_parameterContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_dl_parameter] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#description.
    def enterDescription(self, ctx: tnsnamesParser.DescriptionContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_description])
        self._enteredDescription = True

    # Exit a parse tree produced by tnsnamesParser#description.
    def exitDescription(self, ctx: tnsnamesParser.DescriptionContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_description] == self._tnsStack.pop
        self._enteredDescription = False

    # Enter a parse tree produced by tnsnamesParser#d_params.
    def enterD_params(self, ctx: tnsnamesParser.D_paramsContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_params])

    # Exit a parse tree produced by tnsnamesParser#d_params.
    def exitD_params(self, ctx: tnsnamesParser.D_paramsContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_params] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#d_parameter.
    def enterD_parameter(self, ctx: tnsnamesParser.D_parameterContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_parameter])

    # Exit a parse tree produced by tnsnamesParser#d_parameter.
    def exitD_parameter(self, ctx: tnsnamesParser.D_parameterContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_parameter] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#d_enable.
    def enterD_enable(self, ctx: tnsnamesParser.D_enableContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_enable])

    # Exit a parse tree produced by tnsnamesParser#d_enable.
    def exitD_enable(self, ctx: tnsnamesParser.D_enableContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_enable] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#d_sdu.
    def enterD_sdu(self, ctx: tnsnamesParser.D_sduContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_sdu])

    # Exit a parse tree produced by tnsnamesParser#d_sdu.
    def exitD_sdu(self, ctx: tnsnamesParser.D_sduContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_sdu] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#d_recv_buf.
    def enterD_recv_buf(self, ctx: tnsnamesParser.D_recv_bufContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_recv_buf])

    # Exit a parse tree produced by tnsnamesParser#d_recv_buf.
    def exitD_recv_buf(self, ctx: tnsnamesParser.D_recv_bufContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_recv_buf] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#d_send_buf.
    def enterD_send_buf(self, ctx: tnsnamesParser.D_send_bufContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_send_buf])

    # Exit a parse tree produced by tnsnamesParser#d_send_buf.
    def exitD_send_buf(self, ctx: tnsnamesParser.D_send_bufContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_send_buf] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#d_service_type.
    def enterD_service_type(self, ctx: tnsnamesParser.D_service_typeContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_service_type])

    # Exit a parse tree produced by tnsnamesParser#d_service_type.
    def exitD_service_type(self, ctx: tnsnamesParser.D_service_typeContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_service_type] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#d_security.
    def enterD_security(self, ctx: tnsnamesParser.D_securityContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_security])

    # Exit a parse tree produced by tnsnamesParser#d_security.
    def exitD_security(self, ctx: tnsnamesParser.D_securityContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_security] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#d_conn_timeout.
    def enterD_conn_timeout(self, ctx: tnsnamesParser.D_conn_timeoutContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_conn_timeout])

    # Exit a parse tree produced by tnsnamesParser#d_conn_timeout.
    def exitD_conn_timeout(self, ctx: tnsnamesParser.D_conn_timeoutContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_conn_timeout] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#d_retry_count.
    def enterD_retry_count(self, ctx: tnsnamesParser.D_retry_countContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_retry_count])

    # Exit a parse tree produced by tnsnamesParser#d_retry_count.
    def exitD_retry_count(self, ctx: tnsnamesParser.D_retry_countContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_retry_count] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#d_tct.
    def enterD_tct(self, ctx: tnsnamesParser.D_tctContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_tct])

    # Exit a parse tree produced by tnsnamesParser#d_tct.
    def exitD_tct(self, ctx: tnsnamesParser.D_tctContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_d_tct] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#ds_parameter.
    def enterDs_parameter(self, ctx: tnsnamesParser.Ds_parameterContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_ds_parameter])

    # Exit a parse tree produced by tnsnamesParser#ds_parameter.
    def exitDs_parameter(self, ctx: tnsnamesParser.Ds_parameterContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_ds_parameter] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#address_list.
    def enterAddress_list(self, ctx: tnsnamesParser.Address_listContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_address_list])
        self._enteredAddressList = True

    # Exit a parse tree produced by tnsnamesParser#address_list.
    def exitAddress_list(self, ctx: tnsnamesParser.Address_listContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_address_list] == self._tnsStack.pop
        self._enteredAddressList = False

    # Enter a parse tree produced by tnsnamesParser#al_params.
    def enterAl_params(self, ctx: tnsnamesParser.Al_paramsContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_al_params])

    # Exit a parse tree produced by tnsnamesParser#al_params.
    def exitAl_params(self, ctx: tnsnamesParser.Al_paramsContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_al_params] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#al_parameter.
    def enterAl_parameter(self, ctx: tnsnamesParser.Al_parameterContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_al_parameter])

    # Exit a parse tree produced by tnsnamesParser#al_parameter.
    def exitAl_parameter(self, ctx: tnsnamesParser.Al_parameterContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_al_parameter] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#al_failover.
    def enterAl_failover(self, ctx: tnsnamesParser.Al_failoverContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_al_failover])

    # Exit a parse tree produced by tnsnamesParser#al_failover.
    def exitAl_failover(self, ctx: tnsnamesParser.Al_failoverContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_al_failover] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#al_load_balance.
    def enterAl_load_balance(self, ctx: tnsnamesParser.Al_load_balanceContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_al_load_balance])

    # Exit a parse tree produced by tnsnamesParser#al_load_balance.
    def exitAl_load_balance(self, ctx: tnsnamesParser.Al_load_balanceContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_al_load_balance] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#al_source_route.
    def enterAl_source_route(self, ctx: tnsnamesParser.Al_source_routeContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_al_source_route])

    # Exit a parse tree produced by tnsnamesParser#al_source_route.
    def exitAl_source_route(self, ctx: tnsnamesParser.Al_source_routeContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_al_source_route] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#address.
    def enterAddress(self, ctx: tnsnamesParser.AddressContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_address])

    # Exit a parse tree produced by tnsnamesParser#address.
    def exitAddress(self, ctx: tnsnamesParser.AddressContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_address] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#a_params.
    def enterA_params(self, ctx: tnsnamesParser.A_paramsContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_a_params])

    # Exit a parse tree produced by tnsnamesParser#a_params.
    def exitA_params(self, ctx: tnsnamesParser.A_paramsContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_a_params] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#a_parameter.
    def enterA_parameter(self, ctx: tnsnamesParser.A_parameterContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_a_parameter])

    # Exit a parse tree produced by tnsnamesParser#a_parameter.
    def exitA_parameter(self, ctx: tnsnamesParser.A_parameterContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_a_parameter] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#protocol_info.
    def enterProtocol_info(self, ctx: tnsnamesParser.Protocol_infoContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_protocol_info])

    # Exit a parse tree produced by tnsnamesParser#protocol_info.
    def exitProtocol_info(self, ctx: tnsnamesParser.Protocol_infoContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_protocol_info] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#tcp_protocol.
    def enterTcp_protocol(self, ctx: tnsnamesParser.Tcp_protocolContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_tcp_protocol])

    # Exit a parse tree produced by tnsnamesParser#tcp_protocol.
    def exitTcp_protocol(self, ctx: tnsnamesParser.Tcp_protocolContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_tcp_protocol] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#tcp_params.
    def enterTcp_params(self, ctx: tnsnamesParser.Tcp_paramsContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_tcp_params])

    # Exit a parse tree produced by tnsnamesParser#tcp_params.
    def exitTcp_params(self, ctx: tnsnamesParser.Tcp_paramsContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_tcp_params] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#tcp_parameter.
    def enterTcp_parameter(self, ctx: tnsnamesParser.Tcp_parameterContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_tcp_parameter])

    # Exit a parse tree produced by tnsnamesParser#tcp_parameter.
    def exitTcp_parameter(self, ctx: tnsnamesParser.Tcp_parameterContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_tcp_parameter] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#tcp_host.
    def enterTcp_host(self, ctx: tnsnamesParser.Tcp_hostContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_tcp_host])

    # Exit a parse tree produced by tnsnamesParser#tcp_host.
    def exitTcp_host(self, ctx: tnsnamesParser.Tcp_hostContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_tcp_host] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#tcp_port.
    def enterTcp_port(self, ctx: tnsnamesParser.Tcp_portContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_tcp_port])

    # Exit a parse tree produced by tnsnamesParser#tcp_port.
    def exitTcp_port(self, ctx: tnsnamesParser.Tcp_portContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_tcp_port] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#tcp_tcp.
    def enterTcp_tcp(self, ctx: tnsnamesParser.Tcp_tcpContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_tcp_tcp])

    # Exit a parse tree produced by tnsnamesParser#tcp_tcp.
    def exitTcp_tcp(self, ctx: tnsnamesParser.Tcp_tcpContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_tcp_tcp] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#host.
    def enterHost(self, ctx: tnsnamesParser.HostContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_host])

    # Exit a parse tree produced by tnsnamesParser#host.
    def exitHost(self, ctx: tnsnamesParser.HostContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_host] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#port.
    def enterPort(self, ctx: tnsnamesParser.PortContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_port])

    # Exit a parse tree produced by tnsnamesParser#port.
    def exitPort(self, ctx: tnsnamesParser.PortContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_port] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#ipc_protocol.
    def enterIpc_protocol(self, ctx: tnsnamesParser.Ipc_protocolContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_ipc_protocol])

    # Exit a parse tree produced by tnsnamesParser#ipc_protocol.
    def exitIpc_protocol(self, ctx: tnsnamesParser.Ipc_protocolContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_ipc_protocol] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#ipc_params.
    def enterIpc_params(self, ctx: tnsnamesParser.Ipc_paramsContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_ipc_params])

    # Exit a parse tree produced by tnsnamesParser#ipc_params.
    def exitIpc_params(self, ctx: tnsnamesParser.Ipc_paramsContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_ipc_params] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#ipc_parameter.
    def enterIpc_parameter(self, ctx: tnsnamesParser.Ipc_parameterContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_ipc_parameter])

    # Exit a parse tree produced by tnsnamesParser#ipc_parameter.
    def exitIpc_parameter(self, ctx: tnsnamesParser.Ipc_parameterContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_ipc_parameter] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#ipc_ipc.
    def enterIpc_ipc(self, ctx: tnsnamesParser.Ipc_ipcContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_ipc_ipc])

    # Exit a parse tree produced by tnsnamesParser#ipc_ipc.
    def exitIpc_ipc(self, ctx: tnsnamesParser.Ipc_ipcContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_ipc_ipc] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#ipc_key.
    def enterIpc_key(self, ctx: tnsnamesParser.Ipc_keyContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_ipc_key])

    # Exit a parse tree produced by tnsnamesParser#ipc_key.
    def exitIpc_key(self, ctx: tnsnamesParser.Ipc_keyContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_ipc_key] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#spx_protocol.
    def enterSpx_protocol(self, ctx: tnsnamesParser.Spx_protocolContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_spx_protocol])

    # Exit a parse tree produced by tnsnamesParser#spx_protocol.
    def exitSpx_protocol(self, ctx: tnsnamesParser.Spx_protocolContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_spx_protocol] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#spx_params.
    def enterSpx_params(self, ctx: tnsnamesParser.Spx_paramsContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_spx_params])

    # Exit a parse tree produced by tnsnamesParser#spx_params.
    def exitSpx_params(self, ctx: tnsnamesParser.Spx_paramsContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_spx_params] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#spx_parameter.
    def enterSpx_parameter(self, ctx: tnsnamesParser.Spx_parameterContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_spx_parameter])

    # Exit a parse tree produced by tnsnamesParser#spx_parameter.
    def exitSpx_parameter(self, ctx: tnsnamesParser.Spx_parameterContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_spx_parameter] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#spx_spx.
    def enterSpx_spx(self, ctx: tnsnamesParser.Spx_spxContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_spx_spx])

    # Exit a parse tree produced by tnsnamesParser#spx_spx.
    def exitSpx_spx(self, ctx: tnsnamesParser.Spx_spxContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_spx_spx] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#spx_service.
    def enterSpx_service(self, ctx: tnsnamesParser.Spx_serviceContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_spx_service])

    # Exit a parse tree produced by tnsnamesParser#spx_service.
    def exitSpx_service(self, ctx: tnsnamesParser.Spx_serviceContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_spx_service] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#nmp_protocol.
    def enterNmp_protocol(self, ctx: tnsnamesParser.Nmp_protocolContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_nmp_protocol])

    # Exit a parse tree produced by tnsnamesParser#nmp_protocol.
    def exitNmp_protocol(self, ctx: tnsnamesParser.Nmp_protocolContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_nmp_protocol] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#nmp_params.
    def enterNmp_params(self, ctx: tnsnamesParser.Nmp_paramsContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_nmp_params])

    # Exit a parse tree produced by tnsnamesParser#nmp_params.
    def exitNmp_params(self, ctx: tnsnamesParser.Nmp_paramsContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_nmp_params] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#nmp_parameter.
    def enterNmp_parameter(self, ctx: tnsnamesParser.Nmp_parameterContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_nmp_parameter])

    # Exit a parse tree produced by tnsnamesParser#nmp_parameter.
    def exitNmp_parameter(self, ctx: tnsnamesParser.Nmp_parameterContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_nmp_parameter] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#nmp_nmp.
    def enterNmp_nmp(self, ctx: tnsnamesParser.Nmp_nmpContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_nmp_nmp])

    # Exit a parse tree produced by tnsnamesParser#nmp_nmp.
    def exitNmp_nmp(self, ctx: tnsnamesParser.Nmp_nmpContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_nmp_nmp] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#nmp_server.
    def enterNmp_server(self, ctx: tnsnamesParser.Nmp_serverContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_nmp_server])

    # Exit a parse tree produced by tnsnamesParser#nmp_server.
    def exitNmp_server(self, ctx: tnsnamesParser.Nmp_serverContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_nmp_server] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#nmp_pipe.
    def enterNmp_pipe(self, ctx: tnsnamesParser.Nmp_pipeContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_nmp_pipe])

    # Exit a parse tree produced by tnsnamesParser#nmp_pipe.
    def exitNmp_pipe(self, ctx: tnsnamesParser.Nmp_pipeContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_nmp_pipe] == self._tnsStack.pop


    # Enter a parse tree produced by tnsnamesParser#beq_protocol.
    def enterBeq_protocol(self, ctx: tnsnamesParser.Beq_protocolContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_beq_protocol])

    # Exit a parse tree produced by tnsnamesParser#beq_protocol.
    def exitBeq_protocol(self, ctx: tnsnamesParser.Beq_protocolContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_beq_protocol] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#beq_params.
    def enterBeq_params(self, ctx: tnsnamesParser.Beq_paramsContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_beq_params])

    # Exit a parse tree produced by tnsnamesParser#beq_params.
    def exitBeq_params(self, ctx: tnsnamesParser.Beq_paramsContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_beq_params] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#beq_parameter.
    def enterBeq_parameter(self, ctx: tnsnamesParser.Beq_parameterContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_beq_parameter])

    # Exit a parse tree produced by tnsnamesParser#beq_parameter.
    def exitBeq_parameter(self, ctx: tnsnamesParser.Beq_parameterContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_beq_parameter] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#beq_beq.
    def enterBeq_beq(self, ctx: tnsnamesParser.Beq_beqContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_beq_beq])

    # Exit a parse tree produced by tnsnamesParser#beq_beq.
    def exitBeq_beq(self, ctx: tnsnamesParser.Beq_beqContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_beq_beq] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#beq_program.
    def enterBeq_program(self, ctx: tnsnamesParser.Beq_programContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_beq_program])

    # Exit a parse tree produced by tnsnamesParser#beq_program.
    def exitBeq_program(self, ctx: tnsnamesParser.Beq_programContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_beq_program] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#beq_argv0.
    def enterBeq_argv0(self, ctx: tnsnamesParser.Beq_argv0Context):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_beq_argv0])

    # Exit a parse tree produced by tnsnamesParser#beq_argv0.
    def exitBeq_argv0(self, ctx: tnsnamesParser.Beq_argv0Context):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_beq_argv0] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#beq_args.
    def enterBeq_args(self, ctx: tnsnamesParser.Beq_argsContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_beq_args])

    # Exit a parse tree produced by tnsnamesParser#beq_args.
    def exitBeq_args(self, ctx: tnsnamesParser.Beq_argsContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_beq_args] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#ba_parameter.
    def enterBa_parameter(self, ctx: tnsnamesParser.Ba_parameterContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_ba_parameter])

    # Exit a parse tree produced by tnsnamesParser#ba_parameter.
    def exitBa_parameter(self, ctx: tnsnamesParser.Ba_parameterContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_ba_parameter] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#ba_description.
    def enterBa_description(self, ctx: tnsnamesParser.Ba_descriptionContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_ba_description])

    # Exit a parse tree produced by tnsnamesParser#ba_description.
    def exitBa_description(self, ctx: tnsnamesParser.Ba_descriptionContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_ba_description] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#bad_params.
    def enterBad_params(self, ctx: tnsnamesParser.Bad_paramsContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_bad_params])

    # Exit a parse tree produced by tnsnamesParser#bad_params.
    def exitBad_params(self, ctx: tnsnamesParser.Bad_paramsContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_bad_params] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#bad_parameter.
    def enterBad_parameter(self, ctx: tnsnamesParser.Bad_parameterContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_bad_parameter])

    # Exit a parse tree produced by tnsnamesParser#bad_parameter.
    def exitBad_parameter(self, ctx: tnsnamesParser.Bad_parameterContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_bad_parameter] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#bad_local.
    def enterBad_local(self, ctx: tnsnamesParser.Bad_localContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_bad_local])

    # Exit a parse tree produced by tnsnamesParser#bad_local.
    def exitBad_local(self, ctx: tnsnamesParser.Bad_localContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_bad_local] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#bad_address.
    def enterBad_address(self, ctx: tnsnamesParser.Bad_addressContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_bad_address])

    # Exit a parse tree produced by tnsnamesParser#bad_address.
    def exitBad_address(self, ctx: tnsnamesParser.Bad_addressContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_bad_address] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#connect_data.
    def enterConnect_data(self, ctx: tnsnamesParser.Connect_dataContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_connect_data])

    # Exit a parse tree produced by tnsnamesParser#connect_data.
    def exitConnect_data(self, ctx: tnsnamesParser.Connect_dataContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_connect_data] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#cd_params.
    def enterCd_params(self, ctx: tnsnamesParser.Cd_paramsContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_params])

    # Exit a parse tree produced by tnsnamesParser#cd_params.
    def exitCd_params(self, ctx: tnsnamesParser.Cd_paramsContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_params] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#cd_parameter.
    def enterCd_parameter(self, ctx: tnsnamesParser.Cd_parameterContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_parameter])

    # Exit a parse tree produced by tnsnamesParser#cd_parameter.
    def exitCd_parameter(self, ctx: tnsnamesParser.Cd_parameterContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_parameter] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#cd_service_name.
    def enterCd_service_name(self, ctx: tnsnamesParser.Cd_service_nameContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_service_name])

    # Exit a parse tree produced by tnsnamesParser#cd_service_name.
    def exitCd_service_name(self, ctx: tnsnamesParser.Cd_service_nameContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_service_name] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#cd_sid.
    def enterCd_sid(self, ctx: tnsnamesParser.Cd_sidContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_sid])

    # Exit a parse tree produced by tnsnamesParser#cd_sid.
    def exitCd_sid(self, ctx: tnsnamesParser.Cd_sidContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_sid] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#cd_instance_name.
    def enterCd_instance_name(self, ctx: tnsnamesParser.Cd_instance_nameContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_instance_name])

    # Exit a parse tree produced by tnsnamesParser#cd_instance_name.
    def exitCd_instance_name(self, ctx: tnsnamesParser.Cd_instance_nameContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_instance_name] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#cd_failover_mode.
    def enterCd_failover_mode(self, ctx: tnsnamesParser.Cd_failover_modeContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_failover_mode])

    # Exit a parse tree produced by tnsnamesParser#cd_failover_mode.
    def exitCd_failover_mode(self, ctx: tnsnamesParser.Cd_failover_modeContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_failover_mode] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#cd_global_name.
    def enterCd_global_name(self, ctx: tnsnamesParser.Cd_global_nameContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_global_name])

    # Exit a parse tree produced by tnsnamesParser#cd_global_name.
    def exitCd_global_name(self, ctx: tnsnamesParser.Cd_global_nameContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_global_name] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#cd_hs.
    def enterCd_hs(self, ctx: tnsnamesParser.Cd_hsContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_hs])

    # Exit a parse tree produced by tnsnamesParser#cd_hs.
    def exitCd_hs(self, ctx: tnsnamesParser.Cd_hsContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_hs] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#cd_rdb_database.
    def enterCd_rdb_database(self, ctx: tnsnamesParser.Cd_rdb_databaseContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_rdb_database])

    # Exit a parse tree produced by tnsnamesParser#cd_rdb_database.
    def exitCd_rdb_database(self, ctx: tnsnamesParser.Cd_rdb_databaseContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_rdb_database] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#cd_server.
    def enterCd_server(self, ctx: tnsnamesParser.Cd_serverContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_server])

    # Exit a parse tree produced by tnsnamesParser#cd_server.
    def exitCd_server(self, ctx: tnsnamesParser.Cd_serverContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_server] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#cd_ur.
    def enterCd_ur(self, ctx: tnsnamesParser.Cd_urContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_ur])

    # Exit a parse tree produced by tnsnamesParser#cd_ur.
    def exitCd_ur(self, ctx: tnsnamesParser.Cd_urContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_cd_ur] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#fo_params.
    def enterFo_params(self, ctx: tnsnamesParser.Fo_paramsContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_fo_params])

    # Exit a parse tree produced by tnsnamesParser#fo_params.
    def exitFo_params(self, ctx: tnsnamesParser.Fo_paramsContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_fo_params] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#fo_parameter.
    def enterFo_parameter(self, ctx: tnsnamesParser.Fo_parameterContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_fo_parameter])

    # Exit a parse tree produced by tnsnamesParser#fo_parameter.
    def exitFo_parameter(self, ctx: tnsnamesParser.Fo_parameterContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_fo_parameter] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#fo_type.
    def enterFo_type(self, ctx: tnsnamesParser.Fo_typeContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_fo_type])

    # Exit a parse tree produced by tnsnamesParser#fo_type.
    def exitFo_type(self, ctx: tnsnamesParser.Fo_typeContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_fo_type] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#fo_backup.
    def enterFo_backup(self, ctx: tnsnamesParser.Fo_backupContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_fo_backup])

    # Exit a parse tree produced by tnsnamesParser#fo_backup.
    def exitFo_backup(self, ctx: tnsnamesParser.Fo_backupContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_fo_backup] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#fo_method.
    def enterFo_method(self, ctx: tnsnamesParser.Fo_methodContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_fo_method])

    # Exit a parse tree produced by tnsnamesParser#fo_method.
    def exitFo_method(self, ctx: tnsnamesParser.Fo_methodContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_fo_method] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#fo_retries.
    def enterFo_retries(self, ctx: tnsnamesParser.Fo_retriesContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_fo_retries])

    # Exit a parse tree produced by tnsnamesParser#fo_retries.
    def exitFo_retries(self, ctx: tnsnamesParser.Fo_retriesContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_fo_retries] == self._tnsStack.pop

    # Enter a parse tree produced by tnsnamesParser#fo_delay.
    def enterFo_delay(self, ctx: tnsnamesParser.Fo_delayContext):
        self._tnsStack.push(tnsnamesParser.ruleNames[tnsnamesParser.RULE_fo_delay])

    # Exit a parse tree produced by tnsnamesParser#fo_delay.
    def exitFo_delay(self, ctx: tnsnamesParser.Fo_delayContext):
        assert tnsnamesParser.ruleNames[tnsnamesParser.RULE_fo_delay] == self._tnsStack.pop
