Role Name
=========

L2VNI_only
Add nexus configuration for L2VNI only. Will create VLAN with associated L2VNI, configure the interface in trunk or access mode, add the L2VNI to the VTEP, and perform the EVPN BGP configuration.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.
Variable with the following format has to be defined (VRF, addr, mask are not mandatory for this role, if specified will be ignore on this role) :
L2VNI:
  - { vlan: 300, vni: 30200, vlan_name: L2-VNI-300, interface: ethernet1/9, interface_mode: trunk, addr: 172.21.200.1, mask: 24,  vrf: TST3}
  - { vlan: 301, vni: 30201, vlan_name: L2-VNI-301, interface: ethernet1/9, interface_mode: trunk, addr: 172.21.201.1, mask: 24,  vrf: TST3} 


Dependencies
------------

Will check if VLAN and VNI do not already exist. 
check_vni_l2
check_vlan_l2


