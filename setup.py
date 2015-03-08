from setuptools import setup

setup(
    name='flail',
    version='0.1',
    py_modules=['flail'],
    install_requires=[
        'Click',
        'netaddr',
    ],
    entry_points='''
        [console_scripts]
        flail=flail:cli
    ''',
)
