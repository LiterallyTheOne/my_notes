Setting up sphinx
=================

My goto method
--------------

.. code-block:: shell

    mkdir docs
    cd docs
    sphinx-quickstart

change this in ``docs/source/conf.py``:

.. code-block:: shell

    html_theme = 'sphinx_rtd_theme'

After that

.. code-block:: shell

    make html

Add it to `read-the-docs <https://readthedocs.org/>`_
-----------------------------------------------------

in your project directory:

.. code-block:: shell

    touch .readthedocs.yaml
    touch docs/requirements.txt


In ``.readthedocs.yaml``:

.. code-block:: yaml

    version: "2"

    build:
      os: "ubuntu-22.04"
      tools:
        python: "3.10"

    python:
      install:
        - requirements: docs/requirements.txt

    sphinx:
      configuration: docs/source/conf.py


in ``docs/requirements.txt``:

.. code-block:: text

    sphinx==7.1.2
    sphinx-rtd-theme==1.3.0rc1
