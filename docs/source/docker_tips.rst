Docker tips
===========

docker cli with proxy
---------------------

.. code-block:: shell

    cd /etc/systemd/system/
    sudo mkdir docker.service.d
    sudo touch http-proxy.conf

in ``/etc/systemd/system/http-proxy.conf``:

.. code-block::

    [Service]
    Environment="HTTP_PROXY=http://example_url:example_port/"
    Environment="HTTPS_PROXY=https://example_url:example_port/"
