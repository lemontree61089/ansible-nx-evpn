Nexus EVPN automation
=========

The objective is to automate day 2 operations regarding EVPN Nexus configuration. As for now, the following operations have been automated:
- Add a full tenant with L3VNI and L2VNI associated with it (evpn-tenant.yml)
- Add L2VNI only (evpn-tenant-L2-only.yml)

Parameters such as VLAN, VNI or VRF are checked before doing any changes. If they already exist, the playbook will fail.
The following roles perform those checks:
- check_vrf
- check_vlan
- check_vlan_l2
- check_vni
- check_vni_l2

Also a checkpoint is taken on all devices, so if any tasks fails a rollback will be triggered

evpn-tenant.yml
