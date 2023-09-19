import ipaddress
import time

def calculer_informations_reseau(ip_str):
    try:
        # Convertir l'adresse IP en un objet de classe ipaddress.IPv4Network
        ip = ipaddress.IPv4Network(ip_str, strict=False)
        
        # Classe de l'adresse IP
        classe_ip = 'A' if ip.is_private and ip.prefixlen == 8 else \
                    'B' if ip.is_private and ip.prefixlen == 16 else \
                    'C' if ip.is_private and ip.prefixlen == 24 else \
                    'A' if 1 <= ip.network_address.packed[0] <= 126 else \
                    'B' if 128 <= ip.network_address.packed[0] <= 191 else \
                    'C' if 192 <= ip.network_address.packed[0] <= 223 else 'D ou E'

        masque = ip.netmask                             # Masque de sous-réseau 

        wildcard = ip.hostmask                          # Wildcard

        adresse_reseau = ip.network_address             # Adresse réseau

        adresse_broadcast = ip.broadcast_address        # Adresse de diffusion (broadcast)

        premiere_ip = ip.network_address + 1            # Première adresse IP affectable du sous-réseau

        derniere_ip = ip.broadcast_address - 1          # Dernière adresse IP affectable du sous-réseau

        nombre_hotes = ip.num_addresses - 2             # Nombre d'hôtes

       
        # ______________________________ - Nombre de sous-réseaux - ______________________________

        masque_binaire = bin(int(ip.netmask))[2:].zfill(32)                                         # Obtenir le masque de sous-réseau en format binaire

        longueur_prefixe_sous_reseau = ip.prefixlen                                                 # Longueur du préfixe de sous-réseau

        index_octet_incomplet = longueur_prefixe_sous_reseau // 8                                   # Calcul de l'index de l'octet incomplet

        octet_incomplet = masque_binaire[index_octet_incomplet * 8:(index_octet_incomplet + 1) * 8] # Extraire l'octet incomplet du masque

        nombre_de_bits_1 = octet_incomplet.count('1')                                               # Compter le nombre de bits '1'

        nombre_sous_reseaux = 2 ** nombre_de_bits_1 - 2                                             # Calcule pour le nombre de sous réseaux

        # ______________________________ - Afficher les résultats - ______________________________
        print("CALCULE EN COURS") ; time.sleep(0.25)

        print(f"Classe de l'adresse IP : {classe_ip}") ; time.sleep(0.25)

        print(f"Masque de sous-réseau : {masque}") ; time.sleep(0.25)

        print(f"Wildcard : {wildcard}") ; time.sleep(0.25)

        print(f"Adresse réseau : {adresse_reseau}") ; time.sleep(0.25)

        print(f"Adresse de diffusion : {adresse_broadcast}") ; time.sleep(0.25)

        print(f"Première adresse IP affectable : {premiere_ip}") ; time.sleep(0.25)

        print(f"Dernière adresse IP affectable : {derniere_ip}") ; time.sleep(0.25)

        print(f"Nombre d'hôtes : {nombre_hotes}") ; time.sleep(0.25)

        print(f"Nombre de sous-réseaux possibles : {nombre_sous_reseaux}") ; time.sleep(0.25)
    
    except ValueError:
        print("Adresse IP invalide.")

# ______________________________ - Exemple d'utilisation - ______________________________
adresse_ip = input("Entrez une adresse IP (format CIDR, par exemple 192.168.1.0/24) : ")
calculer_informations_reseau(adresse_ip)

input("Appuyez sur Entrée pour quitter...")