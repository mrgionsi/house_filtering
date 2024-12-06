from datetime import date
import logging
import json
import requests
import time

from manage import JsonObject, addEntry


data = """{
    "count": 1524,
    "totalAds": 1524,
    "isResultsLimitReached": false,
    "results": [
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 102119372,
                "uuid": "9e3ad866-a9e9-58d9-abf3-6a33daacf0ac",
                "advertiser": {
                    "agency": {
                        "id": 121262,
                        "type": "agency",
                        "showOnlyAgentPhone": false,
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "bookableVisit": {
                            "isVisitBookable": true,
                            "virtualVisitEnabled": false
                        },
                        "isPaid": true,
                        "label": "agenzia",
                        "displayName": "Studiocasa",
                        "guaranteed": false,
                        "showAgentPhone": false,
                        "showLogo": true,
                        "imageUrls": {
                            "small": "https://pic.im-cdn.it/imagenoresize/583544570.jpg",
                            "large": "https://pic.im-cdn.it/imagenoresize/583544572.jpg"
                        },
                        "agencyUrl": "https://www.immobiliare.it/agenzie-immobiliari/121262/studiocasa-recale/"
                    },
                    "supervisor": {
                        "type": "agent",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "imageType": "agent",
                        "displayName": "Venere Errico",
                        "label": "agente immobiliare"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 110000,
                    "formattedValue": "€ 110.000",
                    "priceRange": "100.001 - 150.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1301525458,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1301525458/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1301525764,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1301525764/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1301525926,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1301525926/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1301526078,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1301526078/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1301526306,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1301526306/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1301526490,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1301526490/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1301526670,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1301526670/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1301526974,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1301526974/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "floor": {
                            "abbreviation": "R",
                            "value": "Piano rialzato",
                            "floorOnlyValue": "piano rialzato",
                            "ga4FloorValue": "piano rialzato"
                        },
                        "price": {
                            "visible": true,
                            "value": 110000,
                            "formattedValue": "€ 110.000",
                            "priceRange": "100.001 - 150.000 &euro;"
                        },
                        "surface": "100 m²",
                        "typology": {
                            "id": 14,
                            "name": "Appartamento"
                        },
                        "typologyGA4Translation": "Appartamento",
                        "ga4features": [],
                        "caption": "SEMINDIPENDENTE IN CENTRO",
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "photo": {
                            "id": 1301525458,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1301525458/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1301525458/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1301525458/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1301525458/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.0546,
                            "longitude": 14.2995,
                            "marker": "no_map",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Recale",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "surface",
                                "label": "100 m²"
                            },
                            {
                                "type": "floor",
                                "label": "Piano R",
                                "compactLabel": "R"
                            }
                        ]
                    }
                ],
                "title": "Appartamento 100 m², Recale",
                "type": "ad",
                "typology": {
                    "id": 14,
                    "name": "Appartamento"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Appartamento 100 m², Recale",
                "title": "Appartamento 100 m², Recale",
                "metaTitle": "Vendita Appartamento  Recale, rif. 102119372",
                "url": "https://www.immobiliare.it/annunci/102119372/"
            },
            "idGeoHash": "sr61t3u8"
        },
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 102322452,
                "uuid": "85d5fa3b-f2af-51d2-b00f-6b6e8c86eb06",
                "advertiser": {
                    "agency": {
                        "id": 121262,
                        "type": "agency",
                        "showOnlyAgentPhone": false,
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "bookableVisit": {
                            "isVisitBookable": true,
                            "virtualVisitEnabled": false
                        },
                        "isPaid": true,
                        "label": "agenzia",
                        "displayName": "Studiocasa",
                        "guaranteed": false,
                        "showAgentPhone": false,
                        "showLogo": true,
                        "imageUrls": {
                            "small": "https://pic.im-cdn.it/imagenoresize/583544570.jpg",
                            "large": "https://pic.im-cdn.it/imagenoresize/583544572.jpg"
                        },
                        "agencyUrl": "https://www.immobiliare.it/agenzie-immobiliari/121262/studiocasa-recale/"
                    },
                    "supervisor": {
                        "type": "agent",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "imageType": "agent",
                        "displayName": "Venere Errico",
                        "label": "agente immobiliare"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 220000,
                    "formattedValue": "€ 220.000",
                    "priceRange": "200.001 - 300.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1309814412,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1309814412/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1309814440,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1309814440/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1309814480,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1309814480/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1309814512,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1309814512/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1309814546,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1309814546/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1309814578,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1309814578/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1309814604,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1309814604/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1309814626,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1309814626/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1309814644,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1309814644/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1309814656,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1309814656/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1309814678,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1309814678/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1309814688,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1309814688/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1309814700,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1309814700/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1309814710,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1309814710/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "floor": {
                            "abbreviation": null,
                            "value": "Piano rialzato",
                            "floorOnlyValue": "piano rialzato",
                            "ga4FloorValue": "piano rialzato"
                        },
                        "price": {
                            "visible": true,
                            "value": 220000,
                            "formattedValue": "€ 220.000",
                            "priceRange": "200.001 - 300.000 &euro;"
                        },
                        "surface": "10 m²",
                        "typology": {
                            "id": 23,
                            "name": "Villa unifamiliare"
                        },
                        "typologyGA4Translation": "Villa",
                        "ga4features": [],
                        "caption": "VILLA NEL QUARTIERE CANTONE",
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "photo": {
                            "id": 1309814412,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1309814412/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1309814412/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1309814412/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1309814412/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.0371,
                            "longitude": 14.2995,
                            "marker": "no_map",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Marcianise",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "surface",
                                "label": "10 m²"
                            }
                        ]
                    }
                ],
                "title": "Villa unifamiliare 10 m², Marcianise",
                "type": "ad",
                "typology": {
                    "id": 23,
                    "name": "Villa unifamiliare"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Villa unifamiliare 10 m², Marcianise",
                "title": "Villa unifamiliare 10 m², Marcianise",
                "metaTitle": "Vendita Villa unifamiliare  Marcianise. 10 m², rif. 102322452",
                "url": "https://www.immobiliare.it/annunci/102322452/"
            },
            "idGeoHash": "sr61mqsd"
        },
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 110001747,
                "uuid": "147af305-c676-53cd-b2b7-072075039b45",
                "advertiser": {
                    "agency": {
                        "id": 13184,
                        "type": "agency",
                        "showOnlyAgentPhone": false,
                        "phones": [
                            {
                                "type": "vTel1",
                                "value": "0823 136 1738"
                            }
                        ],
                        "bookableVisit": {
                            "isVisitBookable": true,
                            "virtualVisitEnabled": false
                        },
                        "isPaid": true,
                        "label": "agenzia",
                        "displayName": "Mediatec servizi immobiliari",
                        "guaranteed": false,
                        "showAgentPhone": false,
                        "showLogo": true,
                        "imageUrls": {
                            "small": "https://pic.im-cdn.it/imagenoresize/1171131838.jpg",
                            "large": "https://pic.im-cdn.it/imagenoresize/1171131840.jpg"
                        },
                        "agencyUrl": "https://www.immobiliare.it/agenzie-immobiliari/13184/mediatec-casagiove/"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 60000,
                    "formattedValue": "€ 60.000",
                    "priceRange": "fino a 100.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [],
                            "virtualTours": [],
                            "hasMultimedia": false
                        },
                        "bathrooms": "1",
                        "floor": {
                            "abbreviation": "3",
                            "value": "3°",
                            "floorOnlyValue": "3",
                            "ga4FloorValue": "3"
                        },
                        "ga4Condition": "Buono / Abitabile",
                        "price": {
                            "visible": true,
                            "value": 60000,
                            "formattedValue": "€ 60.000",
                            "priceRange": "fino a 100.000 &euro;"
                        },
                        "rooms": "2",
                        "surface": "60 m²",
                        "typology": {
                            "id": 16,
                            "name": "Mansarda"
                        },
                        "ga4Garage": "1 in box privato/box in garage",
                        "typologyGA4Translation": "Attico - Mansarda",
                        "ga4features": [
                            "terrazzo"
                        ],
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "bedRoomsNumber": "1",
                        "location": {
                            "latitude": 41.0776,
                            "longitude": 14.291,
                            "marker": "no_map",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Casapulla",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "rooms",
                                "label": "2 locali",
                                "compactLabel": "2"
                            },
                            {
                                "type": "surface",
                                "label": "60 m²"
                            },
                            {
                                "type": "bathrooms",
                                "label": "1 bagno",
                                "compactLabel": "1"
                            },
                            {
                                "type": "floor",
                                "label": "Piano 3",
                                "compactLabel": "3"
                            },
                            {
                                "type": "elevator",
                                "label": "No Ascensore",
                                "compactLabel": "No"
                            },
                            {
                                "type": "terrace",
                                "label": "Terrazzo"
                            }
                        ]
                    }
                ],
                "title": "Mansarda buono stato, 60 m², Casapulla",
                "type": "ad",
                "typology": {
                    "id": 16,
                    "name": "Mansarda"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Mansarda buono stato, 60 m², Casapulla",
                "title": "Mansarda buono stato, 60 m², Casapulla",
                "metaTitle": "Vendita Mansarda  Casapulla. Buono stato, posto auto, con terrazza, rif. 110001747",
                "url": "https://www.immobiliare.it/annunci/110001747/"
            },
            "idGeoHash": "sr61tjyq"
        },
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 102365386,
                "uuid": "45434055-e451-56db-8088-58b207f125c7",
                "advertiser": {
                    "agency": {
                        "id": 121262,
                        "type": "agency",
                        "showOnlyAgentPhone": false,
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "bookableVisit": {
                            "isVisitBookable": true,
                            "virtualVisitEnabled": false
                        },
                        "isPaid": true,
                        "label": "agenzia",
                        "displayName": "Studiocasa",
                        "guaranteed": false,
                        "showAgentPhone": false,
                        "showLogo": true,
                        "imageUrls": {
                            "small": "https://pic.im-cdn.it/imagenoresize/583544570.jpg",
                            "large": "https://pic.im-cdn.it/imagenoresize/583544572.jpg"
                        },
                        "agencyUrl": "https://www.immobiliare.it/agenzie-immobiliari/121262/studiocasa-recale/"
                    },
                    "supervisor": {
                        "type": "agent",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "imageType": "agent",
                        "displayName": "Venere Errico",
                        "label": "agente immobiliare"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 70000,
                    "formattedValue": "€ 70.000",
                    "priceRange": "fino a 100.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1311201184,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1311201184/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1311201212,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1311201212/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1311201230,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1311201230/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1311201258,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1311201258/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1311201284,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1311201284/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1311201326,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1311201326/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1311201384,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1311201384/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "floor": {
                            "abbreviation": "1",
                            "value": "1°",
                            "floorOnlyValue": "1",
                            "ga4FloorValue": "1"
                        },
                        "price": {
                            "visible": true,
                            "value": 70000,
                            "formattedValue": "€ 70.000",
                            "priceRange": "fino a 100.000 &euro;"
                        },
                        "surface": "100 m²",
                        "typology": {
                            "id": 14,
                            "name": "Appartamento"
                        },
                        "typologyGA4Translation": "Appartamento",
                        "ga4features": [],
                        "caption": "APPARTAMENTO  DUPLEX",
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "photo": {
                            "id": 1311201184,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1311201184/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1311201184/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1311201184/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1311201184/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.0418,
                            "longitude": 14.3074,
                            "marker": "no_map",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Capodrise",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "surface",
                                "label": "100 m²"
                            },
                            {
                                "type": "floor",
                                "label": "Piano 1",
                                "compactLabel": "1"
                            }
                        ]
                    }
                ],
                "title": "Appartamento 100 m², Capodrise",
                "type": "ad",
                "typology": {
                    "id": 14,
                    "name": "Appartamento"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Appartamento 100 m², Capodrise",
                "title": "Appartamento 100 m², Capodrise",
                "metaTitle": "Vendita Appartamento  Capodrise, rif. 102365386",
                "url": "https://www.immobiliare.it/annunci/102365386/"
            },
            "idGeoHash": "sr61mx6m"
        },
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 102229664,
                "uuid": "2b4077f9-2d5a-563a-84a6-61f6ce1420b0",
                "advertiser": {
                    "agency": {
                        "id": 121262,
                        "type": "agency",
                        "showOnlyAgentPhone": false,
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "bookableVisit": {
                            "isVisitBookable": true,
                            "virtualVisitEnabled": false
                        },
                        "isPaid": true,
                        "label": "agenzia",
                        "displayName": "Studiocasa",
                        "guaranteed": false,
                        "showAgentPhone": false,
                        "showLogo": true,
                        "imageUrls": {
                            "small": "https://pic.im-cdn.it/imagenoresize/583544570.jpg",
                            "large": "https://pic.im-cdn.it/imagenoresize/583544572.jpg"
                        },
                        "agencyUrl": "https://www.immobiliare.it/agenzie-immobiliari/121262/studiocasa-recale/"
                    },
                    "supervisor": {
                        "type": "agent",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "imageType": "agent",
                        "displayName": "Venere Errico",
                        "label": "agente immobiliare"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 190000,
                    "formattedValue": "€ 190.000",
                    "priceRange": "150.001 - 200.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1306081184,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1306081184/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1306081186,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1306081186/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1306081188,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1306081188/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1306081190,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1306081190/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1306081192,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1306081192/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1306081194,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1306081194/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1306081196,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1306081196/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "floor": {
                            "abbreviation": null,
                            "value": "Piano rialzato",
                            "floorOnlyValue": "piano rialzato",
                            "ga4FloorValue": "piano rialzato"
                        },
                        "price": {
                            "visible": true,
                            "value": 190000,
                            "formattedValue": "€ 190.000",
                            "priceRange": "150.001 - 200.000 &euro;"
                        },
                        "surface": "210 m²",
                        "typology": {
                            "id": 23,
                            "name": "Villa unifamiliare"
                        },
                        "typologyGA4Translation": "Villa",
                        "ga4features": [],
                        "caption": "INDIPENDENTE CON CORTILE",
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "photo": {
                            "id": 1306081184,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1306081184/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1306081184/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1306081184/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1306081184/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.0546,
                            "longitude": 14.2995,
                            "marker": "no_map",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Recale",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "surface",
                                "label": "210 m²"
                            }
                        ]
                    }
                ],
                "title": "Villa unifamiliare 210 m², Recale",
                "type": "ad",
                "typology": {
                    "id": 23,
                    "name": "Villa unifamiliare"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Villa unifamiliare 210 m², Recale",
                "title": "Villa unifamiliare 210 m², Recale",
                "metaTitle": "Vendita Villa unifamiliare  Recale. 210 m², rif. 102229664",
                "url": "https://www.immobiliare.it/annunci/102229664/"
            },
            "idGeoHash": "sr61t3u8"
        },
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 104894235,
                "uuid": "216626de-ef67-5824-8fb6-00cfb7aa4cd1",
                "advertiser": {
                    "agency": {
                        "id": 121262,
                        "type": "agency",
                        "showOnlyAgentPhone": false,
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "bookableVisit": {
                            "isVisitBookable": true,
                            "virtualVisitEnabled": false
                        },
                        "isPaid": true,
                        "label": "agenzia",
                        "displayName": "Studiocasa",
                        "guaranteed": false,
                        "showAgentPhone": false,
                        "showLogo": true,
                        "imageUrls": {
                            "small": "https://pic.im-cdn.it/imagenoresize/583544570.jpg",
                            "large": "https://pic.im-cdn.it/imagenoresize/583544572.jpg"
                        },
                        "agencyUrl": "https://www.immobiliare.it/agenzie-immobiliari/121262/studiocasa-recale/"
                    },
                    "supervisor": {
                        "type": "agent",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "imageType": "agent",
                        "displayName": "Venere Errico",
                        "label": "agente immobiliare"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 110000,
                    "formattedValue": "€ 110.000",
                    "priceRange": "100.001 - 150.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1374438615,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1374438615/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1374438659,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1374438659/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1374438719,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1374438719/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1374438811,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1374438811/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1374438853,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1374438853/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1374438927,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1374438927/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1374438973,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1374438973/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "floor": {
                            "abbreviation": "2",
                            "value": "2°",
                            "floorOnlyValue": "2",
                            "ga4FloorValue": "2"
                        },
                        "price": {
                            "visible": true,
                            "value": 110000,
                            "formattedValue": "€ 110.000",
                            "priceRange": "100.001 - 150.000 &euro;"
                        },
                        "surface": "153 m²",
                        "typology": {
                            "id": 17,
                            "name": "Loft"
                        },
                        "typologyGA4Translation": "Loft",
                        "ga4features": [],
                        "caption": "MANSARDA",
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "photo": {
                            "id": 1374438615,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1374438615/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1374438615/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1374438615/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1374438615/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.0463,
                            "longitude": 14.3064,
                            "marker": "no_map",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Capodrise",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "surface",
                                "label": "153 m²"
                            },
                            {
                                "type": "floor",
                                "label": "Piano 2",
                                "compactLabel": "2"
                            }
                        ]
                    }
                ],
                "title": "Loft 153 m², Capodrise",
                "type": "ad",
                "typology": {
                    "id": 17,
                    "name": "Loft"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Loft 153 m², Capodrise",
                "title": "Loft 153 m², Capodrise",
                "metaTitle": "Vendita Loft  Capodrise. 153 m², rif. 104894235",
                "url": "https://www.immobiliare.it/annunci/104894235/"
            },
            "idGeoHash": "sr61t838"
        },
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 102430042,
                "uuid": "41094ec0-cd71-579b-9b96-759fd5dcd6ae",
                "advertiser": {
                    "agency": {
                        "id": 121262,
                        "type": "agency",
                        "showOnlyAgentPhone": false,
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "bookableVisit": {
                            "isVisitBookable": true,
                            "virtualVisitEnabled": false
                        },
                        "isPaid": true,
                        "label": "agenzia",
                        "displayName": "Studiocasa",
                        "guaranteed": false,
                        "showAgentPhone": false,
                        "showLogo": true,
                        "imageUrls": {
                            "small": "https://pic.im-cdn.it/imagenoresize/583544570.jpg",
                            "large": "https://pic.im-cdn.it/imagenoresize/583544572.jpg"
                        },
                        "agencyUrl": "https://www.immobiliare.it/agenzie-immobiliari/121262/studiocasa-recale/"
                    },
                    "supervisor": {
                        "type": "agent",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "imageType": "agent",
                        "displayName": "Venere Errico",
                        "label": "agente immobiliare"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 70000,
                    "formattedValue": "€ 70.000",
                    "priceRange": "fino a 100.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1315023610,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023610/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1315023612,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023612/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1315023614,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023614/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1315023616,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023616/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1315023618,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023618/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1315023620,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023620/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1315023622,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023622/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "floor": {
                            "abbreviation": "R",
                            "value": "Piano rialzato",
                            "floorOnlyValue": "piano rialzato",
                            "ga4FloorValue": "piano rialzato"
                        },
                        "price": {
                            "visible": true,
                            "value": 70000,
                            "formattedValue": "€ 70.000",
                            "priceRange": "fino a 100.000 &euro;"
                        },
                        "surface": "80 m²",
                        "typology": {
                            "id": 14,
                            "name": "Appartamento"
                        },
                        "typologyGA4Translation": "Appartamento",
                        "ga4features": [],
                        "caption": "APPARTAMENTO CON INGRESSO INDIPENDENTE",
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "photo": {
                            "id": 1315023610,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1315023610/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1315023610/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1315023610/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1315023610/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.0418,
                            "longitude": 14.3074,
                            "marker": "no_map",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Capodrise",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "surface",
                                "label": "80 m²"
                            },
                            {
                                "type": "floor",
                                "label": "Piano R",
                                "compactLabel": "R"
                            }
                        ]
                    }
                ],
                "title": "Appartamento 80 m², Capodrise",
                "type": "ad",
                "typology": {
                    "id": 14,
                    "name": "Appartamento"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Appartamento 80 m², Capodrise",
                "title": "Appartamento 80 m², Capodrise",
                "metaTitle": "Vendita Appartamento  Capodrise, rif. 102430042",
                "url": "https://www.immobiliare.it/annunci/102430042/"
            },
            "idGeoHash": "sr61mx6m"
        },
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 102232726,
                "uuid": "c9fe309c-2375-53e4-8b2b-cd4a85e29deb",
                "advertiser": {
                    "agency": {
                        "id": 121262,
                        "type": "agency",
                        "showOnlyAgentPhone": false,
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "bookableVisit": {
                            "isVisitBookable": true,
                            "virtualVisitEnabled": false
                        },
                        "isPaid": true,
                        "label": "agenzia",
                        "displayName": "Studiocasa",
                        "guaranteed": false,
                        "showAgentPhone": false,
                        "showLogo": true,
                        "imageUrls": {
                            "small": "https://pic.im-cdn.it/imagenoresize/583544570.jpg",
                            "large": "https://pic.im-cdn.it/imagenoresize/583544572.jpg"
                        },
                        "agencyUrl": "https://www.immobiliare.it/agenzie-immobiliari/121262/studiocasa-recale/"
                    },
                    "supervisor": {
                        "type": "agent",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "imageType": "agent",
                        "displayName": "Venere Errico",
                        "label": "agente immobiliare"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 140000,
                    "formattedValue": "€ 140.000",
                    "priceRange": "100.001 - 150.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1306652398,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1306652398/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1306652400,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1306652400/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1306652402,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1306652402/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1306652404,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1306652404/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1306652406,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1306652406/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1306652408,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1306652408/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1306652410,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1306652410/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1306652412,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1306652412/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1306652414,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1306652414/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "floor": {
                            "abbreviation": "1",
                            "value": "1°",
                            "floorOnlyValue": "1",
                            "ga4FloorValue": "1"
                        },
                        "price": {
                            "visible": true,
                            "value": 140000,
                            "formattedValue": "€ 140.000",
                            "priceRange": "100.001 - 150.000 &euro;"
                        },
                        "surface": "120 m²",
                        "typology": {
                            "id": 14,
                            "name": "Appartamento"
                        },
                        "typologyGA4Translation": "Appartamento",
                        "ga4features": [],
                        "caption": "APPARTAMENTO IN CONDOMINIO",
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "photo": {
                            "id": 1306652398,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1306652398/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1306652398/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1306652398/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1306652398/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.0359,
                            "longitude": 14.2997,
                            "marker": "no_map",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Marcianise",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "surface",
                                "label": "120 m²"
                            },
                            {
                                "type": "floor",
                                "label": "Piano 1",
                                "compactLabel": "1"
                            }
                        ]
                    }
                ],
                "title": "Appartamento 120 m², Marcianise",
                "type": "ad",
                "typology": {
                    "id": 14,
                    "name": "Appartamento"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Appartamento 120 m², Marcianise",
                "title": "Appartamento 120 m², Marcianise",
                "metaTitle": "Vendita Appartamento  Marcianise, rif. 102232726",
                "url": "https://www.immobiliare.it/annunci/102232726/"
            },
            "idGeoHash": "sr61mqke"
        },
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 102430046,
                "uuid": "b2c78ee2-8301-5406-b24e-3b1a9812d114",
                "advertiser": {
                    "agency": {
                        "id": 121262,
                        "type": "agency",
                        "showOnlyAgentPhone": false,
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "bookableVisit": {
                            "isVisitBookable": true,
                            "virtualVisitEnabled": false
                        },
                        "isPaid": true,
                        "label": "agenzia",
                        "displayName": "Studiocasa",
                        "guaranteed": false,
                        "showAgentPhone": false,
                        "showLogo": true,
                        "imageUrls": {
                            "small": "https://pic.im-cdn.it/imagenoresize/583544570.jpg",
                            "large": "https://pic.im-cdn.it/imagenoresize/583544572.jpg"
                        },
                        "agencyUrl": "https://www.immobiliare.it/agenzie-immobiliari/121262/studiocasa-recale/"
                    },
                    "supervisor": {
                        "type": "agent",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "imageType": "agent",
                        "displayName": "Venere Errico",
                        "label": "agente immobiliare"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 110000,
                    "formattedValue": "€ 110.000",
                    "priceRange": "100.001 - 150.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1315023710,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023710/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1315023712,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023712/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1315023714,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023714/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1315023716,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023716/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1315023718,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023718/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1315023720,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023720/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "floor": {
                            "abbreviation": "1",
                            "value": "1°",
                            "floorOnlyValue": "1",
                            "ga4FloorValue": "1"
                        },
                        "price": {
                            "visible": true,
                            "value": 110000,
                            "formattedValue": "€ 110.000",
                            "priceRange": "100.001 - 150.000 &euro;"
                        },
                        "surface": "200 m²",
                        "typology": {
                            "id": 14,
                            "name": "Appartamento"
                        },
                        "typologyGA4Translation": "Appartamento",
                        "ga4features": [],
                        "caption": "DUE APPARTAMENTI",
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "photo": {
                            "id": 1315023710,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1315023710/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1315023710/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1315023710/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1315023710/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.0418,
                            "longitude": 14.3074,
                            "marker": "no_map",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Capodrise",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "surface",
                                "label": "200 m²"
                            },
                            {
                                "type": "floor",
                                "label": "Piano 1",
                                "compactLabel": "1"
                            }
                        ]
                    }
                ],
                "title": "Appartamento 200 m², Capodrise",
                "type": "ad",
                "typology": {
                    "id": 14,
                    "name": "Appartamento"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Appartamento 200 m², Capodrise",
                "title": "Appartamento 200 m², Capodrise",
                "metaTitle": "Vendita Appartamento  Capodrise, rif. 102430046",
                "url": "https://www.immobiliare.it/annunci/102430046/"
            },
            "idGeoHash": "sr61mx6m"
        },
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 102125148,
                "uuid": "04e077fd-1a95-5bf3-a145-82bc93ce6e69",
                "advertiser": {
                    "agency": {
                        "id": 121262,
                        "type": "agency",
                        "showOnlyAgentPhone": false,
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "bookableVisit": {
                            "isVisitBookable": true,
                            "virtualVisitEnabled": false
                        },
                        "isPaid": true,
                        "label": "agenzia",
                        "displayName": "Studiocasa",
                        "guaranteed": false,
                        "showAgentPhone": false,
                        "showLogo": true,
                        "imageUrls": {
                            "small": "https://pic.im-cdn.it/imagenoresize/583544570.jpg",
                            "large": "https://pic.im-cdn.it/imagenoresize/583544572.jpg"
                        },
                        "agencyUrl": "https://www.immobiliare.it/agenzie-immobiliari/121262/studiocasa-recale/"
                    },
                    "supervisor": {
                        "type": "agent",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "imageType": "agent",
                        "displayName": "Venere Errico",
                        "label": "agente immobiliare"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 140000,
                    "formattedValue": "€ 140.000",
                    "priceRange": "100.001 - 150.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1302080818,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302080818/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1302080822,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302080822/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1302080826,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302080826/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1302080828,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302080828/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1302080836,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302080836/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1302080838,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302080838/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "floor": {
                            "abbreviation": "1",
                            "value": "1°",
                            "floorOnlyValue": "1",
                            "ga4FloorValue": "1"
                        },
                        "price": {
                            "visible": true,
                            "value": 140000,
                            "formattedValue": "€ 140.000",
                            "priceRange": "100.001 - 150.000 &euro;"
                        },
                        "surface": "90 m²",
                        "typology": {
                            "id": 14,
                            "name": "Appartamento"
                        },
                        "typologyGA4Translation": "Appartamento",
                        "ga4features": [],
                        "caption": "APPARTAMENTO CON POSTO AUTO E SOTTOTETTO",
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "photo": {
                            "id": 1302080818,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1302080818/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1302080818/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1302080818/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1302080818/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.0546,
                            "longitude": 14.2995,
                            "marker": "no_map",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Recale",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "surface",
                                "label": "90 m²"
                            },
                            {
                                "type": "floor",
                                "label": "Piano 1",
                                "compactLabel": "1"
                            }
                        ]
                    }
                ],
                "title": "Appartamento 90 m², Recale",
                "type": "ad",
                "typology": {
                    "id": 14,
                    "name": "Appartamento"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Appartamento 90 m², Recale",
                "title": "Appartamento 90 m², Recale",
                "metaTitle": "Vendita Appartamento  Recale, rif. 102125148",
                "url": "https://www.immobiliare.it/annunci/102125148/"
            },
            "idGeoHash": "sr61t3u8"
        },
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 102110912,
                "uuid": "2d3cad91-a2df-520a-93a4-63a29dedcad8",
                "advertiser": {
                    "agency": {
                        "id": 121262,
                        "type": "agency",
                        "showOnlyAgentPhone": false,
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "bookableVisit": {
                            "isVisitBookable": true,
                            "virtualVisitEnabled": false
                        },
                        "isPaid": true,
                        "label": "agenzia",
                        "displayName": "Studiocasa",
                        "guaranteed": false,
                        "showAgentPhone": false,
                        "showLogo": true,
                        "imageUrls": {
                            "small": "https://pic.im-cdn.it/imagenoresize/583544570.jpg",
                            "large": "https://pic.im-cdn.it/imagenoresize/583544572.jpg"
                        },
                        "agencyUrl": "https://www.immobiliare.it/agenzie-immobiliari/121262/studiocasa-recale/"
                    },
                    "supervisor": {
                        "type": "agent",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "imageType": "agent",
                        "displayName": "Venere Errico",
                        "label": "agente immobiliare"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 40000,
                    "formattedValue": "€ 40.000",
                    "priceRange": "fino a 100.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1301296614,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1301296614/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1301296918,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1301296918/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1301297070,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1301297070/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1301297172,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1301297172/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1301297264,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1301297264/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1301297354,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1301297354/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "floor": {
                            "abbreviation": "T",
                            "value": "Piano terra",
                            "floorOnlyValue": "piano terra",
                            "ga4FloorValue": "piano terra"
                        },
                        "price": {
                            "visible": true,
                            "value": 40000,
                            "formattedValue": "€ 40.000",
                            "priceRange": "fino a 100.000 &euro;"
                        },
                        "surface": "50 m²",
                        "typology": {
                            "id": 14,
                            "name": "Appartamento"
                        },
                        "typologyGA4Translation": "Appartamento",
                        "ga4features": [],
                        "caption": "ZONA CENTRALE",
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "photo": {
                            "id": 1301296614,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1301296614/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1301296614/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1301296614/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1301296614/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.0546,
                            "longitude": 14.2995,
                            "marker": "no_map",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Recale",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "surface",
                                "label": "50 m²"
                            },
                            {
                                "type": "floor",
                                "label": "Piano T",
                                "compactLabel": "T"
                            }
                        ]
                    }
                ],
                "title": "Appartamento 50 m², Recale",
                "type": "ad",
                "typology": {
                    "id": 14,
                    "name": "Appartamento"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Appartamento 50 m², Recale",
                "title": "Appartamento 50 m², Recale",
                "metaTitle": "Vendita Appartamento  Recale, rif. 102110912",
                "url": "https://www.immobiliare.it/annunci/102110912/"
            },
            "idGeoHash": "sr61t3u8"
        },
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 102125532,
                "uuid": "46f55f26-35bf-5524-9f18-fa740f442997",
                "advertiser": {
                    "agency": {
                        "id": 121262,
                        "type": "agency",
                        "showOnlyAgentPhone": false,
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "bookableVisit": {
                            "isVisitBookable": true,
                            "virtualVisitEnabled": false
                        },
                        "isPaid": true,
                        "label": "agenzia",
                        "displayName": "Studiocasa",
                        "guaranteed": false,
                        "showAgentPhone": false,
                        "showLogo": true,
                        "imageUrls": {
                            "small": "https://pic.im-cdn.it/imagenoresize/583544570.jpg",
                            "large": "https://pic.im-cdn.it/imagenoresize/583544572.jpg"
                        },
                        "agencyUrl": "https://www.immobiliare.it/agenzie-immobiliari/121262/studiocasa-recale/"
                    },
                    "supervisor": {
                        "type": "agent",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "imageType": "agent",
                        "displayName": "Venere Errico",
                        "label": "agente immobiliare"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 160000,
                    "formattedValue": "€ 160.000",
                    "priceRange": "150.001 - 200.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1302082466,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302082466/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1302082468,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302082468/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1302082470,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302082470/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1302082472,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302082472/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1302082474,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302082474/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1302082476,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302082476/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "floor": {
                            "abbreviation": "R",
                            "value": "Piano rialzato",
                            "floorOnlyValue": "piano rialzato",
                            "ga4FloorValue": "piano rialzato"
                        },
                        "price": {
                            "visible": true,
                            "value": 160000,
                            "formattedValue": "€ 160.000",
                            "priceRange": "150.001 - 200.000 &euro;"
                        },
                        "surface": "100 m²",
                        "typology": {
                            "id": 14,
                            "name": "Appartamento"
                        },
                        "typologyGA4Translation": "Appartamento",
                        "ga4features": [],
                        "caption": "APPARTAMENTO CON PATIO E BOX",
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "photo": {
                            "id": 1302082466,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1302082466/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1302082466/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1302082466/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1302082466/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.0546,
                            "longitude": 14.2995,
                            "marker": "no_map",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Recale",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "surface",
                                "label": "100 m²"
                            },
                            {
                                "type": "floor",
                                "label": "Piano R",
                                "compactLabel": "R"
                            }
                        ]
                    }
                ],
                "title": "Appartamento 100 m², Recale",
                "type": "ad",
                "typology": {
                    "id": 14,
                    "name": "Appartamento"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Appartamento 100 m², Recale",
                "title": "Appartamento 100 m², Recale",
                "metaTitle": "Vendita Appartamento  Recale, rif. 102125532",
                "url": "https://www.immobiliare.it/annunci/102125532/"
            },
            "idGeoHash": "sr61t3u8"
        },
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 102124944,
                "uuid": "b1d94af8-d5fb-5104-9579-47cf25050474",
                "advertiser": {
                    "agency": {
                        "id": 121262,
                        "type": "agency",
                        "showOnlyAgentPhone": false,
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "bookableVisit": {
                            "isVisitBookable": true,
                            "virtualVisitEnabled": false
                        },
                        "isPaid": true,
                        "label": "agenzia",
                        "displayName": "Studiocasa",
                        "guaranteed": false,
                        "showAgentPhone": false,
                        "showLogo": true,
                        "imageUrls": {
                            "small": "https://pic.im-cdn.it/imagenoresize/583544570.jpg",
                            "large": "https://pic.im-cdn.it/imagenoresize/583544572.jpg"
                        },
                        "agencyUrl": "https://www.immobiliare.it/agenzie-immobiliari/121262/studiocasa-recale/"
                    },
                    "supervisor": {
                        "type": "agent",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "imageType": "agent",
                        "displayName": "Venere Errico",
                        "label": "agente immobiliare"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 100000,
                    "formattedValue": "€ 100.000",
                    "priceRange": "fino a 100.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1302073296,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302073296/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1302073304,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302073304/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1302073314,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302073314/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1302073324,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302073324/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1302073326,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302073326/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1302073328,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1302073328/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "floor": {
                            "abbreviation": "3",
                            "value": "3°",
                            "floorOnlyValue": "3",
                            "ga4FloorValue": "3"
                        },
                        "price": {
                            "visible": true,
                            "value": 100000,
                            "formattedValue": "€ 100.000",
                            "priceRange": "fino a 100.000 &euro;"
                        },
                        "surface": "135 m²",
                        "typology": {
                            "id": 14,
                            "name": "Appartamento"
                        },
                        "typologyGA4Translation": "Appartamento",
                        "ga4features": [],
                        "caption": "APPARTAMENTO",
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "photo": {
                            "id": 1302073296,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1302073296/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1302073296/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1302073296/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1302073296/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.0546,
                            "longitude": 14.2995,
                            "marker": "no_map",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Recale",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "surface",
                                "label": "135 m²"
                            },
                            {
                                "type": "floor",
                                "label": "Piano 3",
                                "compactLabel": "3"
                            }
                        ]
                    }
                ],
                "title": "Appartamento 135 m², Recale",
                "type": "ad",
                "typology": {
                    "id": 14,
                    "name": "Appartamento"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Appartamento 135 m², Recale",
                "title": "Appartamento 135 m², Recale",
                "metaTitle": "Vendita Appartamento  Recale, rif. 102124944",
                "url": "https://www.immobiliare.it/annunci/102124944/"
            },
            "idGeoHash": "sr61t3u8"
        },
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 102430008,
                "uuid": "589424b6-d672-5224-b9f4-44e689859f98",
                "advertiser": {
                    "agency": {
                        "id": 121262,
                        "type": "agency",
                        "showOnlyAgentPhone": false,
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "bookableVisit": {
                            "isVisitBookable": true,
                            "virtualVisitEnabled": false
                        },
                        "isPaid": true,
                        "label": "agenzia",
                        "displayName": "Studiocasa",
                        "guaranteed": false,
                        "showAgentPhone": false,
                        "showLogo": true,
                        "imageUrls": {
                            "small": "https://pic.im-cdn.it/imagenoresize/583544570.jpg",
                            "large": "https://pic.im-cdn.it/imagenoresize/583544572.jpg"
                        },
                        "agencyUrl": "https://www.immobiliare.it/agenzie-immobiliari/121262/studiocasa-recale/"
                    },
                    "supervisor": {
                        "type": "agent",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1",
                                "value": "0823 466666"
                            },
                            {
                                "type": "cell",
                                "value": "345 095 9380"
                            }
                        ],
                        "imageType": "agent",
                        "displayName": "Venere Errico",
                        "label": "agente immobiliare"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 50000,
                    "formattedValue": "€ 50.000",
                    "priceRange": "fino a 100.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1315023186,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023186/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1315023188,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023188/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1315023190,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023190/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1315023192,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023192/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1315023194,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023194/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1315023196,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1315023196/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "floor": {
                            "abbreviation": "R",
                            "value": "Piano rialzato",
                            "floorOnlyValue": "piano rialzato",
                            "ga4FloorValue": "piano rialzato"
                        },
                        "price": {
                            "visible": true,
                            "value": 50000,
                            "formattedValue": "€ 50.000",
                            "priceRange": "fino a 100.000 &euro;"
                        },
                        "surface": "65 m²",
                        "typology": {
                            "id": 14,
                            "name": "Appartamento"
                        },
                        "typologyGA4Translation": "Appartamento",
                        "ga4features": [],
                        "caption": "APPARTAMENTO CON BOX",
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "photo": {
                            "id": 1315023186,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1315023186/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1315023186/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1315023186/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1315023186/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.0418,
                            "longitude": 14.3074,
                            "marker": "no_map",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Capodrise",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "surface",
                                "label": "65 m²"
                            },
                            {
                                "type": "floor",
                                "label": "Piano R",
                                "compactLabel": "R"
                            }
                        ]
                    }
                ],
                "title": "Appartamento 65 m², Capodrise",
                "type": "ad",
                "typology": {
                    "id": 14,
                    "name": "Appartamento"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Appartamento 65 m², Capodrise",
                "title": "Appartamento 65 m², Capodrise",
                "metaTitle": "Vendita Appartamento  Capodrise, rif. 102430008",
                "url": "https://www.immobiliare.it/annunci/102430008/"
            },
            "idGeoHash": "sr61mx6m"
        },
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 115494827,
                "uuid": "7e3ff0c4-1683-52b3-a9dd-bd4d52845a5a",
                "advertiser": {
                    "supervisor": {
                        "type": "user",
                        "imageGender": "female",
                        "phones": [],
                        "imageType": "user",
                        "label": "privato"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": false,
                    "formattedValue": "prezzo su richiesta",
                    "priceRange": "Prezzo su richiesta"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1593695405,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1593695405/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "floor": {
                            "abbreviation": null,
                            "value": "5 piani: Piano terra, Piano rialzato, da 1° a 3°",
                            "floorOnlyValue": "piano terra, piano rialzato, da 1 a 3",
                            "ga4FloorValue": "piano terra, piano rialzato, da 1 a 3"
                        },
                        "ga4Condition": "Buono / Abitabile",
                        "price": {
                            "visible": false,
                            "formattedValue": "prezzo su richiesta",
                            "priceRange": "Prezzo su richiesta"
                        },
                        "surface": "700 m²",
                        "typology": {
                            "id": 246,
                            "name": "Palazzo - Edificio"
                        },
                        "typologyGA4Translation": "Palazzo - Edificio",
                        "ga4features": [
                            "accesso per disabili",
                            "esposizione doppia"
                        ],
                        "category": {
                            "id": 20,
                            "name": "Palazzi - Edifici"
                        },
                        "energy": {
                            "zeroEnergyBuilding": false,
                            "thermalInsulation": null,
                            "emission": null,
                            "heatingType": "autonomo",
                            "GA4Heating": "Autonomo"
                        },
                        "photo": {
                            "id": 1593695405,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1593695405/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1593695405/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1593695405/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1593695405/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.09016037,
                            "longitude": 14.33135986,
                            "marker": "only_area",
                            "region": "Campania",
                            "province": "Caserta",
                            "macrozone": "Caserta Nord",
                            "microzone": "Puccianiello",
                            "city": "Caserta",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "surface",
                                "label": "700 m²"
                            }
                        ]
                    }
                ],
                "title": "Palazzo - Edificio buono stato, Puccianiello, Caserta",
                "type": "ad",
                "typology": {
                    "id": 246,
                    "name": "Palazzo - Edificio"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Palazzo - Edificio buono stato, Puccianiello, Caserta",
                "title": "Palazzo - Edificio in Vendita",
                "metaTitle": "Palazzo - Edificio buono stato, Caserta, Rif. 115494827 - Immobiliare.it",
                "url": "https://www.immobiliare.it/annunci/115494827/"
            },
            "idGeoHash": "sr61y05z"
        },
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 88822837,
                "uuid": "37f16dd2-81f3-5303-afd6-819951a98205",
                "advertiser": {
                    "agency": {
                        "id": 36193,
                        "type": "agency",
                        "showOnlyAgentPhone": false,
                        "phones": [
                            {
                                "type": "vTel1",
                                "value": "0823 166 6610"
                            }
                        ],
                        "bookableVisit": {
                            "isVisitBookable": true,
                            "virtualVisitEnabled": false
                        },
                        "isPaid": true,
                        "label": "agenzia",
                        "displayName": "MT Servizi Immobiliari",
                        "guaranteed": false,
                        "showAgentPhone": false,
                        "showLogo": true,
                        "imageUrls": {
                            "small": "https://pic.im-cdn.it/imagenoresize/651297442.jpg",
                            "large": "https://pic.im-cdn.it/imagenoresize/651297444.jpg"
                        },
                        "agencyUrl": "https://www.immobiliare.it/agenzie-immobiliari/36193/mt-servizi-caserta/"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": false,
                    "formattedValue": "prezzo su richiesta",
                    "priceRange": "Prezzo su richiesta"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1066449651,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1066449651/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1066449791,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1066449791/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1066449895,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1066449895/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "floor": {
                            "abbreviation": null,
                            "value": "4 piani: Interrato (-1), Piano terra, da 1° a 2°",
                            "floorOnlyValue": "interrato (-1), piano terra, da 1 a 2",
                            "ga4FloorValue": "interrato (-1), piano terra, da 1 a 2"
                        },
                        "price": {
                            "visible": false,
                            "formattedValue": "prezzo su richiesta",
                            "priceRange": "Prezzo su richiesta"
                        },
                        "surface": "2.100 m²",
                        "typology": {
                            "id": 22,
                            "name": "Terratetto plurifamiliare"
                        },
                        "typologyGA4Translation": "Casa indipendente",
                        "ga4features": [],
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "photo": {
                            "id": 1066449651,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1066449651/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1066449651/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1066449651/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1066449651/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.0676,
                            "longitude": 14.329,
                            "marker": "marker",
                            "region": "Campania",
                            "province": "Caserta",
                            "macrozone": "Lincoln - Acquaviva",
                            "microzone": "Via Mondo",
                            "city": "Caserta",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "surface",
                                "label": "2.100 m²"
                            }
                        ]
                    }
                ],
                "title": "Terratetto plurifamiliare via Isonzo, Via Mondo, Caserta",
                "type": "ad",
                "typology": {
                    "id": 22,
                    "name": "Terratetto plurifamiliare"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Terratetto plurifamiliare via Isonzo, Via Mondo, Caserta",
                "title": "Terratetto plurifamiliare via Isonzo, Via Mondo, Caserta",
                "metaTitle": "Vendita Terratetto plurifamiliare  in via Isonzo Caserta. 2100 m², rif. 88822837",
                "url": "https://www.immobiliare.it/annunci/88822837/"
            },
            "idGeoHash": "sr61wh4h"
        },
        {
            "realEstate": {
                "visibility": "premium",
                "dataType": "list-real-estate",
                "id": 100164112,
                "uuid": "ed03545e-1059-5370-8e31-828ca5575b1b",
                "advertiser": {
                    "agency": {
                        "id": 218628,
                        "type": "agency",
                        "showOnlyAgentPhone": false,
                        "phones": [
                            {
                                "type": "vTel1",
                                "value": "0823 166 6914"
                            }
                        ],
                        "bookableVisit": {
                            "isVisitBookable": true,
                            "virtualVisitEnabled": false
                        },
                        "isPaid": true,
                        "label": "agenzia",
                        "displayName": "RS IMMOBILIARE di Roberto Spina",
                        "guaranteed": false,
                        "showAgentPhone": false,
                        "showLogo": true,
                        "imageUrls": {
                            "small": "https://pic.im-cdn.it/imagenoresize/628147150.jpg",
                            "large": "https://pic.im-cdn.it/imagenoresize/628147152.jpg"
                        },
                        "agencyUrl": "https://www.immobiliare.it/agenzie-immobiliari/218628/rs-caserta/"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": false,
                    "formattedValue": "prezzo su richiesta",
                    "priceRange": "Prezzo su richiesta"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1259767618,
                                    "caption": "PIANO TERRA",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1259767618/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1259767632,
                                    "caption": "PIANO PRIMO",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1259767632/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1259767650,
                                    "caption": "PIANO 2°",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1259767650/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1259767662,
                                    "caption": "SEZIONI",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1259767662/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1259767680,
                                    "caption": "COPERTURA",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1259767680/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1259767694,
                                    "caption": "PROSPETTO",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1259767694/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1259767700,
                                    "caption": "PROSPETTO",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1259767700/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "floor": {
                            "abbreviation": null,
                            "value": "3 piani: Piano terra, da 1° a 2°",
                            "floorOnlyValue": "piano terra, da 1 a 2",
                            "ga4FloorValue": "piano terra, da 1 a 2"
                        },
                        "ga4Condition": "Buono / Abitabile",
                        "price": {
                            "visible": false,
                            "formattedValue": "prezzo su richiesta",
                            "priceRange": "Prezzo su richiesta"
                        },
                        "surface": "2.302 m²",
                        "typology": {
                            "id": 246,
                            "name": "Palazzo - Edificio"
                        },
                        "ga4Garage": "8 in parcheggio/garage comune",
                        "typologyGA4Translation": "Palazzo - Edificio",
                        "ga4features": [
                            "esposizione doppia"
                        ],
                        "caption": "Intero fabbricato ad uso commerciale e abitazione",
                        "category": {
                            "id": 20,
                            "name": "Palazzi - Edifici"
                        },
                        "energy": {
                            "zeroEnergyBuilding": false,
                            "thermalInsulation": null,
                            "emission": null,
                            "heatingType": "autonomo",
                            "GA4Heating": "Autonomo"
                        },
                        "photo": {
                            "id": 1259767618,
                            "caption": "PIANO TERRA",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1259767618/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1259767618/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1259767618/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1259767618/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.02590179,
                            "longitude": 14.29430008,
                            "marker": "no_map",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Marcianise",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "surface",
                                "label": "2.302 m²"
                            }
                        ]
                    }
                ],
                "title": "Palazzo - Edificio 3 piani, buono stato, Marcianise",
                "type": "ad",
                "typology": {
                    "id": 246,
                    "name": "Palazzo - Edificio"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Palazzo - Edificio 3 piani, buono stato, Marcianise",
                "title": "Palazzo - Edificio in Vendita",
                "metaTitle": "Palazzo - Edificio 3 piani, buono stato, Marcianise, Rif. 100164112 - Immobiliare.it",
                "url": "https://www.immobiliare.it/annunci/100164112/"
            },
            "idGeoHash": "sr61mk8c"
        },
        {
            "realEstate": {
                "dataType": "list-real-estate",
                "id": 114033075,
                "uuid": "bbf28ce6-a71f-5a84-ab0a-cb4aa59a12c8",
                "advertiser": {
                    "supervisor": {
                        "type": "user",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1"
                            }
                        ],
                        "imageType": "user",
                        "label": "privato",
                        "phoneUrl": "https://media.immobiliare.it/text/tel_114033075_a752d.jpg?k=497f6ab636f268fc503209329ee161d1"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 59900,
                    "formattedValue": "€ 59.900",
                    "priceRange": "fino a 100.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1585625577,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1585625577/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1585625587,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1585625587/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1585625601,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1585625601/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1585625609,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1585625609/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1585625617,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1585625617/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1585625635,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1585625635/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1585625657,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1585625657/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1585625687,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1585625687/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "bathrooms": "1",
                        "floor": {
                            "abbreviation": "R",
                            "value": "Piano rialzato",
                            "floorOnlyValue": "piano rialzato",
                            "ga4FloorValue": "piano rialzato"
                        },
                        "ga4Condition": "Da ristrutturare",
                        "price": {
                            "visible": true,
                            "value": 59900,
                            "formattedValue": "€ 59.900",
                            "priceRange": "fino a 100.000 &euro;"
                        },
                        "rooms": "3",
                        "surface": "70 m²",
                        "typology": {
                            "id": 14,
                            "name": "Appartamento"
                        },
                        "ga4Garage": "1 in parcheggio/garage comune",
                        "typologyGA4Translation": "Appartamento",
                        "ga4features": [
                            "cucina"
                        ],
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "photo": {
                            "id": 1585625577,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1585625577/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1585625577/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1585625577/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1585625577/xxl.jpg"
                            }
                        },
                        "bedRoomsNumber": "2",
                        "location": {
                            "latitude": 41.05604553,
                            "longitude": 14.28084278,
                            "marker": "marker",
                            "region": "Campania",
                            "province": "Caserta",
                            "macrozone": "Centro",
                            "city": "Portico di Caserta",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "rooms",
                                "label": "3 locali",
                                "compactLabel": "3"
                            },
                            {
                                "type": "surface",
                                "label": "70 m²"
                            },
                            {
                                "type": "bathrooms",
                                "label": "1 bagno",
                                "compactLabel": "1"
                            },
                            {
                                "type": "floor",
                                "label": "Piano R",
                                "compactLabel": "R"
                            }
                        ]
                    }
                ],
                "title": "Trilocale via F. Iodice 3, Centro, Portico di Caserta",
                "type": "ad",
                "typology": {
                    "id": 14,
                    "name": "Appartamento"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Trilocale via F. Iodice 3, Centro, Portico di Caserta",
                "title": "Trilocale via F. Iodice 3, Centro, Portico di Caserta",
                "metaTitle": "Vendita Appartamento Portico di Caserta. Trilocale in via F. Iodice 3. Da ristrutturare, piano rialzato, posto auto, rif. 114033075",
                "url": "https://www.immobiliare.it/annunci/114033075/"
            },
            "idGeoHash": "sr61sfnb"
        },
        {
            "realEstate": {
                "dataType": "list-real-estate",
                "id": 79478987,
                "uuid": "74bf6ed5-6513-5db2-92a3-4f9c3797decf",
                "advertiser": {
                    "supervisor": {
                        "type": "user",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1"
                            }
                        ],
                        "imageType": "user",
                        "label": "privato",
                        "phoneUrl": "https://media.immobiliare.it/text/tel_79478987_95a73.jpg?k=ba9421984317660c5eae77bc91a49eeb"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 105000,
                    "formattedValue": "€ 105.000",
                    "priceRange": "100.001 - 150.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 904200995,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/904200995/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 904200999,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/904200999/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 904201001,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/904201001/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 904201003,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/904201003/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 904201005,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/904201005/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 904201007,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/904201007/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 904201009,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/904201009/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 904201013,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/904201013/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 904201017,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/904201017/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 904201019,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/904201019/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 904201033,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/904201033/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 904201025,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/904201025/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 904201029,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/904201029/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "bathrooms": "2",
                        "floor": {
                            "abbreviation": "5",
                            "value": "5° piano, con ascensore",
                            "floorOnlyValue": "5",
                            "ga4FloorValue": "5"
                        },
                        "ga4Condition": "Ottimo / Ristrutturato",
                        "price": {
                            "visible": true,
                            "value": 105000,
                            "formattedValue": "€ 105.000",
                            "priceRange": "100.001 - 150.000 &euro;"
                        },
                        "rooms": "3",
                        "elevator": true,
                        "surface": "110 m²",
                        "typology": {
                            "id": 16,
                            "name": "Mansarda"
                        },
                        "typologyGA4Translation": "Attico - Mansarda",
                        "ga4features": [],
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "energy": {
                            "zeroEnergyBuilding": false,
                            "thermalInsulation": null,
                            "emission": null,
                            "heatingType": "autonomo",
                            "GA4Heating": "Autonomo"
                        },
                        "photo": {
                            "id": 904200995,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/904200995/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/904200995/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/904200995/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/904200995/xxl.jpg"
                            }
                        },
                        "bedRoomsNumber": "2",
                        "location": {
                            "latitude": 41.08449936,
                            "longitude": 14.27509975,
                            "marker": "marker",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "San Prisco",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "rooms",
                                "label": "3 locali",
                                "compactLabel": "3"
                            },
                            {
                                "type": "surface",
                                "label": "110 m²"
                            },
                            {
                                "type": "bathrooms",
                                "label": "2 bagni",
                                "compactLabel": "2"
                            },
                            {
                                "type": "floor",
                                "label": "Piano 5",
                                "compactLabel": "5"
                            },
                            {
                                "type": "elevator",
                                "label": "Ascensore",
                                "compactLabel": "Sì"
                            }
                        ]
                    }
                ],
                "title": "Mansarda viale Trieste 91, San Prisco",
                "type": "ad",
                "typology": {
                    "id": 16,
                    "name": "Mansarda"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Mansarda viale Trieste 91, San Prisco",
                "title": "Mansarda viale Trieste 91, San Prisco",
                "metaTitle": "Vendita Mansarda  in viale Trieste 91 San Prisco. Ottimo stato, rif. 79478987",
                "url": "https://www.immobiliare.it/annunci/79478987/"
            },
            "idGeoHash": "sr61sz4y"
        },
        {
            "realEstate": {
                "dataType": "list-real-estate",
                "id": 90075611,
                "uuid": "38490f2f-2da1-5af1-bd92-a55d754c6e8c",
                "advertiser": {
                    "supervisor": {
                        "type": "user",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1"
                            }
                        ],
                        "imageType": "user",
                        "label": "privato",
                        "phoneUrl": "https://media.immobiliare.it/text/tel_90075611_7a77e.jpg?k=f6b631bb73d9faef2e4d61de45670c4e"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 69000,
                    "formattedValue": "€ 69.000",
                    "priceRange": "fino a 100.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1086308915,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086308915/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086308901,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086308901/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086309051,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086309051/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086309053,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086309053/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086308907,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086308907/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086309061,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086309061/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086308917,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086308917/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086308919,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086308919/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086308923,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086308923/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086309065,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086309065/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086309067,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086309067/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086308933,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086308933/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086309075,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086309075/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086309083,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086309083/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086309085,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086309085/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086309087,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086309087/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086309089,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086309089/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086309091,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086309091/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086309109,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086309109/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1086309123,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1086309123/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "bathrooms": "2",
                        "floor": {
                            "abbreviation": null,
                            "value": "2 piani: Piano rialzato, 1°",
                            "floorOnlyValue": "piano rialzato, 1",
                            "ga4FloorValue": "piano rialzato, 1"
                        },
                        "ga4Condition": "Da ristrutturare",
                        "price": {
                            "visible": true,
                            "value": 69000,
                            "formattedValue": "€ 69.000",
                            "priceRange": "fino a 100.000 &euro;"
                        },
                        "rooms": "5+",
                        "surface": "153 m²",
                        "typology": {
                            "id": 246,
                            "name": "Palazzo - Edificio"
                        },
                        "ga4Garage": "1 in parcheggio/garage comune",
                        "typologyGA4Translation": "Palazzo - Edificio",
                        "ga4features": [
                            "esposizione interna",
                            "balcone"
                        ],
                        "category": {
                            "id": 20,
                            "name": "Palazzi - Edifici"
                        },
                        "photo": {
                            "id": 1086308915,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1086308915/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1086308915/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1086308915/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1086308915/xxl.jpg"
                            }
                        },
                        "location": {
                            "latitude": 41.09098816,
                            "longitude": 14.32635021,
                            "marker": "marker",
                            "region": "Campania",
                            "province": "Caserta",
                            "macrozone": "Caserta Nord",
                            "microzone": "San Leucio - Briano",
                            "city": "Caserta",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "rooms",
                                "label": "5+ locali",
                                "compactLabel": "5+"
                            },
                            {
                                "type": "surface",
                                "label": "153 m²"
                            },
                            {
                                "type": "bathrooms",
                                "label": "2 bagni",
                                "compactLabel": "2"
                            }
                        ]
                    }
                ],
                "title": "Palazzo - Edificio via Ponte 28, San Leucio - Briano, Caserta",
                "type": "ad",
                "typology": {
                    "id": 246,
                    "name": "Palazzo - Edificio"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Palazzo - Edificio via Ponte 28, San Leucio - Briano, Caserta",
                "title": "Palazzo - Edificio in Vendita",
                "metaTitle": "Palazzo - Edificio via Ponte 28, Caserta, Rif. 90075611 - Immobiliare.it",
                "url": "https://www.immobiliare.it/annunci/90075611/"
            },
            "idGeoHash": "sr61y02h"
        },
        {
            "realEstate": {
                "dataType": "list-real-estate",
                "id": 87178490,
                "uuid": "93bb5118-ba50-511f-96c3-2d5b88ee62d9",
                "advertiser": {
                    "supervisor": {
                        "type": "user",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1"
                            }
                        ],
                        "imageType": "user",
                        "label": "privato",
                        "phoneUrl": "https://media.immobiliare.it/text/tel_87178490_8b607.jpg?k=715bc40a8f9be99f19da7c05fe72c578"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 710000,
                    "formattedValue": "€ 710.000",
                    "priceRange": "oltre 500.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1039834858,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039834858/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039834862,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039834862/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039834866,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039834866/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039834890,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039834890/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039834896,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039834896/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039834872,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039834872/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039834902,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039834902/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039834906,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039834906/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039834878,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039834878/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039834882,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039834882/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039834884,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039834884/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039834886,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039834886/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039834888,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039834888/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039940038,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039940038/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039940030,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039940030/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039940016,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039940016/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039940056,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039940056/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1593422241,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1593422241/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1039940428,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1039940428/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "bathrooms": "3+",
                        "floor": {
                            "abbreviation": null,
                            "value": "4 piani: da Seminterrato a Piano terra, da 1° a 2°, con ascensore",
                            "floorOnlyValue": "da seminterrato a piano terra, da 1 a 2",
                            "ga4FloorValue": "da seminterrato a piano terra, da 1 a 2"
                        },
                        "ga4Condition": "Ottimo / Ristrutturato",
                        "price": {
                            "visible": true,
                            "value": 710000,
                            "formattedValue": "€ 710.000",
                            "priceRange": "oltre 500.000 &euro;"
                        },
                        "rooms": "5+",
                        "elevator": true,
                        "surface": "450 m²",
                        "typology": {
                            "id": 26,
                            "name": "Villa a schiera"
                        },
                        "ga4Garage": "2 in box privato/box in garage, 1 in parcheggio/garage comune",
                        "typologyGA4Translation": "Villetta a schiera",
                        "ga4features": [
                            "impianto di allarme",
                            "accesso per disabili",
                            "bagno per disabili",
                            "cucina",
                            "balcone",
                            "terrazzo",
                            "parzialmente arredato",
                            "cantina"
                        ],
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "energy": {
                            "zeroEnergyBuilding": false,
                            "thermalInsulation": null,
                            "emission": null,
                            "heatingType": "autonomo",
                            "GA4Heating": "Autonomo"
                        },
                        "photo": {
                            "id": 1039834858,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1039834858/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1039834858/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1039834858/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1039834858/xxl.jpg"
                            }
                        },
                        "bedRoomsNumber": "4",
                        "location": {
                            "latitude": 41.09418869,
                            "longitude": 14.33742046,
                            "marker": "marker",
                            "region": "Campania",
                            "province": "Caserta",
                            "macrozone": "Caserta Nord",
                            "microzone": "Puccianiello",
                            "city": "Caserta",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "rooms",
                                "label": "5+ locali",
                                "compactLabel": "5+"
                            },
                            {
                                "type": "surface",
                                "label": "450 m²"
                            },
                            {
                                "type": "bathrooms",
                                "label": "3+ bagni",
                                "compactLabel": "3+"
                            },
                            {
                                "type": "elevator",
                                "label": "Ascensore",
                                "compactLabel": "Sì"
                            },
                            {
                                "type": "balcony",
                                "label": "Balcone"
                            },
                            {
                                "type": "terrace",
                                "label": "Terrazzo"
                            },
                            {
                                "type": "furniture",
                                "label": "Parzialmente Arredato"
                            },
                            {
                                "type": "basement",
                                "label": "Cantina"
                            }
                        ]
                    }
                ],
                "title": "Villa a schiera via Antonio Marino 61, Puccianiello, Caserta",
                "type": "ad",
                "typology": {
                    "id": 26,
                    "name": "Villa a schiera"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Villa a schiera via Antonio Marino 61, Puccianiello, Caserta",
                "title": "Villa a schiera via Antonio Marino 61, Puccianiello, Caserta",
                "metaTitle": "Vendita Villa a schiera  in via Antonio Marino 61 Caserta. Ottimo stato, posto auto, con terrazza, riscaldamento autonomo, 450 m², rif. 87178490",
                "url": "https://www.immobiliare.it/annunci/87178490/"
            },
            "idGeoHash": "sr61y2bp"
        },
        {
            "realEstate": {
                "dataType": "list-real-estate",
                "id": 98852146,
                "uuid": "b5dc3a81-9973-5516-9712-54b6f27c3024",
                "advertiser": {
                    "supervisor": {
                        "type": "user",
                        "imageGender": "male",
                        "phones": [],
                        "imageType": "user",
                        "label": "privato"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 240000,
                    "formattedValue": "€ 240.000",
                    "priceRange": "200.001 - 300.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1233158516,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1233158516/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1233158550,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1233158550/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1233158764,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1233158764/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1233158808,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1233158808/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1233158844,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1233158844/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1233158878,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1233158878/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1233159638,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1233159638/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1233160762,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1233160762/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1233160798,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1233160798/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1233160844,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1233160844/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1233160868,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1233160868/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1233160992,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1233160992/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1233161018,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1233161018/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1233161052,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1233161052/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1233161098,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1233161098/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "bathrooms": "1",
                        "floor": {
                            "abbreviation": "S4",
                            "value": "Interrato (-4), con ascensore",
                            "floorOnlyValue": "interrato (-4)",
                            "ga4FloorValue": "interrato (-4)"
                        },
                        "ga4Condition": "Buono / Abitabile",
                        "price": {
                            "visible": true,
                            "value": 240000,
                            "formattedValue": "€ 240.000",
                            "priceRange": "200.001 - 300.000 &euro;"
                        },
                        "rooms": "5",
                        "elevator": true,
                        "surface": "155 m²",
                        "typology": {
                            "id": 14,
                            "name": "Appartamento"
                        },
                        "ga4Garage": "1 in parcheggio/garage comune",
                        "typologyGA4Translation": "Appartamento",
                        "ga4features": [
                            "bagno per disabili",
                            "cucina",
                            "balcone",
                            "cantina"
                        ],
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "energy": {
                            "zeroEnergyBuilding": false,
                            "thermalInsulation": null,
                            "emission": null,
                            "heatingType": "autonomo",
                            "GA4Heating": "Autonomo"
                        },
                        "photo": {
                            "id": 1233158516,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1233158516/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1233158516/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1233158516/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1233158516/xxl.jpg"
                            }
                        },
                        "bedRoomsNumber": "5",
                        "location": {
                            "latitude": 41.07521057,
                            "longitude": 14.33952045,
                            "marker": "marker",
                            "region": "Campania",
                            "province": "Caserta",
                            "macrozone": "Centro",
                            "microzone": "Corso Trieste",
                            "city": "Caserta",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "rooms",
                                "label": "5 locali",
                                "compactLabel": "5"
                            },
                            {
                                "type": "surface",
                                "label": "155 m²"
                            },
                            {
                                "type": "bathrooms",
                                "label": "1 bagno",
                                "compactLabel": "1"
                            },
                            {
                                "type": "floor",
                                "label": "Piano S4",
                                "compactLabel": "S4"
                            },
                            {
                                "type": "elevator",
                                "label": "Ascensore",
                                "compactLabel": "Sì"
                            },
                            {
                                "type": "balcony",
                                "label": "Balcone"
                            },
                            {
                                "type": "basement",
                                "label": "Cantina"
                            }
                        ]
                    }
                ],
                "title": "Appartamento via Michele Ferrara 23, Corso Trieste, Caserta",
                "type": "ad",
                "typology": {
                    "id": 14,
                    "name": "Appartamento"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Appartamento via Michele Ferrara 23, Corso Trieste, Caserta",
                "title": "Appartamento via Michele Ferrara 23, Corso Trieste, Caserta",
                "metaTitle": "Vendita Appartamento  in via Michele Ferrara 23. Caserta. Buono stato, interrato (-4), posto auto, con balcone, riscaldamento autonomo, rif. 98852146",
                "url": "https://www.immobiliare.it/annunci/98852146/"
            },
            "idGeoHash": "sr61wm98"
        },
        {
            "realEstate": {
                "dataType": "list-real-estate",
                "id": 88166469,
                "uuid": "edc583a3-6f76-58fd-9870-faaa5352de18",
                "advertiser": {
                    "supervisor": {
                        "type": "user",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1"
                            }
                        ],
                        "imageType": "user",
                        "label": "privato",
                        "phoneUrl": "https://media.immobiliare.it/text/tel_88166469_fdc9a.jpg?k=9ac0dfa294076911bc61c8d28b18e3b4"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 165000,
                    "formattedValue": "€ 165.000",
                    "priceRange": "150.001 - 200.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1121115156,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1121115156/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1144542482,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1144542482/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1144542488,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1144542488/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1055972157,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1055972157/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1055972309,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1055972309/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1121116586,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1121116586/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1055970397,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1055970397/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1055970857,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1055970857/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1055970609,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1055970609/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1055972441,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1055972441/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1055972617,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1055972617/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1055973499,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1055973499/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1121114940,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1121114940/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1121119568,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1121119568/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1144542492,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1144542492/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "bathrooms": "2",
                        "floor": {
                            "abbreviation": "1",
                            "value": "1°, con ascensore",
                            "floorOnlyValue": "1",
                            "ga4FloorValue": "1"
                        },
                        "ga4Condition": "Da ristrutturare",
                        "price": {
                            "visible": true,
                            "value": 165000,
                            "formattedValue": "€ 165.000",
                            "priceRange": "150.001 - 200.000 &euro;"
                        },
                        "rooms": "3",
                        "elevator": true,
                        "surface": "80 m²",
                        "typology": {
                            "id": 14,
                            "name": "Appartamento"
                        },
                        "typologyGA4Translation": "Appartamento",
                        "ga4features": [
                            "balcone",
                            "cantina"
                        ],
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "photo": {
                            "id": 1121115156,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1121115156/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1121115156/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1121115156/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1121115156/xxl.jpg"
                            }
                        },
                        "bedRoomsNumber": "2",
                        "location": {
                            "latitude": 41.07389069,
                            "longitude": 14.33220959,
                            "marker": "marker",
                            "region": "Campania",
                            "province": "Caserta",
                            "macrozone": "Centro",
                            "microzone": "Corso Trieste",
                            "city": "Caserta",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "rooms",
                                "label": "3 locali",
                                "compactLabel": "3"
                            },
                            {
                                "type": "surface",
                                "label": "80 m²"
                            },
                            {
                                "type": "bathrooms",
                                "label": "2 bagni",
                                "compactLabel": "2"
                            },
                            {
                                "type": "floor",
                                "label": "Piano 1",
                                "compactLabel": "1"
                            },
                            {
                                "type": "elevator",
                                "label": "Ascensore",
                                "compactLabel": "Sì"
                            },
                            {
                                "type": "balcony",
                                "label": "Balcone"
                            },
                            {
                                "type": "basement",
                                "label": "Cantina"
                            }
                        ]
                    }
                ],
                "title": "Trilocale via del Redentore 30, Corso Trieste, Caserta",
                "type": "ad",
                "typology": {
                    "id": 14,
                    "name": "Appartamento"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Trilocale via del Redentore 30, Corso Trieste, Caserta",
                "title": "Trilocale via del Redentore 30, Corso Trieste, Caserta",
                "metaTitle": "Vendita Appartamento Caserta. Trilocale in via del Redentore 30. Da ristrutturare, primo piano, con balcone, rif. 88166469",
                "url": "https://www.immobiliare.it/annunci/88166469/"
            },
            "idGeoHash": "sr61wjk2"
        },
        {
            "realEstate": {
                "dataType": "list-real-estate",
                "id": 93055138,
                "uuid": "f8591bdd-fcb1-516b-bdd7-0a472d1cfc32",
                "advertiser": {
                    "supervisor": {
                        "type": "user",
                        "imageGender": "male",
                        "phones": [],
                        "imageType": "user",
                        "label": "privato"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": true,
                    "value": 100000,
                    "formattedValue": "€ 100.000",
                    "priceRange": "fino a 100.000 &euro;"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1133971470,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1133971470/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1133971740,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1133971740/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1133971760,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1133971760/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1133971818,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1133971818/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1133971842,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1133971842/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1133971860,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1133971860/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1133971520,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1133971520/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1133971890,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1133971890/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1133971538,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1133971538/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1133971904,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1133971904/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1133971580,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1133971580/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1133971930,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1133971930/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1133971654,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1133971654/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1133971954,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1133971954/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1133971684,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1133971684/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1133971710,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1133971710/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "bathrooms": "3",
                        "floor": {
                            "abbreviation": "T",
                            "value": "Piano terra",
                            "floorOnlyValue": "piano terra",
                            "ga4FloorValue": "piano terra"
                        },
                        "ga4Condition": "Ottimo / Ristrutturato",
                        "price": {
                            "visible": true,
                            "value": 100000,
                            "formattedValue": "€ 100.000",
                            "priceRange": "fino a 100.000 &euro;"
                        },
                        "rooms": "3",
                        "surface": "100 m²",
                        "typology": {
                            "id": 14,
                            "name": "Appartamento"
                        },
                        "ga4Garage": "1 in box privato/box in garage, 1 in parcheggio/garage comune",
                        "typologyGA4Translation": "Appartamento",
                        "ga4features": [
                            "cucina",
                            "balcone",
                            "parzialmente arredato"
                        ],
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "energy": {
                            "zeroEnergyBuilding": false,
                            "thermalInsulation": null,
                            "emission": null,
                            "heatingType": "autonomo",
                            "GA4Heating": "Autonomo"
                        },
                        "photo": {
                            "id": 1133971470,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1133971470/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1133971470/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1133971470/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1133971470/xxl.jpg"
                            }
                        },
                        "bedRoomsNumber": "2",
                        "location": {
                            "latitude": 41.04669189,
                            "longitude": 14.29907036,
                            "marker": "marker",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Capodrise",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "rooms",
                                "label": "3 locali",
                                "compactLabel": "3"
                            },
                            {
                                "type": "surface",
                                "label": "100 m²"
                            },
                            {
                                "type": "bathrooms",
                                "label": "3 bagni",
                                "compactLabel": "3"
                            },
                            {
                                "type": "floor",
                                "label": "Piano T",
                                "compactLabel": "T"
                            },
                            {
                                "type": "balcony",
                                "label": "Balcone"
                            },
                            {
                                "type": "furniture",
                                "label": "Parzialmente Arredato"
                            }
                        ]
                    }
                ],
                "title": "Trilocale via San Pietro 3, Capodrise",
                "type": "ad",
                "typology": {
                    "id": 14,
                    "name": "Appartamento"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Trilocale via San Pietro 3, Capodrise",
                "title": "Trilocale via San Pietro 3, Capodrise",
                "metaTitle": "Vendita Appartamento Capodrise. Trilocale in via San Pietro 3. Ottimo stato, piano terra, posto auto, con balcone, riscaldamento autonomo, rif. 93055138",
                "url": "https://www.immobiliare.it/annunci/93055138/"
            },
            "idGeoHash": "sr61t2k6"
        },
        {
            "realEstate": {
                "dataType": "list-real-estate",
                "id": 106514431,
                "uuid": "2a77f65d-a781-5300-b1a9-39182e82716c",
                "advertiser": {
                    "supervisor": {
                        "type": "user",
                        "imageGender": "male",
                        "phones": [
                            {
                                "type": "tel1"
                            }
                        ],
                        "imageType": "user",
                        "label": "privato",
                        "phoneUrl": "https://media.immobiliare.it/text/tel_106514431_140d5.jpg?k=5ee21ff91844a6d93a878ea41b5dd076"
                    },
                    "hasCallNumbers": true
                },
                "contract": "sale",
                "isNew": false,
                "luxury": false,
                "price": {
                    "visible": false,
                    "formattedValue": "prezzo su richiesta",
                    "priceRange": "Prezzo su richiesta"
                },
                "properties": [
                    {
                        "multimedia": {
                            "photos": [
                                {
                                    "id": 1414576313,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414576313/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1414665047,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414665047/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1415517677,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1415517677/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1414578683,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414578683/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1414581505,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414581505/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1414605513,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414605513/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1414606941,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414606941/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1414604171,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414604171/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1414602695,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414602695/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1414596117,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414596117/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1414589199,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414589199/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1414589573,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414589573/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1415513707,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1415513707/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1414593421,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414593421/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1414593737,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414593737/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1414594049,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414594049/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1414619821,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414619821/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1414601909,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414601909/xxs-c.jpg"
                                    }
                                },
                                {
                                    "id": 1414610301,
                                    "caption": "",
                                    "urls": {
                                        "small": "https://pwm.im-cdn.it/image/1414610301/xxs-c.jpg"
                                    }
                                }
                            ],
                            "virtualTours": [],
                            "hasMultimedia": true
                        },
                        "bathrooms": "3+",
                        "floor": {
                            "abbreviation": null,
                            "value": "4 piani: Piano terra, Piano rialzato, da 1° a 2°",
                            "floorOnlyValue": "piano terra, piano rialzato, da 1 a 2",
                            "ga4FloorValue": "piano terra, piano rialzato, da 1 a 2"
                        },
                        "ga4Condition": "Buono / Abitabile",
                        "price": {
                            "visible": false,
                            "formattedValue": "prezzo su richiesta",
                            "priceRange": "Prezzo su richiesta"
                        },
                        "rooms": "5+",
                        "surface": "600 m²",
                        "typology": {
                            "id": 29,
                            "name": "Casale"
                        },
                        "ga4Garage": "3 in box privato/box in garage, 20 in parcheggio/garage comune",
                        "typologyGA4Translation": "Rustico - Casale",
                        "ga4features": [
                            "impianto di allarme",
                            "accesso per disabili",
                            "cucina",
                            "balcone",
                            "parzialmente arredato",
                            "cantina"
                        ],
                        "category": {
                            "id": 1,
                            "name": "Residenziale"
                        },
                        "energy": {
                            "zeroEnergyBuilding": false,
                            "thermalInsulation": null,
                            "emission": null,
                            "heatingType": "autonomo",
                            "GA4Heating": "Autonomo"
                        },
                        "photo": {
                            "id": 1414576313,
                            "caption": "",
                            "urls": {
                                "thumb": "https://pwm.im-cdn.it/image/1414576313/thumb.jpg",
                                "small": "https://pwm.im-cdn.it/image/1414576313/xxs-c.jpg",
                                "medium": "https://pwm.im-cdn.it/image/1414576313/m-c.jpg",
                                "large": "https://pwm.im-cdn.it/image/1414576313/xxl.jpg"
                            }
                        },
                        "bedRoomsNumber": "4",
                        "location": {
                            "latitude": 41.09043884,
                            "longitude": 14.29693985,
                            "marker": "marker",
                            "region": "Campania",
                            "province": "Caserta",
                            "city": "Casapulla",
                            "nation": {
                                "id": "IT",
                                "name": "Italia",
                                "keyurl": "Italia"
                            }
                        },
                        "featureList": [
                            {
                                "type": "rooms",
                                "label": "5+ locali",
                                "compactLabel": "5+"
                            },
                            {
                                "type": "surface",
                                "label": "600 m²"
                            },
                            {
                                "type": "bathrooms",
                                "label": "3+ bagni",
                                "compactLabel": "3+"
                            },
                            {
                                "type": "balcony",
                                "label": "Balcone"
                            },
                            {
                                "type": "furniture",
                                "label": "Parzialmente Arredato"
                            },
                            {
                                "type": "basement",
                                "label": "Cantina"
                            }
                        ]
                    }
                ],
                "title": "Casale via Vicinale San Giovanni, Casapulla",
                "type": "ad",
                "typology": {
                    "id": 29,
                    "name": "Casale"
                },
                "hasMainProperty": false,
                "isProjectLike": false,
                "isMosaic": false
            },
            "seo": {
                "anchor": "Casale via Vicinale San Giovanni, Casapulla",
                "title": "Casale via Vicinale San Giovanni, Casapulla",
                "metaTitle": "Vendita Casale  in via Vicinale San Giovanni Casapulla. Buono stato, posto auto, 600 m², rif. 106514431",
                "url": "https://www.immobiliare.it/annunci/106514431/"
            },
            "idGeoHash": "sr61v268"
        }
    ],
    "breadcrumbs": [
        {
            "label": "Immobiliare.it",
            "link": {
                "url": "https://www.immobiliare.it/"
            }
        },
        {
            "label": "area disegnata su mappa"
        }
    ],
    "agencies": [],
    "seoData": {
        "title": "Case in vendita - Pag. 56 - Immobiliare.it",
        "subtitle": "case in vendita",
        "description": "1.524 annunci di case in vendita. Scopri tutti gli annunci privati e di agenzie e scegli con Immobiliare.it la tua futura casa.",
        "searchName": "Case in vendita",
        "facebookSettings": {
            "prefix": "",
            "title": "Case in vendita - Pag. 56 - Immobiliare.it",
            "description": "1.524 annunci di case in vendita. Scopri tutti gli annunci privati e di agenzie e scegli con Immobiliare.it la tua futura casa.",
            "image": "",
            "subtitle": "case in vendita",
            "searchName": "Case in vendita"
        },
        "robots": null,
        "alternate": [
            {
                "rel": "alternate",
                "hreflang": "en",
                "href": "https://www.immobiliare.it/en/search-list/?idCategoria=1&idContratto=1&idNazione=IT&ordine=desc&pag=56&vrt=41.104579,14.31879;41.099017,14.272099;41.070163,14.250641;41.037542,14.272614;41.022391,14.288063;41.023298,14.324284;41.033399,14.34454;41.064339,14.362907;41.090996,14.348831;41.104579,14.31879&pag=56?pag=56"
            },
            {
                "rel": "alternate",
                "hreflang": "de",
                "href": "https://www.immobiliare.it/de/search-list/?idCategoria=1&idContratto=1&idNazione=IT&ordine=desc&pag=56&vrt=41.104579,14.31879;41.099017,14.272099;41.070163,14.250641;41.037542,14.272614;41.022391,14.288063;41.023298,14.324284;41.033399,14.34454;41.064339,14.362907;41.090996,14.348831;41.104579,14.31879&pag=56?pag=56"
            },
            {
                "rel": "alternate",
                "hreflang": "es",
                "href": "https://www.immobiliare.it/es/search-list/?idCategoria=1&idContratto=1&idNazione=IT&ordine=desc&pag=56&vrt=41.104579,14.31879;41.099017,14.272099;41.070163,14.250641;41.037542,14.272614;41.022391,14.288063;41.023298,14.324284;41.033399,14.34454;41.064339,14.362907;41.090996,14.348831;41.104579,14.31879&pag=56?pag=56"
            },
            {
                "rel": "alternate",
                "hreflang": "fr",
                "href": "https://www.immobiliare.it/fr/search-list/?idCategoria=1&idContratto=1&idNazione=IT&ordine=desc&pag=56&vrt=41.104579,14.31879;41.099017,14.272099;41.070163,14.250641;41.037542,14.272614;41.022391,14.288063;41.023298,14.324284;41.033399,14.34454;41.064339,14.362907;41.090996,14.348831;41.104579,14.31879&pag=56?pag=56"
            },
            {
                "rel": "alternate",
                "hreflang": "el",
                "href": "https://www.immobiliare.it/el/search-list/?idCategoria=1&idContratto=1&idNazione=IT&ordine=desc&pag=56&vrt=41.104579,14.31879;41.099017,14.272099;41.070163,14.250641;41.037542,14.272614;41.022391,14.288063;41.023298,14.324284;41.033399,14.34454;41.064339,14.362907;41.090996,14.348831;41.104579,14.31879&pag=56?pag=56"
            },
            {
                "rel": "alternate",
                "hreflang": "pt",
                "href": "https://www.immobiliare.it/pt/search-list/?idCategoria=1&idContratto=1&idNazione=IT&ordine=desc&pag=56&vrt=41.104579,14.31879;41.099017,14.272099;41.070163,14.250641;41.037542,14.272614;41.022391,14.288063;41.023298,14.324284;41.033399,14.34454;41.064339,14.362907;41.090996,14.348831;41.104579,14.31879&pag=56?pag=56"
            },
            {
                "rel": "alternate",
                "hreflang": "ru",
                "href": "https://www.immobiliare.it/ru/search-list/?idCategoria=1&idContratto=1&idNazione=IT&ordine=desc&pag=56&vrt=41.104579,14.31879;41.099017,14.272099;41.070163,14.250641;41.037542,14.272614;41.022391,14.288063;41.023298,14.324284;41.033399,14.34454;41.064339,14.362907;41.090996,14.348831;41.104579,14.31879&pag=56?pag=56"
            },
            {
                "rel": "alternate",
                "hreflang": "it",
                "href": "https://www.immobiliare.it/search-list/?idCategoria=1&idContratto=1&idNazione=IT&ordine=desc&pag=56&vrt=41.104579,14.31879;41.099017,14.272099;41.070163,14.250641;41.037542,14.272614;41.022391,14.288063;41.023298,14.324284;41.033399,14.34454;41.064339,14.362907;41.090996,14.348831;41.104579,14.31879&pag=56?pag=56"
            },
            {
                "rel": "alternate",
                "hreflang": "x-default",
                "href": "https://www.immobiliare.it/search-list/?idCategoria=1&idContratto=1&idNazione=IT&ordine=desc&pag=56&vrt=41.104579,14.31879;41.099017,14.272099;41.070163,14.250641;41.037542,14.272614;41.022391,14.288063;41.023298,14.324284;41.033399,14.34454;41.064339,14.362907;41.090996,14.348831;41.104579,14.31879&pag=56?pag=56"
            }
        ],
        "canonical": "https://www.immobiliare.it/search-list/?idCategoria=1&idContratto=1&idNazione=IT&ordine=desc&pag=56&vrt=41.104579,14.31879;41.099017,14.272099;41.070163,14.250641;41.037542,14.272614;41.022391,14.288063;41.023298,14.324284;41.033399,14.34454;41.064339,14.362907;41.090996,14.348831;41.104579,14.31879&pag=56?pag=56",
        "appleItunesApp": {
            "appId": 335948517,
            "affiliateData": "ct=Smart-banner-safari&pt=304468",
            "appArgument": "immogrp2://urlrev=2"
        },
        "prevPage": "https://www.immobiliare.it/search-list/?idCategoria=1&idContratto=1&idNazione=IT&ordine=desc&pag=55&vrt=41.104579%2C14.31879%3B41.099017%2C14.272099%3B41.070163%2C14.250641%3B41.037542%2C14.272614%3B41.022391%2C14.288063%3B41.023298%2C14.324284%3B41.033399%2C14.34454%3B41.064339%2C14.362907%3B41.090996%2C14.348831%3B41.104579%2C14.31879",
        "nextPage": "https://www.immobiliare.it/search-list/?idCategoria=1&idContratto=1&idNazione=IT&ordine=desc&pag=57&vrt=41.104579%2C14.31879%3B41.099017%2C14.272099%3B41.070163%2C14.250641%3B41.037542%2C14.272614%3B41.022391%2C14.288063%3B41.023298%2C14.324284%3B41.033399%2C14.34454%3B41.064339%2C14.362907%3B41.090996%2C14.348831%3B41.104579%2C14.31879"
    },
    "relatedSearches": {
        "title": null,
        "data": []
    },
    "suggestedSearchData": {
        "token": "1e528a82286ee1201930d5c5478c80d4",
        "verticaleSito": "annunci_residenziali"
    },
    "currentPage": 56,
    "maxPages": 61
}"""

