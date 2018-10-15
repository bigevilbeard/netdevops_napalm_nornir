#!/usr/bin/env python

##############################################################
# Author: Stuart Clark <stuaclar@cisco.com>
#
#
# Allows you to validate configurations to an IOS-XR device
# python
##############################################################

from nornir.core import InitNornir
from nornir.plugins.tasks.networking import napalm_get
from nornir.plugins.functions.text import print_result


nr = InitNornir()

result = nr.run(
             napalm_get,
             getters=['get_facts'])

print_result(result)
