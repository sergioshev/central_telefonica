# $Id: getLocation.py,v 1.4 2012-03-20 17:27:36 sshevtsov Exp $
# -*- coding: utf-8 -*-
# No eliminar la linea de arriba. Es para que el interprete trate el codigo 
#   como utf8, ese magico tiene que ser primera o segunda linea.

from sys import stdout
import argparse
areaCodesTree={
      '1':
        {
          '1':
            {
              'name':u'Ciudad de Buenos Aires y Alrededores'
            },
          'name':None
        },
      '3':
        {
          'name':None,
          '3':
            {
              '8':
                {
                  '8':
                    {
                      'name':u'General Villegas'
                    },
                  '2':
                    {
                      'name':u'Rufino'
                    },
                  '5':
                    {
                      'name':u'Laboulaye'
                    },
                  'name':None,
                  '7':
                    {
                      'name':u'Bouchard'
                    }
                },
              '2':
                {
                  '9':
                    {
                      'name':u'San Pedro (Prov. Buenos Aires)'
                    },
                  'name':None,
                  '7':
                    {
                      'name':u'Lopez Camelo'
                    }
                },
              'name':None
            },
          '5':
            {
              'name':None,
              '1':
                {
                  'name':u'Cordoba'
                },
              '3':
                {
                  '3':
                    {
                      'name':u'Las Varillas'
                    },
                  '2':
                    {
                      'name':u'Oliva'
                    },
                  'name':u'Villa Maria',
                  '4':
                    {
                      'name':u'Bell Ville'
                    }
                },
              '2':
                {
                  '1':
                    {
                      'name':u'Dean Funes'
                    },
                  '2':
                    {
                      'name':u'Villa De Maria De Rio Seco'
                    },
                  '5':
                    {
                      'name':u'Jesus Maria'
                    },
                  'name':None,
                  '4':
                    {
                      'name':u'Villa Del Totoral'
                    }
                },
              '4':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'Villa Carlos Paz'
                    },
                  '3':
                    {
                      'name':u'Argüello'
                    },
                  '2':
                    {
                      'name':u'Salsacate'
                    },
                  '4':
                    {
                      'name':u'Villa Dolores'
                    },
                  '7':
                    {
                      'name':u'Alta Gracia'
                    },
                  '6':
                    {
                      'name':u'Santa Rosa De Calamuchita'
                    },
                  '9':
                    {
                      'name':u'Cruz Del Eje'
                    },
                  '8':
                    {
                      'name':u'La Falda'
                    }
                },
              '7':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'Rio Tercero'
                    },
                  '3':
                    {
                      'name':u'Villa Del Rosario (Prov. Cordoba)'
                    },
                  '2':
                    {
                      'name':u'Rio Segundo'
                    },
                  '5':
                    {
                      'name':u'La Puerta (Prov. Cordoba)'
                    },
                  '4':
                    {
                      'name':u'Rio Primero'
                    },
                  '6':
                    {
                      'name':u'Arroyito (Prov. Cordoba)'
                    }
                },
              '6':
                {
                  '3':
                    {
                      'name':u'Balnearia'
                    },
                  '2':
                    {
                      'name':u'Morteros'
                    },
                  'name':None,
                  '4':
                    {
                      'name':u'San Francisco (Prov. Cordoba)'
                    }
                },
              '8':
                {
                  '3':
                    {
                      'name':u'Vicuña Mackenna'
                    },
                  '2':
                    {
                      'name':u'Sampacho'
                    },
                  '5':
                    {
                      'name':u'Adelia Maria'
                    },
                  'name':u'Rio Cuarto',
                  '4':
                    {
                      'name':u'La Carlota'
                    }
                }
            },
          '4':
            {
              'name':None,
              '1':
                {
                  'name':u'Rosario'
                },
              '0':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'El Trebol'
                    },
                  '0':
                    {
                      'name':u'Villa Constitucion'
                    },
                  '2':
                    {
                      'name':u'Arroyo Seco'
                    },
                  '5':
                    {
                      'name':u'San Javier (Prov. Santa Fe)'
                    },
                  '4':
                    {
                      'name':u'San Carlos Centro'
                    },
                  '7':
                    {
                      'name':u'Ramallo'
                    },
                  '6':
                    {
                      'name':u'San Jorge (Prov. Santa Fe)'
                    },
                  '9':
                    {
                      'name':u'Moises Ville'
                    },
                  '8':
                    {
                      'name':u'San Cristobal'
                    }
                },
              '3':
                {
                  '8':
                    {
                      'name':u'Bovril'
                    },
                  '5':
                    {
                      'name':u'Nogoya'
                    },
                  'name':u'Parana',
                  '7':
                    {
                      'name':u'La Paz (Prov. Entre Rios)'
                    },
                  '6':
                    {
                      'name':u'Victoria'
                    }
                },
              '2':
                {
                  'name':u'Santa Fe'
                },
              '5':
                {
                  '8':
                    {
                      'name':u'San Jose De Feliciano'
                    },
                  '6':
                    {
                      'name':u'Chajari'
                    },
                  '5':
                    {
                      'name':u'Villaguay'
                    },
                  'name':u'Concordia',
                  '4':
                    {
                      'name':u'Federal'
                    }
                },
              '4':
                {
                  'name':None,
                  '2':
                    {
                      'name':u'Concepcion Del Uruguay'
                    },
                  '5':
                    {
                      'name':u'Rosario Del Tala'
                    },
                  '4':
                    {
                      'name':u'Gualeguay'
                    },
                  '7':
                    {
                      'name':u'Colon (Prov. Entre Rios)'
                    },
                  '6':
                    {
                      'name':u'Gualeguaychu'
                    }
                },
              '7':
                {
                  '1':
                    {
                      'name':u'Cañada De Gomez'
                    },
                  '2':
                    {
                      'name':u'Marcos Juarez'
                    },
                  'name':None,
                  '6':
                    {
                      'name':u'San Lorenzo (Prov. Santa Fe)'
                    }
                },
              '6':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'San Nicolas'
                    },
                  '0':
                    {
                      'name':u'Santa Teresa (Prov. Santa Fe)'
                    },
                  '3':
                    {
                      'name':u'Canals'
                    },
                  '2':
                    {
                      'name':u'Venado Tuerto'
                    },
                  '5':
                    {
                      'name':u'Firmat'
                    },
                  '4':
                    {
                      'name':u'Casilda'
                    },
                  '7':
                    {
                      'name':u'Cruz Alta'
                    },
                  '6':
                    {
                      'name':u'Barrancas (Prov. Santa Fe)'
                    },
                  '9':
                    {
                      'name':u'Acebal'
                    },
                  '8':
                    {
                      'name':u'Corral De Bustos'
                    }
                },
              '9':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'Ceres'
                    },
                  '3':
                    {
                      'name':u'Sunchales'
                    },
                  '2':
                    {
                      'name':u'Rafaela'
                    },
                  '7':
                    {
                      'name':u'Llambi Campbell'
                    },
                  '6':
                    {
                      'name':u'Esperanza (Prov. Santa Fe)'
                    },
                  '8':
                    {
                      'name':u'San Justo (Prov. Santa Fe)'
                    }
                },
              '8':
                {
                  'name':None,
                  '3':
                    {
                      'name':u'Vera'
                    },
                  '2':
                    {
                      'name':u'Reconquista'
                    },
                  '7':
                    {
                      'name':u'Zarate'
                    },
                  '9':
                    {
                      'name':u'Campana'
                    },
                  '8':
                    {
                      'name':u'Escobar'
                    }
                }
            },
          '7':
            {
              'name':None,
              '1':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'Ingeniero Guillermo N. Juarez'
                    },
                  '5':
                    {
                      'name':u'Las Lomitas'
                    },
                  '7':
                    {
                      'name':u'Formosa'
                    },
                  '6':
                    {
                      'name':u'Ibarreta'
                    },
                  '8':
                    {
                      'name':u'Clorinda'
                    }
                },
              '3':
                {
                  '1':
                    {
                      'name':u'Charata'
                    },
                  '2':
                    {
                      'name':u'Presidencia Roque Saenz Peña'
                    },
                  '5':
                    {
                      'name':u'Villa Angela'
                    },
                  'name':None,
                  '4':
                    {
                      'name':u'Presidencia De La Plaza'
                    }
                },
              '2':
                {
                  '1':
                    {
                      'name':u'Charadai'
                    },
                  '2':
                    {
                      'name':u'Resistencia'
                    },
                  '5':
                    {
                      'name':u'General Jose De San Martin'
                    },
                  'name':None
                },
              '5':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'Eldorado'
                    },
                  '2':
                    {
                      'name':u'Posadas'
                    },
                  '5':
                    {
                      'name':u'Obera'
                    },
                  '4':
                    {
                      'name':u'Leandro N. Alem (Prov. Misiones)'
                    },
                  '7':
                    {
                      'name':u'Puerto Iguazu'
                    },
                  '6':
                    {
                      'name':u'Santo Tome'
                    },
                  '8':
                    {
                      'name':u'Apostoles'
                    }
                },
              '4':
                {
                  '1':
                    {
                      'name':u'Bernardo De Irigoyen'
                    },
                  '3':
                    {
                      'name':u'Puerto Rico'
                    },
                  'name':None
                },
              '7':
                {
                  'name':None,
                  '3':
                    {
                      'name':u'Mercedes (Prov. Corrientes)'
                    },
                  '2':
                    {
                      'name':u'Paso De Los Libres'
                    },
                  '5':
                    {
                      'name':u'Monte Caseros'
                    },
                  '4':
                    {
                      'name':u'Curuzu Cuatia'
                    },
                  '7':
                    {
                      'name':u'Goya'
                    }
                },
              '8':
                {
                  '1':
                    {
                      'name':u'Caa Cati'
                    },
                  '3':
                    {
                      'name':u'Corrientes'
                    },
                  '2':
                    {
                      'name':u'Saladas'
                    },
                  'name':None,
                  '6':
                    {
                      'name':u'Ituzaingo'
                    }
                }
            },
          '8':
            {
              'name':None,
              '1':
                {
                  'name':u'San Miguel De Tucuman'
                },
              '3':
                {
                  'name':None,
                  '3':
                    {
                      'name':u'Catamarca'
                    },
                  '2':
                    {
                      'name':u'Recreo (Prov. Catamarca)'
                    },
                  '5':
                    {
                      'name':u'Andalgala'
                    },
                  '7':
                    {
                      'name':u'Tinogasta'
                    },
                  '8':
                    {
                      'name':u'Santa Maria (Prov. Catamarca)'
                    }
                },
              '2':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'Chepes'
                    },
                  '2':
                    {
                      'name':u'La Rioja'
                    },
                  '5':
                    {
                      'name':u'Chilecito'
                    },
                  '7':
                    {
                      'name':u'Aimogasta'
                    },
                  '6':
                    {
                      'name':u'Chamical'
                    }
                },
              '5':
                {
                  'name':u'Santiago Del Estero',
                  '5':
                    {
                      'name':u'Suncho Corral'
                    },
                  '4':
                    {
                      'name':u'Frias'
                    },
                  '7':
                    {
                      'name':u'Bandera'
                    },
                  '6':
                    {
                      'name':u'Ojo De Agua (Santiago Del Estero)'
                    },
                  '8':
                    {
                      'name':u'Termas De Rio Hondo'
                    }
                },
              '4':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'Monte Quemado'
                    },
                  '3':
                    {
                      'name':u'Quimili'
                    },
                  '5':
                    {
                      'name':u'Loreto'
                    },
                  '4':
                    {
                      'name':u'Añatuya'
                    },
                  '6':
                    {
                      'name':u'Tintina'
                    }
                },
              '7':
                {
                  '8':
                    {
                      'name':u'Oran'
                    },
                  '5':
                    {
                      'name':u'Tartagal (Prov. Salta)'
                    },
                  'name':u'Salta',
                  '7':
                    {
                      'name':u'Joaquin V. Gonzalez'
                    },
                  '6':
                    {
                      'name':u'Metan'
                    }
                },
              '6':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'Nueva Esperanza'
                    },
                  '3':
                    {
                      'name':u'Monteros'
                    },
                  '2':
                    {
                      'name':u'Trancas'
                    },
                  '5':
                    {
                      'name':u'Concepcion (Prov. Tucuman)'
                    },
                  '7':
                    {
                      'name':u'Tafi Del Valle'
                    },
                  '9':
                    {
                      'name':u'Ranchillos'
                    },
                  '8':
                    {
                      'name':u'Cafayate'
                    }
                },
              '9':
                {
                  '1':
                    {
                      'name':u'La Madrid'
                    },
                  '2':
                    {
                      'name':u'Amaicha Del Valle'
                    },
                  'name':None,
                  '4':
                    {
                      'name':u'Burruyacu'
                    }
                },
              '8':
                {
                  '6':
                    {
                      'name':u'Libertador General San Martin'
                    },
                  '5':
                    {
                      'name':u'La Quiaca'
                    },
                  'name':u'San Salvador De Jujuy',
                  '7':
                    {
                      'name':u'Humahuaca'
                    },
                  '4':
                    {
                      'name':u'San Pedro (Prov. Jujuy)'
                    }
                }
            }
        },
      '2':
        {
          'name':None,
          '3':
            {
              'name':None,
              '1':
                {
                  '6':
                    {
                      'name':u'Daireaux'
                    },
                  'name':None,
                  '7':
                    {
                      'name':u'9 De Julio (Prov. Buenos Aires)'
                    },
                  '4':
                    {
                      'name':u'Bolivar'
                    }
                },
              '0':
                {
                  '2':
                    {
                      'name':u'General Pico'
                    },
                  'name':None
                },
              '3':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'Realico'
                    },
                  '3':
                    {
                      'name':u'Quemu Quemu'
                    },
                  '5':
                    {
                      'name':u'Caleufu'
                    },
                  '4':
                    {
                      'name':u'Eduardo Castex'
                    },
                  '7':
                    {
                      'name':u'America'
                    },
                  '6':
                    {
                      'name':u'Huinca Renanco'
                    },
                  '8':
                    {
                      'name':u'Victorica'
                    }
                },
              '2':
                {
                  'name':None,
                  '0':
                    {
                      'name':u'Jose C. Paz'
                    },
                  '3':
                    {
                      'name':u'Lujan (Prov. Buenos Aires)'
                    },
                  '2':
                    {
                      'name':u'Pilar (Prov. Buenos Aires)'
                    },
                  '5':
                    {
                      'name':u'San Andres De Giles'
                    },
                  '4':
                    {
                      'name':u'Mercedes (Prov. Buenos Aires)'
                    },
                  '6':
                    {
                      'name':u'San Antonio De Areco'
                    }
                },
              '5':
                {
                  'name':None,
                  '3':
                    {
                      'name':u'General Arenales'
                    },
                  '2':
                    {
                      'name':u'Chacabuco'
                    },
                  '5':
                    {
                      'name':u'Lincoln'
                    },
                  '4':
                    {
                      'name':u'Vedia'
                    },
                  '7':
                    {
                      'name':u'Carlos Tejedor'
                    },
                  '6':
                    {
                      'name':u'General Pinto'
                    },
                  '8':
                    {
                      'name':u'Los Toldos (Prov. Buenos Aires)'
                    }
                },
              '4':
                {
                  'name':None,
                  '3':
                    {
                      'name':u'Norberto De La Riestra'
                    },
                  '2':
                    {
                      'name':u'Bragado'
                    },
                  '5':
                    {
                      'name':u'25 De Mayo (Prov. Buenos Aires)'
                    },
                  '4':
                    {
                      'name':u'Saladillo (Prov. Buenos Aires)'
                    },
                  '6':
                    {
                      'name':u'Chivilcoy'
                    }
                },
              '7':
                {
                  'name':u'Moreno'
                },
              '6':
                {
                  '2':
                    {
                      'name':u'Junin (Prov. Buenos Aires)'
                    },
                  'name':None
                },
              '9':
                {
                  'name':None,
                  '3':
                    {
                      'name':u'Salazar'
                    },
                  '2':
                    {
                      'name':u'Trenque Lauquen'
                    },
                  '5':
                    {
                      'name':u'Carlos Casares'
                    },
                  '4':
                    {
                      'name':u'Tres Lomas'
                    },
                  '6':
                    {
                      'name':u'Pehuajo'
                    }
                }
            },
          '2':
            {
              'name':None,
              '1':
                {
                  'name':u'La Plata'
                },
              '0':
                {
                  '2':
                    {
                      'name':u'Gonzalez Catan'
                    },
                  'name':u'Merlo (Prov. Buenos Aires)'
                },
              '3':
                {
                  'name':u'Mar Del Plata'
                },
              '2':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'Magdalena'
                    },
                  '3':
                    {
                      'name':u'Coronel Brandsen'
                    },
                  '5':
                    {
                      'name':u'Alejandro Korn'
                    },
                  '4':
                    {
                      'name':u'Glew'
                    },
                  '7':
                    {
                      'name':u'Lobos'
                    },
                  '6':
                    {
                      'name':u'Cañuelas'
                    },
                  '9':
                    {
                      'name':u'Juan Maria Gutierrez'
                    }
                },
              '5':
                {
                  '2':
                    {
                      'name':u'San Clemente Del Tuyu'
                    },
                  '5':
                    {
                      'name':u'Villa Gesell'
                    },
                  'name':None,
                  '7':
                    {
                      'name':u'Mar De Ajo'
                    },
                  '4':
                    {
                      'name':u'Pinamar'
                    }
                },
              '4':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'Chascomus'
                    },
                  '3':
                    {
                      'name':u'General Belgrano'
                    },
                  '2':
                    {
                      'name':u'Lezama'
                    },
                  '5':
                    {
                      'name':u'Dolores (Prov. Buenos Aires)'
                    },
                  '4':
                    {
                      'name':u'Las Flores (Prov. Buenos Aires)'
                    },
                  '6':
                    {
                      'name':u'Santa Teresita'
                    }
                },
              '7':
                {
                  '1':
                    {
                      'name':u'Monte'
                    },
                  '3':
                    {
                      'name':u'Carmen De Areco'
                    },
                  '2':
                    {
                      'name':u'Navarro'
                    },
                  'name':None,
                  '4':
                    {
                      'name':u'Carlos Spegazzini'
                    }
                },
              '6':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'Loberia'
                    },
                  '2':
                    {
                      'name':u'Necochea'
                    },
                  '5':
                    {
                      'name':u'Coronel Vidal'
                    },
                  '4':
                    {
                      'name':u'La Dulce'
                    },
                  '7':
                    {
                      'name':u'General Madariaga'
                    },
                  '6':
                    {
                      'name':u'Balcarce'
                    },
                  '8':
                    {
                      'name':u'Maipu (Prov. Buenos Aires)'
                    }
                },
              '9':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'Miramar (Prov. Buenos Aires)'
                    },
                  '3':
                    {
                      'name':u'Tandil'
                    },
                  '2':
                    {
                      'name':u'Benito Juarez'
                    },
                  '7':
                    {
                      'name':u'Rauch'
                    },
                  '6':
                    {
                      'name':u'Ayacucho'
                    }
                },
              '8':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'Azul'
                    },
                  '3':
                    {
                      'name':u'Tapalque'
                    },
                  '5':
                    {
                      'name':u'Laprida'
                    },
                  '4':
                    {
                      'name':u'Olavarria'
                    },
                  '6':
                    {
                      'name':u'General Lamadrid'
                    }
                }
            },
          '4':
            {
              'name':None,
              '7':
                {
                  'name':None,
                  '3':
                    {
                      'name':u'Colon (Prov. Buenos Aires)'
                    },
                  '5':
                    {
                      'name':u'Rojas'
                    },
                  '4':
                    {
                      'name':u'Salto'
                    },
                  '7':
                    {
                      'name':u'Pergamino'
                    },
                  '8':
                    {
                      'name':u'Arrecifes'
                    }
                }
            },
          '6':
            {
              '1':
                {
                  'name':u'Mendoza'
                },
              '2':
                {
                  'name':None,
                  '3':
                    {
                      'name':u'San Martin (Prov. Mendoza)'
                    },
                  '2':
                    {
                      'name':u'Tunuyan'
                    },
                  '5':
                    {
                      'name':u'General Alvear (Prov. Mendoza)'
                    },
                  '4':
                    {
                      'name':u'Uspallata'
                    },
                  '7':
                    {
                      'name':u'San Rafael (Prov. Mendoza)'
                    },
                  '6':
                    {
                      'name':u'La Paz (Prov. Mendoza)'
                    }
                },
              '5':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'San Francisco Del Monte De Oro'
                    },
                  '2':
                    {
                      'name':u'San Luis (Prov. San Luis)'
                    },
                  '5':
                    {
                      'name':u'La Toma'
                    },
                  '7':
                    {
                      'name':u'Mercedes (Prov. San Luis)'
                    },
                  '6':
                    {
                      'name':u'Tilisarao'
                    },
                  '8':
                    {
                      'name':u'Buena Esperanza'
                    }
                },
              'name':None,
              '4':
                {
                  '8':
                    {
                      'name':u'Calingasta'
                    },
                  'name':u'San Juan',
                  '7':
                    {
                      'name':u'Jachal'
                    },
                  '6':
                    {
                      'name':u'San Agustin Del Valle Fertil'
                    }
                }
            },
          '9':
            {
              'name':None,
              '1':
                {
                  'name':u'Bahia Blanca'
                },
              '0':
                {
                  '1':
                    {
                      'name':u'Ushuaia'
                    },
                  '3':
                    {
                      'name':u'Rio Mayo'
                    },
                  '2':
                    {
                      'name':u'Rio Turbio'
                    },
                  'name':None
                },
              '3':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'Rio Colorado (Prov. Rio Negro)'
                    },
                  '3':
                    {
                      'name':u'Huanguelen Sur'
                    },
                  '2':
                    {
                      'name':u'Punta Alta'
                    },
                  '5':
                    {
                      'name':u'Rivera'
                    },
                  '4':
                    {
                      'name':u'San Antonio Oeste'
                    },
                  '6':
                    {
                      'name':u'Carhue'
                    }
                },
              '2':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'Coronel Dorrego'
                    },
                  '0':
                    {
                      'name':u'Viedma'
                    },
                  '3':
                    {
                      'name':u'Pigüe'
                    },
                  '2':
                    {
                      'name':u'Coronel Pringles'
                    },
                  '5':
                    {
                      'name':u'Villa Iris'
                    },
                  '4':
                    {
                      'name':u'Darregueira'
                    },
                  '7':
                    {
                      'name':u'Medanos (Prov. Buenos Aires)'
                    },
                  '6':
                    {
                      'name':u'Coronel Suarez'
                    },
                  '9':
                    {
                      'name':u'Guamini'
                    },
                  '8':
                    {
                      'name':u'Pedro Luro'
                    }
                },
              '5':
                {
                  '3':
                    {
                      'name':u'Macachin'
                    },
                  '2':
                    {
                      'name':u'General Acha'
                    },
                  'name':None,
                  '4':
                    {
                      'name':u'Santa Rosa (Prov. La Pampa)'
                    }
                },
              '4':
                {
                  'name':None,
                  '1':
                    {
                      'name':u'General Roca (Prov. Rio Negro)'
                    },
                  '0':
                    {
                      'name':u'Ingeniero Jacobacci'
                    },
                  '2':
                    {
                      'name':u'Zapala'
                    },
                  '5':
                    {
                      'name':u'Esquel'
                    },
                  '4':
                    {
                      'name':u'San Carlos De Bariloche'
                    },
                  '6':
                    {
                      'name':u'Choele Choel'
                    },
                  '8':
                    {
                      'name':u'Chos Malal'
                    }
                },
              '7':
                {
                  '2':
                    {
                      'name':u'San Martin De Los Andes'
                    },
                  'name':u'Comodoro Rivadavia'
                },
              '6':
                {
                  'name':None,
                  '3':
                    {
                      'name':u'Perito Moreno'
                    },
                  '2':
                    {
                      'name':u'San Julian'
                    },
                  '5':
                    {
                      'name':u'Trelew'
                    },
                  '4':
                    {
                      'name':u'Rio Grande (Prov. Tierra Del Fuego)'
                    },
                  '6':
                    {
                      'name':u'Rio Gallegos'
                    }
                },
              '9':
                {
                  'name':u'Neuquen'
                },
              '8':
                {
                  '3':
                    {
                      'name':u'Tres Arroyos'
                    },
                  '2':
                    {
                      'name':u'Orense'
                    },
                  'name':None
                }
            }
        }
    }


