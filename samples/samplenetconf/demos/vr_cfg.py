#!/usr/bin/python

# Copyright (c) 2015,  BROCADE COMMUNICATIONS SYSTEMS, INC

# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from this
# software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.

"""

@authors: Gary Greenberg
@status: Development
@version: 1.0


"""

import logging
import argparse
import sys


from pysdn.controller.controller import Controller
from pysdn.netconfdev.vrouter.vrouter5600 import VRouter5600
from pysdn.common.status import STATUS
from pysdn.common.utils import load_dict_from_file
from pysdn.netconfdev.vrouter.interfaces import DataPlaneInterface
from pysdn.netconfdev.vrouter.protocols import Ospf


def read_in_vr_cfg_file():
    f = "vr_cfg.yml"
    d = {}
    if load_dict_from_file(f, d) is False:
        print("Config file '%s' read error: " % f)
        exit()

    try:
        ctrlIpAddr = d['ctrlIpAddr']
        ctrlPortNum = d['ctrlPortNum']
        ctrlUname = d['ctrlUname']
        ctrlPswd = d['ctrlPswd']

        nodeName_1 = d['nodeName_1']
        nodeIpAddr_1 = d['nodeIpAddr_1']
        nodePortNum_1 = d['nodePortNum_1']
        nodeUname_1 = d['nodeUname_1']
        nodePswd_1 = d['nodePswd_1']

        nodeName_2 = d['nodeName_2']
        nodeIpAddr_2 = d['nodeIpAddr_2']
        nodePortNum_2 = d['nodePortNum_2']
        nodeUname_2 = d['nodeUname_2']
        nodePswd_2 = d['nodePswd_2']

        nodeName_3 = d['nodeName_3']
        nodeIpAddr_3 = d['nodeIpAddr_3']
        nodePortNum_3 = d['nodePortNum_3']
        nodeUname_3 = d['nodeUname_3']
        nodePswd_3 = d['nodePswd_3']

    except:
        logging.info ("Failed to get Controller and Node device attributes from Configuration file %s" % f)
        exit(0)

    return d

def set_bgp_cfg_1(ctrl, vr_cfg_params):
    templateUrl = ("http://{}:{}/restconf/config/"
                    "opendaylight-inventory:nodes/node/{}/"
                   "yang-ext:mount/"
                   "vyatta-protocols:protocols/vyatta-protocols-ospf:ospf")
    url = templateUrl.format(vr_cfg_params['ctrlIpAddr'], vr_cfg_params['ctrlPortNum'], vr_cfg_params['nodeName_1'])

    var = ''
    {
        "vyatta-protocols-bgp:bgp": [
            {
                "tagnode": {},
                "neighbor": [
                    {
                        "tagnode": "{}",
                        "remote-as": {},
                        "address-family": {
                            "{}": {}
                        },
                        "update-source": "{}"
                    }
                ],
                "parameters": {
                    "router-id": "{}"
                }
            }
        ]
  }

    payload = var.format(vr_cfg_params['bgpGroup_1'],
                         vr_cfg_params['bgpNbr1_1'],
                         vr_cfg_params['bgpRemoteAS_1'],
                         vr_cfg_params['bgpNbrAddrFam1_1'],
                         vr_cfg_params['bgpUpdateSrc_1'],
                         vr_cfg_params['bgpParamsRtrId1_1'])
    headers = {"content-type": "application/json", "accept": "application/json"}

    logging.info(url)
    logging.info(payload)

    resp = ctrl.http_put_request(url, payload, headers)

    logging.info(resp)



def set_loopback_interface_1(ctrl, vr_cfg_params):
    templateUrl = ("http://{}:{}/restconf/config/"
                    "opendaylight-inventory:nodes/node/{}/"
                   "yang-ext:mount/"
                   "vyatta-interfaces:interfaces/vyatta-interfaces-loopback:loopback/{}")
    url = templateUrl.format(vr_cfg_params['ctrlIpAddr'], vr_cfg_params['ctrlPortNum'], vr_cfg_params['nodeName_1'], vr_cfg_params['lpbkName_1'])

