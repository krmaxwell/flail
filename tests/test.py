import flail
import netaddr
from nose.tools import with_setup

#import click
#from click.testing import CliRunner


def test_load_crop_present():
    flail.load_crop('crop.json')


def test_search_IP_addresses():
    assert flail.search_nets(['192.0.2.0']) == netaddr.IPSet(['192.0.2.0/32'])
    assert flail.search_nets(['192.0.2.0/24']) == netaddr.IPSet(['192.0.2.0/24'])
