Role Name
=========

L3VNI
Add nexus configuration for L3VNI only. Will create VLAN with associated L3VNI, configure the VRF, SVI, BGP, VTEP config

Requirements
------------

Variable with the following format has to be defined :

L3VNI:
  - { vlan: 502, vni: 5502, vlan_name: L3-TST3, vrf: TST3 }
  - { vlan: 503, vni: 5503, vlan_name: L3-TST4, vrf: TST4 }



