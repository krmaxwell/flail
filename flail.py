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
import click
import json
import pprint
import re
from netaddr import IPAddress, IPNetwork, IPSet


@click.command()
@click.option('--targets', '-t', help='targets (comma-separated if >1)')
@click.option('--inputfile', '-i', help='file containing targets, one per line')
@click.argument('crop', help='path to crop.json',
                type=click.Path(exists=True, dir_okay=False),
                default='crop.json')
def cli(targets, inputfile):
    '''Search blacklists for networks, autonomous systems, and domains'''
    crop = load_crop(crop)
    terms = []
    if inputfile:
        with click.open_file(inputfile, 'r') as f:
            terms = list(f)
    if targets:
        terms.append(targets.split(','))


def load_crop(cropfile):
    with open(cropfile, 'rb') as f:
        crop = json.load(f)
    return crop


def main():
    if nets:
        ournet = IPSet(IPNetwork(n) for n in nets)
    else:
        ournet = None

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