#    voo = '{{\"vyatta-interfaces-loopback:loopback\": [{{\"tagnode\": \"{}\",\"address\": [\"{}\"]}}]}}'

    var = '{{\"vyatta-interfaces-loopback:loopback\": [{{\"tagnode\": \"{}\",\"address\": [\"{}\"]}}]}}'
    payload = var.format(vr_cfg_params['lpbkName_1'], vr_cfg_params['lpbkAddr_1'])
    headers = {"content-type": "application/json", "accept": "application/json"}

    logging.info(url)
    logging.info(payload)

    resp = ctrl.http_put_request(url, payload, headers)

    logging.info(resp)

def set_loopback_interface_2(ctrl, vr_cfg_params):
    templateUrl = ("http://{}:{}/restconf/config/"
                    "opendaylight-inventory:nodes/node/{}/"
                   "yang-ext:mount/"
                   "vyatta-interfaces:interfaces/vyatta-interfaces-loopback:loopback/{}")
    url = templateUrl.format(vr_cfg_params['ctrlIpAddr'], vr_cfg_params['ctrlPortNum'], vr_cfg_params['nodeName_2'], vr_cfg_params['lpbkName_2'])

    var = '{{\"vyatta-interfaces-loopback:loopback\": [{{\"tagnode\": \"{}\",\"address\": [\"{}\"]}}]}}'
    payload = var.format(vr_cfg_params['lpbkName_2'], vr_cfg_params['lpbkAddr_2'])
    headers = {"content-type": "application/json", "accept": "application/json"}

    logging.info(url)
    logging.info(payload)

    resp = ctrl.http_put_request(url, payload, headers)

    logging.info(resp)

def set_loopback_interface_3(ctrl, vr_cfg_params):
    templateUrl = ("http://{}:{}/restconf/config/"
                    "opendaylight-inventory:nodes/node/{}/"
                   "yang-ext:mount/"
                   "vyatta-interfaces:interfaces/vyatta-interfaces-loopback:loopback/{}")
    url = templateUrl.format(vr_cfg_params['ctrlIpAddr'], vr_cfg_params['ctrlPortNum'], vr_cfg_params['nodeName_3'], vr_cfg_params['lpbkName_3'])

    var = '{{\"vyatta-interfaces-loopback:loopback\": [{{\"tagnode\": \"{}\",\"address\": [\"{}\"]}}]}}'
    payload = var.format(vr_cfg_params['lpbkName_3'], vr_cfg_params['lpbkAddr_3'])
    headers = {"content-type": "application/json", "accept": "application/json"}

    logging.info(url)
    logging.info(payload)

    resp = ctrl.http_put_request(url, payload, headers)

    logging.info(resp)


def set_ospf_cfg_1(ctrl, vr_cfg_params):
    templateUrl = ("http://{}:{}/restconf/config/"
                    "opendaylight-inventory:nodes/node/{}/"
                   "yang-ext:mount/"
                   "vyatta-protocols:protocols/vyatta-protocols-ospf:ospf")
    url = templateUrl.format(vr_cfg_params['ctrlIpAddr'], vr_cfg_params['ctrlPortNum'], vr_cfg_params['nodeName_1'])
    var = '{{\"vyatta-protocols-ospf:ospf\": {{\"passive-interface\": [\"{}"],\"area\": [{{\"tagnode\": \"{}\",\"network\": [\"{}\"]}},{{\"tagnode\": \"{}\",\"network\": [\"{}\",\"{}\",\"{}\"]}}],\"parameters\": {{\"router-id\": \"{}\"}}}}}}'
    payload = var.format(vr_cfg_params['ospfPsvIf_1'],
                         vr_cfg_params['ospfArea4_1'],
                         vr_cfg_params['ospfNetwork4_1'],
                         vr_cfg_params['ospfArea3_1'],
                         vr_cfg_params['ospfNetwork3_1'],
                         vr_cfg_params['ospfNetwork2_1'],
                         vr_cfg_params['ospfNetwork1_1'],
                         vr_cfg_params['ospfParamRouterId_1'])
    headers = {"content-type": "application/json", "accept": "application/json"}

    logging.info(url)
    logging.info(payload)

    resp = ctrl.http_put_request(url, payload, headers)

    logging.info(resp)

