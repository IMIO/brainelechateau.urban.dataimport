from brainelechateau.urban.dataimport.csv.mappers import *
from imio.urban.dataimport.mapper import SimpleMapper

OBJECTS_NESTING = [
    (
        'LICENCE', [
            ('CONTACT', []),
            ('PARCEL', []),
            # ('DEPOSIT EVENT 1', []),
            ('DECISION EVENT', []),
            # ('DOCUMENTS', []),
        ],
    ),
]

FIELDS_MAPPINGS = {
    'LICENCE':
    {
        'factory': [LicenceFactory],

        'mappers': {
            SimpleMapper: (
                {
                    'from': 'ref',
                    'to': 'referenceDGATLP',
                },
            ),

            IdMapper: {
                'from': 'id',
                'to': 'id',
            },

            PortalTypeMapper: {
                'from': 'Type',
                'to': ('portal_type', 'folderCategory',)
            },

            LicenceSubjectMapper: {
                'from': ('Genre de Travaux', 'Divers'),
                'to': 'licenceSubject',
            },

            WorklocationMapper: {
                'from': ('Adresse', 'num'),
                'to': 'workLocations',
            },

           ArchitectMapper: {
               'allowed_containers': ['BuildLicence'],
               'from': ('Architecte',),
               'to': ('architects',)
           },

            # WorkTypeMapper: {
            #     'allowed_containers': ['BuildLicence', 'ParcelOutLicence'],
            #     'from': 'Code_220+',
            #     'to': 'workType',
            # },

            # InquiryStartDateMapper: {
            #     'allowed_containers': ['BuildLicence', 'ParcelOutLicence', 'UrbanCertificateTwo'],
            #     'from': 'E_Datdeb',
            #     'to': 'investigationStart',
            # },
            #
            # InquiryEndDateMapper: {
            #     'allowed_containers': ['BuildLicence', 'ParcelOutLicence', 'UrbanCertificateTwo'],
            #     'from': 'E_Datfin',
            #     'to': 'investigationEnd',
            # },
            #
            # InquiryReclamationNumbersMapper: {
            #     'allowed_containers': ['BuildLicence', 'ParcelOutLicence', 'UrbanCertificateTwo'],
            #     'from': 'NBRec',
            #     'to': 'investigationWriteReclamationNumber',
            # },
            #
            # InquiryArticlesMapper: {
            #     'allowed_containers': ['BuildLicence', 'ParcelOutLicence', 'UrbanCertificateTwo'],
            #     'from': 'Enquete',
            #     'to': 'investigationArticles',
            # },
            #
            # ObservationsMapper: {
            #     'from': 'Memo_Urba',
            #     'to': 'description',
            # },
            #
            # TechnicalConditionsMapper: {
            #     'from': ('memo_Autorisation', 'memo_Autorisation2'),
            #     'to': 'locationTechnicalConditions',
            # },

#            GeometricianMapper: {
#                'allowed_containers': ['ParcelOutLicence'],
#                'from': ('Titre', 'Nom', 'Prenom'),
#                'to': ('geometricians',)
#            },

            # ParcellingsMapper: {
            #     'table': 'LOTISSEM',
            #     'KEYS': ('Cle_Urba', 'Cle_Lot'),
            #     'mappers': {
            #         SimpleMapper: (
            #             {
            #                 'from': 'Lot',
            #                 'to': 'subdivisionDetails',
            #             },
            #         ),
            #         ParcellingUIDMapper: {
            #             'from': 'Lotis',
            #             'to': 'parcellings',
            #         },
            #
            #         IsInSubdivisionMapper: {
            #             'from': 'Lotis',
            #             'to': 'isInSubdivision',
            #         }
            #     },
            # },
            #
            # PcaMapper: {
            #     'table': 'PPA',
            #     'KEYS': ('Cle_Urba', 'Cle_PPA'),
            #     'mappers': {
            #         SimpleMapper: (
            #             {
            #                 'from': 'PPA_Affectation',
            #                 'to': 'pcaDetails',
            #             },
            #         ),
            #         PcaUIDMapper: {
            #             'from': 'PPA',
            #             'to': 'pca',
            #         },
            #
            #         IsInPcaMapper: {
            #             'from': 'PPA',
            #             'to': 'isInPCA',
            #         }
            #     },
            # },

            # EnvRubricsMapper: {
            #     'allowed_containers': ['EnvClassOne', 'EnvClassTwo', 'EnvClassThree'],
            #     'from': 'LibNat',
            #     'to': 'description',
            # },
            #
            CompletionStateMapper: {
                'from': 'date permis',
                'to': (),  # <- no field to fill, its the workflow state that has to be changed
            },

            ErrorsMapper: {
                'from': (),
                'to': ('description',),  # log all the errors in the description field
            }
        },
    },

    'PARCEL':
    {
        'factory': [ParcelFactory, {'portal_type': 'PortionOut'}],

        'mappers': {
            ParcelDataMapper: {
                'from': ('num parcelle', 'Sect', 'Div'),
                'to': (),
            },
        },
    },

    'CONTACT':
    {
        'factory': [ContactFactory],

        'mappers': {
            SimpleMapper: (
                {
                    'from': 'Nom',
                    'to': 'name1',
                },
                {
                    'from': ('num'),
                    'to': 'number',
                },
                {
                    'from': ('Adresse'),
                    'to': 'street',
                },
            ),

            ContactIdMapper: {
                'from': ('Nom', 'ref'),
                'to': 'id',
            },
        },
    },

    'DECISION EVENT':
    {
        'factory': [UrbanEventFactory],

        'mappers': {
            DecisionEventTypeMapper: {
                'from': (),
                'to': 'eventtype',
            },

            DecisionEventIdMapper: {
                'from': (),
                'to': 'id',
            },

            DecisionEventDateMapper: {
                'from': 'date permis',
                'to': 'decisionDate',
            },

            DecisionEventDecisionMapper: {
                'from': 'date permis',
                'to': 'decision',
            },

            DecisionEventNotificationDateMapper: {
                'from': 'date permis',
                'to': 'eventDate',
            }
        },
    },
}