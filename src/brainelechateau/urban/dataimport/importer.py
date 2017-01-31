# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.agorawin.importer import AgorawinDataImporter
from brainelechateau.urban.dataimport.interfaces import IBrainelechateauDataImporter


class BrainelechateauDataImporter(AgorawinDataImporter):
    """ """

    implements(IBrainelechateauDataImporter)
