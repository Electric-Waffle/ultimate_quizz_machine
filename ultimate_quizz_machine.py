import random
import os
import time
import traceback
import sys
import csv
import ast

# Bibliotheque de questions et réponses
BASE_DE_DONNEE = {
    "Les Répertoires à la Racine": {


        "Les répertoires de base sont tous fils de la racine, qui s'écrit :" : {

            "reponse" : [
                "root",
                "/root", 
                "racine",
                "/racine",
                "\\",
                ],
            
            "solution" :  "/",

            "explication" : "La racine s'écrit / .\nA l'interieur se trouvent tout les dossiers du SGF."

        },

        "Le répertoire /bin est :" : {

            "reponse" : [
                "un répertoire contenant les données effacées",
                "enfaite un lien menant a /usr/bin, contenant les données effacées",
                "un répertoire contenant les programmes commun aux utilisateurs",
                "un répertoire contenant les répertoires personnels des utilisateurs",
                "enfaite un lien menant a /etc/bin, contenant les programmes commun aux utilisateurs",
                ],
            
            "solution" :  "enfaite un lien menant a /usr/bin, contenant les programmes commun aux utilisateurs.",

            "explication" : "Le répertoire /bin est un lien menant au répertoire /usr/bin, contenant les programmes commun aux utilisateurs."

        },

        "Quel répertoire est enfaite un lien menant au répertoire contenant les programmes communs aux utilisateurs ?" : {

            "reponse" : [
                "/",
                "/etc", 
                "/dev",
                "/home",
                "/media",
                ],
            
            "solution" :  "/bin",

            "explication" : "Le répertoire /bin est un lien menant au répertoire /usr/bin, contenant les programmes commun aux utilisateurs."

        },

        "Le répertoire /boot contient :" : {

            "reponse" : [
                "les executables lancés a la connexion de l'utilisateur",
                "les fichiers textes contenant l'historique des commandes utilisées", 
                "l'executable permettant d'utiliser bash",
                "les fichiers qui se lancent lorsque l'on fait /boot dans le terminal, un peu comme une macro",
                "les fichiers corrompus par une soudaine mise hors tension du système",
                ],
            
            "solution" :  "les fichiers qui se lancent lors du boot du système",

            "explication" : "Le répertoire /boot contient les fichiers qui se lancent lors du boot du système"

        },

        "Quel répertoire contient les fichiers qui se lancent au démarrage du système ?" : {

            "reponse" : [
                "/usr",
                "/lib", 
                "/home",
                "/begin",
                "/launch",
                ],
            
            "solution" :  "/boot",

            "explication" : "Le répertoire /boot contient les fichiers qui se lancent lors du boot du système"

        },

        "Le répertoire /dev contient :" : {

            "reponse" : [
                "les répertoires dans lesquels sont montés les périphériques amovibles",
                "les disques durs montés dans le système", 
                "les bibliotheques compilés nécessaires au lancements de certains executables",
                "le skel, template de chaque /home pour les nouveaux utilisateurs",
                "les applications optionnelles",
                ],
            
            "solution" :  "les fichiers devices qui interragissent avec les périphériques",

            "explication" : "Le répertoire /dev contient les fichiers devices qui interragissent avec les périphériques"

        },

        "quel répertoire contient les fichiers qui interragissent avec les périphériques ?" : {

            "reponse" : [
                "/boot",
                "/per", 
                "/media",
                "/root",
                "/amovible",
                ],
            
            "solution" :  "/dev",

            "explication" : "Le répertoire /dev contient les fichiers devices qui interragissent avec les périphériques"

        },

        "Le répertoire /dev est appelé ainsi car :" : {

            "reponse" : [
                "il contient des informations relatives aux DEVeloppeurs de l'os",
                "il contient des fichiers relatifs au DEVeloppement des executables", 
                "il contient des repertoires contenant les DEVlogs, aka historiques de programmation",
                "il a été créé par DEVin, le créateur de DEBIAN 12",
                "il contient des fichiers textes relatifs aux DIVergences entre linux.old et linux",
                ],
            
            "solution" :  "il contient les fichiers DEVices, aka fichiers de périphériques.",

            "explication" : "Le répertoire /dev est appelé ainsi car il contient les fichiers DEVices, aka fichiers de périphériques. Ces fichiers permettent d'interragir avec le materiel."

        },

        "Le répertoire /etc contient :" : {

            "reponse" : [
                "les librairies de fonctions communes entre les utilisateurs",
                "la configuration du systeme d'exploitation", 
                "les fichiers temporaires, vidés entre chaque boot du systeme",
                "les applications personnelles",
                "les fichiers qui ne rentrent dans aucun autre répertoire",
                ],
            
            "solution" :  "les fichiers de configuration du système et de ses applications",

            "explication" : "Le répertoire /etc contient les fichiers de configuration du système et de ses applications"

        },

        "Quel répertoire contient les fichiers de configuration du système et de ses applications ?" : {

            "reponse" : [
                "/sbin",
                "/lib", 
                "/config",
                "/option",
                "/conf",
                ],
            
            "solution" :  "/etc",

            "explication" : "Le répertoire /etc contient les fichiers de configuration du système et de ses applications"

        },

        "Le répertoire etc est nommé ainsi car il correspond a :" : {

            "reponse" : [
                "Et CeTera",
                "End of Terminal Compatibility", 
                "Erase Transaction from Correspondance",
                "E-log Titan Capabilities",
                "Executable Thu'um Cry",
                ],
            
            "solution" :  "Editable Text Configuration",

            "explication" : "Le répertoire etc est nommé ainsi car il correspond a Editable Text Configuration, aka configuration éditable en mode texte."

        },

        "Le répertoire /home contient :" : {

            "reponse" : [
                "les fichiers lancés au boot du système",
                "les librairies", 
                "les processus en cours d'execution",
                "les applications optionnelles",
                "les fichiers corrompus",
                ],
            
            "solution" :  "les répertoires personnels des utilisateurs du système",

            "explication" : "Le répertoire /home contient les répertoires personnels des utilisateurs du système"

        },

        "que repertoire contient les répertoires personnels des utilisateurs du système ?" : {

            "reponse" : [
                "/dev",
                "/etc", 
                "/mnt",
                "/private",
                "/bin",
                ],
            
            "solution" :  "/home",

            "explication" : "Le répertoire /home contient les répertoires personnels des utilisateurs du système"

        },

        "Les repertoires personnels des utilisateurs viennent directement partitionnés, suivant ainsi le template contenu dans :" : {

            "reponse" : [
                "/template",
                "/user_repartition", 
                "/exemple",
                "/libx32",
                "/user",
                ],
            
            "solution" :  "/skel",

            "explication" : "Les répertoires des users suivent le template contenu dans /skell, lui meme contenu dans un autre répertoire"

        },

        "le skel, contenant les templates selon lesquels les repertoires personnels sont partitionnés, est contenu dans :" : {

            "reponse" : [
                "/user",
                "/bin", 
                "/sbin",
                "/dev",
                "/home",
                ],
            
            "solution" :  "/etc",

            "explication" : "les templates sont contenu dans /etc/skel"

        },

        "Les librairies sont des :" : {

            "reponse" : [
                "bibliotheque contenant des executables",
                "repertoires contenant des logs", 
                "executables récuperants le chemin d'acces des programmes",
                "répertoires contenant des donnees temporaires",
                "fichiers de récupération des donnees corrompues",
                ],
            
            "solution" :  "bibliotheque contenant des fonctions communes aux programmes",

            "explication" : "Les librairies sont des bibliotheque contenant des fonctions communes aux programmes."

        },

        "Il existe differents types de librairie, car :" : {

            "reponse" : [
                "differentes librairies pour differents utilisateurs",
                "differentes librairies pour differents executables", 
                "differentes librairies pour differents fonctions",
                "differentes librairies pour differents os",
                "differentes librairies pour differents types d'utilisateurs",
                ],
            
            "solution" :  "differentes librairies pour differents processeurs",

            "explication" : "Il existe differents types de librairie, car les librairies sont compilées, et chaque processeur necessite un type de compilage different."

        },

        "Le répertoire lost+found contient :" : {

            "reponse" : [
                "les fichiers qui récupèrent les informations des périphériques",
                "les fichiers supprimés", 
                "les programmes communs aux utilisateurs",
                "les applications personnelles",
                "la configuration du système d'exploitation",
                ],
            
            "solution" :  "les fichiers corrompus en cas d'arret soudain de la machine.",

            "explication" : "Le répertoire lost+found contient les fichiers (souvent beaucoup trop) corrompus en cas d'arret soudain de la machine."

        },

        "Quel répertoire contient les dichiers corrompus en cas d'arret soudain de la machine ?" : {

            "reponse" : [
                "/lib32",
                "/skel", 
                "/opt",
                "/tmp",
                "/var",
                ],
            
            "solution" :  "/lost+found",

            "explication" : "Le répertoire lost+found contient les fichiers (souvent beaucoup trop) corrompus en cas d'arret soudain de la machine."

        },

        "Le répertoire /media contient :" : {

            "reponse" : [
                "les applications qui se lancent au démarrage du système",
                "les applications optionelles", 
                "les repertoires personnels des utilisateurs",
                "l'ensemble des fichiers qui ont tendance a varier en taille",
                "les fichiers qui interragissent avec les informations des périphériques",
                ],
            
            "solution" :  "les périphériques amovibles, automatiquement montés a cet endroit",

            "explication" : "Le répertoire /media contient les périphériques amovibles, automatiquement montés a cet endroit."

        },

        "Quel répertoire contient les périphériques amovibles, automatiquement montés a cet endroit ?" : {

            "reponse" : [
                "/dev",
                "/mnt", 
                "/proc",
                "/boot",
                "/bin",
                ],
            
            "solution" :  "/media",

            "explication" : "Le répertoire /media contient les périphériques amovibles, automatiquement montés a cet endroit"

        },

        "Que signifie *monter* dans le contexte des sgf ?" : {

            "reponse" : [
                "remonter dans l'arborescence de répertoires",
                "ajouter un répertoire en amont du working directory", 
                "rendre un systeme fichier accessible en l'associant a un répertoire",
                "brancher un périphérique amovible",
                "écrire dans un fichier par dessus ce qui avait été déja écrit",
                ],
            
            "solution" :  "rendre un systeme fichier accessible en l'associant a un répertoire",

            "explication" : "*monter* signifie rendre un systeme fichier accessible en l'associant a un répertoire"

        },

        "Le répertoire /mnt contient :" : {

            "reponse" : [
                "les fichiers de périphériques",
                "les fichiers correspondant au processus en cours d'execution", 
                "les logs en format textuel",
                "les programmes communs aux utilisateurs",
                "l'ensemble de fichiers qui ont tendance a varier en taille",
                ],
            
            "solution" :  "des systemes de fichiers montés manuellement",

            "explication" : "Le répertoire /mnt contient les systemes de fichiers montés manuellement"

        },
        
        "Quel répertoire contient les systemes de fichiers montés manuellement ?" : {

            "reponse" : [
                "/media",
                "/dev", 
                "/opt",
                "/fich",
                "/man",
                ],
            
            "solution" :  "/mnt",

            "explication" : "Le répertoire /mnt contient les systemes de fichiers montés manuellement"

        },
        
        "D'ou vient le nom du répertoire /mnt ?" : {

            "reponse" : [
                "mined",
                "mass folder neuteuring", 
                "moaning t-rex",
                "nested naln tirectory ",
                "more nachos terry",
                ],
            
            "solution" :  "mount",

            "explication" : "Le répertoire /mnt vient de MouNT car il contient les fichiers *montés* manuellement."

        },
        
        "Le répertoire /opt contient :" : {

            "reponse" : [
                "les applications essentielles a l'os",
                "les fichiers personnels des utilisateurs", 
                "les références aux répertoires contenant les fichiers amovibles",
                "un lien amenant vers /usr/opt",
                "l'ensemble des fichiers corrompus lors d'une mise hors tension soudaine du système",
                ],
            
            "solution" :  "les applications optionelles",

            "explication" : "Le répertoire /opt contient les applications optionelles du systeme."

        },
        
        "Quel répertoire contient les applications optionelles du systeme ?" : {

            "reponse" : [
                "/lost+found",
                "/dev", 
                "/home",
                "/nest",
                "/app",
                ],
            
            "solution" :  "/opt",

            "explication" : "Le répertoire /opt contient les applications optionelles du systeme."

        },
        
        "Le répertoire /proc contient :" : {

            "reponse" : [
                "les variables nécéssaires au fonctionnement de l'os",
                "les fichiers lancés au démarrage du systeme", 
                "les programmes communs aux utilisateurs",
                "les programmes réservés aux super-utilisateurs",
                "la configuration du système d'exploitation",
                ],
            
            "solution" :  "les fichiers correspondants aux processus en cours",

            "explication" : "Le répertoire /proc contient les fichiers correspondants aux processus en cours"

        },
        
        "Quel répertoire contient les fichiers correspondants aux processus en cours ?" : {

            "reponse" : [
                "/bin",
                "/sbin", 
                "/usr",
                "/sys",
                "/prc",
                ],
            
            "solution" :  "/proc",

            "explication" : "Le répertoire /proc contient les fichiers correspondants aux processus en cours"

        },
        
        "Le répertoire /root contient :" : {

            "reponse" : [
                "le répertoire /",
                "le répertoire parent a tout les répertoires", 
                "le template du partionnement des /homes des utilisateurs",
                "les fichiers qui communiquent avec les périphériques amovibles",
                "les fichiers qui permettent de monter des systemes de fichiers",
                ],
            
            "solution" :  "les fichiers personnels de l'administrateur",

            "explication" : "Le répertoire /root contient les fichiers personnels de l'administrateur"

        },
        
        "Quel répertoire contient les fichiers personnels de l'administrateur ?" : {

            "reponse" : [
                "/pers",
                "/usr", 
                "/admn",
                "/mnt",
                "/loot",
                ],
            
            "solution" :  "/root",

            "explication" : "Le répertoire /root contient les fichiers personnels de l'administrateur"

        },
        
        "Le répertoire /run contient:" : {

            "reponse" : [
                "l'ensemble des fichiers nécéssaires au bon fonctionnement de l'os",
                "un lien vers /usr/root", 
                "des logs en fichiers texte",
                "le bash et l'ensemble des commandes qu'il contient",
                "les processus en cours d'utilisation",
                ],
            
            "solution" :  "les données variables d'execution des applications",

            "explication" : "Le répertoire /run contient les données variables d'execution des applications"

        },
        
        "Quel répertoire contient les données variables d'execution des applications ?" : {

            "reponse" : [
                "/exe",
                "/usr", 
                "/app",
                "/mnt",
                "/mvc",
                ],
            
            "solution" :  "/run",

            "explication" : "Le répertoire /run contient les données variables d'execution des applications"

        },
        
        "Le répertoire /sbin contient :" : {

            "reponse" : [
                "un lien vers /usr/bin contenant les programmes communs aux utilisateurs",
                "les fichiers communiquant avec les périphériques amovibles", 
                "les fichiers et données supprimées",
                "les périphériques montés manuellement",
                "la configuration du systéme d'exploitation",
                ],
            
            "solution" :  "un lien vers /usr/sbin contenant les programmes réservés aux superutilisateurs",

            "explication" : "Le répertoire /sbin contient un lien vers /usr/sbin contenant les programmes réservés aux superutilisateurs"

        },
        
        "Quel répertoire contient un lien vers un répertoire contenant les programmes réservés aux superutilisateurs ?" : {

            "reponse" : [
                "/bin",
                "/rootfolder", 
                "/admn",
                "/mnt",
                "/media",
                ],
            
            "solution" :  "/sbin",

            "explication" : "Le répertoire /sbin contient un lien vers /usr/sbin contenant les programmes réservés aux superutilisateurs"

        },
        
        "Le répertoire /srv contient :" : {

            "reponse" : [
                "les données d'accès du serveur",
                "les fichiers executables pouvant lancer les serveurs", 
                "l'addresse MAC",
                "un récepteur aux fréquences de WTAN",
                "les fichiers temporaires, vidés a chaque reset de la machine",
                ],
            
            "solution" :  "l'ensemble des services réseaux proposés par les serveur",

            "explication" : "Le répertoire /srv contient l'ensemble des services réseaux proposés par les serveur."

        },
        
        "Quel répertoire contient l'ensemble des services réseaux proposés par les serveurs ?" : {

            "reponse" : [
                "/connct",
                "/root", 
                "/usr/srv",
                "/sys",
                "/tmp",
                ],
            
            "solution" :  "/srv",

            "explication" : "Le répertoire /srv contient l'ensemble des services réseaux proposés par les serveur."

        },
        
        "Le répertoire /sys contient :" : {

            "reponse" : [
                "les fichiers soeurs communs entre les utilisateurs",
                "les données variables d'execution des applications", 
                "les librairies communes aux programmes",
                "les applications personnelles",
                "les fichiers personnels de l'administrateur",
                ],
            
            "solution" :  "la configuration du système d'exploitation",

            "explication" : "Le répertoire /sys contient la configuration du système d'exploitation."

        },
        
        "Quel répertoire contient la configuration du système d'exploitation ?" : {

            "reponse" : [
                "/config",
                "/opt", 
                "/mtn",
                "/media",
                "/sbin",
                ],
            
            "solution" :  "/sys",

            "explication" : "Le répertoire /sys contient la configuration du système d'exploitation."

        },
        
        "Le répertoire /tmp contient :" : {

            "reponse" : [
                "l'ensemble des services réseau proposés aux utilisateurs",
                "les fichiers corrompus par la mise hors tension soudaine de la machine", 
                "les données variable d'execution des applications",
                "l'ensemble des fichiers qui ont tendance a varier en taille",
                "le lien /usr/tmp contenant les programmes réservés aux super utilisateurs",
                ],
            
            "solution" :  "les fichiers temporaires, vidés a chaque reset de la machine",

            "explication" : "Le répertoire /tmp contient les fichiers temporaires, vidés a chaque reset de la machine."

        },
        
        "Quel répertoire contient les fichiers temporaires, vidés a chaque reset de la machine ?" : {

            "reponse" : [
                "/temp",
                "/usr", 
                "/sys",
                "/mnt",
                "/var",
                ],
            
            "solution" :  "/tmp",

            "explication" : "Le répertoire /tmp contient les fichiers temporaires, vidés a chaque reset de la machine."

        },
        
        "Le répertoire /usr contient :" : {

            "reponse" : [
                "les fichiers correspondant aux  processus en cours d'execution",
                "les fichiers personnels de l'administrateur du système", 
                "les fichiers qui communiquent avec les périphériques amovibles",
                "les fichiers lancés au démarrage du système",
                "les fichiers de configuration du systeme et de ses applications",
                ],
            
            "solution" :  "les executables ainsi que les librairies dont ils ont besoin",

            "explication" : "Le répertoire /usr contient les executables ainsi que les librairies dont ils ont besoin."

        },
        
        "Quel répertoire contient les executables ainsi que les librairies dont ils ont besoin ?" : {

            "reponse" : [
                "/usr/bin",
                "/tmp/dev", 
                "/skel",
                "/etc",
                "/sys",
                ],
            
            "solution" :  "/usr",

            "explication" : "Le répertoire /usr contient les executables ainsi que les librairies dont ils ont besoin."

        },
        
        "Le répertoire /var contient :" : {

            "reponse" : [
                "la configuration du systeme d'exploitation",
                "les données variable d'execution des applications", 
                "les répertoires personnels des utilisateurs",
                "les fichiers temporaires vidés a chaque reset",
                "les applications optionnelles",
                ],
            
            "solution" :  "l'ensemble des fichiers qui ont tendance a varier en taille",

            "explication" : "Le répertoire /var contient l'ensemble des fichiers qui ont tendance a varier en taille."

        },
        
        "Quel répertoire contient l'ensemble des fichiers qui ont tendance a varier en taille ?" : {

            "reponse" : [
                "/tmp",
                "/root", 
                "/sys",
                "/log",
                "/opt",
                ],
            
            "solution" :  "/var",

            "explication" : "Le répertoire /var contient l'ensemble des fichiers qui ont tendance a varier en taille."

        },
        
        "Le répertoire /vmlinuz contient :" : {

            "reponse" : [
                "La configuration du système d'exploitation",
                "les données varaiables d'executions des applications", 
                "les fichiers correspondant aux processus en cours d'execution",
                "les fichiers temporaires, vidés a chaque reset",
                "la description de l'os",
                ],
            
            "solution" :  "le noyau du système actuel",

            "explication" : "Le répertoire /vmlinuz contient le noyau du système actuel."

        },
        
        "Quel répertoire contient le noyau du système actuel ?" : {

            "reponse" : [
                "/vmlinuz.old",
                "/sys", 
                "/vmlinux",
                "/opt",
                "/mnt",
                ],
            
            "solution" :  "/vmlinuz",

            "explication" : "Le répertoire /vmlinuz contient le noyau du système actuel."

        },
        
        "Le répertoire /vmlinuz.old contient :" : {

            "reponse" : [
                "La configuration du système d'exploitation précédent",
                "le noyau du système", 
                "les fichiers correspondant aux processus en cours d'execution",
                "les fichiers temporaires, vidés a chaque reset",
                "la description de l'os précédent",
                ],
            
            "solution" :  "le noyau du système précédent",

            "explication" : "Le répertoire /vmlinuz.old contient le noyau du système précédent."

        },
        
        "Quel répertoire contient le noyau du système précédent ?" : {

            "reponse" : [
                "/sys.old",
                "/tmp", 
                "/var",
                "/opt.old",
                "/vmlinux.old",
                ],
            
            "solution" :  "/vmlinuz.old",

            "explication" : "Le répertoire /vmlinuz.old contient le noyau du système précédent."

        },
        
        
    },

    "Cejm : Définitions chapitre 3": {


        "Les Pourparlers sont une phase :" : {

            "reponse" : [
                "d'exécution du contrat",
                "postérieure à la signature du contrat", 
                "de résiliation du contrat",
                "de validation juridique finale",
                "de négociation obligatoire avant tout engagement"
            ],
            
            "solution" :  "préliminaire à la conclusion (ou passation) du contrat",

            "explication" : "flemme de donner une explication dsl"

        },

        "Les Pourparlers sont une phase durant laquelle" : {

            "reponse" : [
                "le contrat est signé",
                "les parties s'engagent définitivement",
                "les pénalités de rupture sont fixées",
                "le contenu final du contrat est validé",
                "les obligations sont formalisées"
            ],
                    
            "solution" :  "sont discutées les clauses qu'il pourrait contenir",

            "explication" : "flemme de donner une explication dsl"

        },

        "Les Pourparlers, dans leurs conditions, engagent :" : {

            "reponse" : [
                "toutes les parties",
                "la partie initiatrice",
                "les avocats des parties",
                "les partenaires financiers",
                "les tiers concernés par le contrat"
            ],
                    
            "solution" :  "aucune partie",

            "explication" : "flemme de donner une explication dsl"

        },

        "Phase préliminaire à la conclusion (ou passation) du contrat durant laquelle sont discutées les clauses qu'il pourrait contenir" : {

            "reponse" : [
                "Accord de principe",
                "Négociation définitive",
                "Contrat cadre",
                "Protocole d'accord",
                "Convention d'exécution"
            ],
                    
            "solution" :  "Pourparlers",

            "explication" : "flemme de donner une explication dsl"

        },

        "Quelle est la finalité d'une phase d'Avant-contrat ?" : {

            "reponse" : [
                "valider les conditions du contrat",
                "exécuter le contrat",
                "s'assurer de la résiliation correcte du contrat",
                "fixer les clauses de rupture",
                "finaliser les termes de l'accord"
            ],
                    
            "solution" :  "préparer la conclusion d'un contrat à venir.",

            "explication" : "flemme de donner une explication dsl"

        },

        "A sa base, qu'est ce qu'un Avant-contrat ?" : {

            "reponse" : [
                "une discussion informelle",
                "une simple promesse",
                "une négociation sans engagement",
                "une entente verbale",
                "un accord de principe sans valeur juridique"
            ],
                    
            "solution" :  "un engagement contractuel",

            "explication" : "flemme de donner une explication dsl"

        },

        "Engagement contractuel d'une ou de plusieurs parties dont la finalité est de préparer la conclusion d'un contrat à venir." : {

            "reponse" : [
                "Protocole d'accord",
                "Accord de principe",
                "Entente préliminaire",
                "Contrat préparatoire",
                "Convention provisoire"
            ],
                    
            "solution" :  "Avant-contrat",

            "explication" : "flemme de donner une explication dsl"

        },

        "Le Pacte de préférence force celui qui le signe" : {

            "reponse" : [
                "de conclure le contrat avec toute personne intéressée",
                "de ne pas signer d'autre contrat similaire",
                "de négocier avec plusieurs parties en même temps",
                "de prioriser ses intérêts personnels",
                "de contracter immédiatement avec le bénéficiaire"
            ],
                    
            "solution" :  "de traiter prioritairement avec le bénéficiaire désigné",

            "explication" : "flemme de donner une explication dsl"

        },

        "Engagement d'une personne à proposer prioritairement au bénéficiaire désigné de traiter avec lui pour le cas où elle déciderait de contracter." : {

            "reponse" : [
                "Accord préalable",
                "Protocole d'accord",
                "Contrat cadre",
                "Clause préférentielle",
                "Entente de principe"
            ],
                    
            "solution" :  "Pacte de préférence",

            "explication" : "flemme de donner une explication dsl"

        },

        "La Promesse unilatérale de contrat engage :" : {

            "reponse" : [
                "les deux parties dès le début",
                "toutes les personnes impliquées",
                "la partie bénéficiaire uniquement",
                "les partenaires financiers",
                "tous les sous-traitants du contrat"
            ],
                    
            "solution" :  "seulement la partie qui en est à l'origine.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Engagement d'une personne de passer un contrat, qui n'engage que la partie qui en est à l'origine." : {

            "reponse" : [
                "Clause de non-concurrence",
                "Accord préliminaire",
                "Protocole de négociation",
                "Entente de coopération",
                "Contrat conditionnel"
            ],
                    
            "solution" :  "Promesse unilatérale de contrat",

            "explication" : "flemme de donner une explication dsl"

        },


        "Quel autre nom peut on donner a une promesse bilatérale de contrat ?" : {

        "reponse" : [
            "contrat conditionnel",
            "engagement unilatéral",
            "promesse unilatérale",
            "accord verbal",
            "entente provisoire"
        ],
                
        "solution" :  "promesse synallagmatique",

        "explication" : "flemme de donner une explication dsl"

        },

        "Quel est l'autre nom de la Promesse synallagmatique ?" : {

        "reponse" : [
            "promesse unilatérale",
            "contrat à durée déterminée", 
            "accord de partenariat",
            "entente commerciale",
            "protocole d'accord"
        ],
                
        "solution" :  "Promesse bilatérale de contrat",

        "explication" : "flemme de donner une explication dsl"

        },

        "Engagement de deux personnes de passer un contrat, qui engage les deux parties concernées." : {

        "reponse" : [
            "entente informelle",
            "accord verbal",
            "contrat unilatéral",
            "protocole d'engagement",
            "accord préliminaire"
        ],
                
        "solution" :  "Promesse bilatérale de contrat",

        "explication" : "flemme de donner une explication dsl"

        },

        "Quelles informations ne sommes nous pas obligé de donner selon le principe d'Obligation d'information ?" : {

        "reponse" : [
            "les conditions de paiement",
            "la durée du contrat", 
            "les pénalités de retard",
            "les raisons de l'engagement",
            "les méthodes de livraison"
        ],
                
        "solution" :  "la valeur du bien",

        "explication" : "flemme de donner une explication dsl"

        },

        "Obligation, pour un contractant, de communiquer à son cocontractant, les informations susceptibles d'être déterminantes de son consentement." : {

        "reponse" : [
            "Obligation de confidentialité",
            "Clause de non-concurrence",
            "Droit de rétractation",
            "Obligation de mise à jour",
            "Engagement de résultat"
        ],
                
        "solution" :  "Obligation d'information",

        "explication" : "flemme de donner une explication dsl"

        },

        "La Liberté contractuelle consiste en la liberté de :" : {

        "reponse" : [
            "négocier sans limite",
            "modifier unilatéralement le contrat", 
            "choisir de rompre le contrat",
            "définir les modalités de paiement",
            "engager plusieurs parties"
        ],
                
        "solution" :  "contracter ou de ne pas contracter",

        "explication" : "flemme de donner une explication dsl"

        },

        "La Liberté contractuelle consiste en la liberté de :" : {

        "reponse" : [
            "déterminer les modalités d'exécution",
            "choisir leur partenaire commercial",
            "changer le contenu sans préavis",
            "renoncer à des clauses",
            "réaliser des contrats à l'international"
        ],
                
        "solution" :  "choisir leur cocontractant",

        "explication" : "flemme de donner une explication dsl"

        },

        "La Liberté contractuelle consiste en la liberté de :" : {

        "reponse" : [
            "imposer des conditions",
            "définir les droits de propriété",
            "choisir les lois applicables",
            "décider des obligations de l'autre partie",
            "modifier le contrat après signature"
        ],
                
        "solution" :  "déterminer le contenu et la forme du contrat",

        "explication" : "flemme de donner une explication dsl"

        },
        "Principe juridique selon lequel les personnes sont libres de contracter ou de ne pas contracter, de choisir leur cocontractant, de déterminer le contenu et la forme du contrat (dans les limites fixées par la loi)." : {

            "reponse" : [
                "Liberté d'association",
                "Droit à l'information",
                "Principe d'équité",
                "Liberté d'expression",
                "Liberté de négociation"
            ],
                    
            "solution" :  "Liberté contractuelle",

            "explication" : "flemme de donner une explication dsl"

        },

        "Dans un Contrat, comment appelle on les deux entités qui font un contrat ?" : {

            "reponse" : [
                "cocontractants",
                "partenaires", 
                "participants",
                "associés",
                "intervenants"
            ],
                    
            "solution" :  "parties",

            "explication" : "flemme de donner une explication dsl"

        },

        "Dans un Contrat, quel est le terme utilisé qui désigne une annulation des obligations ?" : {

            "reponse" : [
                "révocation",
                "résiliation",
                "extinction",
                "annulation",
                "modification"
            ],
                    
            "solution" :  "éteindre",

            "explication" : "flemme de donner une explication dsl"

        },

        "Accord de volontés entre deux ou plusieurs personnes, appelées parties, destiné à créer, modifier, transmettre ou éteindre des obligations." : {

            "reponse" : [
                "engagement",
                "accord",
                "convention", 
                "protocole",
                "entente"
            ],
                    
            "solution" :  "contrat",

            "explication" : "flemme de donner une explication dsl"

        },

        "Consentement peut naitre de la rencontre :" : {

            "reponse" : [
                "l'accord verbal",
                "l'échange de lettres",
                "la négociation formelle",
                "l'offre d'un bien",
                "l'acceptation tacite"
            ],
                    
            "solution" :  "l'offre et de l'acceptation",

            "explication" : "flemme de donner une explication dsl"

        },

        "Accord des volontés des parties à un contrat réalisé par la rencontre de l'offre et de l'acceptation." : {

            "reponse" : [
                "Engagement",
                "Entente préalable",
                "Accord formel",
                "Concordance",
                "Consensus"
            ],
                    
            "solution" :  "Consentement",

            "explication" : "flemme de donner une explication dsl"

        },

        "Absence de consentement libre (en cas de violence) et éclairé (en cas d'erreur ou de dol) entraînant la nullité du contrat." : {

            "reponse" : [
                "Vices de forme",
                "Vices d'engagement",
                "Vices d'exécution", 
                "Vices d'accord",
                "Vices de légalité"
            ],
                    
            "solution" :  "Vices du consentement",

            "explication" : "flemme de donner une explication dsl"

        },

        "Une dissimulation non intentionnelle, vice du consentement, est ?" : {

            "reponse" : [
                "Dol",
                "Coup de bluff", 
                "Mauvaise foi",
                "Violence",
                "Omission"
            ],
                    
            "solution" :  "Erreur",

            "explication" : "flemme de donner une explication dsl"

        },

        "Une dissimulation intentionnelle, vice du consentement, est ?" : {

            "reponse" : [
                "Erreur",
                "Omission",
                "Coup de bluff",
                "Manipulation",
                "Violence"
            ],
                    
            "solution" :  "Dol",

            "explication" : "flemme de donner une explication dsl"

        },

        "Vice du consentement qui affecte la validité du contrat si l'erreur porte sur une des qualités essentielles de la prestation due ou sur celles du cocontractant." : {

            "reponse" : [
                "Vice caché",
                "Délai de réflexion", 
                "Droit de rétractation",
                "Dol",
                "Problème d'interprétation"
            ],
                    
            "solution" :  "Erreur",

            "explication" : "flemme de donner une explication dsl"

        },

        "Vice du consentement, constitué par des manoeuvres, des mensonges ou une dissimulation intentionnelle par une partie pour obtenir le consentement de son cocontractant." : {

            "reponse" : [
                "Erreur",
                "Manipulation",
                "Fraude", 
                "Dissimulation",
                "Chantage"
            ],
                    
            "solution" :  "Dol",

            "explication" : "flemme de donner une explication dsl"

        },

        "Vice du consentement, constitué par une contrainte physique ou morale (chantage) exercée par une personne pour obtenir l'accord de l'autre partie à un contrat." : {

            "reponse" : [
                "Délit",
                "Cohésion",
                "Pression", 
                "Dol",
                "Manipulation"
            ],
                    
            "solution" :  "Violence",

            "explication" : "flemme de donner une explication dsl"

        },

        "Aptitude d'une personne à être titulaire de droits et à les exercer." : {

            "reponse" : [
                "Responsabilité",
                "Droits civils",
                "Capacité d'agir", 
                "Capacité juridique",
                "État civil"
            ],
                    
            "solution" :  "Capacité juridique",

            "explication" : "flemme de donner une explication dsl"

        },

        "Incapacité à exercer les droits dont on est titulaire (comme conclure un contrat) en raison de l'âge (minorité) ou de l'altération des facultés personnelles chez certains majeurs (majeurs protégés)." : {

            "reponse" : [
                "Incapacité légale",
                "Inaptitude",
                "Capacité juridique", 
                "Diminution des droits",
                "Protection juridique"
            ],
                    
            "solution" :  "L'incapacité juridique",

            "explication" : "flemme de donner une explication dsl"

        },

        "Mécanisme par lequel une personne, appelée «le représentant (un dirigeant de société, un tuteur), est investie du pouvoir d'agir pour le compte d'une autre personne, appelée 'le représenté' (une société, un majeur sous tutelle)." : {
            
            "reponse" : [
                "Délégation",
                "Mandat",
                "Pouvoir de représentation", 
                "Contrat de représentation",
                "Imprésentation juridique"
            ],
                    
            "solution" :  "Représentation juridique",

            "explication" : "flemme de donner une explication dsl"

        },

        "Ensemble des engagements des parties constituant leurs obligations contractuelles." : {

            "reponse" : [
                "Conditions",
                "Dispositions",
                "Clauses", 
                "Obligations contractuelles",
                "Engagements"
            ],
                    
            "solution" :  "Contenu du contrat",

            "explication" : "flemme de donner une explication dsl"

        },

        "Sanction de l'absence d'une condition de validité du contrat consistant en l'anéantissement du contrat." : {

            "reponse" : [
                "Suspension",
                "Annulation",
                "Rupture", 
                "Non Execution",
                "Invalité"
            ],
                    
            "solution" :  "Nullité",

            "explication" : "flemme de donner une explication dsl"

        },

        "Quelle sanction est prononcée en cas d'invalidité du contrat ?" : {

            "reponse" : [
                "Dommages et intérêts",
                "Récupération des fonds",
                "Indemnisation", 
                "Amende",
                "Résiliation"
            ],
                    
            "solution" :  "L'anéantissement du contrat et de ses clauses.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Clause du contrat qui autorise le vendeur à récupérer le bien objet de la vente si l'acheteur n'a pas intégralement payé le prix selon les modalités fixées au contrat." : {

            "reponse" : [
                "Clause résolutoire",
                "Clause d'exécution",
                "Clause de rétractation", 
                "Clause de non confiidentialité",
                "Clause de non-conformité"
            ],
                    
            "solution" :  "Clause de réserve de propriété",

            "explication" : "flemme de donner une explication dsl"

        },

        "Quelle clause intervient avant la réception d'un bien, en cas de non paiement de celui-ci ?" : {

            "reponse" : [
                "Clause de livraison",
                "Clause de paiement",
                "Clause résolutoire", 
                "Clause pénale",
                "Clause de garantie"
            ],
                    
            "solution" :  "Clause de réserve de propriété",

            "explication" : "flemme de donner une explication dsl"

        },

        "Quelle clause intervient après la réception d'un bien, en cas de non paiement de celui-ci ?" : {

            "reponse" : [
                "Clause de résolution",
                "Clause de dédommagement",
                "Clause de remboursement", 
                "Clause de réserve de propriété",
                "Clause de non-paiement"
            ],
                    
            "solution" :  "Clause pénale",

            "explication" : "flemme de donner une explication dsl"

        },
        "Principe juridique selon lequel les personnes sont libres de contracter ou de ne pas contracter, de choisir leur cocontractant, de déterminer le contenu et la forme du contrat (dans les limites fixées par la loi)." : {

            "reponse" : [
                "Liberté d'engagement",
                "Droit de choix contractuel",
                "Autonomie de négociation",
                "Contrat volontaire",
                "Engagement contractuel libre"
            ],
            
            "solution" :  "Liberté contractuelle",

            "explication" : "flemme de donner une explication dsl"

        },
        "Clause du contrat qui détermine à l'avance la pénalité pécuniaire due par la partie qui n'exécuterait pas ses obligations." : {

            "reponse" : [
                "Clause compensatoire",
                "Pénalité contractuelle",
                "Avenant financier",
                "Contrat de garantie",
                "Indemnité précontractuelle"
            ],
            
            "solution" :  "Clause pénale",

            "explication" : "flemme de donner une explication dsl"

        },

        "Dispositions d'un contrat. Il existe des clauses générales, comme celle relative à l'identification des parties, et des clauses spécifiques à chaque type de contrat (vente, bail, etc.)" : {

            "reponse" : [
                "Dispositions contractuelles",
                "Articles de contrat",
                "Termes juridiques",
                "Sections d'accord",
                "Paragraphes réglementaires"
            ],
            
            "solution" :  "Clause",

            "explication" : "flemme de donner une explication dsl"

        },

        "Par quel mot pourrait on remplacer 'clause' ?" : {

            "reponse" : [
                "Article",
                "Section",
                "Extrait",
                "Point",
                "Disposition"
            ],
            
            "solution" :  "Paragraphe",

            "explication" : "flemme de donner une explication dsl"

        },

        "Changement de circonstances, imprévisible au jour du contrat, qui permet à la partie victime de demander la révision du contrat." : {

            "reponse" : [
                "Révision contractuelle",
                "Force majeure",
                "Modification unilatérale",
                "Alteration de contrat",
                "Adaptation légale"
            ],
            
            "solution" :  "Imprévision",

            "explication" : "flemme de donner une explication dsl"

        },

        "Principe selon lequel le contrat engage les parties et ne peut être remis en cause par la décision unilatérale de l'une d'entre elles." : {

            "reponse" : [
                "Engagement contractuel",
                "Responsabilité unilatérale",
                "Obligation de bonne foi",
                "Stabilité contractuelle",
                "Solidarité des parties"
            ],
            
            "solution" :  "Effet obligatoire du contrat",

            "explication" : "flemme de donner une explication dsl"

        },

        "Principe selon lequel le contrat n'a d'effet qu'entre les parties contractantes." : {

            "reponse" : [
                "Effet interne du contrat",
                "Droit des parties",
                "Limitation contractuelle",
                "Effet exclusif",
                "Impact restreint"
            ],
            
            "solution" :  "Effet relatif du contrat",

            "explication" : "flemme de donner une explication dsl"

        },

        "Dans quelle catégorie d'effet la conséquence d'une assurance vie rentre-elle ?" : {

            "reponse" : [
                "Effet direct",
                "Impact personnel",
                "Droit de créance",
                "Répercussion légale",
                "Efficacité personnelle"
            ],
            
            "solution" :  "Effet relatif du contrat",

            "explication" : "flemme de donner une explication dsl"

        },

        "Contrat par lequel un stipulant fait promettre à un promettant d'accomplir une prestation au profit d'un bénéficiaire (tiers au contrat)." : {

            "reponse" : [
                "Engagement pour autrui",
                "Promesse de service",
                "Contrat de représentation",
                "Avenant tiers",
                "Accord de bénéfice"
            ],
            
            "solution" :  "Stipulation pour autrui",

            "explication" : "flemme de donner une explication dsl"

        },

        "Element clé de l'accord des parties dans certains contrats tels que la vente et devant être déterminé ou déterminable lors de la conclusion du contrat." : {

            "reponse" : [
                "Montant déterminé",
                "Évaluation contractuelle",
                "Valeur de l'objet",
                "Quantité convenue",
                "Taux de contrat"
            ],
            
            "solution" :  "Prix",

            "explication" : "flemme de donner une explication dsl"

        },
        "Prix" : {

            "reponse" : [
                "Montant arbitraire fixé par le vendeur sans lien avec le marché.",
                "Droit accordé à une partie de renoncer à un contrat sans conséquence.",
                "Élément facultatif d'un contrat qui peut être ignoré par les parties.",
                "Condition de conformité à des normes juridiques, sans impact sur l'accord.",
                "Récompense donnée pour la création d'un document contractuel."
            ],
            
            "solution" :  "Element clé de l'accord des parties dans certains contrats tels que la vente et devant etre déterminé ou déterminable lors de la conclusion du contrat.",

            "explication" : "flemme de donner une explication dsl"

        },
        "Stipulation pour autrui" : {

            "reponse" : [
                "Accord par lequel deux parties s'engagent à partager les bénéfices d'une activité commerciale.",
                "Contrat qui impose une obligation de confidentialité à toutes les parties concernées.",
                "Engagement entre un employeur et un salarié pour un travail à durée indéterminée.",
                "Dispositif légal permettant à un créancier de céder ses droits à un tiers.",
                "Accord qui stipule les modalités de résiliation d'un contrat entre deux parties."
            ],
            
            "solution" :  "Contrat par lequel un stipulant fait promettre à un promettant d'accomplir une prestation au profit d'un bénéficiaire (tiers au contrat).",

            "explication" : "flemme de donner une explication dsl"

        },

        "Effet relatif du contrat" : {

            "reponse" : [
                "Concept qui stipule que le contrat doit être enregistré auprès d'une autorité pour être valide.",
                "Principe qui impose un délai de réflexion de 30 jours avant la signature d'un contrat.",
                "Condition selon laquelle les contrats doivent être rédigés en plusieurs langues.",
                "Règle qui permet à une partie de modifier unilatéralement les termes d'un contrat sans accord préalable.",
                "Élément qui nécessite une validation par un notaire pour être exécutoire."
            ],
            
            "solution" :  "Principe selon lequel le contrat n'a d'effet qu'entre les parties contractantes.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Effet obligatoire du contrat" : {

            "reponse" : [
                "Conditions de forme qui définissent la durée d'un contrat.",
                "Principe qui permet à l'une des parties de se désengager après un an.",
                "Droit pour une partie de renoncer à ses obligations sans conséquence.",
                "Élément qui stipule qu'un contrat peut être modifié par simple courriel.",
                "Règle qui annule tout contrat si une des parties change d'avis."
            ],
            
            "solution" :  "Principe selon lequel le contrat engage les parties et ne peut être remis en cause par la décision unilatérale de l'une d'entre elles.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Imprévision" : {

            "reponse" : [
                "Changement de responsable dans une entreprise qui impacte les contrats.",
                "Règle qui impose une révision annuelle de tous les contrats.",
                "Événement qui permet de changer l'adresse d'une partie sans formalité.",
                "Modification des conditions de travail d'un salarié à la suite d'un contrat.",
                "Situation où un contrat devient caduc après cinq ans."
            ],
            
            "solution" :  "Changement de circonstances, imprévisible au jour du contrat, qui permet à la partie victime de demander la révision du contrat.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Clause pénale" : {

            "reponse" : [
                "Dispositif qui annule automatiquement un contrat en cas de non-respect.",
                "Condition qui permet de réduire les obligations d'une partie en cas de litige.",
                "Article d'un contrat qui oblige à une médiation avant toute action judiciaire.",
                "Élément qui détermine les droits d'auteur sur un contrat.",
                "Règle qui impose un délai d'attente avant de signaler une infraction."
            ],
            
            "solution" :  "Clause du contrat qui détermine à l'avance la pénalité pécuniaire due par la partie qui n'exécuterait pas ses obligations.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Clause" : {

            "reponse" : [
                "Élément qui détermine le lieu de signature d'un contrat.",
                "Article qui impose des obligations sans lien avec le contrat.",
                "Disposition qui permet d'annuler le contrat sans raison.",
                "Condition qui fixe la durée de validité d'un contrat.",
                "Section qui détermine les modalités de paiement après la signature."
            ],
            
            "solution" :  "Dispositions d'un contrat. II existe des clauses générales, comme celle relative à l'identification des parties, et des clauses spécifiques à chaque type de contrat (vente, bail, etc.)",

            "explication" : "flemme de donner une explication dsl"

        },

        "Clause de réserve de propriété" : {

            "reponse" : [
                "Condition qui stipule le remboursement des frais de livraison.",
                "Dispositif permettant d'évaluer les biens avant la vente.",
                "Article qui impose une garantie de qualité sur les biens vendus.",
                "Élément qui autorise le vendeur à annuler un contrat sans préavis.",
                "Règle qui fixe le prix d'un bien pendant une période déterminée."
            ],
            
            "solution" :  "Clause du contrat qui autorise le vendeur à récupérer le bien objet de la vente si l'acheteur n'a pas intégralement payé le prix selon les modalités fixées au contrat",

            "explication" : "flemme de donner une explication dsl"

        },

        "Nullité" : {

            "reponse" : [
                "Disposition qui nécessite la réévaluation des biens dans un contrat.",
                "Condition qui impose des sanctions pour retard dans la signature.",
                "Règle qui permet de modifier un contrat après sa signature.",
                "Sanction qui annule les obligations d'un contrat en raison d'un accord verbal.",
                "Élément qui prolonge la durée d'un contrat en cas de litige."
            ],
            
            "solution" :  "Sanction de l'absence d'une condition de validité du contrat consistant en l'anéantissement du contrat.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Contenu du contrat" : {

            "reponse" : [
                "Élément qui définit les responsabilités des témoins d'un contrat.",
                "Partie d'un contrat qui concerne uniquement le respect des délais.",
                "Section qui décrit le processus de résiliation d'un contrat.",
                "Ensemble des conditions générales s'appliquant à tous les contrats.",
                "Règle définissant le nombre de copies d'un contrat à établir."
            ],
            
            "solution" :  "Ensemble des engagements des parties constituant leurs obligations contractuelles.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Représentation juridique" : {

            "reponse" : [
                "Concept qui stipule que tous les contrats doivent être enregistrés par un avocat.",
                "Mécanisme permettant à un notaire de créer des contrats au nom d'autres personnes.",
                "Principe selon lequel un avocat peut agir pour toute personne physique.",
                "Règle qui impose à chaque partie de se faire représenter par un tiers.",
                "Dispositif qui autorise un juge à modifier un contrat sans consentement."
            ],
            
            "solution" :  "Mécanisme par lequel une personne, appelée «le représentant (un dirigeant de société, un tuteur), est investie du pouvoir d'agir pour le compte d'une autre personne, appelée 'le représenté' (une société, un majeur sous tutelle).",

            "explication" : "flemme de donner une explication dsl"

        },

        "L'incapacité juridique" : {

            "reponse" : [
                "État qui empêche de recevoir des héritages.",
                "Condition qui limite le droit d'une personne à voyager à l'étranger.",
                "Dispositif qui annule les dettes d'une personne au-delà d'un certain âge.",
                "Règle qui interdit à un mineur de voter ou de signer des documents officiels.",
                "Concept qui empêche une personne de témoigner en justice."
            ],
            
            "solution" :  "est l'incapacité à exercer les droits dont on est titulaire (comme conclure un contrat) en raison de l'âge (minorité) ou de l'altération des facultés personnelles chez certains majeurs (majeurs protégés).",

            "explication" : "flemme de donner une explication dsl"

        },


        "Capacité juridique" : {

            "reponse" : [
                "Aptitude à participer à des activités sportives et culturelles.",
                "Condition qui limite les droits d'une personne à cause de sa nationalité.",
                "Droit d'un individu à voter aux élections locales et nationales.",
                "Compétence requise pour posséder des biens immobiliers.",
                "État d'une personne concernant sa capacité à gérer ses finances."
            ],
            
            "solution" :  "Aptitude d'une personne à être titulaire de droits et à les exercer",

            "explication" : "flemme de donner une explication dsl"

        },

        "Violence" : {

            "reponse" : [
                "État d'un contrat qui n'a pas été rédigé correctement.",
                "Situation où une partie refuse de négocier avec l'autre.",
                "Rupture d'un contrat en raison d'un manque de confiance.",
                "Condition qui nécessite une approbation légale pour un contrat.",
                "Événement naturel qui empêche la réalisation d'un contrat."
            ],
            
            "solution" :  "Vice du consentement, constitué par une contrainte physique ou morale (chantage) exercée par une personne pour obtenir l'accord de l'autre partie à un contrat.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Dol" : {

            "reponse" : [
                "Mécanisme permettant d'ajouter des clauses après la signature d'un contrat.",
                "Situation où les parties décident de prolonger un contrat existant.",
                "Condition qui impose un délai de grâce pour un paiement.",
                "Dispositif de révision automatique des prix d'un contrat.",
                "Règle qui fixe une date limite pour l'acceptation d'une offre."
            ],
            
            "solution" :  "Vice du consentement, constitué par des manoeuvres, des mensonges ou une dissimulation intentionnelle par une partie pour obtenir le consentement de son cocontractant.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Erreur" : {

            "reponse" : [
                "État de confusion qui survient avant la signature d'un contrat.",
                "Condition qui permet de changer d'avis après la signature.",
                "Élément qui justifie une réclamation de dommages et intérêts.",
                "Situation qui permet d'annuler un contrat pour des raisons de santé.",
                "Dispositif qui permet de modifier le montant d'un contrat après accord."
            ],
            
            "solution" :  "Vice du consentement qui affecte la validité du contrat si l'erreur porte sur une des qualités essentielles de la prestation due ou sur celles du cocontractant.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Vices du consentement" : {

            "reponse" : [
                "Conditions imposées par la loi pour signer un contrat.",
                "Sanctions prévues pour le non-respect d'un contrat.",
                "Obligations d'une partie à indemniser l'autre en cas de litige.",
                "Critères qui déterminent le type de contrat à établir.",
                "Éléments qui facilitent la modification des contrats existants."
            ],
            
            "solution" :  "Absence de consentement libre (en cas de violence) et éclairé (en cas d'erreur ou de dol) entraînant la nullité du contrat.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Consentement" : {

            "reponse" : [
                "Accord nécessaire pour obtenir un prêt bancaire.",
                "Nécessité d'enregistrer un contrat auprès des autorités.",
                "Engagement à respecter des normes éthiques dans un contrat.",
                "Déclaration de la volonté d'une partie à rompre un contrat.",
                "Conditions à remplir pour que le contrat soit considéré comme valide."
            ],
            
            "solution" :  "Accord des volontés des parties à un contrat réalisé par la rencontre de l'offre et de l'acceptation.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Contrat" : {

            "reponse" : [
                "Accord verbal entre deux amis sur un sujet quelconque.",
                "Document qui résume les obligations fiscales d'une entreprise.",
                "Démarche qui impose des tarifs pour des services administratifs.",
                "Évaluation de la satisfaction des clients d'un service.",
                "Convention qui définit les horaires de travail d'un employé."
            ],
            
            "solution" :  "Accord de volontés entre deux ou plusieurs personnes, appelées parties, destiné à créer, modifier, trans- mettre ou éteindre des obligations.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Liberté contractuelle" : {

            "reponse" : [
                "Principe qui oblige les parties à respecter des tarifs imposés.",
                "Règle qui exige que tous les contrats soient notariés.",
                "Condition qui limite le choix d'un partenaire commercial.",
                "Dispositif qui permet de changer le contenu d'un contrat à tout moment.",
                "Exigence de divulguer les revenus de chaque partie avant un contrat."
            ],
            
            "solution" :  "Principe juridique selon lequel les personnes sont libres de contracter ou de ne pas contracter, de choisir leur cocontractant, de déterminer le contenu et la forme du contrat (dans les limites fixées par la loi).",

            "explication" : "flemme de donner une explication dsl"

        },

        "Obligation d'information" : {

            "reponse" : [
                "Condition de former une équipe pour signer un contrat.",
                "Exigence de fournir des documents financiers avant un accord.",
                "Règle qui impose de consulter un avocat avant toute négociation.",
                "Droit de demander des informations sur les concurrents.",
                "Principe qui impose un délai pour fournir des preuves d'identité."
            ],
            
            "solution" :  "Obligation, pour un contractant, de communiquer à son cocontractant, les informations susceptibles d'être déterminantes de son consentement.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Promesse bilatérale de contrat" : {

            "reponse" : [
                "Engagement d'une personne à informer l'autre de ses intentions.",
                "Accord verbal sans formalité écrite.",
                "Engagement d'une seule personne à signer un contrat plus tard.",
                "Règle qui impose un paiement avant la signature d'un contrat.",
                "Obligation de respecter un code de conduite durant les négociations."
            ],
            
            "solution" :  "Engagement de deux personnes de passer un contrat, qui engage les deux parties concernées.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Promesse unilatérale de contrat" : {

            "reponse" : [
                "Accord qui exige l'acceptation d'un tiers pour être valide.",
                "Engagement qui annule automatiquement les obligations d'un contrat.",
                "Dispositif qui impose un délai de réflexion avant la signature.",
                "Engagement qui nécessite une approbation écrite de tous les partis.",
                "Condition qui permet de renoncer à un contrat à tout moment."
            ],
            
            "solution" :  "Engagement d'une personne de passer un contrat, qui n'engage que la partie qui en est à l'origine.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Pacte de préférence" : {

            "reponse" : [
                "Engagement à informer le public avant de signer un contrat.",
                "Accord qui permet à une partie de ne pas signer si elle le souhaite.",
                "Dispositif qui fixe des conditions de paiement pour un contrat.",
                "Obligation de s'inscrire sur une liste pour avoir droit à un contrat.",
                "Règle qui nécessite un vote pour décider de la validité d'un contrat."
            ],
            
            "solution" :  "Engagement d'une personne à proposer prioritairement au bénéficiaire désigné de traiter avec lui pour le cas où elle déciderait de contracter.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Avant-contrat" : {

            "reponse" : [
                "Accord de confidentialité entre deux parties.",
                "Engagement qui empêche une partie de signer un contrat.",
                "Condition qui impose une réévaluation des prix.",
                "Dispositif qui fixe des délais de paiement pour un contrat.",
                "Règle qui exige que toutes les modifications soient notifiées."
            ],
            
            "solution" :  "Engagement contractuel d'une ou de plusieurs parties dont la finalité est de préparer la conclusion d'un contrat à venir.",

            "explication" : "flemme de donner une explication dsl"

        },

        "Pourparlers" : {

            "reponse" : [
                "Phase où les parties signent un contrat.",
                "Étape qui nécessite une approbation officielle.",
                "Discussions entre avocats avant la signature d'un contrat.",
                "Évaluation des risques financiers avant un contrat.",
                "Négociations qui impliquent des représentants gouvernementaux."
            ],
            
            "solution" :  "Phase préliminaire à la conclusion (ou passation) du contrat durant laquelle sont discutées les clauses qu'il pourrait contenir. Aucune partie n'est engagée à ce stade.",

            "explication" : "flemme de donner une explication dsl"

        },


    },
    "theme2": {


        "3 + 3" : {

            "reponse" : [
                "reponse1",
                "reponse2", 
                "reponse3",
                "reponse4",
                "reponse5",
                ],
            
            "solution" :  "6",

            "explication" : "explication"

        },

        "4 + 4" : {

            "reponse" : [
                "reponse1",
                "reponse2",
                "reponse3",
                "reponse4",
                "reponse5",
                ],
            
            "solution" :  "8",

            "explication" : "explication"

        },
    },
}

class Machine:
    
    def __init__(self):
        # Poser une question, verifier sa réponse
        self.question_actuelle = None
        self.reponses_possibles = []
        self.panel_de_reponses = []
        self.explications = None
        self.solution = None
        self.theme_actuel = None
        self.reponse_choisie = None
        self.numero_de_la_question = 1

        # Parametres 
        self.mode_sans_echec = False
        self.mode_correction = False
        self.indice_de_question_a_reposer = 0
        self.mode_timer = False
        self.timer = 0
        self.temps_debut = 0
        self.temps_fin = 0
        self.score = 0
        self.nombre_de_reponses = 4
        self.theme_possible = []
        self.questions_mal_repondues = []
        self.nombre_de_question_max = 20
        self.jeu_termine = True
        self.partie_en_cours = True
        self.dictionnaire_de_sauvegarde = {}

    def GenererUnLog(self, erreur):
        """
        Ecrit un log contenant l'erreur ayant cause le crash du quizz
        """

        dir_path = os.path.dirname(os.path.realpath(__file__))
        chemin_du_fichier = dir_path + "/" + "error_log.txt"
        date_et_heure = time.strftime("%Y-%m-%d %H:%M")
        erreur = traceback.format_exc()
        with open(chemin_du_fichier, "a") as fichier:
            fichier.write(
                "-----------------------------------------"
                "------------------------------------------"
                "------------------------------------------"
                "------------------------------------------"
                f"---------\n{date_et_heure}\nDébut du Log\n\n"
            )
            fichier.write(f"{erreur}")
            fichier.write(
                "\nFin du Log\n-----------------------------"
                "-------------------------------------------"
                "-------------------------------------------"
                "-------------------------------------------"
                "------------------\n"
            )
        print("Une erreur est survenue pendant le déroulement du quizz.")
        print(
            "L'écriture d'un rapport d'erreur est en cours dans le fichier error_log.txt."
        )
        print("Veuilez patienter 3 secondes...")
        time.sleep(3)
        self.AppuyerSurEntreePourContinuer()

    def GenererQuestion(self):
        """
        Genere une question aleatoire a partir d'un theme aleatoire parmis une liste de ceux choisis
        """

        if self.mode_correction:

            question_a_poser = self.questions_mal_repondues[self.indice_de_question_a_reposer]

            # Mettre a jour les variables de l'objet
            self.theme_actuel = question_a_poser["theme"]
            self.question_actuelle = question_a_poser["question"]
            self.reponses_possibles = question_a_poser["reponse"]
            self.solution = question_a_poser["solution"]
            self.explications = question_a_poser["explication"]
            self.numero_de_la_question = question_a_poser["numero de question"]

        else:

            # choisir un theme aléatoire parmis ceux choisis par l'utilisateur
            theme_a_utiliser = random.choice(tuple(self.theme_possible))

            # affecter l'ensemble des question de ce theme a une variable
            dictionnaire_de_question = BASE_DE_DONNEE[theme_a_utiliser]

            # prendre une question aleatoire dans la variable
            question_generee_aleatoirement = random.choice(tuple(dictionnaire_de_question.keys()))

            # recuperer toute les valeurs de la clé *question genere aleatoirement* dans la base de donnee
            reponses_et_solution_de_la_question = BASE_DE_DONNEE[theme_a_utiliser][question_generee_aleatoirement]

            # recuperer la liste de reponses possibles
            liste_de_reponses = reponses_et_solution_de_la_question["reponse"]

            # recuperer la veritable reponse : la solution
            solution_de_la_question = reponses_et_solution_de_la_question["solution"]

            # recuperer l'explication, si l'utilisateur se trompe
            explication_de_la_solution = reponses_et_solution_de_la_question["explication"]
            
            # Mettre a jour les variables de l'objet
            self.theme_actuel = theme_a_utiliser
            self.question_actuelle = question_generee_aleatoirement
            self.reponses_possibles = list(liste_de_reponses)
            self.solution = solution_de_la_question
            self.explications = explication_de_la_solution

    def GenererPanelDeReponses(self):
        liste_de_reponses = list(self.reponses_possibles)
        position_de_la_solution = random.randint(0, self.nombre_de_reponses - 1)
        panel_de_reponses = []

        position_de_la_reponse = 0
        for _ in range(0, self.nombre_de_reponses):
            random.shuffle(liste_de_reponses)
            if position_de_la_reponse == position_de_la_solution:
                panel_de_reponses.append(self.solution)
            else:
                reponse_a_mettre_dans_panel = liste_de_reponses.pop(0)
                panel_de_reponses.append(reponse_a_mettre_dans_panel)
            position_de_la_reponse += 1
        
        self.panel_de_reponses = list(panel_de_reponses)
    
    def AppuyerSurEntreePourContinuer(self):
        """
        Demande un input puis nettoie la console
        """
        input("(Appuyez sur entrée pour continuer)")
        self.ClearConsole()

    def ClearConsole(self):
        os.system("cls" if os.name == "nt" else "clear")


    def PoserQuestion(self):

        self.temps_debut = time.time()

        while True:
            try:

                print(f"Question {self.numero_de_la_question} :\n\n")
                print(f"{self.question_actuelle}\n\n")

                index_de_la_reponse = 0
                for position_de_la_reponse in range(1, self.nombre_de_reponses + 1):
                    print(f"    {position_de_la_reponse} - {self.panel_de_reponses[index_de_la_reponse]}")
                    index_de_la_reponse += 1
                
                choix_de_lutilisateur = int(input("\n\nFaites votre choix avec les nombres : "))
                self.ClearConsole()

                if choix_de_lutilisateur in range(1, self.nombre_de_reponses + 1):
                    self.reponse_choisie = self.panel_de_reponses[choix_de_lutilisateur - 1]
                    self.numero_de_la_question += 1
                    break

            except ValueError:
                self.ClearConsole()

    def ResultatQuestion(self):

        if self.mode_timer:

            self.temps_fin = time.time()
            temps_mis_a_repondre = self.temps_fin - self.temps_debut

            if self.reponse_choisie == self.solution and temps_mis_a_repondre <= self.timer :

                print("C'est Exact !\n")
                self.AppuyerSurEntreePourContinuer()

                self.score += 1

                if self.mode_correction:
                    self.questions_mal_repondues.pop(self.indice_de_question_a_reposer)

            else:
                
                if self.reponse_choisie != self.solution:

                    if self.mode_correction:
                        self.indice_de_question_a_reposer += 1

                    print("C'est Faux ! Voici l'explication :\n\n")
                    print(f"{self.explications}\n")

                else:

                    if self.mode_correction:
                        self.indice_de_question_a_reposer += 1

                    print("C'est vrai ! Mais vous avez mis trop de temps a répondre.")

                self.AppuyerSurEntreePourContinuer()

                if not self.mode_correction:
                    valeurs_de_la_question_mal_repondue = {
                        "theme" : self.theme_actuel,
                        "question" : self.question_actuelle,
                        "reponse" : self.reponses_possibles,
                        "solution" : self.solution,
                        "explication" : self.explications,
                        "numero de question" : self.numero_de_la_question - 1
                    }

                    self.questions_mal_repondues.append(valeurs_de_la_question_mal_repondue)


        else:
            if self.reponse_choisie == self.solution :

                if self.mode_correction:
                    self.questions_mal_repondues.pop(self.indice_de_question_a_reposer)

                print("C'est Exact !\n")
                self.AppuyerSurEntreePourContinuer()

                self.score += 1

            else:

                print("C'est Faux ! Voici l'explication :\n\n")
                print(f"{self.explications}\n")
                self.AppuyerSurEntreePourContinuer()

                if self.mode_correction:
                    self.indice_de_question_a_reposer += 1

                if not self.mode_correction:
                    valeurs_de_la_question_mal_repondue = {
                        "theme" : self.theme_actuel,
                        "question" : self.question_actuelle,
                        "reponse" : self.reponses_possibles,
                        "solution" : self.solution,
                        "explication" : self.explications,
                        "numero de question" : self.numero_de_la_question - 1
                    }

                    self.questions_mal_repondues.append(valeurs_de_la_question_mal_repondue)
    
    def LanceUnRound(self):

        Quizz.GenererQuestion()
        Quizz.GenererPanelDeReponses()
        
        Quizz.PoserQuestion()    

        Quizz.ResultatQuestion()

    def ResultatsFinaux(self):
        nombre_de_question_mal_repondues = len(self.questions_mal_repondues)
        if self.mode_sans_echec and nombre_de_question_mal_repondues != 0 :

            print(f"Vous avez fait {nombre_de_question_mal_repondues} erreurs.")
            print("Corrigez cela !")
            self.AppuyerSurEntreePourContinuer()

            self.nombre_de_question_max = nombre_de_question_mal_repondues
            self.mode_correction = True
            self.indice_de_question_a_reposer = 0
            


        else:
            if self.mode_sans_echec:
                self.nombre_de_question_max = self.score
                self.mode_correction = False
                self.questions_mal_repondues = []

            while True:
                try :
                    print("Résultats Finaux :\n\n")
                    print(f"         {self.score} / {self.nombre_de_question_max}\n\n")
                    print("Refaire une partie ?")
                    print("\n       1 - Oui")
                    print("       2 - Non\n")
                    choix_de_lutilisateur = int(input("Faites votre choix avec les nombres : "))
                    self.ClearConsole()

                    if choix_de_lutilisateur in [1, 2]:
                        self.indice_de_question_a_reposer = 0
                        self.score = 0
                        self.numero_de_la_question = 1
                        self.partie_en_cours = False
                        break

                except ValueError:
                    self.ClearConsole()
            
            if choix_de_lutilisateur == 2:
                self.jeu_termine = False

    def FinDePartie(self):
        print("Bye-bye !")
        time.sleep(2)
        sys.exit()

    def MenuPrincipal(self):
        while True:
            while True:
                try:
                    print("             -=The *ULTIMATE* Quizz Machine=-")
                    print("\n\n     1 - Options\n")
                    print("     2 - Charger une configuration\n")
                    print("     3 - Lancer une partie avec les options suivantes :")
                    print(f"             Thème(s) abordé(s) : {self.theme_possible}")
                    print(f"             Nombre de questions : {self.nombre_de_question_max}")
                    print(f"             Nombre de réponses : {self.nombre_de_reponses}")
                    if Quizz.mode_timer:
                        print(f"             Timer : {self.timer}")
                    else:
                        print(f"             Timer : Non")
                    if Quizz.mode_sans_echec:
                        print(f"             Mode sans échec : Oui\n\n")
                    else:
                        print(f"             Mode sans échec : Non\n\n")

                    choix_de_lutilisateur = int(input("Faites votre choix avec les nombres : "))
                    self.ClearConsole()
                    if choix_de_lutilisateur in [1, 2, 3]:
                        break
                
                except ValueError:
                    self.ClearConsole()
                
            if choix_de_lutilisateur == 1:
                self.AppliqueDesOptions()
            
            
            elif choix_de_lutilisateur == 2:
                Quizz.ChargeConfiguration()

            else:
                self.partie_en_cours = True
                break



    def AppliqueDesOptions(self):
        while True:
            while True:
                try:

                    print("                  -=OPTIONS=-")
                    print(f"\n\n        Thème(s) abordé(s) : {self.theme_possible}")
                    print(f"        Nombre de questions : {self.nombre_de_question_max}")
                    print(f"        Nombre de réponses : {self.nombre_de_reponses}")
                    if Quizz.mode_timer:
                        print(f"        Timer : {self.timer}")
                    else:
                        print(f"        Timer : Non")
                    if Quizz.mode_sans_echec:
                        print(f"        Mode sans échec : Oui\n\n")
                    else:
                        print(f"        Mode sans échec : Non\n")
                    print("\n\n     1 - Gérer le(s) thèmes abordés")
                    print("     2 - Gérer le nombre de questions à poser")
                    print("     3 - Gérer le nombre de réponses proposés")
                    print("     4 - Gérer le timer")
                    print("     5 - Gérer le mode sans échec\n\n")
                    print("     6 - Sauvegarder la configuration actuelle\n\n")
                    print("     7 - Retourner au menu principal\n\n")

                    choix_de_lutilisateur = int(input("Faites votre choix avec les nombres : "))
                    self.ClearConsole()

                    if choix_de_lutilisateur in range(1, 8):
                        break

                except ValueError:
                    self.ClearConsole()
            
            if choix_de_lutilisateur == 1:
                Quizz.GereLesThemes()

            elif choix_de_lutilisateur == 2:
                Quizz.GereLesNombresDeQuestions()

            elif choix_de_lutilisateur == 3:
                Quizz.GereLesNombresDeReponse()

            elif choix_de_lutilisateur == 4:
                Quizz.GereLeTimer()

            elif choix_de_lutilisateur == 5:
                Quizz.GereLeModeSansEchec()

            elif choix_de_lutilisateur == 6:
                Quizz.SauvegardeConfiguration()

            else:
                break

    def SauvegardeConfiguration(self):

        # transformer les parametres en dictionaire
        self.dictionnaire_de_sauvegarde["Themes Abordés"] = self.theme_possible
        self.dictionnaire_de_sauvegarde["Nombre De Questions"] = self.nombre_de_question_max
        self.dictionnaire_de_sauvegarde["Nombre de Réponses"] = self.nombre_de_reponses
        self.dictionnaire_de_sauvegarde["Mode Timer"] = self.mode_timer
        self.dictionnaire_de_sauvegarde["Timer"] = self.timer
        self.dictionnaire_de_sauvegarde["Mode Sans Echec"] = self.mode_sans_echec

        # sauvegarder le dictionnaire sur un fichier texte
        dir_path = os.path.dirname(os.path.realpath(__file__))
        chemin_du_fichier_save = dir_path + "/configuration_sauvegarde.txt"
        with open(chemin_du_fichier_save, "w") as fichier:
            fichier.write("Option|Valeur")
            for caracteristic in self.dictionnaire_de_sauvegarde:
                fichier.write(
                    f"\n{caracteristic}|{self.dictionnaire_de_sauvegarde[caracteristic]}"
                )
            
        print("\n\n\n                 Fichier Sauvegardé !\n\n")
        self.AppuyerSurEntreePourContinuer()

    def ChargeConfiguration(self):

        # recuperer les donnees du txt et les mettre dans le dictionnaire
        dir_path = os.path.dirname(os.path.realpath(__file__))
        # fichier de sauvegarde 
        chemin_du_fichier_save = dir_path + "/configuration_sauvegarde.txt"
        with open(chemin_du_fichier_save, "r") as fichier:
            reader = csv.DictReader(fichier, delimiter="|")
            for line in reader:
                self.dictionnaire_de_sauvegarde[line["Option"]] = line[
                    "Valeur"
                ]

        # transformer le dictionnaire en parametre
        self.theme_possible = ast.literal_eval(self.dictionnaire_de_sauvegarde["Themes Abordés"])
        self.nombre_de_question_max = int(self.dictionnaire_de_sauvegarde["Nombre De Questions"])
        self.nombre_de_reponses = int(self.dictionnaire_de_sauvegarde["Nombre de Réponses"])
        self.mode_timer = ast.literal_eval(self.dictionnaire_de_sauvegarde["Mode Timer"])
        self.timer = int(self.dictionnaire_de_sauvegarde["Timer"])
        self.mode_sans_echec = ast.literal_eval(self.dictionnaire_de_sauvegarde["Mode Sans Echec"])


    def GereLeModeSansEchec(self):
        while True:
            while True:
                try:

                    print("                -=Mode Sans Echec=-")
                    print(f"\n\n     Permet de continuer la partie après sa fin,")
                    print(f"     en reposant uniquement les questions auxquelles vous avez échoué,")
                    print(f"     jusqu'à ce qu'il n'y aie plus de questions a poser.")
                    if self.mode_sans_echec:
                        print(f"\n\n            Mode Sans Echec : Activé")
                    else:
                        print(f"\n\n            Mode Sans Echec : Désactivé")
                    print("\n\n     1 - Activer/Désactiver cette option")
                    print("     2 - Retourner aux options")
                    choix_de_lutilisateur = int(input("\n\nFaites votre choix avec les nombres : "))
                    self.ClearConsole()
                    if choix_de_lutilisateur in [1, 2]:
                        break

                except ValueError:
                    self.ClearConsole()
            
            if choix_de_lutilisateur == 1 and self.mode_sans_echec:
                self.mode_sans_echec = False

            elif choix_de_lutilisateur == 1 and not self.mode_sans_echec:
                self.mode_sans_echec = True

            elif choix_de_lutilisateur == 2:
                break

    def GereLesNombresDeReponse(self):
        while True:
            try:

                print("             -=Nombre de réponses proposés=-")
                print(f"\n\n     Nombre Actuel : {self.nombre_de_reponses}")
                choix_de_lutilisateur = int(input("\n\nFaites un choix entre 2 et 6 compris : "))
                self.ClearConsole()
                if choix_de_lutilisateur in range(2, 7):
                    self.nombre_de_reponses = choix_de_lutilisateur
                    break

            except ValueError:
                self.ClearConsole()

    def GereLesNombresDeQuestions(self):
        while True:
            try:

                print("             -=Nombre de questions a poser=-")
                print(f"\n\n     Nombre Actuel : {self.nombre_de_question_max}")
                choix_de_lutilisateur = int(input("\n\nDonnez un nombre superieur a 0 : "))
                self.ClearConsole()
                if choix_de_lutilisateur >= 1:
                    self.nombre_de_question_max = choix_de_lutilisateur
                    break

            except ValueError:
                self.ClearConsole()

    def GereLeTimer(self):
        while True:
            try:

                print("             -=Le Timer=-")
                print(f"\n\n     Timer* : {self.timer}")
                print("\n*Temps limite, en seconde entiere, pour répondre a chaque questions.\nUne réponse juste mais donnée trop lentement sera fausse.\nMettez le timer a 0 pour le désactiver.")
                choix_de_lutilisateur = int(input("\n\nDonnez un nombre : "))
                self.ClearConsole()

                if choix_de_lutilisateur == 0:
                    self.mode_timer = False
                    self.timer = choix_de_lutilisateur
                    break
                elif choix_de_lutilisateur > 0 :
                    self.mode_timer = True
                    self.timer = choix_de_lutilisateur
                    break

            except ValueError:
                self.ClearConsole()


    def GereLesThemes(self):
        while True:
            while True:
                try:

                    liste_de_themes_disponibles = []

                    for cle in BASE_DE_DONNEE:
                        liste_de_themes_disponibles.append(cle)

                    print("             -=Liste des thèmes disponibles=-\n\n")
                    
                    position_du_theme = 1
                    for cle in liste_de_themes_disponibles:
                        
                        if cle in self.theme_possible:
                            print(f"        {position_du_theme} - Désactiver le thème {cle}")

                        else:
                            print(f"        {position_du_theme} - Activer le thème {cle}")

                        position_du_theme += 1
                    print(f"        {position_du_theme} - Revenir aux options\n\n")

                    choix_de_lutilisateur = int(input("Faites votre choix avec les nombres : "))
                    self.ClearConsole()

                    if choix_de_lutilisateur in range (1, position_du_theme + 1):
                        break

                except ValueError:
                    self.ClearConsole()

            if choix_de_lutilisateur == position_du_theme :
                break

            else:
                theme_choisi = liste_de_themes_disponibles[choix_de_lutilisateur - 1]

                if theme_choisi in self.theme_possible:
                    self.theme_possible.remove(theme_choisi)

                else:
                    self.theme_possible.append(theme_choisi)


                

            

            
        
        
    

Quizz = Machine()

while Quizz.jeu_termine:

    try:

        Quizz.MenuPrincipal()

        while Quizz.partie_en_cours:

            for _ in range(0, Quizz.nombre_de_question_max):

                Quizz.LanceUnRound()

            Quizz.ResultatsFinaux()
        
    except Exception as error:

        Quizz.GenererUnLog(error)

Quizz.FinDePartie()

        
