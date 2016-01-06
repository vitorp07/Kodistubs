Kodistubs
=========
**(former xbmcstubs)**
----------------------

These files can help you to develop a script or an addon for `Kodi (XBMC)`_ Media Center.
Use them in your favorite IDE to enable autocompletion of function, class and method names and access docstrings
for each function, class and method.

Typically, a Python IDE (Integrated Development Environment) allows you add a "source directory" containing
the Kodistubs files to your development project. Then you will be able to "import" the modules as you normally would
in Python.

E.g. in `PyCharm IDE`_ go to ``File** > Settings > Project xxx > Project Structure``,
click ``+ Add Content Root`` and select a folder with Koditubs ``.py`` files.
Then you will get auto-completion, quick help and code inspection for Kodi Python API fuctions/classes/methods.

**Warning**: Kodistubs are literally stubs and do not include any useful code,
so don't try to run your program outside Kodi unless you add some testing code into Kodistubs
or use some mocking library to mock Kodi Pyhton API.

`Kodistubs documentation`_

`Discussion topic on Kodi forum`_

License: `GPL v.3`_

.. _Kodi (XBMC): http://kodi.tv
.. _PyCharm IDE: https://www.jetbrains.com/pycharm
.. _Kodistubs documentation: http://romanvm.github.io/Kodistubs/docs
.. _Discussion topic on Kodi forum: http://forum.kodi.tv/showthread.php?tid=173780
.. _GPL v.3: http://www.gnu.org/licenses/gpl.html