def set_ospf_cfg_2(ctrl, vr_cfg_params):
    templateUrl = ("http://{}:{}/restconf/config/"
                    "opendaylight-inventory:nodes/node/{}/"
                   "yang-ext:mount/"
                   "vyatta-protocols:protocols/vyatta-protocols-ospf:ospf")
    url = templateUrl.format(vr_cfg_params['ctrlIpAddr'], vr_cfg_params['ctrlPortNum'], vr_cfg_params['nodeName_2'])

    var = '{{\"vyatta-protocols-ospf:ospf\": {{\"passive-interface\": [\"{}\"],\"area\": [{{\"tagnode\": \"{}\",\"network\": [\"{}\"]}},{{\"tagnode\": \"{}\",\"network\": [\"{}\",\"{}\"]}}],\"parameters\": {{\"router-id\": \"10.0.0.12\"}}}}}}'
    payload = var.format(vr_cfg_params['ospfPsvIf_2'],
                         vr_cfg_params['ospfArea3_2'],
                         vr_cfg_params['ospfNetwork3_2'],
                         vr_cfg_params['ospfArea1_2'],
                         vr_cfg_params['ospfNetwork2_2'],
                         vr_cfg_params['ospfNetwork1_2'],
                         vr_cfg_params['ospfNetwork2_2'],
                         vr_cfg_params['ospfParamRouterId_2'])
    headers = {"content-type": "application/json", "accept": "application/json"}

    logging.info(url)
    logging.info(payload)

    resp = ctrl.http_put_request(url, payload, headers)

    logging.info(resp)

def set_ospf_cfg_3(ctrl, vr_cfg_params):
    templateUrl = ("http://{}:{}/restconf/config/"
                    "opendaylight-inventory:nodes/node/{}/"
                   "yang-ext:mount/"
                   "vyatta-protocols:protocols/vyatta-protocols-ospf:ospf")
    url = templateUrl.format(vr_cfg_params['ctrlIpAddr'], vr_cfg_params['ctrlPortNum'], vr_cfg_params['nodeName_3'])

    var = '{{\"vyatta-protocols-ospf:ospf\": {{\"area\": [{{\"tagnode\": \"{1}\",\"network\": [\"{2}\",\"{3}\"]}}],\"parameters\": {{\"router-id\": "{4}"}}}}'
    payload = var.format(vr_cfg_params['ospfArea1_3'],
                         vr_cfg_params['ospfNetwork1_3'],
                         vr_cfg_params['ospfNetwork2_3'],
                         vr_cfg_params['ospfParamRouterId_3'])
    headers = {"content-type": "application/json", "accept": "application/json"}

    logging.info(url)
    logging.info(payload)

    resp = ctrl.http_put_request(url, payload, headers)

    logging.info(resp)

