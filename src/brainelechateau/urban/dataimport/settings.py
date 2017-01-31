# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm


class BrainelechateauImporterSettingsForm(ImporterSettingsForm):
    """ """

class BrainelechateauImporterSettings(ImporterSettings):
    """ """
    form = BrainelechateauImporterSettingsForm


class BrainelechateauImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = BrainelechateauImporterSettings


