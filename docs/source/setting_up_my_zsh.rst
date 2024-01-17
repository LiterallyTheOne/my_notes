Setting up my zsh
=================

install zsh
-----------

in Arch linux:

.. code-block:: shell

    sudo pacman -S zsh

in Ubuntu:

.. code-block:: shell

    sudo apt update
    sudo apt install zsh

install oh-my-zsh
-----------------

.. code-block::

    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

.. note::

    source: https://ohmyz.sh/#install

install powerlevel10k
---------------------

Download and install these fonts:

* `MesloLGS NF Regular.ttf <https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf>`_
* `MesloLGS NF Bold.ttf <https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf>`_
* `MesloLGS NF Italic.ttf <https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf>`_
* `MesloLGS NF Bold Italic.ttf <https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf>`_

then:

.. code-block:: shell

    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

After that make a change in ``~/.zshrc``:

.. code-block::

    ZSH_THEME="powerlevel10k/powerlevel10k"

.. note::

    source: https://github.com/romkatv/powerlevel10k

install zsh-syntax-highlighting
-------------------------------

.. code-block::

    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

Then add ``zsh-syntax-highlighting``
to ``plugins`` in ``~/.zshrc``.

.. note::

    source: https://github.com/zsh-users/zsh-syntax-highlighting

install zsh-autosuggestions
---------------------------

.. code-block::

    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

Then add ``zsh-autosuggestions`` to ``plugins`` in ``~/.zshrc``.

.. note::

    source: https://github.com/zsh-users/zsh-autosuggestions

install zsh-vi-mode
-------------------

.. code-block::

    git clone https://github.com/jeffreytse/zsh-vi-mode $ZSH_CUSTOM/plugins/zsh-vi-mode

Then add ``zsh-vi-mode`` to ``plugins`` in ``~/.zshrc``.

.. note::

    source: https://github.com/jeffreytse/zsh-vi-mode

plugins after all steps in ``~/.zshrc``
---------------------------------------

.. code-block:: text

    plugins=(
        git
        zsh-autosuggestions
        zsh-syntax-highlighting
        zsh-vi-mode
    )





