# -*- coding: iso-8859-1 -*-
"""
MoinMoin - test wiki configuration

@copyright: 2000-2004 by Juergen Hermann <jh@web.de>
@license: GNU GPL, see COPYING for details.
"""

import os

from MoinMoin.config.multiconfig import DefaultConfig


class Config(DefaultConfig):
    sitename = u'Developer Test Wiki'
    logo_string = sitename

    _base_dir = os.path.join(os.path.dirname(__file__), 'wiki')
    data_dir = os.path.join(_base_dir, "data")
    data_underlay_dir = os.path.join(_base_dir, "underlay")

    show_hosts = 1
    # used to check if it is really a wiki we may modify
    is_test_wiki = True
