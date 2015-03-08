#!/usr/bin/env python

# Flail is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Flail is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Flail.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import json
import pprint
import re
from netaddr import IPAddress, IPNetwork, IPSet


def main():
    argparse = argparse.ArgumentParser()
    argparse.add_argument('-n', '--networks', help='target network in CIDR format (comma-separated if >1)')
    argparse.add_argument('-i', '--input', help='file containing target networks in CIDR format, one per line')
    argparse.add_argument('-d', '--domain', help="substring to search in domains")
    argparse.add_argument('-c', '--crop', help="path to crop.json")
    args = argparse.parse_args()

    if args.crop:
        cropfile = args.crop
    else:
        cropfile = 'crop.json'

    with open(cropfile, 'rb') as f:
        harvest = json.load(f)

    if args.networks:
        nets = args.networks.split(',')
    elif args.input:
        with open(args.input, 'rb') as f:
            nets = list(f)
    else:
        nets = None

    if nets:
        ournet = IPSet(IPNetwork(n) for n in nets)
    else:
        ournet = None

    if args.domain:
        ourdomain = args.domain
    else:
        ourdomain = None

    hosts = []
    pp = pprint.PrettyPrinter(indent=2)

    for address in harvest:
        if ournet and re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', address[0]) and IPAddress(address[0]) in ournet:
            hosts.append(address)
        elif ourdomain and re.match(ourdomain, address[0], flags=re.IGNORECASE):
            hosts.append(address)

    pp.pprint(hosts)


if __name__ == "__main__":
    main()
