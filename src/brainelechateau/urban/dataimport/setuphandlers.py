# -*- coding: utf-8 -*-


def isNotCurrentProfile(context):
    return context.readDataFile("brainelechateauurbandataimport_marker.txt") is None


def post_install(context):
    """Post install script"""
    if isNotCurrentProfile(context): return
    portal = context.getSite()
