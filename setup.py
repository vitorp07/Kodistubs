from io import open
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = '17.6.0'

with open('README.rst', encoding='utf-8') as fo:
    long_descr = fo.read()

setup(
    name='Kodistubs',
    version=VERSION,
    py_modules=['xbmc', 'xbmcaddon', 'xbmcgui', 'xbmcplugin', 'xbmcvfs'],
    requires=['typing'],
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
