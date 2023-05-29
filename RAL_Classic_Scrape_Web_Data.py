
from urllib.request import urlopen
from urllib.error import URLError
import re
import csv
from time import sleep

RAL_CLASSIC = [
    [ 'RAL 1000', 'Beige Vert' ],
    [ 'RAL 1001', 'Beige' ],
    [ 'RAL 1002', 'Jaune Sable' ],
    [ 'RAL 1003', 'Jaune Sécurité' ],
    [ 'RAL 1004', 'Jaune Or' ],
    [ 'RAL 1005', 'Jaune Miel' ],
    [ 'RAL 1006', 'Jaune Maïs' ],
    [ 'RAL 1007', 'Jaune Narcisse' ],
    [ 'RAL 1011', 'Beige Brun' ],
    [ 'RAL 1012', 'Jaune Citron' ],
    [ 'RAL 1013', 'Blanc Perle' ],
    [ 'RAL 1014', 'Ivoire' ],
    [ 'RAL 1015', 'Ivoire Clair' ],
    [ 'RAL 1016', 'Ivoire Clair' ],
    [ 'RAL 1017', 'Jaune Safran' ],
    [ 'RAL 1018', 'Jaune Zinc' ],
    [ 'RAL 1019', 'Beige Gris' ],
    [ 'RAL 1020', 'Jaune Olive' ],
    [ 'RAL 1021', 'Jaune Colza' ],
    [ 'RAL 1023', 'Jaune Signalisation' ],
    [ 'RAL 1024', 'Jaune Ocre' ],
    [ 'RAL 1026', 'Jaune Fluorescent' ],
    [ 'RAL 1027', 'Jaune Curry' ],
    [ 'RAL 1028', 'Jaune Melon' ],
    [ 'RAL 1032', 'Jaune Genet' ],
    [ 'RAL 1033', 'Jaune Dahlia' ],
    [ 'RAL 1034', 'Jaune Pastel' ],
    [ 'RAL 1035', 'Beige Nacré' ],
    [ 'RAL 1036', 'Or Nacré' ],
    [ 'RAL 1037', 'Jaune Soleil' ],
    [ 'RAL 2000', 'Orange Jaune' ],
    [ 'RAL 2001', 'Orange Rouge' ],
    [ 'RAL 2002', 'Orange Sang' ],
    [ 'RAL 2003', 'Orange Pastel' ],
    [ 'RAL 2004', 'Orangé Pur' ],
    [ 'RAL 2005', 'Orange Fluorescent' ],
    [ 'RAL 2007', 'Orange Fluorescent Lumineux' ],
    [ 'RAL 2008', 'Orange Rouge Lumière' ],
    [ 'RAL 2009', 'Orange Signalisation' ],
    [ 'RAL 2010', 'Orange Signalisation Sécurité' ],
    [ 'RAL 2011', 'Orange Profond' ],
    [ 'RAL 2012', 'Orangé Saumon' ],
    [ 'RAL 2013', 'Orangé Nacré' ],
    [ 'RAL 3000', 'Rouge Feu' ],
    [ 'RAL 3001', 'Rouge Sécurité' ],
    [ 'RAL 3002', 'Rouge Carmin' ],
    [ 'RAL 3003', 'Rouge Rubis' ],
    [ 'RAL 3004', 'Rouge Pourpre' ],
    [ 'RAL 3005', 'Rouge Vin' ],
    [ 'RAL 3007', 'Rouge Noir' ],
    [ 'RAL 3009', 'Rouge Oxyde' ],
    [ 'RAL 3011', 'Rouge Marron' ],
    [ 'RAL 3012', 'Rouge Beige' ],
    [ 'RAL 3013', 'Rouge Tomate' ],
    [ 'RAL 3014', 'Rose Ancien' ],
    [ 'RAL 3015', 'Rose Clair' ],
    [ 'RAL 3016', 'Rouge Corail' ],
    [ 'RAL 3017', 'Rose' ],
    [ 'RAL 3018', 'Rouge Fraise' ],
    [ 'RAL 3020', 'Rouge Signalisation' ],
    [ 'RAL 3022', 'Rouge Saumon' ],
    [ 'RAL 3024', 'Rouge Fluorescent' ],
    [ 'RAL 3026', 'Rouge Fluorescent Lumineux' ],
    [ 'RAL 3027', 'Rouge Framboise' ],
    [ 'RAL 3028', 'Rouge Pur' ],
    [ 'RAL 3031', 'Rouge Oriental' ],
    [ 'RAL 3032', 'Rouge Rubis Nacré' ],
    [ 'RAL 3033', 'Rose Nacré' ],
    [ 'RAL 4001', 'Rouge Lilas' ],
    [ 'RAL 4002', 'Violet Rouge' ],
    [ 'RAL 4004', 'Violet Bordeaux' ],
    [ 'RAL 4005', 'Bleu Lilas' ],
    [ 'RAL 4006', 'Pourpre Signalisation' ],
    [ 'RAL 4007', 'Violet Pourpre' ],
    [ 'RAL 4008', 'Violet Sécurité' ],
    [ 'RAL 4009', 'Violet Pastel' ],
    [ 'RAL 4010', 'Telemagenta' ],
    [ 'RAL 4011', 'Violet Nacré' ],
    [ 'RAL 4012', 'Mûre Nacré' ],
    [ 'RAL 5000', 'Bleu Violet' ],
    [ 'RAL 5001', 'Bleu Vert' ],
    [ 'RAL 5002', 'Bleu Outremer' ],
    [ 'RAL 5003', 'Bleu Saphir' ],
    [ 'RAL 5004', 'Bleu Noir' ],
    [ 'RAL 5005', 'Bleu Sécurité' ],
    [ 'RAL 5007', 'Bleu Brillant' ],
    [ 'RAL 5008', 'Bleu Gris' ],
    [ 'RAL 5009', 'Bleu Azur' ],
    [ 'RAL 5010', 'Bleu Gentiane' ],
    [ 'RAL 5011', 'Bleu Acier' ],
    [ 'RAL 5012', 'Bleu Clair' ],
    [ 'RAL 5013', 'Bleu Cobalt' ],
    [ 'RAL 5014', 'Bleu Pigeon' ],
    [ 'RAL 5015', 'Bleu Ciel' ],
    [ 'RAL 5017', 'Bleu Signalisation' ],
    [ 'RAL 5018', 'Bleu Turquoise' ],
    [ 'RAL 5019', 'Bleu Capri' ],
    [ 'RAL 5020', 'Bleu Océan' ],
    [ 'RAL 5021', 'Bleu Eau' ],
    [ 'RAL 5022', 'Bleu Nuit' ],
    [ 'RAL 5023', 'Bleu Distant' ],
    [ 'RAL 5024', 'Bleu Pastel' ],
    [ 'RAL 5025', 'Bleu Gentiane Nacré' ],
    [ 'RAL 5026', 'Bleu Nuit Nacré' ],
    [ 'RAL 6000', 'Vert Patine' ],
    [ 'RAL 6001', 'Vert Emeraude' ],
    [ 'RAL 6002', 'Vert Feuillage' ],
    [ 'RAL 6003', 'Vert Olive' ],
    [ 'RAL 6004', 'Vert Bleu' ],
    [ 'RAL 6005', 'Vert Mousse' ],
    [ 'RAL 6006', 'Olive Gris' ],
    [ 'RAL 6007', 'Vert Bouteille' ],
    [ 'RAL 6008', 'Vert Marron' ],
    [ 'RAL 6009', 'Vert Sapin' ],
    [ 'RAL 6010', 'Vert Gazon' ],
    [ 'RAL 6011', 'Vert Réséda' ],
    [ 'RAL 6012', 'Vert Noir' ],
    [ 'RAL 6013', 'Vert Jonc' ],
    [ 'RAL 6014', 'Olive Jaune' ],
    [ 'RAL 6015', 'Olive Noir' ],
    [ 'RAL 6016', 'Vert Turquoise' ],
    [ 'RAL 6017', 'Vert Mai' ],
    [ 'RAL 6018', 'Vert Jaune' ],
    [ 'RAL 6019', 'Vert Pastel' ],
    [ 'RAL 6020', 'Vert Chrome' ],
    [ 'RAL 6021', 'Vert Pale' ],
    [ 'RAL 6022', 'Olive Brun (DRAB)' ],
    [ 'RAL 6024', 'Vert Signalisation' ],
    [ 'RAL 6025', 'Vert Fougere' ],
    [ 'RAL 6026', 'Vert Opale' ],
    [ 'RAL 6027', 'Vert Clair' ],
    [ 'RAL 6028', 'Vert Sapin' ],
    [ 'RAL 6029', 'Vert Menthe' ],
    [ 'RAL 6031', 'Vert Camouflage Bronze' ],
    [ 'RAL 6032', 'Vert Securite' ],
    [ 'RAL 6033', 'Turquoise Menthe' ],
    [ 'RAL 6034', 'Turquoise Pastel' ],
    [ 'RAL 6035', 'Vert Nacre' ],
    [ 'RAL 6036', 'Vert Opal Nacré' ],
    [ 'RAL 6037', 'Vert Pur' ],
    [ 'RAL 6038', 'Vert Fluorescent' ],
    [ 'RAL 7000', 'Gris Petit Gris' ],
    [ 'RAL 7001', 'Gris Argent' ],
    [ 'RAL 7002', 'Gris Olive' ],
    [ 'RAL 7003', 'Gris Mousse' ],
    [ 'RAL 7004', 'Gris Securite' ],
    [ 'RAL 7005', 'Gris Souris' ],
    [ 'RAL 7006', 'Gris Beige' ],
    [ 'RAL 7008', 'Gris Kaki' ],
    [ 'RAL 7009', 'Gris Vert' ],
    [ 'RAL 7010', 'Gris Tente' ],
    [ 'RAL 7011', 'Gris Fer' ],
    [ 'RAL 7012', 'Gris Basalte' ],
    [ 'RAL 7013', 'Gris Marron Brun' ],
    [ 'RAL 7015', 'Gris Ardoise' ],
    [ 'RAL 7016', 'Gris Anthracite' ],
    [ 'RAL 7021', 'Gris Noir' ],
    [ 'RAL 7022', 'Gris Ombre' ],
    [ 'RAL 7023', 'Gris Beton' ],
    [ 'RAL 7024', 'Gris Graphite' ],
    [ 'RAL 7026', 'Gris Granite' ],
    [ 'RAL 7030', 'Gris Pierre' ],
    [ 'RAL 7031', 'Gris Bleu' ],
    [ 'RAL 7032', 'Gris Caillou' ],
    [ 'RAL 7033', 'Gris Ciment' ],
    [ 'RAL 7034', 'Gris Jaune' ],
    [ 'RAL 7035', 'Gris Clair' ],
    [ 'RAL 7036', 'Gris Platine' ],
    [ 'RAL 7037', 'Gris Poussiere' ],
    [ 'RAL 7038', 'Gris Agate' ],
    [ 'RAL 7039', 'Gris Quartz' ],
    [ 'RAL 7040', 'Gris Fenetre' ],
    [ 'RAL 7042', 'Gris Signalisation A' ],
    [ 'RAL 7043', 'Gris Signalisation B' ],
    [ 'RAL 7044', 'Gris Soie' ],
    [ 'RAL 7045', 'Telegris 1' ],
    [ 'RAL 7046', 'Telegris 2' ],
    [ 'RAL 7047', 'Telegris 4' ],
    [ 'RAL 7048', 'Gris Souris Nacré' ],
    [ 'RAL 8000', 'Marron Vert' ],
    [ 'RAL 8001', 'Marron Ocre' ],
    [ 'RAL 8002', 'Brun Securite' ],
    [ 'RAL 8003', 'Brun Argile' ],
    [ 'RAL 8004', 'Brun Cuivre' ],
    [ 'RAL 8007', 'Brun Fauve' ],
    [ 'RAL 8008', 'Brun Olive' ],
    [ 'RAL 8011', 'Brun Noisette' ],
    [ 'RAL 8012', 'Brun Rouge' ],
    [ 'RAL 8014', 'Brun Sepia' ],
    [ 'RAL 8015', 'Marron Chataigne' ],
    [ 'RAL 8016', 'Brun Acajou' ],
    [ 'RAL 8017', 'Brun Chocolat' ],
    [ 'RAL 8019', 'Brun Gris' ],
    [ 'RAL 8022', 'Brun Noir' ],
    [ 'RAL 8023', 'Brun Orange' ],
    [ 'RAL 8024', 'Brun Beige' ],
    [ 'RAL 8025', 'Brun Pâle' ],
    [ 'RAL 8027', 'Marron Camouflage Otan' ],
    [ 'RAL 8028', 'Marron Terre' ],
    [ 'RAL 8029', 'Cuivre Nacre' ],
    [ 'RAL 9001', 'Blanc Creme' ],
    [ 'RAL 9002', 'Blanc Gris' ],
    [ 'RAL 9003', 'Blanc Securite' ],
    [ 'RAL 9005', 'Noir Profond' ],
    [ 'RAL 9006', 'Aluminium Blanc' ],
    [ 'RAL 9007', 'Aluminium Gris' ],
    [ 'RAL 9010', 'Blanc Pur' ],
    [ 'RAL 9011', 'Noir Graphite' ],
    [ 'RAL 9017', 'Noir signalisation' ],
    [ 'RAL 9018', 'Blanc Papyrus' ],
    [ 'RAL 9021', 'Noir Camouflage Otan Goudron' ],
    [ 'RAL 9023', 'Gris Foncé Nacré' ],
]

