#!/usr/bin/env python
# coding : utf-8

class Test():
    
 @classmethod
 def testport(cls):

    import socket
    import subprocess
    import sys
    from datetime import datetime
    
    # On efface l'écran
    subprocess.call('cls', shell=True)
    
    # On demande à l'utilisateur d'entrer un hôte distant pour pouvoir le scanner
    remoteServer    = input("Merci d'entrer l'hôte à scanner: ")
    remoteServerIP  = socket.gethostbyname(remoteServer)
    
    # Pour faire patienter notre utilisateur une jolie mise en forme
    print ("--" * 60)
    print ("Patience scan en cours", remoteServerIP)
    print ("--" * 60)
    
    # On effectue une mise à jour de l'heure à laquelle le script a été lancé
    t1 = datetime.now()
    
    # Dans une boucle FOR, on utilise RANGE pour définir les ports à scanner (le nombre total des ports est de : 65535)
    # Il est possible de définir un nombre moins élevé de ports en changeant la valeur 65535 dans le RANGE 
    
    # Avec les lignes except.. On vérifie qu'il n'y ait aucune erreur
    
    try:
        for port in range(1,65535):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print ("Port {}:      Open".format(port))
            sock.close()
    
    except KeyboardInterrupt:
        print ("Vous avez stoppez le script en appuyant sur Ctrl+C")
        sys.exit()
    
    except socket.gaierror:
        print ("Le nom de l'hôte n'a pas pu être résolu. Ciao")
        sys.exit()
    
    except socket.error:
        print ("Impossible de se connecter au serveur")
        sys.exit()
    
    # On effectue une deuxième vérification du temps
    t2 = datetime.now()
    
    # On calcule grâce à nos deux temps, la différence entre le début et la fin du script
    total =  t2 - t1
    
    # On peut maintenant afficher le résultat à l'utilisateur
    print ('Scan complet en : ', total)