Docker tips
===========

docker cli with proxy
---------------------

.. code-block:: shell

    cd /etc/systemd/system/
    sudo mkdir docker.service.d
    cd docker.service.d
    sudo touch http-proxy.conf

in ``/etc/systemd/system/docker.service.d/http-proxy.conf``:

.. code-block:: shell

    [Service]
    Environment="HTTP_PROXY=http://example_url:example_port/"
    Environment="HTTPS_PROXY=https://example_url:example_port/"

.. code-block:: shell

    sudo systemctl daemon-reload
    sudo systemctl restart docker.service