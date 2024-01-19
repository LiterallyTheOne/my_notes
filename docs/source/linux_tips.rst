Linux tips
==========

Add a ``user`` to a ``group``
-----------------------------

.. code-block:: shell

    sudo usermod -aG group user

Remove a ``user`` from a ``group``
----------------------------------

.. code-block:: shell

    sudo gpasswd --delete user group

See all the groups with their users
-----------------------------------

.. code-block:: shell

    sudo vim /etc/group

Format a partition to ext4
--------------------------

.. code-block:: shell

    sudo mkfs -t ext4 /dev/sdxn

    # example:
    sudo mkfs -t ext4 /dev/sdb1