def remove_accents( raw_text ):
    raw_text = re.sub( u"[àáâãäå]", 'a', raw_text )
    raw_text = re.sub( u"[èéêë]", 'e', raw_text )
    raw_text = re.sub( u"[ìíîï]", 'i', raw_text )
    raw_text = re.sub( u"[òóôõö]", 'o', raw_text )
    raw_text = re.sub( u"[ùúûü]", 'u', raw_text )
    raw_text = re.sub( u"[ýÿ]", 'y', raw_text )
    raw_text = re.sub( u"[ß]", 'ss', raw_text )
    raw_text = re.sub( u"[ñ]", 'n', raw_text )
    
    return raw_text 

array_ral_classic = []
for i in range( len( RAL_CLASSIC ) ):
    try:
        link    = "https://nuancier-ral.com/" 
        + remove_accents( RAL_CLASSIC[ i ][ 0 ].replace ( " ", "-" ) 
                         + "-" 
                         + RAL_CLASSIC[ i ][ 1 ].replace ( " ", "-" ) )
        
        print ( "=====> " + link )

        f           = urlopen( link )
        respData    = f.read()

        table       = re.findall( r'<table>(.*?)</table>', str( respData ) )
        bloc        = re.findall( r'<td>(.*?)</td>', str( table[ 0 ] ) )

        # Hexadécimal
        hex         = bloc[ 0 ].replace ( " ", "" )

        # RGB
        rgb         = bloc[ 1 ].split( '|' )
        rgb_r       = rgb[ 0 ].replace ( " ", "" )
        rgb_g       = rgb[ 1 ].replace ( " ", "" )
        rgb_b       = rgb[ 2 ].replace ( " ", "" )

        # CMJN (CMYK)
        cmyk        = bloc[ 2 ].split( '<br/>' )
        cmyk_c      = cmyk[ 0 ].replace ( "Cyan: ", "" ).replace ( "%", "" )
        cmyk_m      = cmyk[ 1 ].replace ( "Magenta: ", "" ).replace ( "%", "" )
        cmyk_y      = cmyk[ 2 ].replace ( "Jaune: ", "" ).replace ( "%", "" )
        cmyk_k      = cmyk[ 3 ].replace ( "Noir: ", "" ).replace ( "%", "" )

        # HSV
        hsv         = bloc[ 3 ].split( '|' )
        hsv_h       = hsv[ 0 ].replace ( " ", "" )
        hsv_s       = hsv[ 1 ].replace ( " ", "" )
        hsv_v       = hsv[ 2 ].replace ( " ", "" )

        array_ral_classic.append ( (
            RAL_CLASSIC[ i ][ 0 ], 
            RAL_CLASSIC[ i ][ 1 ], 
            hex, 
            rgb_r, 
            rgb_g, 
            rgb_b, 
            cmyk_c, 
            cmyk_m, 
            cmyk_y, 
            cmyk_k, 
            hsv_h, 
            hsv_s, 
            hsv_v ) 
        )

        sleep(5)

    except URLError as e:
        print(e.reason)

with open( "RAL_Classic.csv", "w+" ) as ral_classic_csv:
    csvWriter = csv.writer( ral_classic_csv, delimiter = ',' )
    csvWriter.writerows( array_ral_classic )