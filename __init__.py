# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from picking_list_report import PickingListReport


def register():
    Pool.register(
        PickingListReport,
        module='picking_list_report', type_='report'
    )
