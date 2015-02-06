# -*- coding: utf-8 -*-
'''
Execution module to provide logging
==========================
:maintainer: Joe Julian <me@joejulian.name>
:maturity: new
:platform: Linux
.. versionadded:: 2014.7.0
'''

__virtualname__ = 'logger'

import logging as log
from pprint import pformat
import json
import yaml

def pretty(var):
    return pformat(yaml.load(json.dumps(var)))

def __virtual__():
    return __virtualname__

def debug(var, string = ""):
    '''
    Print a var to a debug output.
    '''
    ret = string + pretty(var)
    log.debug(ret)
    return ret

def info(var, string = ""):
    '''
    Print a var to a info output.
    '''
    ret = string + pretty(var)
    log.info(ret)
    return ret

def warning(var, string = ""):
    '''
    Print a var to a warning output.
    '''
    ret = string + pretty(var)
    log.warning(ret)
    return ret

def error(var, string = ""):
    '''
    Print a var to a error output.
    '''
    ret = string + pretty(var)
    log.error(ret)
    return ret

def critical(var, string = ""):
    '''
    Print a var to a critical output.
    '''
    ret = string + pretty(var)
    log.critical(ret)
    return ret
