De base le projet consister � pouvoir g�rer et trouver au besoin des outils n�cessaires � la pr�vention de la s�curit� routi�re, des outils tels que voiture tonneau, voiture choc... Afin que les gens voulant r�aliser ce type d'�v�nement puissent facilement trouver ce qu'il faut.

Par manque de temps nous avons utilis� l'API donn� par OptimData sur des outis industriels, ainsi que l'API de Wit.ai pour r�aliser l'entra�nement du chatbot.

Installation :

-Avoir python3 installer

-Soit installer sur le python soit cr�er un nouvel environnement

pip install -r requirements.txt 
 
-Lancez l'application :

python chatbot.py

-Vous pouvez ensuite poser des questions au chatbot qui vous r�pondra. Il comprends les questions m�me avec des fautes d'orthographe raisonnables.

        - Afficher la liste des machines :
        
        Peux-tu me donner toutes les machines disponibles ? / Peux-tu me donner la liste des machines disponibles ? / Liste machine ...
        
        - Se connecter � une machine : 
        
        Je veux me connecter � nom_machine / Connexion nom_machine
        
        - G�ocaliser la machine :
        
        O� se trouve cette machine ? / O� se trouve nom_machine
        
        - Acc�der � la documentation d�une machine
        
        Donne moi la documentation de la machine actuelle

        - Acc�der aux propri�t�s de la machine :
        
        Donne moi les valeurs que je peux consulter de cette machine / Donne moi les propri�t�s de cette machine
        
        � quand remonte la derni�re erreur de cette machine ? 