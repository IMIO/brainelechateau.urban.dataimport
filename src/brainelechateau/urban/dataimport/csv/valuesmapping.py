# -*- coding: utf-8 -*-

from imio.urban.dataimport.mapping import table

VALUES_MAPS = {

    'eventtype_id_map': table({
        'header'             : ['decision_event', 'college_report_event'],
        'BuildLicence'       : ['delivrance-du-permis-octroi-ou-refus', 'rapport-du-college'],
        'ParcelOutLicence'   : ['delivrance-du-permis-octroi-ou-refus', ''],
        'Declaration'        : ['deliberation-college', ''],
        'UrbanCertificateOne': ['octroi-cu1', ''],
        'UrbanCertificateTwo': ['octroi-cu2', ''],
        'MiscDemand'         : ['deliberation-college', ''],
        'EnvClassOne'        : ['decision', ''],
        'EnvClassTwo'        : ['desision', ''],
        'EnvClassThree'      : ['acceptation-de-la-demande', ''],
    }),

    'solicitOpinionDictionary': {
               '1' :        "service-technique-provincial", #Avis Service technique provincial
               '2' :        "direction-des-cours-deau", #Avis Dir Cours d'eau
               '3' :        "pi", #Avis Zone de secours
               '4' :        "ores", #Avis ORES
               '5' :        "cibe", #Avis Vivaqua
               '6' :        "agriculture", #Avis Dir Développement rural
               '7' :        "dnf", #Avis Département Nature et Forêts
               '8' :        "forces-armees", #Avis Forces armées
               '9' :        "spw-dgo1", #Avis Dir Routes BW
               '10':        "swde", #Avis SWDE/IECBW
               '11':        "belgacom", #Avis PROXIMUS
               '12':        "infrabel", #Avis TEC
               '13':        "ibw", #Avis IBW
               '14':        "voo", #Avis VOO
               '15':        "bec", #Avis Service technique communal
               '16':        "ccatm", #Avis CCATM
            },

    'zoneDictionary': {
           "zone d'habitat à caractère rural"                                      : 'zhcr'                                         ,
           "zone agricole"                                                         : 'za'                                           ,
           "zone agricole d'intérêt paysager"                                      : 'zone-agricole-dinteret-paysager'              ,
           "zone d'activité économique industrielle"                               : 'zaei'                                         ,
           "zone d'activité économique industrielle (Wauthier-Braine)"             : 'zaei'                                         ,
           "zone d'activité économique mixte"                                      : 'zaem'                                         ,
           "zone d'aménagement communal concerté"                                  : 'zone-damenagement-communal-concerte'          ,
           "zone d'aménagement différé"                                            : 'zone-damenagement-differe'                    ,
           "zone d'espaces verts"                                                  : 'zev'                                          ,
           "zone d'espaces verts d'intérêt paysager"                               : 'zone-despaces-verts-dinteret-paysager'        ,
           "zone d'extraction"                                                     : 'ze'                                           ,
           "zone d'extraction sur fond de zone agricole"                           : 'zone-dextraction-sur-fond-de-zone-agricole'   ,
           "zone d'habitat"                                                        : 'zh'                                           ,
           "zone de loisirs"                                                       : 'zl'                                           ,
           "zone de parc"                                                          : 'zp'                                           ,
           "zone de parc d'intérêt paysager"                                       : 'zone-de-parc-dinteret-paysager'               ,
           "zone de services publics et d'équipements communautaires"              : 'zspec'                                        ,
           "zone forestière"                                                       : 'zf'                                           ,
           "zone forestière d'intérêt paysager"                                    : 'zone-forestiere-dinteret-paysager'            ,
           "zone non affectée"                                                     : 'zone-non-affectee'                            ,
    },

}