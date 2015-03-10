import flail
#import click
#from click.testing import CliRunner


def test_load_crop_present():
    flail.load_crop('crop.json')


def test_search_IP_addresses():
    assert flail.search_nets(['192.0.2.0']) == ['192.0.2.0']
    assert flail.search_nets(['192.0.2.0/24']) == ['192.0.2.0/24']
