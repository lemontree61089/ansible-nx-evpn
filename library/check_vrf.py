#!/usr/bin/python

from ansible.module_utils.basic import *


def main():

	fields = {
      "vrf_list": {
        "required": True,
        "type": "list",
	   },
	   "vrf_name":{
	    "required": True,
	    "type": "str"
	   }
	}

	module = AnsibleModule(argument_spec=fields)

	vrf_list = module.params["vrf_list"]
	vrf_name = module.params["vrf_name"]

	list_size = len(vrf_list)
	var = "notexist"
	l = 0

	while l < list_size:
	  if vrf_name.lower() == vrf_list[l]["vrf_name"].lower():
	  	var = "exist"
	  l = l +1

	response = {"vrf": var}

	module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()