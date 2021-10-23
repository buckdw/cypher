#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

JSON_TKN_SYMMETRICAL_KEY = "symmetrical_key"
JSON_TKN_SALTED_SYMMETRICAL_KEY = "salted_symmetrical_key"


def salt(key):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=os.urandom(16),
        iterations=100000
    )
    safekey = bytes(key, "utf-8")
    return base64.urlsafe_b64encode(kdf.derive(safekey))


def salt_module():
    result = dict(
        changed=True,
    )
    module_args = dict(
        JSON_TKN_SYMMETRICAL_KEY=dict(type='str', required=True),
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    result[JSON_TKN_SALTED_SYMMETRICAL_KEY] = salt(module.params[JSON_TKN_SYMMETRICAL_KEY])
    module.exit_json(**result)


def main():
    salt_module()


if __name__ == '__main__':
    main()
