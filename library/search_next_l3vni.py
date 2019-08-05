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

	vni = module.params

	for i in vni["list"]:
		if "L3" in i["type"]:
		  var = i["vni"]

	var = int(var)+1

	response = {"l3vni_free": var}

	module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()