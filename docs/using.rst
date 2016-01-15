Using Kodistubs
###############

Writing Code
============

The main purpose of Kodistubs is to help you to write Kodi addon code in various IDEs
(Integrated Development Environments) by providing code completion, quick help based on Kodistubs docstrings,
and code inspection (linting) in IDEs that provide this feature.

Below are the instructions for using Kodistubs in popular Python IDEs.

PyCharm
-------

To add Kodistubs to current project open ``Settings`` > ``Project`` > ``Project Structure``,
click ``+ Add Content Root`` and select a folder where Kodistubs ``.py`` files are located.

.. figure:: _static/pycharm_add_content_root.jpg

    **Adding Kodistubs to the current project in PyCharm**

After that you'll get code completion and quick help for Kodi Python API functions/classes/methods.

.. figure:: _static/pycharm_autocompletion.jpg

    **Code completion and quick help in PyCharm**

.. note:: PyCharm quick help partially supports reStructuredText formatting.

Eclipse + PyDev
---------------

In PyDev right-click the project's name, select ``Properties`` > ``PyDev - PYTHONPATH`` >
``External Libraries``, click ``Add source folder`` and select a folder where Kodistubs ``.py``
files are located.

.. figure:: _static/pydev_add_source_folder.jpg

    **Adding Kodistubs to the current project in PyDev**

After that you'll get code completion and quick help for Kodi Python API functions/classes/methods.

.. figure:: _static/pydev_autocompletion.jpg

     **Code completion and quick help in PyDev**

Python Tools for Visual Studio
------------------------------

In **Solution Explorer** right-click **Search Paths**, in a context menu select **Add Folder To Search Path...**
and select a folder where Kodistubs ``.py`` files are located.

.. figure:: _static/ptvs_add_to_search_path.jpg

    **Adding Kodistubs to the current project in PTVS**

After that you'll get code completion and quick help for Kodi Python API functions/classes/methods.

.. figure:: _static/ptvs_autocompletion.jpg

    **Code completion and quick help in PTVS**

Testing Code
============

You can use Kodistubs in combination with some mocking library, e.g. `mock`_,
to write unit tests for your addon code.

.. _mock: https://pypi.python.org/pypi/mock

Documenting Code
================


