#!/usr/bin/python

from ansible.module_utils.basic import *


def main():

	fields = {
      "vlan_list_running": {
        "required": True,
        "type": "list",
	   },
      "vlan_config": {
        "required": True,
        "type": "str",
	   },
	}

	module = AnsibleModule(argument_spec=fields)

	vlan_list_running = module.params["vlan_list_running"]
	vlan_config = module.params["vlan_config"]

	list_size = len(vlan_list_running)
	exist = False
	l = 0

	while l < list_size and not exist:
	  if vlan_config == vlan_list_running[l]["vlanshowbr-vlanid"]:
	  	exist = "True"
	  l = l +1

	if exist:
		response = {vlan_config: "Exist"}
		module.fail_json(changed=False, meta=response, msg="VLAN already exist")
	else:
		response = {vlan_config: "Does not exist"}
		module.exit_json(changed=False, meta=response)

if __name__ == '__main__':
    main()