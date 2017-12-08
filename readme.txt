De base le projet consister à pouvoir gérer et trouver au besoin des outils nécessaires à la prévention de la sécurité routière, des outils tels que voiture tonneau, voiture choc... Afin que les gens voulant réaliser ce type d'évènement puissent facilement trouver ce qu'il faut.

Par manque de temps nous avons utilisé l'API donné par OptimData sur des outis industriels, ainsi que l'API de Wit.ai pour réaliser l'entraînement du chatbot.

Installation :

-Avoir python3 installer

-Soit installer sur le python soit créer un nouvel environnement

pip install -r requirements.txt 
 
-Lancez l'application :

python chatbot.py

-Vous pouvez ensuite poser des questions au chatbot qui vous répondra. Il comprends les questions même avec des fautes d'orthographe raisonnables.

        - Afficher la liste des machines :
        
        Peux-tu me donner toutes les machines disponibles ? / Peux-tu me donner la liste des machines disponibles ? / Liste machine ...
        
        - Se connecter à une machine : 
        
        Je veux me connecter à nom_machine / Connexion nom_machine
        
        - Géocaliser la machine :
        
        Où se trouve cette machine ? / Où se trouve nom_machine
        
        - Accéder à la documentation d’une machine
        
        Donne moi la documentation de la machine actuelle

        - Accéder aux propriétés de la machine :
        
        Donne moi les valeurs que je peux consulter de cette machine / Donne moi les propriétés de cette machine
        
        À quand remonte la dernière erreur de cette machine ? 