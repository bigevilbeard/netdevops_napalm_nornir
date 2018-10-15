#!/usr/bin/env python

##############################################################
# Author: Stuart Clark <stuaclar@cisco.com>
#
#
# Allows you to get router facts change to an IOS-XR device
# python get_facts.py -ip [ip address]
##############################################################

from napalm import get_network_driver
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
print ('Napalm Is Running........')
router_dic = device.get_facts()


for i in router_dic:
   if type(router_dic[i]) == list:
     for k in router_dic[i]:
       print("\t -{}".format(k))
   else:
     print("{}: {}".format(i, router_dic[i]))


device.close()
