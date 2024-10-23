A - Installation du programme

Faut python 3.7 (téléchargeable en ligne ou sur le Microsoft store)
Apres tu double clique sur le programme et c'est good. 
au pire tu me fait un mp discord et j'essayerait de voit pk ca marche pas.

NB : moi je suis sur Windows, donc je sais pas si ca marche sur linux. devrait pas y avoir de problèmes, mais on sait jamais, au cas ou tu m'appelle.

NB 2: le truc est codé aux petits oignons, et marche même sur ton portable ! No joke, moi j'arrive a le lancer sur mon android avec l'appli *Pydroid3*.





B - Utilisation du programme

Dans les options tu peut configurer ta partie. Genre, aborder un ou plusieurs thèmes, mettre en mode contre la montre, etc. 

Une fois que ta mis ce que tu voulais en options, tu peut enregistrer ces options (elles seront mises dans le fichier texte configuration sauvegarde)
   comme ca si tu quitte la partie et que tu veux ne refaire une, ta pas besoin de repasser 50 ans dans les options a remettre ce que tu voulais,
   tu peut juste charger une configuration (les options que ta sauvegardé) dans le menu principal et lancer une partie.

Apres, tu lance la partie. Ta des questions, tu répond avec les nombres, et si j'ai pas la flemme je te donne une explication qui donne la bonne réponse
   si tu t'es gourré.

C'est pas sorcier mdrrr






C - Ajout de themes et questions personnalisées


Vous voulez rajouter vos propres questions et themes ? c'est facile !
C'est même intuitif !
Mais si vous n'y arrivez pas, voici un guide extensif :

1 - Théorie

Dans la variable BASE_DE_DONNEE, on a plusieurs boites "theme". 
Cela correspond aux différents themes des questions, genre "les répertoires" ou "compter en base binaire".
Ces boites sont des dictionnaires, donc leur nom doit etre suivi de : { et doit se refermer quelque part avec un }
Vous remplacez le nom "theme" de ces boites par le nom de votre theme (Cours sur les réseaux)

Dans les boites dictionnaires, on a plusieurs boites "questions".
Elles correspondent aux question possible du theme, et c'est aussi des dictionnaires, donc : { et } .
Vous remplacez le nom "question" de ces boite par la question que vous voulez poser (genre, "Combien font 2 + 2 ?")

Dans les boites "questions", on a plusieurs boites.

la boite "réponse" est une liste contenant les différentes réponses proposées a la question. Ces réponses sont fausses, donc ne mettez pas la bonne réponse parmis elle.
C'est une liste, donc chaque réponse se trouve dans un [ ] , séparés par des virgules.
Vous remplacez les "reponse1" "réponse2" etc par des réponses fausses destinées a tromper le joueur.

la boite "solution" est une simple valeur, a laquelle on associe la bonne réponse a la question, cachées parmis les mauvaises réponses mises dans la boite "reponse".
Vous remplacez la valeur associée, juste derriere le : apres "solution", par la véritable bonne réponse.

la boite "explication" est similaire a la boite "solution", sauf quelle donne une explication unique a toute mauvaise réponse de la question. Genre si le joueur se trompe, il verra ce qui est dans la boite explication, et comprendra son erreur, ou a minima la bonne réponse qu'il fallait choisir.

En gros, on a des boites "Theme" dans lesquelles se trouvent des boites "Questions", dans lesquelles se trouvent une boite "Réponses" donnant une liste de réponses fausses, une boite "Solution" donnant la bonne réponse unique, et une boite "Explication" donnant des explication en cas de mauvaise réponse.

NB: ne pas mettre plus de 5 réponses fausses dans la boite "Réponse".

2 - Pratique 

voici la structure d'une boite theme (a copier coller a outrance, y compris les boites question a poser numero x") :




      "Theme des Questions": {
      
        "Question a Poser Numéro 1" : {

            "reponse" : [
                "Reponse Fausse Numero 1",
                "Reponse Fausse Numero 2", 
                "Reponse Fausse Numero 3",
                "Reponse Fausse Numero 4",
                "Reponse Fausse Numero 5",
                ],
            
            "solution" :  "Véritable et Unique Bonne Réponse",

            "explication" : "Explication a donner en cas de mauvaise réponse"

        },

        "Question a Poser Numéro 2" : {

            "reponse" : [
                "Reponse Fausse Numero 1",
                "Reponse Fausse Numero 2", 
                "Reponse Fausse Numero 3",
                "Reponse Fausse Numero 4",
                "Reponse Fausse Numero 5",
                ],
            
            "solution" :  "Véritable et Unique Bonne Réponse",

            "explication" : "Explication a donner en cas de mauvaise réponse"

        },
        
      },

NB : ne jamais changer le nom "reponse" "solution" et "explication". Le reste, faites ce que vous voulez.
