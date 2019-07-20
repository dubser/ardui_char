# ardui_char
Projet de plateforme basée sur Arduino-Raspburrypi
Voir le Wiki a la page Home pour la documentation diverse.
# Commentaires
Je viens tout juste de terminer la mise en route de ce Kit, que j'ai interfacé avec un RPI3b. Tout ce qui est annoncé fonctionne correctement et la documentation est précise et sans erreurs laissant peu de place a interprétation. La documentation écrite fournie avec le kit est aussi disponible sur le site de SunFounder. Leur site complète l'écrit et donne les références pour tous les modules utilisés. Le fonctionnement avec un une console Androide est assez fluide. Tout le logiciel est ouvert et visible sur GitHub incluant l'interface Androide construite avec MIT Application Inventor. Constitue une source très complète d'exemples pour ceux intéressés par la robotique et dans une moindre mesure Iot.

# Notes

Je décèle cependant quelques faiblesses et fragilités dont l'examen va me permettre d'approfondir les technologies en présence:
1. Incompréhension de la technique de calibration avec l'application Android.
2. Clignotement occasionnel de la LED rouge du Rpi
3. Perte de connexion occasionnelle.


# Debugging

* L'application WebMin a été installée avec succès sur le Rpi à ma grande surprise. Ceci sera d'une grande utilité pour aider au diagnostic sur ce pc headless.
* Le logging a été rendu possible dans view.pi de Django en utilisant:

<blockquote>
import syslog  
  
syslog.syslog("Message de test de Sdube")  
</blockquote>  

* Pour suivre en continu les inscription dans syslog la commande suivante est utile:  

<blockquote>
tail -f /var/log/syslog
</blockquote> 
