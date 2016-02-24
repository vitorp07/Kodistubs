Using Kodistubs
###############

Writing Code
============

The main purpose of Kodistubs is to help you to write Kodi addon code in various
:abbr:`IDEs(Integrated Development Environments)` by providing code completion,
quick access to Kodi Python API docstrings, and code inspection (linting)
in IDEs that provide this feature.

Below are the instructions for using Kodistubs in popular Python IDEs.

PyCharm
-------

To add Kodistubs to the current project open
:menuselection:`Settings --> Project --> Project Structure`,
click :guilabel:`+ Add Content Root` and select a folder where Kodistubs :file:`.py` files are located.

.. figure:: _static/pycharm_add_content_root.jpg

    **Adding Kodistubs to the current project in PyCharm**

This enables code completion and docstrings pop-ups for Kodi Python API functions/classes/methods.

.. figure:: _static/pycharm_autocompletion.jpg

    **Code completion and a docstring pop-up in PyCharm**

.. note:: PyCharm docstrings pop-ups partially support reStructuredText formatting.

Eclipse + PyDev
---------------

In PyDev right-click the project's name, select
:menuselection:`Properties --> PyDev - PYTHONPATH --> External Libraries`,
click :guilabel:`Add source folder` and select a  folder
where Kodistubs :file:`.py` files are located.

.. figure:: _static/pydev_add_source_folder.jpg

    **Adding Kodistubs to the current project in PyDev**

This enables code completion and docstrings pop-ups for Kodi Python API functions/classes/methods.

.. figure:: _static/pydev_autocompletion.jpg

     **Code completion and a docstring pop-up in PyDev**

Python Tools for Visual Studio
------------------------------

In :guilabel:`Solution Explorer` right-click :guilabel:`Search Paths`,
in the context menu select :guilabel:`Add Folder To Search Path...`
and then select a folder where Kodistubs :file:`.py` files are located.

.. figure:: _static/ptvs_add_to_search_path.jpg

    **Adding Kodistubs to the current project in PTVS**

This enables code completion and docstrings pop-ups for Kodi Python API functions/classes/methods.

.. figure:: _static/ptvs_autocompletion.jpg

    **Code completion and a docstring pop-up in PTVS**

Sublime Text 3 + Anaconda
-------------------------

In :guilabel:`Preferences` select :menuselection:`Package Settings --> Anaconda --> Settings - User`,
and add the folder with Kodistubs :file:`.py` files to ``extra_paths`` list
of Anaconda User configuraiton file.

.. note:: Sublime Text configuration files have JSON formatting.

For example:

.. code-block:: json

  {
      "extra_paths":
      [
          "d:\\Python\\Kodistubs"
      ]
  }

This enables code completion and docstrings pop-ups for Kodi Python API functions/classes/methods.

.. figure:: _static/sublime_text_anaconda.jpg

    **Code completion and a docstring pop-up in Sublime Text 3**


Testing Code
============

You can use Kodistubs in combination with some mocking library, e.g. `mock`_,
to write unit tests for your addon code.

.. _mock: https://pypi.python.org/pypi/mock

Documenting Code
================

Currently `Sphinx`_ is in fact the standard tool for documenting Python code. But for generating
documentation from docstrings it requires that your modules can be imported without any side-effects
(i.e. exceptions). If you want to document your addon with Sphinx, add Kodi stubs folder to
:data:`sys.path` of :file:`conf.py` file in your Sphinx project and in most cases your addon modules will be
imported without issues. Just don't forget to protect your module-level exetutable code with
``if __name__ == '__main__'`` condition.

Also the root URL of this documentation (without :file:`index.html`) can be used as a reference point
for `intersphinx`_. For example::

    intersphinx_mapping = {
        'https://docs.python.org/2.7': None,
        'http://romanvm.github.io/Kodistubs': None,  # Reference to Kodi stubs
    }

This will enable cross-references to Kodi Python API objects in your Sphinx-generated documentation.

.. _Sphinx: http://www.sphinx-doc.org/en/stable/
.. _intersphinx: http://www.sphinx-doc.org/en/stable/ext/intersphinx.html

