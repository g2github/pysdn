Requirements

1. To install pip

        - On Linux
            $ sudo apt-get install python-pip

        - On Windows
            - Download https://raw.github.com/pypa/pip/master/contrib/get-pip.py being careful to save it 
              as a .py file rather than .txt. 
            - Then, run it from the command prompt.
            $ python get-pip.py
                
2. To install globally with pip (if you have pip 1.3 or greater installed globally):
        
        - $ sudo pip install virtualenv

3. Create your local virtual environment
        
        - $ virtualenv <give-it-a-name>
        - $ cd <your-name-dir>
        - $ source bin/activate
        - You will see the name of the directory in you command prompt
        
                
4. To install pysdn (which contains the sample overlay manager scripts)

        - $ git clone https://github.com/brocade/pysdn.git
        - $ python setup.py develop

5. The BVR (Brocade VRouter) Configuration Sample script (vr_cfg.py) will provision a single VR5600 according to a 
   pre-set configuration as instantiated in the script code and mapped to the real environment by way of vr_cfg.yml file 
   configuration (see step 6).
        
6. To setup the sample scripts for your environment
        
        - $ cd /pysdn/samples/overlay_manager/
        - $ chmod +x *.py
        - Edit the following file /pysdnc/samples/overlay_manager/ovrly_mgr_cfg.yml

            # Set the following parameters according to your local network
            # environment setup (please take a look at NOTE in above)
            
            # Controller
            ctrlIpAddr: 192.168.7.153  # 10.252.30.161
            ctrlPortNum: 8181
            ctrlUname: "admin"
            ctrlPswd: "admin"
            ctrlTimeOut: "5"
            
            # You must specify "--vr" and one of the following nodeName_x strings at the vr_cfg.py command line
            #  *****************CPE1**********************************************************
            nodeName_1: "vr5600-CPE1"           # Specify this name at vr_cfg.py --vr command line to provision CPE1 VR
            nodeIpAddr_1: 192.168.7.20  # 10.252.30.196
            nodePortNum_1: 830
            nodeUname_1: "vyatta"
            nodePswd_1: "vyatta"
            
            #  set interfaces loopback lo address 10.0.0.11/32
            #  set interfaces dataplane dp0s3 address 192.168.21.1/24
            #  set interfaces dataplane dp0s6 address 192.168.11.1/24
            #  set interfaces dataplane dp0s8 address 192.168.22.1/24
            lpbkName_1: lo
            lpbkAddr_1: 10.0.0.11/32
            dp1Name_1: dp0p224p1 #dp0s3
            dp1Addr_1: 224.100.8.30/24 #192.168.21.1/24
            dp2Name_1: dp0s6
            dp2Addr_1: 192.168.11.1/24
            dp3Name_1: dp0s8
            dp3Addr_1: 192.168.22.1/24
            
            #  set protocols ospf parameters routerÅ-id 10.0.0.11
            #  set protocols ospf area 0.0.0.0 network 192.168.21.0/24
            #  set protocols ospf area 0.0.0.0 network 192.168.22.0/24
            #  set protocols ospf area 0.0.0.0 network 10.0.0.11/32
            #  set protocols ospf area 0.0.0.1 network 192.168.11.0/24
            #  set protocols ospf passive-interface dp0s6
            ospfParamRouterId_1: 10.0.0.11
            ospfArea1_1: 0.0.0.0
            ospfNetwork1_1: 192.168.21.0/24
            ospfArea2_1: 0.0.0.0
            ospfNetwork2_1: 192.168.22.0/24
            ospfArea3_1: 0.0.0.0
            ospfNetwork3_1: 10.0.0.11/32
            ospfArea4_1: 0.0.0.1
            ospfNetwork4_1: 192.168.11.0/24
            ospfPsvIf_1: dp0p224p1 #dp0s6
            
            # HOLD OFF
            #  ibgp to datacenter A
            #  set protocols bgp 100 parameters router-id 10.0.0.11
            #  set protocols bgp 100 neighbor 10.0.0.22 nexthop-self
            #  set protocols bgp 100 neighbor 10.0.0.22 remote-as 100
            #  set protocols bgp 100 neighbor 10.0.0.22 update-source 10.0.0.11
            #  set protocols bgp 100 neighbor 10.0.0.22 address-family ipv4-unicast
            bgpGroup_1: 100
            bgpNbr_1: 10.0.0.22
            bgpNxtHop_1: "nexthop-self"
            bgpRemoteAS_1: 100
            bgpUpdateSrc_1: 10.0.0.11
            bgpAddrFam_1: "ipv4-unicast"
            
            # HOLD OFF
            #  ebgp to customer
            #  set protocols bgp neighbor X.X.X.X remote-as 100
            #  set protocols bgp 100 neighbor X.X.X.X address-family ipv4-unicast
            #  set protocols bgp 100 address-family ipv4-unicast network x.x.x.x/24 (Any local netowrks that we want to advertise)
            
            
            #  ******************CPE2*********************************************************
            nodeName_2: "vr5600-CPE2"         # Specify this name at vr-cfg --vr command line to provision CPE2 VR
            nodeIpAddr_2: 192.168.7.20  #10.252.30.203
            nodePortNum_2: 830
            nodeUname_2: "vyatta"
            nodePswd_2: "vyatta"
            
            #  set interfaces loopback lo address 10.0.0.12/32
            #  set interfaces dataplane dp0s3 address 192.168.21.2/24
            #  set interfaces dataplane dp0s6 address 192.168.12.1/24
            lpbkName_2: lo
            lpbkAddr_2: 10.0.0.12/32
            dp1Name_2: dp0s3
            dp1Addr_2: 192.168.21.1/24
            dp2Name_2: dp0s6
            dp2Addr_2: 192.168.12.1/24
            
            #  set protocols ospf parameters router-id 10.0.0.12
            #  set protocols ospf area 0.0.0.0 network 192.168.21.0/24
            #  set protocols ospf area 0.0.0.0 network 10.0.0.12/32
            #  set protocols ospf area 0.0.0.2 network 192.168.12.0/24
            #  set protocols ospf passive-interface dp0s6
            ospfParamRouterId_2: 10.0.0.12
            ospfArea1_2: 0.0.0.0
            ospfNetwork1_2: 192.168.21.0/24
            ospfArea2_2: 0.0.0.0
            ospfNetwork2_2: 10.0.0.12/32
            ospfArea3_2: 0.0.0.2
            ospfNetwork3_2: 192.168.12.0/24
            ospfPsvIf_2: dp0p224p1
            
            # HOLD OFF
            #  ******************Datacenter A**********************************************************
            nodeName_3: "vr5600-Datacenter A" # Specify this name at vr-cfg --vr command line to provision Datacenter A VR
            nodeIpAddr_3: 192.168.7.21
            nodePortNum_3: 830
            nodeUname_3: "vyatta"
            nodePswd_3: "vyatta"
            
            #  set interfaces loopback lo address 10.0.0.22/32
            #  set interfaces dataplane dp0s3 address 192.168.21.2/24
            #  set interfaces dataplane dp0s6 address 10.252.30.206/30
            lpbkName_3: lo
            lpbkAddr_3: 10.0.0.22/32
            dp1Name_3: dp0s3
            dp1Addr_3: 192.168.21.2/24
            dp2Name_3: dp0s6
            dp2Addr_3: 10.252.30.206/30
            
            #  set protocols ospf parameters routerÅ-id 10.0.0.22
            #  set protocols ospf area 0.0.0.0 network 192.168.21.0/24
            #  set protocols ospf area 0.0.0.0 network 10.0.0.22/32
            #  set protocols ospf default-information originate always (im not sure if we need this)
            ospfParams-RouterId_1: 10.0.0.22
            ospfArea-0000-1_1: 192.168.21.0/24
            ospfArea-0000-2_1: 10.0.0.22/32
            
            # HOLD OFF
            #  ibgp ro CPE1
            #  set protocols bgp 100 parameters routerÅ-id 10.0.0.22
            #  set protocols bgp 100 neighbor 10.0.0.11 nexthop-self
            #  set protocols bgp 100 neighbor 10.0.0.11 remoteÅ-as 100
            #  set protocols bgp 100 neighbor 10.0.0.11 address-family ipv4-unicast
            #  set protocols bgp 100 neighbor 10.0.0.11 address-family ipv4-unicast routeÅ-reflectorÅ-client
            #  set protocols bgp 100 neighbor 10.0.0.11 update-source 10.0.0.22
            #
            #
            #
            # HOLD OFF
            #  ebgp to Juniper MX
            #  set protocols bgp neighbor X.X.X.X remote-as 300
            #  set protocols bgp 100 neighbor X.X.X.X addressÅ-family ipv4Å-unicast
            #  set protocols bgp 100 address-family ipv4-unicast network x.x.x.x/24 (Any local netowrks that we want to advertise)
            #
            #
            #  ----------------------------------------------------------------------------------------
            #
            #
            #  Usefull commands
            #  show ip bgp summary
            #  show ip bgp

7. There is one VR5600 Configuration Sample script that will confgure a single VR5600 as specified with the command 
   line switch --vr.  There are two files for this script, and are as follows:

    - vr_cfg.yml - Sample resource configuration

    - vr_cfg.py - Performs the vrouter configuration.  Expects at least a single command line 
                        parameter, --vr with value vr5600-CPE1 or vr5600-CPE2 depending upon which vrouter is
                        desired to be provisioned.  An optional second command line parameter, --log with values INFO 
                        or DEBUG may also be provided if troubleshooting or general flow visibility is required or 
                        desired.
                        
                        - Example: $ python ./vr_cfg.py --vr vr5600-CPE1
