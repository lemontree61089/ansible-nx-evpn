#!/usr/bin/python

from ansible.module_utils.basic import *


def main():

	fields = {
      "list": {
        "required": True,
        "type": "list",
	   },
	}

	module = AnsibleModule(argument_spec=fields)

	vlan = module.params

	for i in vlan["list"]:
		var = i["vlanshowbr-vlanid"]

	var = int(var)+1

	response = {"vlan_free": var}

	module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()