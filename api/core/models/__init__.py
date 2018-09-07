# -*- coding: utf-8 -*-
"""
Initializing db in api.models.base instead of in api.__init__.py  to prevent
circular dependencies

@author: NikolaLohinski (https://github.com/NikolaLohinski)
@date: 02/02/09
"""
from .Invention import Invention
from .base import db