countriesCodesTree={
      '1':
        {
          'name':u'Estados Unidos/Canada',
          '3':
            {
              'name':None,
              '4':
                {
                  '0':
                    {
                      'name':u'Islas Vírgenes Estados Unidos'
                    },
                  '5':
                    {
                      'name':u'Caimanes'
                    },
                  'name':None
                }
            },
          '2':
            {
              '8':
                {
                  'name':None,
                  '4':
                    {
                      'name':u'Islas Vírgenes Británicas'
                    }
                },
              '4':
                {
                  '2':
                    {
                      'name':u'Antigua y Barbuda'
                    },
                  'name':None,
                  '6':
                    {
                      'name':u'Barbados'
                    }
                },
              'name':None,
              '6':
                {
                  'name':None,
                  '4':
                    {
                      'name':u'Anguilla'
                    }
                }
            },
          '4':
            {
              '9':
                {
                  '3':
                    {
                      'name':u'Granada'
                    },
                  'name':None
                },
              'name':None,
              '4':
                {
                  '1':
                    {
                      'name':u'Bermudas'
                    },
                  'name':None
                }
            },
          '7':
            {
              '8':
                {
                  'name':None,
                  '7':
                    {
                      'name':u'Puerto Rico'
                    },
                  '4':
                    {
                      'name':u'San Vicente y las Granadinas'
                    }
                },
              '5':
                {
                  '8':
                    {
                      'name':u'Santa Lucia'
                    },
                  'name':None
                },
              'name':None,
              '6':
                {
                  'name':None,
                  '7':
                    {
                      'name':u'Dominica'
                    }
                }
            },
          '6':
            {
              '8':
                {
                  'name':None,
                  '4':
                    {
                      'name':u'Samoa Americana'
                    }
                },
              '4':
                {
                  '9':
                    {
                      'name':u'Turks y Caicos'
                    },
                  'name':None
                },
              'name':None,
              '7':
                {
                  '1':
                    {
                      'name':u'Guam'
                    },
                  'name':None
                },
              '6':
                {
                  'name':None,
                  '4':
                    {
                      'name':u'Montserrat'
                    }
                }
            },
          '9':
            {
              '0':
                {
                  'name':None,
                  '7':
                    {
                      'name':u'Alaska'
                    }
                },
              'name':None
            },
          '8':
            {
              '0':
                {
                  '9':
                    {
                      'name':u'República Dominicana'
                    },
                  '8':
                    {
                      'name':u'Hawai'
                    },
                  'name':None
                },
              'name':None,
              '7':
                {
                  'name':None,
                  '6':
                    {
                      'name':u'Jamaica'
                    }
                },
              '6':
                {
                  '9':
                    {
                      'name':u'San Cristobal y Nieves'
                    },
                  '8':
                    {
                      'name':u'Trinidad y Tobago'
                    },
                  'name':None
                }
            }
        },
      '3':
        {
          'name':None,
          '1':
            {
              'name':u'Holanda'
            },
          '0':
            {
              'name':u'Grecia'
            },
          '3':
            {
              'name':u'Francia'
            },
          '2':
            {
              'name':u'Belgica'
            },
          '5':
            {
              'name':None,
              '1':
                {
                  'name':u'Portugal'
                },
              '3':
                {
                  'name':u'Irlanda'
                },
              '2':
                {
                  'name':u'Luxemburgo'
                },
              '5':
                {
                  'name':u'Albania'
                },
              '4':
                {
                  'name':u'Islandia'
                },
              '7':
                {
                  'name':u'Chipre'
                },
              '6':
                {
                  'name':u'Malta'
                },
              '9':
                {
                  'name':u'Bulgaria'
                },
              '8':
                {
                  'name':u'Finlandia'
                }
            },
          '7':
            {
              'name':None,
              '1':
                {
                  'name':u'Letonia'
                },
              '0':
                {
                  'name':u'Lituania'
                },
              '3':
                {
                  'name':u'Moldavia'
                },
              '2':
                {
                  'name':u'Estonia'
                },
              '5':
                {
                  'name':u'Bielorrusia'
                },
              '4':
                {
                  'name':u'Armenia'
                },
              '7':
                {
                  'name':u'Monaco'
                },
              '6':
                {
                  'name':u'Andorra'
                },
              '8':
                {
                  'name':u'San Marino'
                }
            },
          '6':
            {
              'name':u'Hungria'
            },
          '9':
            {
              'name':u'Italia'
            },
          '8':
            {
              'name':None,
              '1':
                {
                  'name':u'Serbia'
                },
              '0':
                {
                  'name':u'Ucrania'
                },
              '2':
                {
                  'name':u'Montenegro'
                },
              '5':
                {
                  'name':u'Croacia'
                },
              '6':
                {
                  'name':u'Eslovenia'
                },
              '9':
                {
                  'name':u'Macedonia'
                }
            }
        },
      '2':
        {
          'name':None,
          '1':
            {
              '8':
                {
                  'name':u'Libia'
                },
              '3':
                {
                  'name':u'Argelia'
                },
              '2':
                {
                  'name':u'Marruecos'
                },
              'name':None,
              '6':
                {
                  'name':u'Tunez'
                }
            },
          '0':
            {
              'name':u'Egipto'
            },
          '3':
            {
              'name':None,
              '1':
                {
                  'name':u'Liberia'
                },
              '0':
                {
                  'name':u'Mauricio'
                },
              '3':
                {
                  'name':u'Ghana'
                },
              '2':
                {
                  'name':u'Sierra Leona'
                },
              '5':
                {
                  'name':u'Chad'
                },
              '4':
                {
                  'name':u'Nigeria'
                },
              '7':
                {
                  'name':u'Camerun'
                },
              '6':
                {
                  'name':u'República Centroafrinaca'
                },
              '9':
                {
                  'name':u'Santo Tome y Principe'
                },
              '8':
                {
                  'name':u'Cabo Verde'
                }
            },
          '2':
            {
              'name':None,
              '1':
                {
                  'name':u'Senegal'
                },
              '0':
                {
                  'name':u'Gambia'
                },
              '3':
                {
                  'name':u'Mali'
                },
              '2':
                {
                  'name':u'Mauritania'
                },
              '5':
                {
                  'name':u'Costa de Marfil'
                },
              '4':
                {
                  'name':u'República de Guinea'
                },
              '7':
                {
                  'name':u'Niger'
                },
              '6':
                {
                  'name':u'Burkina Faso'
                },
              '9':
                {
                  'name':u'Benin'
                },
              '8':
                {
                  'name':u'Togo'
                }
            },
          '5':
            {
              'name':None,
              '1':
                {
                  'name':u'Etiopia'
                },
              '0':
                {
                  'name':u'Ruanda'
                },
              '3':
                {
                  'name':u'Yibuti'
                },
              '2':
                {
                  'name':u'Somalia'
                },
              '5':
                {
                  'name':u'Tanzania'
                },
              '4':
                {
                  'name':u'Kenia'
                },
              '7':
                {
                  'name':u'Burundi'
                },
              '6':
                {
                  'name':u'Uganda'
                },
              '8':
                {
                  'name':u'Mozambique'
                }
            },
          '4':
            {
              'name':None,
              '1':
                {
                  'name':u'Gabon'
                },
              '0':
                {
                  'name':u'Guinea Ecuat.'
                },
              '3':
                {
                  'name':u'República Democrática del Congo'
                },
              '2':
                {
                  'name':u'República del Congo'
                },
              '5':
                {
                  'name':u'Guinea Bissau'
                },
              '4':
                {
                  'name':u'Angola'
                },
              '7':
                {
                  'name':u'Ascension'
                },
              '6':
                {
                  'name':u'Diego Garcia'
                },
              '9':
                {
                  'name':u'Sudan'
                },
              '8':
                {
                  'name':u'Seychelles'
                }
            },
          '7':
            {
              'name':u'Sudafrica'
            },
          '6':
            {
              'name':None,
              '1':
                {
                  'name':u'Malgache'
                },
              '0':
                {
                  'name':u'Zambia'
                },
              '3':
                {
                  'name':u'Zimbabwe'
                },
              '2':
                {
                  'name':u'Islas Reunión'
                },
              '5':
                {
                  'name':u'Malawi'
                },
              '4':
                {
                  'name':u'Namibia'
                },
              '7':
                {
                  'name':u'Botswana'
                },
              '6':
                {
                  'name':u'Lesotho'
                },
              '9':
                {
                  'name':u'Islas Comores'
                },
              '8':
                {
                  'name':u'Suazilandia'
                }
            },
          '9':
            {
              'name':None,
              '1':
                {
                  'name':u'Eritrea'
                },
              '0':
                {
                  'name':u'Santa Elena'
                },
              '7':
                {
                  'name':u'Aruba'
                },
              '9':
                {
                  'name':u'Groenlandia'
                },
              '8':
                {
                  'name':u'Islas Feroe'
                }
            }
        },
      '5':
        {
          'name':None,
          '1':
            {
              'name':u'Peru'
            },
          '0':
            {
              'name':None,
              '1':
                {
                  'name':u'Belize'
                },
              '0':
                {
                  'name':u'Islas Marianas'
                },
              '3':
                {
                  'name':u'El Salvador'
                },
              '2':
                {
                  'name':u'Guatemala'
                },
              '5':
                {
                  'name':u'Nicaragua'
                },
              '4':
                {
                  'name':u'Honduras'
                },
              '7':
                {
                  'name':u'Panama'
                },
              '6':
                {
                  'name':u'Costa Rica'
                },
              '9':
                {
                  'name':u'Haiti'
                },
              '8':
                {
                  'name':u'San Pedro y Miquelon'
                }
            },
          '3':
            {
              'name':u'Cuba'
            },
          '2':
            {
              'name':u'Mexico'
            },
          '5':
            {
              'name':u'Brasil'
            },
          '4':
            {
              'name':u'Argentina'
            },
          '7':
            {
              'name':u'Colombia'
            },
          '6':
            {
              'name':u'Chile'
            },
          '9':
            {
              'name':None,
              '1':
                {
                  'name':u'Bolivia'
                },
              '0':
                {
                  'name':u'Guadalupe'
                },
              '3':
                {
                  'name':u'Ecuador'
                },
              '2':
                {
                  'name':u'Guyana'
                },
              '5':
                {
                  'name':u'Paraguay'
                },
              '4':
                {
                  'name':u'Guayana Francesa'
                },
              '7':
                {
                  'name':u'Surinam'
                },
              '6':
                {
                  'name':u'Martinica'
                },
              '9':
                {
                  'name':u'Antillas Holandesas'
                },
              '8':
                {
                  'name':u'Uruguay'
                }
            },
          '8':
            {
              'name':u'Venezuela'
            }
        },
      '4':
        {
          'name':None,
          '1':
            {
              'name':u'Suiza'
            },
          '0':
            {
              'name':u'Rumania'
            },
          '3':
            {
              'name':u'Austria'
            },
          '2':
            {
              '1':
                {
                  'name':u'Eslovaquia'
                },
              '0':
                {
                  'name':u'República Checa'
                },
              'name':None
            },
          '5':
            {
              'name':u'Dinamarca'
            },
          '4':
            {
              'name':u'Inglaterra'
            },
          '7':
            {
              'name':u'Noruega'
            },
          '6':
            {
              'name':u'Suecia'
            },
          '9':
            {
              'name':u'Alemania'
            },
          '8':
            {
              'name':u'Polonia'
            }
        },
      '7':
        {
          'name':u'Rusia'
        },
      '6':
        {
          'name':None,
          '1':
            {
              'name':u'Australia'
            },
          '0':
            {
              'name':u'Malasia'
            },
          '3':
            {
              'name':u'Filipinas'
            },
          '2':
            {
              'name':u'Indonesia'
            },
          '5':
            {
              'name':u'Singapur'
            },
          '4':
            {
              'name':u'Nueva Zelanda'
            },
          '7':
            {
              'name':None,
              '0':
                {
                  'name':u'Timor Oriental'
                },
              '3':
                {
                  'name':u'Brunei'
                },
              '5':
                {
                  'name':u'Papua Nueva Guinea'
                },
              '4':
                {
                  'name':u'Nauru'
                },
              '7':
                {
                  'name':u'Salomon'
                },
              '6':
                {
                  'name':u'Islas Tonga'
                },
              '9':
                {
                  'name':u'Islas Fiyi'
                },
              '8':
                {
                  'name':u'Vanuatu'
                }
            },
          '6':
            {
              'name':u'Tailandia'
            },
          '9':
            {
              '1':
                {
                  'name':u'Micronesia'
                },
              '0':
                {
                  'name':u'Tokelau'
                },
              '2':
                {
                  'name':u'Islas Marshall'
                },
              'name':None
            },
          '8':
            {
              'name':None,
              '1':
                {
                  'name':u'Wallis y Futuna'
                },
              '0':
                {
                  'name':u'Palaos'
                },
              '3':
                {
                  'name':u'Niue'
                },
              '2':
                {
                  'name':u'Islas Cook'
                },
              '5':
                {
                  'name':u'Samoa Occid.'
                },
              '7':
                {
                  'name':u'Nueva Caledonia'
                },
              '6':
                {
                  'name':u'Kiribati'
                },
              '9':
                {
                  'name':u'Polinesia Francesa'
                },
              '8':
                {
                  'name':u'Tuvalu'
                }
            }
        },
      '9':
        {
          'name':None,
          '1':
            {
              'name':u'India'
            },
          '0':
            {
              'name':u'Turquia'
            },
          '3':
            {
              'name':u'Afganistan'
            },
          '2':
            {
              'name':u'Pakistan'
            },
          '5':
            {
              'name':u'Myanmar',
              '6':
                {
                  'name':None,
                  '7':
                    {
                      'name':u'Gibraltar'
                    }
                }
            },
          '4':
            {
              'name':u'Sri Lanka'
            },
          '7':
            {
              'name':None,
              '1':
                {
                  'name':u'Emiratos Arabes'
                },
              '0':
                {
                  'name':u'Palestina'
                },
              '3':
                {
                  'name':u'Bahrein'
                },
              '2':
                {
                  'name':u'Israel'
                },
              '5':
                {
                  'name':u'Bhutan'
                },
              '4':
                {
                  'name':u'Qatar'
                },
              '7':
                {
                  'name':u'Nepal'
                },
              '6':
                {
                  'name':u'Mongolia'
                }
            },
          '6':
            {
              'name':None,
              '1':
                {
                  'name':u'Libano'
                },
              '0':
                {
                  'name':u'Maldivas'
                },
              '3':
                {
                  'name':u'Siria'
                },
              '2':
                {
                  'name':u'Jordania'
                },
              '5':
                {
                  'name':u'Kuwait'
                },
              '4':
                {
                  'name':u'Iraq'
                },
              '7':
                {
                  'name':u'Yemen'
                },
              '6':
                {
                  'name':u'Arabia Saudi'
                },
              '8':
                {
                  'name':u'Oman'
                }
            },
          '9':
            {
              'name':None,
              '3':
                {
                  'name':u'Turkmenistan'
                },
              '2':
                {
                  'name':u'Tadjikistan'
                },
              '5':
                {
                  'name':u'Georgia'
                },
              '4':
                {
                  'name':u'Azerbaijan'
                },
              '6':
                {
                  'name':u'Kirguizistan'
                },
              '8':
                {
                  'name':u'Uzbekistan'
                }
            },
          '8':
            {
              'name':u'Iran'
            }
        },
      '8':
        {
          'name':None,
          '1':
            {
              'name':u'Japon'
            },
          '2':
            {
              'name':u'Corea del Norte'
            },
          '5':
            {
              'name':None,
              '0':
                {
                  'name':u'Corea del Sur'
                },
              '3':
                {
                  'name':u'Macao'
                },
              '2':
                {
                  'name':u'Hong Kong'
                },
              '5':
                {
                  'name':u'Camboya'
                },
              '6':
                {
                  'name':u'Laos'
                }
            },
          '4':
            {
              'name':u'Vietnam'
            },
          '6':
            {
              'name':u'China'
            },
          '8':
            {
              '0':
                {
                  'name':u'Bangladesh'
                },
              'name':None,
              '6':
                {
                  'name':u'Taiwan'
                }
            }
        }
    }