count_page=1
#url=f"https://www.immobiliare.it/api-next/search-list/real-estates/?vrt=41.104579%2C14.31879%3B41.099017%2C14.272099%3B41.070163%2C14.250641%3B41.037542%2C14.272614%3B41.022391%2C14.288063%3B41.023298%2C14.324284%3B41.033399%2C14.34454%3B41.064339%2C14.362907%3B41.090996%2C14.348831%3B41.104579%2C14.31879&idContratto=1&idCategoria=1&__lang=it&pag={count_page}&paramsCount=6&path=%2Fsearch-list%2F"
_DEBUG=False
_DELAY=15
logging.basicConfig(
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s %(message)s",
)


def fetch_data(page_number):
    url=f"https://www.immobiliare.it/api-next/search-list/real-estates/?vrt=41.104579%2C14.31879%3B41.099017%2C14.272099%3B41.070163%2C14.250641%3B41.037542%2C14.272614%3B41.022391%2C14.288063%3B41.023298%2C14.324284%3B41.033399%2C14.34454%3B41.064339%2C14.362907%3B41.090996%2C14.348831%3B41.104579%2C14.31879&idContratto=1&idCategoria=1&boxAuto[0]=1&boxAuto[1]=3&boxAuto[2]=4&__lang=it&minLat=39.156826&maxLat=42.913068&minLng=14.229242&maxLng=14.379274&pag={page_number}&paramsCount=11&path=%2Fsearch-list%2F"

    logging.debug(url)
    logging.debug(" ")
    logging.debug(" ")

    try:
        response = requests.get(url)
        logging.debug(response)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse response as JSON
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error during HTTP request: {e}")
        return None
    except ValueError:
        print("Error decoding JSON response.")
        return None


