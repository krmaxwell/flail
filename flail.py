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

import click
import json


@click.command()
@click.option('--targets', help='comma-separated list of targets')
@click.option('--inputfile', help='file containing targets, one per line')
@click.argument('crop', default='crop.json')
def cli(targets, inputfile, crop):
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
