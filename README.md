Nexus EVPN automation
=========

The objective is to automate day 2 operations regarding EVPN Nexus configuration. As for now, the following operations have been automated:
- Add a full tenant with L3VNI and L2VNI associated with it (evpn-tenant.yml)
- Add L2VNI only (evpn-tenant-L2-only.yml)

Parameters such as VLAN, VNI or VRF are checked before doing any changes using custom python modules. If they already exist, the playbook will fail. This is to avoid overriding an existing configuration.
The following roles perform those checks:
- check_vrf
- check_vlan
- check_vlan_l2
- check_vni
- check_vni_l2

Also a checkpoint is taken on all devices, so if any tasks fails a rollback will be triggered. This is to avoid a state where only some of the configuration has been done. This is either all playbook tasks succeeded or not

At this point, the variables are defined in a group variables file.

