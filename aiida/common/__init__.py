# -*- coding: utf-8 -*-
###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida_core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################
"""Internal functionality that is needed by multiple modules of AiiDA"""
import logging
import sys


aiidalogger = logging.getLogger("aiida")
# aiidalogger.addHandler(logging.StreamHandler(sys.stderr))
#FORMAT = '[%(name)s@%(levelname)s] %(message)s'
#logging.basicConfig(format=FORMAT)
