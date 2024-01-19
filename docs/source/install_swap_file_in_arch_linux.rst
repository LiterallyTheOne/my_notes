Install swap file in arch linux
===============================

.. code-block:: shell

    sudo dd if=/dev/zero of=/swapfile bs=1M count=8k status=progress
    sudo chmod 0600 /swapfile
    sudo mkswap -U clear /swapfile
    sudo swapon /swapfile

then in file ``/etc/fstab`` add:

.. code-block:: text

    /swapfile none swap defaults 0 0

