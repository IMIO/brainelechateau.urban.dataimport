# -*- coding: utf-8 -*-
"""Init and utils."""

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('brainelechateau.urban.dataimport')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
