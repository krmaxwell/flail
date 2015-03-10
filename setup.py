from setuptools import setup

setup(
    name='flail',
    version='0.1',
    py_modules=['flail'],
    install_requires=[
        'click',
        'netaddr'
    ],
    entry_points='''
        [console_scripts]
        flail=flail:cli
    ''',
)
