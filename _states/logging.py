# -*- coding: utf-8 -*-
'''
Logging output
==========================
:maintainer: Joe Julian <me@joejulian.name>
:maturity: new
:platform: Linux
.. versionadded:: 2014.7.0
:configuration: See :py:mod:`salt.modules.logging` for setup instructions.
.. code-block:: yaml
    debugmyvar:
        logger.debug:
            - name: myvar
            - string: "myvar is :"
'''

__virtual_name__ = 'logging'

def __virtual__():
    return __virtual_name__

def debug(name, obj, string = ''):
    ret = {'name': name,
           'changes': {},
           'result': True,
           'comment': __salt__['logger.debug'](obj, string)}
    return ret

def info(name, obj, string = ''):
    ret = {'name': name,
           'changes': {},
           'result': True,
           'comment': __salt__['logger.info'](obj, string)}
    return ret

def warning(name, obj, string = ''):
    ret = {'name': name,
           'changes': {},
           'result': True,
           'comment': __salt__['logger.warning'](obj, string)}
    return ret

def error(name, obj, string = ''):
    ret = {'name': name,
           'changes': {},
           'result': True,
           'comment': __salt__['logger.error'](obj, string)}
    return ret

def critical(name, obj, string = ''):
    ret = {'name': name,
           'changes': {},
           'result': True,
           'comment': __salt__['logger.critical'](obj, string)}
    return ret