def do_vr_cfg_1(vr_cfg_params):
    logging.info("in do_vr_cfg_1 for %s", vr_cfg_params['nodeName_1'])

    ctrl = Controller(vr_cfg_params['ctrlIpAddr'], vr_cfg_params['ctrlPortNum'],
                      vr_cfg_params['ctrlUname'], vr_cfg_params['ctrlPswd'])

    vrouter = VRouter5600(ctrl, vr_cfg_params['nodeName_1'], vr_cfg_params['nodeIpAddr_1'],
                          vr_cfg_params['nodePortNum_1'], vr_cfg_params['nodeUname_1'], vr_cfg_params['nodePswd_1'])

    node_configured = False
    result = ctrl.check_node_config_status(vr_cfg_params['nodeName_1'])
    status = result.get_status()
    if status.eq(STATUS.NODE_CONFIGURED):
        node_configured = True
        print ("<<< '%s' is configured on the Controller" % vr_cfg_params['nodeName_1'])
    elif status.eq(STATUS.DATA_NOT_FOUND):
        node_configured = False
    else:
        logging.info ("\n")
        logging.info ("Failed to get configuration status for the '%s'" % vr_cfg_params['nodeName_1'])
        logging.info ("!!!Demo terminated, reason: %s" % status.detailed())
        exit(0)

    if node_configured is False:
        result = ctrl.add_netconf_node(vrouter)
        status = result.get_status()
        if status.eq(STATUS.OK):
            logging.info ("<<< '%s' added to the Controller" % vr_cfg_params['nodeName_1'])
        else:
            logging.info ("\n")
            logging.info ("!!!Demo terminated, reason: %s" % status.detailed())
            exit(0)

    result = ctrl.check_node_conn_status(vr_cfg_params['nodeName_1'])
    status = result.get_status()
    if status.eq(STATUS.NODE_CONNECTED):
        logging.info ("<<< '%s' is connected to the Controller" % vr_cfg_params['nodeName_1'])
    else:
        logging.info ("\n")
        logging.info ("!!!Demo terminated, reason: %s" % status.brief().lower())
        exit(0)

    set_loopback_interface_1(ctrl, vr_cfg_params)

    dp1_1 = DataPlaneInterface(vr_cfg_params['dp1Name_1'])
    dp1_1.set_address(vr_cfg_params['dp1Addr_1'])
    vrouter.set_dataplane_interface_cfg(dp1_1)

    dp2_1 = DataPlaneInterface(vr_cfg_params['dp1Name_2'])
    dp2_1.set_address(vr_cfg_params['dp1Addr_2'])
    vrouter.set_dataplane_interface_cfg(dp2_1)

    dp3_1 = DataPlaneInterface(vr_cfg_params['dp1Name_3'])
    dp3_1.set_address(vr_cfg_params['dp1Addr_3'])
    vrouter.set_dataplane_interface_cfg(dp3_1)

    set_ospf_cfg_1(ctrl, vr_cfg_params)
    set_bgp_cfg_1(ctrl, vr_cfg_params)

    sys.exit(0)

def do_vr_cfg_2(vr_cfg_params):
    logging.info("in do_vr_cfg_2 for %s", vr_cfg_params['nodeName_2'])

    ctrl = Controller(vr_cfg_params['ctrlIpAddr'], vr_cfg_params['ctrlPortNum'],
                      vr_cfg_params['ctrlUname'], vr_cfg_params['ctrlPswd'])

    vrouter = VRouter5600(ctrl, vr_cfg_params['nodeName_2'], vr_cfg_params['nodeIpAddr_2'],
                          vr_cfg_params['nodePortNum_2'], vr_cfg_params['nodeUname_2'], vr_cfg_params['nodePswd_2'])

    node_configured = False
    result = ctrl.check_node_config_status(vr_cfg_params['nodeName_2'])
    status = result.get_status()
    if status.eq(STATUS.NODE_CONFIGURED):
        node_configured = True
        logging.info ("<<< '%s' is configured on the Controller" % vr_cfg_params['nodeName_2'])
    elif status.eq(STATUS.DATA_NOT_FOUND):
        node_configured = False
    else:
        logging.info ("\n")
        logging.info ("Failed to get configuration status for the '%s'" % vr_cfg_params['nodeName_2'])
        logging.info ("!!!Demo terminated, reason: %s" % status.detailed())
        exit(0)

    if node_configured is False:
        result = ctrl.add_netconf_node(vrouter)
        status = result.get_status()
        if status.eq(STATUS.OK):
            logging.info ("<<< '%s' added to the Controller" % vr_cfg_params['nodeName_2'])
        else:
            logging.info ("\n")
            logging.info ("!!!Demo terminated, reason: %s" % status.detailed())
            exit(0)

    result = ctrl.check_node_conn_status(vr_cfg_params['nodeName_2'])
    status = result.get_status()
    if status.eq(STATUS.NODE_CONNECTED):
        logging.info ("<<< '%s' is connected to the Controller" % vr_cfg_params['nodeName_2'])
    else:
        logging.info ("\n")
        logging.info ("!!!Demo terminated, reason: %s" % status.brief().lower())
        exit(0)

    set_loopback_interface_2(ctrl, vr_cfg_params)

    dp1_2 = DataPlaneInterface(vr_cfg_params['dp1Name_2'])
    dp1_2.set_address(vr_cfg_params['dp1Addr_2'])
    vrouter.set_dataplane_interface_cfg(dp1_2)

    dp2_2 = DataPlaneInterface(vr_cfg_params['dp2Name_2'])
    dp2_2.set_address(vr_cfg_params['dp2Addr_2'])
    vrouter.set_dataplane_interface_cfg(dp2_2)

    set_ospf_cfg_2(ctrl, vr_cfg_params)

    sys.exit(0)

