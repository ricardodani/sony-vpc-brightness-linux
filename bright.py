# -*- encoding: utf-8 -*-

# Author: Ricardo Dani
# github.com/ricardodani
# ricardodani@gmail.com

'''
Class to change brightness in Sony VPC Series notebook`s in Linux.

    >>> b = Brightness()
    >>> b.set_max() # set the brightness to 100%
    >>> b.set_min() # set the brightness to 10%
    >>> b.set_up() # plus the brigthness to 15% (5% step)
    >>> b.set(96) # plus the brigthness to 96%
    >>> b.set_up() # not possible change to 101%
    Wrong percentage. Must be > 10% and < 100%.
    >>> b.set_down() # set the brightness to 91%
    >>> b.set(10) # set the brightness to 10%
    >>> b.set_down() # not possible change to 5%
    Wrong percentage. Must be > 10% and < 100%.
    >>> type(b.max_bright) == type(1)
    True
    >>> b.set(90, True)
    Setted percentage to 90%.
    >>> 
'''

import commands

_COMMANDS = {
    'max': 'cat /sys/class/backlight/intel_backlight/max_brightness',
    'change': 'echo %d| tee /sys/class/backlight/intel_backlight/brightness',
    'actual': 'cat /sys/class/backlight/intel_backlight/brightness'
}
_MIN_BRIGHT_RATIO = 0.1
_STEP = 0.05

class Brightness(object):
    
    def __init__(self):
        self._output = []
        self._max = self._get_max_bright()
        self._min = self._get_min_bright()

    def _get_last_output(self):
        return self._output[-1]

    def _get_max_bright(self):
        return int(self._execute_command(_COMMANDS['max']))

    def _get_min_bright(self):
        return int(self._max * _MIN_BRIGHT_RATIO)

    def _get_current_bright(self):
        return int(self._execute_command(_COMMANDS['actual']))

    def _execute_command(self, command, verbose=False):
        self._output.append(commands.getoutput(command))
        if verbose:
            print _get_last_output()
        return self._get_last_output()

    @property
    def max_bright(self):
        return self._max

    @property
    def min_bright(self):
        return self._min

    @property
    def history(self):
        return '\n'.join(self._output[::-1])

    @property
    def actual_bright(self):
        return self._get_current_bright()

    def set_up(self):
        actual_ratio = (self.actual_bright / float(self.max_bright))
        self.set(100 * (actual_ratio + _STEP))

    def set_down(self):
        actual_ratio = (self.actual_bright / float(self.max_bright))
        self.set(100 * (actual_ratio - _STEP))

    def set_min(self):
        self.set(int(100 * _MIN_BRIGHT_RATIO))

    def set_max(self):
        self.set(100)
        
    def set(self, percent, verbose=False):
        min_bright = 100 * _MIN_BRIGHT_RATIO
        if (min_bright) <= percent <= 100:
            bright = int(self._max * (percent/100.))
            self._execute_command(_COMMANDS['change'] % bright)
            if verbose:
                print 'Setted percentage to %d%%.' % percent
        else:
            print 'Wrong percentage. Must be > %d%% and < 100%%.' % min_bright

if __name__ == '__main__':
    b = Brightness()