localCodesTree={
 '1' : {
   'name' : None,
   '5' : {
     'name' : u'Celular'
   }
  },
 '4' : {
   'name' : u'Local'
 },
 '5' : {
   'name' : u'Local'
 }
}

def getLocation(number,mainHash):
  theHash = mainHash
  locationName = "None"
  lastFoundPos = -1
  for i in range(0,len(number)):
    try:
      #para debug
      #print i, number[i], theHash[number[i]]['name']
      if theHash[number[i]]['name']:
        locationName = theHash[number[i]]['name']
        found = True
        lastFoundPos = i
      theHash = theHash[number[i]]
    except KeyError, e:
      break
  code = "X"
  telNumber = '0'
  if lastFoundPos >= 0:
    code = number[0:lastFoundPos+1]
    telNumber = number[lastFoundPos+1:]
  return code+":"+locationName+":"+telNumber

def getInterurbanLocation(number):
  return getLocation(number,areaCodesTree)

def getInternationalLocation(number):
  return getLocation(number,countriesCodesTree)

def getLocalLocation(number):
  return getLocation(number,localCodesTree)
    
def getCallType(number):
  prefix = number[0:2]
  if prefix == '00':
    return 'INTERNATIONAL'
  elif prefix == '08':
    return '08XXCALL'
  elif prefix[0:1] == '0':
    return 'INTERURBAN'
  return 'LOCAL'
  

def guessNumber(number):
  callType = getCallType(number)
  number = number.strip('0')
  stdout.write(callType+"#")
  if callType == 'INTERNATIONAL':
    stdout.write(getInternationalLocation(number))
  elif callType == '08XXCALL':
    stdout.write('08XX')
  elif callType == 'INTERURBAN':
    iuLocation = getInterurbanLocation(number)
    stdout.write(iuLocation+"#"+getLocalLocation(iuLocation.split(':')[2]))
  elif callType == 'LOCAL':
    stdout.write(getLocalLocation(number))
  else:
    stdout.write("ERROR_GUESSING_NUMBER")
#  print

argParser = argparse.ArgumentParser()
argParser.add_argument("--num", nargs='?', required=True)
args = argParser.parse_args()
number = str(args.num)
guessNumber(number)


""" 
#para debug  
guessNumber('0220453512')
guessNumber('02202453512')
guessNumber('02282453512')# no existe
guessNumber('02983431650')
guessNumber('0341156744422')
guessNumber('0018775876900')
guessNumber('0223155464435')
guessNumber('15415933')
guessNumber('429664')
"""