def do_vr_cfg_3(vr_cfg_params):
    logging.info("in do_vr_cfg_3 for %s", vr_cfg_params['nodeName_3'])

    ctrl = Controller(vr_cfg_params['ctrlIpAddr'], vr_cfg_params['ctrlPortNum'],
                      vr_cfg_params['ctrlUname'], vr_cfg_params['ctrlPswd'])
    vrouter = VRouter5600(ctrl, vr_cfg_params['nodeName_3'], vr_cfg_params['nodeIpAddr_3'],
                          vr_cfg_params['nodePortNum_3'], vr_cfg_params['nodeUname_3'], vr_cfg_params['nodePswd_3'])

    logging.info ("<<< 'Controller': %s, '%s': %s"
           % (vr_cfg_params['ctrlIpAddr'], vr_cfg_params['nodeName_3'], vr_cfg_params['nodeIpAddr_3']))

    #  set interfaces loopback lo address 10.0.0.22/32
    #  set interfaces dataplane dp0s3 address 192.168.21.2/24
    #  set interfaces dataplane dp0s6 address 10.252.30.206/30

    set_loopback_interface_3(ctrl, vr_cfg_params)

    dp1_3 = DataPlaneInterface(vr_cfg_params['dp1Name_3'])
    dp1_3.set_address(vr_cfg_params['dp1Addr_3'])
    vrouter.set_dataplane_interface_cfg(dp1_3)

    dp2_3 = DataPlaneInterface(vr_cfg_params['dp2Name_3'])
    dp2_3.set_address(vr_cfg_params['dp2Addr_3'])
    vrouter.set_dataplane_interface_cfg(dp2_3)

    set_ospf_cfg_3(ctrl, vr_cfg_params)

    sys.exit(0)

if __name__ == "__main__":
    vr_params = {}

    # Command line parser
    parser = argparse.ArgumentParser(description="BSC VR5600 Router Provisioning.")

    parser.add_argument("--log", default=None, type=str, help='specify the log message level [INFO | DEBUG]')
    parser.add_argument("--vr", type=str, help='specify the vrouter node cfg num')

    args = parser.parse_args()

    logging.basicConfig(level=args.log)

    doo = read_in_vr_cfg_file()

    args.vr = doo['nodeName_2']

    if args.vr == doo['nodeName_1']:
        do_vr_cfg_1(doo)
        sys.exit(0)

    elif args.vr == doo['nodeName_2']:
        do_vr_cfg_2(doo)
        sys.exit(0)

    elif args.vr == doo['nodeName_3']:
        do_vr_cfg_3(doo)
        sys.exit(0)

    else:
        parser.print_help()
        sys.exit(0)