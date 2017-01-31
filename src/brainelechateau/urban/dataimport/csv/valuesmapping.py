# -*- coding: utf-8 -*-

from imio.urban.dataimport.mapping import table

VALUES_MAPS = {

    'division_map': {
        'I': '1',
        'II': '2',
        'III': '3',
        'IV': '4',
        'V': '5',
        'VI': '6',
    },

    'eventtype_id_map': table({
        'header'             : ['decision_event'],
        'BuildLicence'       : ['delivrance-du-permis-octroi-ou-refus'],
        'ParcelOutLicence'   : ['delivrance-du-permis-octroi-ou-refus'],
        'Declaration'        : ['deliberation-college'],
        'UrbanCertificateOne': ['octroi-cu1'],
        'UrbanCertificateTwo': ['octroi-cu2'],
        'MiscDemand'         : ['deliberation-college'],
        'EnvClassOne'        : ['decision'],
        'EnvClassTwo'        : ['desision'],
        'EnvClassThree'      : ['acceptation-de-la-demande'],
    }),
}