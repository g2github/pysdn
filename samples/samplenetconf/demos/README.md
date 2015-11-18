README for vr_vif_cfg_script.py
###############################
Requirements
0. To install pip
        - On Linux
            $ sudo apt-get install python-pip
        - On Windows
            - Download https://raw.github.com/pypa/pip/master/contrib/get-pip.py being careful to save it 
              as a .py file rather than .txt. 
            - Then, run it from the command prompt.
            $ python get-pip.py
                
1. To install globally with pip (if you have pip 1.3 or greater installed globally):
        $ sudo pip install virtualenv

2. Create your local virtual environment
        $ virtualenv <give-it-a-name>
        $ cd <your-name-dir>
        $ source bin/activate
        - You will see the name of the directory in you command prompt
        
                
3. To install pysdn, which contains the sample vr_vif_cfg_script.py
        $ git clone https://github.com/g2github/pysdn.git
        
4. To setup the script for your environment
        $ cd /pysdn/samples/samplenetconfdev/demos
        $ chmod +x vr_vif_cfg_script.py

        - Edit the following file /pysdnc/samples/overlay_manager/vr_vif_cfg_script.yml

        # Controller
        ctrlIpAddr: <env-ip-addr>
        ctrlPortNum: 8181
        ctrlUname: "admin"
        ctrlPswd: "admin"
        
        # NETCONF device #1
        # (It is expected by the scripts that the device is accessible on the network
        #  if this configuration is used)
        nodeName: "vr5600-1"        # you can change this name
        nodeIpAddr: <env-ip-addr>
        nodePortNum: 830
        nodeUname: "vyatta"
        nodePswd: "vyatta"
        
        # NETCONF device interfaces
        # (Make sure these interfaces are configured on the device)
        interfaceName: "dp0p192p1"  # this must match the interface name on the vr5600
        loopback: "lo1"
        
        
        vifId: 40                   # you can change this number

            

5. To run the script        
        - From terminal type, 
            $ ./vr_vif_cfg_script.py
            
            Results:
            - The "ovrly_mgr_script will run the following operations in order...
                1. Mount the vr5600 to the configured controller
                2. Configure the VIF on the vr5600 dataplane interface
                3. Delete the vr5600 from the configured controller
            - The user will be prompted to enter any key to initiate each operation before running it
        