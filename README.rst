Test Teach
==========

This is a test lesson plan. It introduces logging with Python. There are code samples and source files for the documentation.

The documentation is written in restructuredText for use with Sphinx and is in the docs directory.

To generate the HTML version of the docs you need python with sphinx installed.

.. code-block:: bash

    $ cd docs
    $ make html

Then you can open test_teach/docs/_build/html/index.html to see the lesson.

To generate a PDF version of the docs, you also need rst2pdf installed.

See http://thyagjs.blogspot.com/2012/05/create-pdf-document-from-your-sphinx.html
and https://github.com/ralsina/rst2pdf