def start_search_scraping():
    count_page=1
    _DEBUG=False
    _DELAY=15
    if not _DEBUG:
        logging.info(
            "Debug is disabled. You can define DEBUG environment variable to enable it."
        )
    else:
        logging.getLogger().setLevel(logging.DEBUG)
    json_data =fetch_data(count_page)
    logging.debug(json_data['count'])
    max_page=json_data['maxPages']
    logging.info(f"Number of pages  {max_page}")
    yield f"Number of pages  {max_page}"
    while count_page <= max_page:
        time.sleep(_DELAY)
        logging.info(f"Risultati in pagina {count_page}")
        yield f"Risultati in pagina {count_page}"
        json_data = fetch_data(count_page)
        results = json_data['results']
        count_page=int(count_page) + 1
        for res in results:
            logging.debug(res['realEstate'])
            logging.debug(" ")
            advertiser = res.get('realEstate', {}).get('advertiser', {})
            if 'supervisor' in advertiser:
            ### here check if label is privato or label exists. If not, it should be private anyway
            ##    if advertiser['supervisor']['label'] == 'privato':
                if (
                    'supervisor' in advertiser and 
                    isinstance(advertiser['supervisor'], dict) and
                    (
                        ##'label' in advertiser['supervisor'] or 
                        ('type' in advertiser['supervisor'] and advertiser['supervisor']['type'] == 'user')
                    )
                ):   
                    house = JsonObject(
                        id=res['realEstate']['id'],  # Directly assign value, no {}
                        title=res['seo']['title'],  # Directly assign value, no {}
                        price = res['realEstate']['price'].get('value', res['realEstate']['price'].get('formattedValue')), ##Get value if not found is needed due to price private
                        formattedValue=res['realEstate']['price']['formattedValue'],  # Directly assign value, no {}
                        link=res['seo']['url'],  # Directly assign value, no {}
                        img=res['realEstate']['properties'][0]['photo']['urls']['medium'],
                        date_added=str(date.today()),
                        clicked=False)  # Correct date format
                       
                    yield from addEntry(house)

                    logging.info(f"Titolo: {res['seo']['title']} - {res['realEstate']['price']['formattedValue']} ")
                    logging.info(f"Link: {res['seo']['url']}")
                    logging.info(house.price)
                    




if __name__ == "__main__":
    start_search_scraping()