#!/usr/bin/python

import logging
import argparse
import sys

from pysdn.netconfdev.ovs.overlay_mgr import Ovrly_mgr
from samples.overlay_manager.ovrly_mgr_cfg import read_in_ovrly_cfg


if __name__ == "__main__":
    vtep_hvsrA = {}
    vtep_hvsrB = {}

    # Command line parser
    parser = argparse.ArgumentParser(description="BSC Overlay Manager VTEP Creation.")

    parser.add_argument("--log", default=None, type=str, help='specify the log message level [INFO | DEBUG]')
    parser.add_argument("--tnl", type=str, help='specify the VTEP Set to create [tnl#1 | tnl#2]')

    args = parser.parse_args()

    logging.basicConfig(level=args.log)

    if args.tnl == "tnl#1":
        # Read in the controller and overlay configuration
        doo = read_in_ovrly_cfg()

        # Configure VTEP 1 onto Hypervisor 1 and reference this set as vtep_hvsrA
        vtep_hvsrA['hvsrIp'] = doo['hvsrIp_1']
        vtep_hvsrA['hvsrPortNum'] = doo['hvsrPortNum_1']
        vtep_hvsrA['vtepName'] = doo['vtepName_1']
        vtep_hvsrA['hvsrName'] = doo['hvsrName_1']
        vtep_hvsrA['vtep_hvsr_name'] = doo['vtepName_1'] + doo['hvsrName_1']
        vtep_hvsrA['switchName'] = doo['switchName_1']

        # Configure VTEP 1 onto Hypervisor 2 and reference this set as vtep_hvsrB
        vtep_hvsrB['hvsrIp'] = doo['hvsrIp_2']
        vtep_hvsrB['hvsrPortNum'] = doo['hvsrPortNum_2']
        vtep_hvsrB['vtepName'] = doo['vtepName_2']
        vtep_hvsrB['hvsrName'] = doo['hvsrName_2']
        vtep_hvsrB['vtep_hvsr_name'] = doo['vtepName_2'] + doo['hvsrName_2']
        vtep_hvsrB['switchName'] = doo['switchName_2']
    elif args.tnl == "tnl#2":
        # Read in the controller and overlay configuration
        doo = read_in_ovrly_cfg()

        # Configure VTEP 1 onto Hypervisor 3 and reference this set as vtep_hvsrA
        vtep_hvsrA['hvsrIp'] = doo['hvsrIp_3']
        vtep_hvsrA['hvsrPortNum'] = doo['hvsrPortNum_3']
        vtep_hvsrA['vtepName'] = doo['vtepName_3']
        vtep_hvsrA['hvsrName'] = doo['hvsrName_3']
        vtep_hvsrA['vtep_hvsr_name'] = doo['vtepName_3'] + doo['hvsrName_3']
        vtep_hvsrA['switchName'] = doo['switchName_3']

        # Configure VTEP 1 onto Hypervisor 4 and reference this set as vtep_hvsrB
        vtep_hvsrB['hvsrIp'] = doo['hvsrIp_4']
        vtep_hvsrB['hvsrPortNum'] = doo['hvsrPortNum_4']
        vtep_hvsrB['vtepName'] = doo['vtepName_4']
        vtep_hvsrB['hvsrName'] = doo['hvsrName_4']
        vtep_hvsrB['vtep_hvsr_name'] = doo['vtepName_4'] + doo['hvsrName_4']
        vtep_hvsrB['switchName'] = doo['switchName_4']
    else:
        parser.print_help()
        sys.exit(0)

    # Instantiate the Overlay Manager
    overlay_manager = Ovrly_mgr(doo['ctrlIpAddr'], doo['ctrlPortNum'], doo['ctrlUname'],
                                doo['ctrlPswd'], doo['ctrlTimeOut'])

    logging.info("Creating 2 tunnel VTEP endpoints: %s on hypervisor %s and %s on hypervisor %s",
                 vtep_hvsrA['vtepName'], vtep_hvsrA['hvsrName'],
                 vtep_hvsrB['vtepName'], vtep_hvsrB['hvsrName'])

    overlay_manager.register_hypervisor(vtep_hvsrA)
    overlay_manager.resister_vtep_on_hypervisor(vtep_hvsrA)
    overlay_manager.register_hypervisor(vtep_hvsrB)
    overlay_manager.resister_vtep_on_hypervisor(vtep_hvsrB)
