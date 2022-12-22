# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
    ['sjbilling']

package_data = \
    {'': ['*']}

install_requires = \
    ['kvdroid @ https://github.com/kvdroid/Kvdroid/archive/refs/heads/master.zip',
     'pyjnius>=1.4.2,<2.0.0']

setup_kwargs = {
    'name': 'sjbilling',
    'version': '2022.1.0',
    'description': 'port google play billing (android) to python',
    'long_description': '# SJAndroidBilling\nport google play billing (android) to python \n',
    'author': 'Kenechukwu Akubue',
    'author_email': 'kengoon19@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}

setup(**setup_kwargs)
