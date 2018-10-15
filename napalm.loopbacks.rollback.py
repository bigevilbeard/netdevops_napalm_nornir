#!/usr/bin/env python

##############################################################
# Author: Stuart Clark <stuaclar@cisco.com>
#
#
# Allows you to merge configurations to an IOS-XR device
# python napalm_loopbacks.rollback.py -ip [ip address]
##############################################################

from napalm import get_network_driver
import sys
import argparse



parser = argparse.ArgumentParser()
parser.add_argument("-ip", "--router_ip", help="Enter device ip address")
args = parser.parse_args()
device_ip = args.router_ip

driver = get_network_driver('iosxr')
device = driver(username='vagrant',
                password='vagrant',
                optional_args={'port':2221},
                hostname=device_ip)


device.open()
print('Napalm Is Running........')
device.load_merge_candidate(filename='new_loopbacks.cfg')
diffs = device.compare_config()


if len(diffs) > 0:
    print(diffs)

    commit = input("Type COMMIT to commit the configuration or hit ENTER to abort: ")
    if commit == 'COMMIT':

        try:
            device.commit_config()


        except Exception as inst:
            print('\nAn error occurred with the commit: ')
            print(type(inst))
            sys.exit(inst)
            print()

        else:
            print('Config committed')

    else:
        sys.exit('Script aborted by user')

else:
    print('No changes needed')
    device.discard_config()
    sys.exit()
    device.close()

rollback = input("Type ROLLBACK to revert changes or hit ENTER to abort: ")

if rollback == 'ROLLBACK':

        try:
            device.rollback()


        except Exception as inst:
            print('\nAn error occurred with the rollback: ')
            print(type(inst))
            sys.exit(inst)
            print()

        else:
            print('Configuration Reverted')

else:
    sys.exit()


device.close()
