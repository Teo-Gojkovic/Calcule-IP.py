
## A propos

Calcule de 9 informations à partir d'un IP acompagné de son CIDR (exemple : 192.168.1.5/21)

![Version programme](https://img.shields.io/badge/Version-v1.0-blue.svg)

## Fonctionnement

Le programme peut s'exécuter comme tout ficher et apparaîtra sur la console par défaut de votre appareil. 

Le code est fait à partir d'une fonction `def calculer_informations_reseau(ip_str) :` et à l'intérieur, J'ai mis tout notre code pour simplifier les futures mises à jour. 

Vu que le programme utilise la bibliothèque ipaddress il faut convertir l'input qu'on fera pour avoir un objet de classe ipaddress.IPV4Network
```py
ip = ipaddress.IPv4Network(ip_str, strict=False)
```
Ensuite, il faudra déterminer la classe IP qui se fait avec des if else :
```py
# Classe de l'adresse IP
classe_ip = 'A' if ip.is_private and ip.prefixlen == 8 else \
            'B' if ip.is_private and ip.prefixlen == 16 else \
            'C' if ip.is_private and ip.prefixlen == 24 else \
            'A' if 1 <= ip.network_address.packed[0] <= 126 else \
            'B' if 128 <= ip.network_address.packed[0] <= 191 else \
            'C' if 192 <= ip.network_address.packed[0] <= 223 else 'D ou E'
```

Une fois qu'on a déterminé la classe, il faudra trouver le masque/ wildcard /adresse réseau/broadcast/1er hôte/dernier hôte et nombre d'hôtes par sous réseau : 

```py
masque = ip.netmask                             # Masque de sous-réseau 

wildcard = ip.hostmask                          # Wildcard

adresse_reseau = ip.network_address             # Adresse réseau

adresse_broadcast = ip.broadcast_address        # Adresse de diffusion (broadcast)

premiere_ip = ip.network_address + 1            # Première adresse IP affectable du sous-réseau

derniere_ip = ip.broadcast_address - 1          # Dernière adresse IP affectable du sous-réseau

nombre_hotes = ip.num_addresses - 2             # Nombre d'hôtes
```
On a de la chance la bibliothèque s'occupe de tout, il ne reste que le nombre de sous réseau qui est calculé à partir de nombre de bit '1' dans l'octet incomplet donc il fallait le trouver :

```py
# ______________________________ - Nombre de sous-réseaux - ______________________________

masque_binaire = bin(int(ip.netmask))[2:].zfill(32)                                         # Obtenir le masque de sous-réseau en format binaire

longueur_prefixe_sous_reseau = ip.prefixlen                                                 # Longueur du préfixe de sous-réseau

index_octet_incomplet = longueur_prefixe_sous_reseau // 8                                   # Calcul de l'index de l'octet incomplet

octet_incomplet = masque_binaire[index_octet_incomplet * 8:(index_octet_incomplet + 1) * 8] # Extraire l'octet incomplet du masque

nombre_de_bits_1 = octet_incomplet.count('1')                                               # Compter le nombre de bits '1'

nombre_sous_reseaux = 2 ** nombre_de_bits_1 - 2                                             # Calcule pour le nombre de sous réseaux
```

Ensuite se ne sont que des print pour afficher nos valeur qui sont espacer d'un quart de seconde pour être plus agréable pour l'oeil. 

J'ai mis tout dans try pour s'assurer que l'adresse mise est une IPV4 avec son CIDR. 

A la fin du code il y a un simple input pour la fonction que j'ai crée avant et j'ai ajouter `input("Appuyez sur Entrée pour quitter...")` pour éviter que si c'est executer comme un programme que la fenetre du CMD se ferme a la fin des calculs.
## Documentation

- [ipaddress](https://docs.python.org/3/library/ipaddress.html)
- [time](https://docs.python.org/3/library/time.html)


## Auteur

[![Teo GOJKOVIC](https://img.shields.io/badge/Teo_GOJKOVIC-222e45?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Teo-Gojkovic)

