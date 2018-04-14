Welcome to Kodistubs documentation!
===================================
(former xbmcstubs)
------------------

Kodi stubs are Python files that can help you develop addons for `Kodi (XBMC)`_ Media Center.
Use them in your favorite :abbr:`IDE (Integrated Developement Environment)`
to enable autocompletion and view docstrings for Kodi Python API functions, classes and methods.

Currently Kodistubs are automatically generated (indirectly) from Kodi sources so they
should reflect the exact state of Kodi Python API, including function and method
signatures and return values. Kodistubs also include `mypy`_-compatible
type annotations for all functions and methods.

The version of Kodistubs corresponds to the Kodi version they are created from.

If you notice discrepancies with the actual state of Kodi Python API, don't hesitate to open issues
or submit pull requests in the Kodistubs Github repo.

.. warning:: Kodistubs are literally stubs and do not include any useful code beyond absolute minimum
    so that not to rise syntax errors.
    Don't try to run your program outside Kodi unless you add some testing code into Kodistubs
    or use some mocking library to mock Kodi Pyhton API.

`Discussion topic on Kodi forum`_.

License: `GPL v.3`_

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Kodi (XBMC): http://kodi.tv
.. _PyCharm IDE: https://www.jetbrains.com/pycharm
.. _Discussion topic on Kodi forum: http://forum.kodi.tv/showthread.php?tid=173780
.. _GPL v.3: http://www.gnu.org/licenses/gpl.html
.. _official Kodi Python API docs: https://codedocs.xyz/xbmc/xbmc/group__python.html
.. _Kodi sources: https://github.com/xbmc/xbmc
.. _mypy: http://mypy-lang.org/

.. toctree::
    :caption: Contents:
    :maxdepth: 4

    using
    modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

