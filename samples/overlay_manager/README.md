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

5. The Overlay Manager Samples provide a collection of scripts that call upon the NETCONF device OVS drivers 
   (pysdn/netconfdev/ovs/overlay_mgr.py).  These samples are based on a sample network configuration comprised of one
   BSC controller, four hypervisors, OVS switches, and VTEPs.  The user is able to map these samples to their 
   environment by editing a configuration file (pysdn/samples/overlay_manager/ovrly_mgr_cfg.yml) such that no code 
   changes are required.  
        
6. To setup the sample scripts for your environment
        
        - $ cd /pysdn/samples/overlay_manager/
        - $ chmod +x *.py
        - Edit the following file /pysdnc/samples/overlay_manager/ovrly_mgr_cfg.yml

            # Controller
            ctrlIpAddr: 192.168.7.153
            ctrlPortNum: 8181
            ctrlUname: "admin"
            ctrlPswd: "admin"
            ctrlTimeOut: "5"
            
            # Overlay Tunnel #1 Configuration
            tunnelName_1: tunnel1
            
            # Hypervisors and Switches
            hvsrIp_1: 192.168.7.151
            hvsrPortNum_1: 16640
            hvsrName_1: "Hypervisor1"
            switchName_1: "ovsbr100"
            
            hvsrIp_2: 192.168.7.152
            hvsrPortNum_2: 16640
            hvsrName_2: "Hypervisor2"
            switchName_2: "ovsbr200"
            
            # VTEPs
            vtepName_1: "vtep1"
            vtepName_2: "vtep1
            
            # VXLAN Identifiers
            vniId_1: 100
            
            # Overlay Tunnel #2 Configuration
            # Hypervisors and Switches
            tunnelName_2: tunnel2
            
            hvsrIp_3: 192.168.7.161
            hvsrPortNum_3: 16640
            hvsrName_3: "Hypervisor3"
            switchName_3: "ovsbr300"
            
            hvsrIp_4: 192.168.7.162
            hvsrPortNum_4: 16640
            hvsrName_4: "Hypervisor4"
            switchName_4: "ovsbr400"
            
            # VTEPs
            vtepName_3: "vtep1"
            vtepName_4: "vtep1"
            
            # VXLAN Identifiers
            vniId_2: 200

7. There are four Overlay Manager Sample scripts that perform VTEP and associated resource setup and deletion, and 
   overlay tunnel setup and deletion.  Two files provide configuration file support routines.  These files are all
   located in pysdn/samples/overlay_manager, and are as follows:

    - overly_mgr_cfg.yml - Sample resource configuration

    - overly_mgr_cfg.py - Sample resource configuration file supporting routines

    - create_vteps.py - Sets up tunnel VTEPs and associated resources.  Expects at least a single command line 
                        parameter, --tnl with value tnl#1 or tnl#2 depending upon which tunnel setup is desired.
                        An optional second command line parameter, --log with values INFO or DEBUG may also be provided
                        if troubleshooting or general flow visibility is required or desired.
                        
                        - Example: $ python ./create_vteps.py --tnl tnl#1 --log=DEBUG

    - delete_vteps.py - Deletes tunnel VTEPs and associated resources.  Expects at least a single command line
                        parameter, --tnl with value tnl#1 or tnl#2 depending upon which tunnel setup is desired.  An 
                        optional second command line parameter, --log with values INFO or DEBUG may also be provided
                        if troubleshooting or general flow visibility is required or desired.
                        
                        - Example: $ python ./delete_vteps.py --tnl tnl#1 --log=INFO

    - build_tunnel.py - Builds a tunnel.  Expects at least a single command line parameter, --tnl with value tnl#1 or 
                        tnl#2 depending upon which tunnel setup is desired.  An optional second command line parameter, 
                        --log with values INFO or DEBUG may also be provided if troubleshooting or general flow 
                        visibility is required or desired.
                        
                        - Example: $ python ./build_tunnel.py --tnl tnl#1

    - delete_tunnel.py - Deletes a tunnel.  Expects at least a single command line parameter, --tnl with value tnl#1 or 
                         tnl#2 depending upon which tunnel setup is desired.  An optional second command line parameter, 
                         --log with values INFO or DEBUG may also be provided if troubleshooting or general flow 
                         visibility is required or desired.
                         
                         - Example: $ python ./delete_tunnel.py --tnl tnl#1 --log=INFO
         
        
        

