#!/usr/bin/env python
from pkg_resources import resource_filename
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read(resource_filename(__name__, 'config.ini'))