sony-vpc-brightness-linux
=========================

Class to change brightness in Sony VPC Series notebook`s in Linux.

How it works:
-------------

To change the brightness of the monitor in SONY VAIO VPC series notebooks in Linux, this script
changes the value of the file '/sys/class/backlight/intel_backlight/brightness' to a value between
the value of '/sys/class/backlight/intel_backlight/max_brightness' and 10% of it.

To facilitate this, the script use percentage values to abstract the real values. You can use
max, min, up and down functions.


How to test:
-------------

    $ python -m doctest bright.py

How you can improove it?
-------------

The final goal is to associate this scripts to the Brightness hotkeys of the Enviroment (Gnome, KDE, xfce, etc).
If you know how to do it, please, help us ;)

Usage:
-------------

    $ sudo ./bright.py 50
    $ sudo ./bright.py up
    $ sudo ./bright.py down
    $ sudo ./bright.py max
    $ sudo ./bright.py min


TODO:
-------------

- Make shell commands
- Ask for credentials if needed.
- Alert if the user dont have privilege to write in the config file.

Known bugs
-------------

- If you execute without a privilege to the config file, nothing happens.
