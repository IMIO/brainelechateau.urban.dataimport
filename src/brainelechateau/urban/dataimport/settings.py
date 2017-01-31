# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm
from imio.urban.dataimport.agorawin.settings import AgorawinImporterFromImportSettings


class BrainelechateauImporterSettingsForm(ImporterSettingsForm):
    """ """

class BrainelechateauImporterSettings(ImporterSettings):
    """ """
    form = BrainelechateauImporterSettingsForm


class BrainelechateauImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = BrainelechateauImporterSettings


class BrainelechateauImporterFromImportSettings(AgorawinImporterFromImportSettings):
    """ """

    def get_importer_settings(self):
        """
        Return the db name to read.
        """
        settings = super(BrainelechateauImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'db_name': '',
        }

        settings.update(db_settings)

        return settings
