#!/usr/bin/python

from ansible.module_utils.basic import *


def main():

	fields = {
      "vni_list": {
        "required": True,
        "type": "list",
	   },
	  "vni_id":{
	    "required": True,
	    "type": "str"
	   }
	}

	module = AnsibleModule(argument_spec=fields)

	vni_list = module.params["vni_list"]
	vni_id = module.params["vni_id"]

	list_size = len(vni_list)
	exist = False
	l = 0

	while l < list_size and not exist:
	  if vni_id == vni_list[l]["vni"]:
	  	exist = "True"
	  l = l +1

	if exist:
		response = {vni_id: "Exist"}
		module.fail_json(changed=False, meta=response, msg="VNI already exist")
	else:
		response = {vni_id: "Does not exist"}
		module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()