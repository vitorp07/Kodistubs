import sys
import json
from hashlib import md5
from decimal import Decimal
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

modules = ['xbmc', 'xbmcaddon', 'xbmcgui', 'xbmcplugin', 'xbmcvfs']

with open('README.rst') as fo:
    long_descr = fo.read()

contents = b''
for module in modules:
    with open(module + '.py', 'rb') as fo:
        contents += fo.read()

md5_hash = md5(contents).hexdigest()

with open('metadata.json', 'rb') as fo:
    metadata = json.load(fo)

if 'build' in sys.argv and md5_hash != metadata['md5_hash']:
    metadata['version'] = str(Decimal(metadata['version']) + Decimal('0.000001'))
    metadata['md5_hash'] = md5_hash
    with open('metadata.json', 'wb') as fo:
        json.dump(metadata, fo)

setup(
    name='Kodistubs',
    version=metadata['version'],
    py_modules=modules,
    zip_safe=False,
    description='Stub modules that re-create Kodi Python API',
    long_description=long_descr,
    author='Tenzer, twinther, Roman V.M.',
    maintainer='Roman V.M.',
    maintainer_email='roman1972@gmail.com',
    url='https://github.com/romanvm/Kodistubs',
    license='GPLv3',
    keywords="kodi documentation inspection",
    classifieres=[
        'Environment :: Plugins',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)
