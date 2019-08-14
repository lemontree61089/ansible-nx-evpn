Role Name
=========

L2VNI.
Add nexus configuration for L2VNI and associate it to an L3VNI. Will create VLAN with associated L2VNI, configure the interface in trunk or access mode, add the L2VNI to the VTEP, perform the EVPN BGP configuration, create the SVI associated with the VRF. Enable anycast gw and arp-suppression

Requirements
------------

Variable with the following format has to be defined:

L2VNI:
  - { vlan: 300, vni: 30200, vlan_name: L2-VNI-300, interface: ethernet1/9, interface_mode: trunk, addr: 172.21.200.1, mask: 24,  vrf: TST3}
  - { vlan: 301, vni: 30201, vlan_name: L2-VNI-301, interface: ethernet1/9, interface_mode: trunk, addr: 172.21.201.1, mask: 24,  vrf: TST3} 


