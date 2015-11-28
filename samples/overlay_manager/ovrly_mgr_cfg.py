#!/usr/bin/python

import logging

from pysdn.common.utils import load_dict_from_file
from pysdn.netconfdev.ovs.overlay_mgr import Ovrly_mgr


def read_in_ovrly_cfg():
    f = "ovrly_mgr_cfg.yml"
    d = {}
    if load_dict_from_file(f, d) is False:
        print("Config file '%s' read error: " % f)
        exit()

    try:
        ctrlIpAddr = d['ctrlIpAddr']
        ctrlPortNum = d['ctrlPortNum']
        ctrlUname = d['ctrlUname']
        ctrlPswd = d['ctrlPswd']
        ctrlTimeOut = d['ctrlTimeOut']

        tunnelName_1 = d['tunnelName_1']
        vniId_1 = d['vniId_1']

        hvsrIp_1 = d['hvsrIp_1']
        hvsrPortNum_1 = d['hvsrPortNum_1']
        hvsrName_1 = d['hvsrName_1']
        hvsrIp_2 = d['hvsrIp_2']
        hvsrPortNum_2 = d['hvsrPortNum_2']
        hvsrName_2 = d['hvsrName_2']

        vtepName_1 = d['vtepName_1']
        vtepName_2 = d['vtepName_2']

        tunnelName_2 = d['tunnelName_2']
        vniId_2 = d['vniId_2']

        hvsrIp_3 = d['hvsrIp_3']
        hvsrPortNum_3 = d['hvsrPortNum_3']
        hvsrName_3 = d['hvsrName_3']
        hvsrIp_4 = d['hvsrIp_4']
        hvsrPortNum_4 = d['hvsrPortNum_4']
        hvsrName_4 = d['hvsrName_4']

        vtepName_3 = d['vtepName_3']
        vtepName_4 = d['vtepName_4']

    except:
        logging.info ("Failed to get Controller and Node device attributes from Configuration file %s" % f)
        exit(0)

    return d


# def setup_cfg_vteps():
#     vtep_hvsrA = {}
#     vtep_hvsrB = {}
#
#     # Configure VTEP 1 onto Hypervisor 1 and reference this set as vtep_hvsrA
#     vtep_hvsrA['hvsrIp'] = doo['hvsrIp_1']
#     vtep_hvsrA['hvsrPortNum'] = doo['hvsrPortNum_1']
#     vtep_hvsrA['vtepName'] = doo['vtepName_1']
#     vtep_hvsrA['hvsrName'] = doo['hvsrName_1']
#     vtep_hvsrA['vtep_hvsr_name'] = doo['vtepName_1'] + doo['hvsrName_1']
#     vtep_hvsrA['switchName'] = doo['switchName_1']
#
#     # Configure VTEP 1 onto Hypervisor 1 and reference this set as vtep_hvsrA
#     vtep_hvsrB['hvsrIp'] = doo['hvsrIp_2']
#     vtep_hvsrB['hvsrPortNum'] = doo['hvsrPortNum_2']
#     vtep_hvsrB['vtepName'] = doo['vtepName_2']
#     vtep_hvsrB['hvsrName'] = doo['hvsrName_2']
#     vtep_hvsrB['vtep_hvsr_name'] = doo['vtepName_1'] + doo['hvsrName_2']
#     vtep_hvsrB['switchName'] = doo['switchName_2']
#
#     # Instantiate the Overlay Manager
#     overlay_manager = Ovrly_mgr(doo['ctrlIpAddr'], doo['ctrlPortNum'], doo['ctrlUname'],
#                                 doo['ctrlPswd'], doo['ctrlTimeOut'])

