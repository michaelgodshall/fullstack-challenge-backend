============================
New Developer Setup
============================
This guide assumes you are running the latest version of OSX on a Mac.


Install Xcode Command Line Tools
============================
If you haven't installed Xcode or the Xcode Command Line Tools, please, choose one of the following options.

1. Install Xcode from the App Store.  Search for "xcode" and it should be the first result.

OR

2. Install the Xcode Command Line Tools via Terminal.

Open the Termial App.

Install Xcode Command Line Tools::

    $ xcode-select --install

A window will popup.  Click "Install" to download and install Xcode Command Line Tools.


Install Python
============================
More detailed instructions can be found at http://docs.python-guide.org/en/latest/starting/install/osx/

Open the Terminal app

Install Homebrew::

    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Open your shell startup file (.profile) in your root user directory using a text editor of your choice::

    $ subl ~/.profile

Add the following line to .profile and save the file::

    export PATH=/usr/local/bin:/usr/local/sbin:$PATH

Back in Terminal, reload your startup file::

    $ source ~/.profile

Install Python 3::

    $ brew update
    $ brew install python3


Install Virtualenv and Virtualenvwrapper
============================

Install virtualenv::

    $ pip install virtualenv

Install virtualenvwrapper::

    $ pip install virtualenvwrapper

Open your shell startup file (.profile) in your root user directory using a text editor of your choice::

    $ subl ~/.profile

Add the following lines and save the file::

    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh

Back in Terminal, reload your startup file::

    $ source ~/.profile


Install Node
============================
Install Node::

    $ brew install node

Install gulp-cli globally::

    $ npm install -g gulp-cli


Install Redis
============================
Install Redis via Homebrew::

    $ brew update
    $ brew install redis

Read the "Caveats" output from the installation for additional instructions.

This is what my redis installation recommended for starting redis at login (double check your instructions before copying and pasting)::

    $ ln -sfv /usr/local/opt/redis/*.plist ~/Library/LaunchAgents

This is what my redis installation recommended to launch redis now (double check your instructions before copying and pasting)::

    $ launchctl load ~/Library/LaunchAgents/homebrew.mxcl.redis.plist
