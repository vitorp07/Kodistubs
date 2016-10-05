try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as fobj:
    long_descr = fobj.read()

setup(
    name='Kodistubs',
    version='2.0.0',
    py_modules=['xbmc', 'xbmcaddon', 'xbmcgui', 'xbmcplugin', 'xbmcvfs'],
    zip_safe=False,
    description='Stub modules that re-create Kodi Python API',
    long_description=long_descr,
    author='Tenzer, twinther, Roman V.M.',
    maintainer='Roman V.M.',
    maintainer_email='romanvm@yandex.ua',
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
