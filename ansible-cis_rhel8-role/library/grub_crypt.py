#!/usr/bin/python

from __future__ import print_function
import argparse
from hashlib import pbkdf2_hmac
from os import urandom
from sys import stdin, stderr, exit as sysexit
from binascii import hexlify

def gen_pass(passphrase, iterCount=100000, saltLength=64):
    algo = 'sha512'
    try:
        binSalt = urandom(saltLength)
        hexSalt = hexlify(binSalt)
        passHash = hexlify(pbkdf2_hmac(algo, passphrase, binSalt, iterCount))
    except:
        print("Unexpected error generating hash!\n", file=stderr)
        raise
    return("grub.pbkdf2.{}.{}.{}.{}".format(algo, iterCount, hexSalt, passHash))


def main():
    module = AnsibleModule(
            argument_spec = dict(
                paraphrase = dict(no_log=True, required=False, default='random', type='str'),
                )

            )
    paraphrase = module.params['paraphrase']

    salted_pass = gen_pass(paraphrase)
    module.exit_json(changed=False, passhash=salted_pass)

from ansible.module_utils.basic import *
if __name__ == '__main__':
        main()
