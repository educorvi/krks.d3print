.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

============
krks.d3print
============

Octoprint-Integration in Plone

Features
--------

- Add multiple printers on one or multiple instances of OctoPrint or Servers running OctoPrint
- View, manage and monitor all printers in Plone
- Add as many printable objects as you want - Having multiple GCode-Files for the same Object (Maybe for different printers, with different settings or for different materials)? - You add as many GCODE-Files to the printable Object as needed
- Print the GCODE-Files with one click directly from the Object-Overview

Documentation
-------------

You will be able to see our full documentation here on GitHub in the future, as soon as the project has been completed and the package is finally ready.

Translations
------------

Currently, this product is only available in German, but it might be translated to English in the future.

Installation
------------

Install krks.d3print by adding it to your buildout::

    [buildout]

    ...

    eggs =
        krks.d3print


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/krks.d3print/issues
- Source Code: https://github.com/collective/krks.d3print
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
Feel free to open an issue at any time, or get in touch with me at:
seppo.walther@educorvi.de

License
-------

The project is licensed under the GPLv2.
