define m = Character('Moi', color="#c8ffc8")
define t = Character('Tom', color="#c8ffc8")
define l = Character('Luca', color="#c8ffc8")
define e = Character('Emilien', color="#c8ffc8")
define w = Character('Will', color="#c8ffc8")

label start:

    "Cette année était parfaitement normale, jusqu’a ce qu’un virus qui transforme les gens en Zombie s’échappe du laboratoire près de chez moi... Ca fait deux jours que je suis coincée dans mon école à me cacher des zombies...Mais je commence à faiblir... AHH les zombies m’ont repéré..."

    "...Qu’est ce qui c’est passe ??"
    
    "...La dernière chose dont je me rappelle... c’est les zombies qui m’ont attaquée"

    "...est ce que je suis morte? \nNan ma tete me fait trop mal pour ca."

    scene ecole with dissolve
    show tom_neutral with dissolve
   
    "AHHH un monstre!!!"

    "...non il a l’air humain"

    menu:
        t "Tu vas bien ?"

        "Pas trop, ma tête me fait mal. C’est toi qui m’as sauvé? Merci !":
            $ temp = False 
        "C’est les zombies qui t’ont pris ton t-shirt?":
            $ temp = False
        "Oui ça va.":
            $ temp = False

    menu:
        t "Tu es seule? Tu veux que je te raccompagne? \n\n\n(…Il a l’air fort, ça pourrait m’être utile. Mais je ne l’ai jamais vu, est ce que c’est un élève ?)" 
    
        "Comment tu t’appelles?":
            hide tom_neutral
            show tom_happy
            t "Je suis Tom du TD05, c’est mon premier jour, viens on va rejoindre mes amis."
        "Non, je peux me débrouiller toute seule":
            hide tom_neutral
            show tom_happy
            t "Je suis Tom du TD05, c’est mon premier jour, viens on va rejoindre mes amis."

    hide tom_happy

    "...Je marche dans les couloirs, mais j’entends un bruit sur la droite, qu’est ce que c’est..."
    "DES ZOMBIES !!!"

    "CCCCOOOOMMMMMBBBBAAAAATTTTTTT"

    hide tom_happy
    show luca_angry

    l "Mais où t'étais Tom ? Je meurs de faim, ça fait 4 heures que je t’ai envoyé chercher des sandwichs à la cafet"

    "… Mais je le connais lui, c’est Luca. C’est le gars le plus populaire de l’école, qu’est ce qu’il est beau…"
    
    "J’ai entendu dire qu’il était insupportable. mais qu’est ce qu’il est beau…"

    menu:
        l "Et c’est qui ce boulet, pourquoi elle a le front ouvert? Tu l’as trouvé ou?"

        "Je me suis faite attaquer par des zombies, et Tom m’as sauvée":
            l "C’est pas à toi que je parlais, et arrête de mettre du sang partout, tu vas attirer les zombies !"

        " Et toi t’es qui?":
            l "C’est pas à toi que je parlais, et arrête de mettre du sang partout, tu vas attirer les zombies !"
      
        " Waw Luca t’es vraiment trop beau":
            l "C’est pas à toi que je parlais, et arrête de mettre du sang partout, tu vas attirer les zombies !"

    "Charmant… tiens, derrière eux il y a une tente.\nJ’entre dedans et je manque de m’étaler. Quel chantier."

    hide luca_angry
    show emilien_neutral

    menu:
        "Et se cachant derrière ses lunettes, il y a Emilien, un geek un peu timide."

        "Waaw C’est quoi ce bazar!":
            e "J’essaie de construire une radio.. On ne sait jamais, ça pourrait nous être utile de communiquer avec des gens en plein apocalypse."
        "Oh c’est ton matériel tout ça? Tu construis quelque chose?":
            e "J’essaie de construire une radio.. On ne sait jamais, ça pourrait nous être utile de communiquer avec des gens en plein apocalypse."

    "...Après qu’Emilien m’ait désinfecté la plaie et m’ait donné des pansements, je le laisse dans la tente et sort rejoindre les autres dehors..."

    "...On est tous assis autour d’un feu..."

    hide emilien_neutral
    show emilien_happy

    e "VENEZ VITE JE CROIS QUE JE TIENS QUELQUE CHOSE!"

    "…On se lève tous le rejoindre dans la tente…"
    
    e "Silence… Écoutez.."

    "…Bien reçu…J’écoute…Personne…"

    "...Il a donc réussi à mettre au point sa radio, on perçoit des voix mais ce n’est pas très clair..."

    "Radio" "…Rejoindre… Zone…Bien reçu…"

    "Radio" "…Zone sans zombies…"

    "Vous avez bien entendu ce que j’ai entendu?"

    hide emilien_happy
    show luca_neutral

    l "Emilien soit clair, qu’est ce que t’en déduis?"

    hide luca_neutral
    show emilien_happy

    e "Je pense qu'il y a bien une zone libre, comme je m’en doutais, sans zombie et que ces personnes essaient de l’atteindre."

    hide emilien_happy
    show tom_happy

    menu:
        t "T’es sûr mec? Parce qu’ils avaient juste l’air de balancer des mots au hasard..?"

        "Je suis d’accord avec Emilien, à les entendre on dirait qu’ils essaient de rejoindre une zone spéciale":
            hide tom_happy
            show emilien_neutral
            e "Je vais continuer d’écouter la radio jusqu'à avoir d'autres infos."
        "C’est vrai qu' il y avait rien de clair dans ces messages":
            hide tom_happy
            show emilien_neutral
            e "Je vais continuer d’écouter la radio jusqu'à avoir d'autres infos."
        "Ok, mais on a pas d’adresse ca nous avance pas à grand chose":
            hide tom_happy
            show emilien_neutral
            e "Je vais continuer d’écouter la radio jusqu'à avoir d'autres infos."

    hide emilien_neutral

    "…BOUUUUM… On entend un gros bruit qui vient de l’extérieur… Je sors ma tête de la tente et je vois… UN ZOMBIE"

    show luca_scared
    
    l "Bon, Comme je l’avais prévu ton sang nous a ramené des zombies. Essaie de te cacher."

    menu:
        "Qui vais-je choisir pour combattre ?"

        "Luca":
            $ fighter = "Luca"
            "Luca à l'attaque !"
            hide luca_scared
            show luca_angry

        "Emilien":
            $ fighter = "Emilien"
            "Emilien à l'attaque !"
            hide luca_scared
            show emilien_angry

        "Tom":
            $ fighter = "Tom"
            "Tom à l'attaque !"
            hide luca_scared
            show tom_angry


    "CCCCOOOOMMMMMBBBBAAAAATTTTTTT"


    menu:
        "[fighter] est blessé"

        "Ta plaie est énorme, tu devrais t’asseoir" if fighter == "Luca":
            hide luca_angry
            show luca_scared
            "[fighter] se fait soigner..."
            hide luca_scared
        "Dommage je pensais qu’il t’avait fait plus mal" if fighter == "Luca":
            hide luca_angry
            show luca_scared
            "[fighter] se fait soigner..."
            hide luca_scared
        "Bon c’est a mon tour de te soigner, laisse moi désinfecter ta plaie." if fighter == "Emilien":
            hide emilien_angry
            show emilien_scared
            "[fighter] se fait soigner..."
            hide emilien_scared
        "Tiens, des pansements et de l’alcool" if fighter == "Emilien":
            hide emilien_angry
            show emilien_scared
            "[fighter] se fait soigner..."
            hide emilien_scared
        "Tu as été super courageux" if fighter == "Tom":
            hide tom_angry
            show tom_scared
            "[fighter] se fait soigner..."
            hide tom_scared
        "C’était stupide de t’envoyer combattre le zombie tout seul" if fighter == "Tom":
            hide tom_angry
            show tom_scared
            "[fighter] se fait soigner..."
            hide tom_scared

        
    show luca_neutral

    l "Bon ça sert plus a rien de rester ici, prenez le nécessaire et on s’en va."

    hide ecole
    hide luca_neutral

    jump supermarket
    

label supermarket:

    scene supermarket with dissolve

    "…On se retrouve dans un supermarché…"

    show luca_neutral
    
    l "Pour aller plus vite on va se séparer en deux groupes, un groupe s’occupe de prendre de la nourriture et l’autre s’occupe de la partie soin."

    hide luca_neutral

    menu:
        "...Je choisis de faire équipe avec"

        "Emilien":
            $ teammate = "Emilien"
            show emilien_happy
            e "On va former une bonne équipe..."
        "Luca":
            $ teammate = "Luca"
            show luca_neutral
            l "Me ralentis pas"
        "Tom":
            $ teammate = "Tom"
            show tom_happy
            t "J’ai trop envie de chocolat."
    
    if teammate == "Emilien":
        menu:
            "T'en penses quoi ?"

            "Si tu le dis":
                $ temp = False
            "Oui, c’est sûr":
                $ temp = False

        hide emilien_happy
        show emilien_neutral

        menu: 
            e "Je pense qu’on devrait chercher le Doliprane en premier"

            "Je pense pas que ce soit très utile":
                "...En fait, je connais rien de lui. Je me demande comment il a atterri ici..."

            "Oui ça peut être utile tu as raison!":
                "...En fait, je connais rien de lui. Je me demande comment il a atterri ici..."
        
        "Ça fait combien de temps que vous êtes cachés derrière le lycée ?"

        e "Alors moi j’ai rejoint Tom et Luca, il y a une semaine je crois"

        "Et t’étais où avant ?"

        hide emilien_neutral
        show emilien_sad

        menu: 
            e "Au nord-est de la ville. Je vivais avec ma famille, on partait souvent camper en forêt..."

            "Et pourquoi tu les as pas amené avec toi ?":
                $ temp = False
            "Ah…. Et si c’est pas indiscret, ils vont bien ?":
                $ temp = False

        menu:
            e "Mes parents sont restés chez moi . Mais ma petite soeur elle...elle est...C’est devenu un zombie..."

            "Ohh... Je suis désolée":
                e "… C’est pour ça que j’ai construit la radio…pour trouver la zone libre. Je pourrais y amener mes parents et les mettre à l’abri."
            "T’as pas su la protéger":
                e "… C’est pour ça que j’ai construit la radio…pour trouver la zone libre. Je pourrais y amener mes parents et les mettre à l’abri."

        hide emilien_sad
        show luca_neutral

        l "Vous en avez mis du temps"
        
        "Emilien m’a raconté comment il a atterri ici, ça fait combien de temps que t’es avec eux toi ?"
        
        l "Ca fait 2 semaines que je me suis barré de chez moi."

        "Et t’étais où avant ?"

        hide luca_neutral
        show luca_angry

        l "Je vivais avec mon frère, mais je vois pas trop en quoi ça te regarde."

        hide luca_angry
        show tom_neutral

        "Et toi Tom c’est quoi ton histoire ?"

        hide tom_neutral
        show tom_sad

        t "Moi, je venais d’emménager ici. Je vivais avec ma soeur, qui faisait le meilleur curry du monde, et ma mère. Mais on était juste à côté de l’hôpital, donc…je ne pourrais jamais savoir ce que ma soeur mettait dedans maintenant."
        t "J’espère que ma mère a pu trouver la zone libre."

        hide tom_sad

    elif teammate == "Tom":
        menu:
            "Viens on va en chercher !"

            "Moi aussi, on devrait en faire un stock!":
                t "Ok chef!"

            "On devrait d’abord commencer par rassembler les aliments essentiels et on s’occupera du chocolat a la fin":
                t "Ok chef!"
        
        "...En fait, je connais rien de lui, je me demande comment il a atterri ici..."

        "Ça fait combien de temps que vous êtes cachés derrière le lycée ?"

        t "Ca fait 4 jours que je suis là bas."

        "Et t’étais où avant ?"

        hide tom_happy
        show tom_sad

        menu:
            t "Je vivais avec ma mère, qui travaille hors de la ville, et ma grande soeur. Vu que j’étais archi-nul en cuisine, c’est toujours elle qui nous faisait à manger..."

            "Pourquoi elle est pas ici, avec toi ?":
                t  "Ma grande soeur s’est faite mordre par un zombie…"
            "Il lui est arrivé quelque chose ?":
                t  "Ma grande soeur s’est faite mordre par un zombie…"

        "Ohh... Je suis désolée..."

        t  "Je me suis dit que ma mère avait peut-être trouvé la zone libre..."

        t "Bon assez parlé. On peut aller chercher le chocolat maintenant ?"

        hide tom_sad
        show luca_neutral

        l "Vous en avez mis du temps"
        
        "Emilien m’a raconté comment il a atterri ici, ça fait combien de temps que t’es avec eux toi ?"
        
        l "Ca fait 2 semaines que je me suis barré de chez moi."

        "Et t’étais où avant ?"

        hide luca_neutral
        show luca_angry

        l "Je vivais avec mon frère, mais je vois pas trop en quoi ça te regarde."

        hide luca_angry
        show emilien_neutral

        "Et toi Emilien c’est quoi ton histoire ?"

        e "Alors moi j’ai rejoint Tom et Luca, il y a 1 semaine je crois"

        "Et t’étais où avant ?"

        hide emilien_neutral
        show emilien_sad

        e "Avec ma famille… Mais je venais de rentrer d’une sortie scout quand l’épidémie a commencé. J’ai construit la radio pour pouvoir trouver la zone libre. Je pourrais y amener mes parents et les mettre à l’abri."

        hide emilien_sad

    else:
        menu:
            "Compris ?!"

            "T'inquiète pas, je te laisse tout porter !":
                hide luca_neutral
                show luca_happy
                l  "Moins de blabla, plus d’actions"
            "C’est bon, je suis capable de porter 2-3 paquets!":
                hide luca_neutral
                show luca_happy
                l  "Moins de blabla, plus d’actions"

        "...En fait, je connais rien de lui, je me demande comment il a atterri ici..."

        "Ça fait combien de temps que vous êtes cachés derrière le lycée?"

        hide luca_happy
        show luca_neutral

        l  "Ca fait un peu plus de 2 semaines que je dois être la"

        "Et t’étais où avant ?"

        hide luca_neutral
        show luca_sad 

        menu: 
            l "Je vivais avec mon grand frère au 40ème étage d’un building. Nos parents n'habitent pas là mais on avait une domestique qui venait nettoyer l’appart et nous faire à manger."

            "Et pourquoi ton frère est pas ici, avec toi ?":
                l "Il s’est fait mordre c’est pour ca que je suis parti."
            "Il lui est arrivé quelque chose?":
                l "Il s’est fait mordre c’est pour ca que je suis parti."

        menu:
            l "La coloc avec un zombie ça me disait rien"

            "Je suis désolée pour ton frère...":
                l "Bon, il faut qu’on parte vite d’ici"
            "J’imagine...":
                l "Bon, il faut qu’on parte vite d’ici"
        
        "...On finit de prendre ce qui nous manquait et on retrouve les autres à l’entrée du supermarché..."

        hide luca_sad
        show emilien_neutral

        e "Vous avez pu récupérer tout ce qu’il vous fallait?"

        "C’est bon pour nous et vous?"

        e "Ouais c’est Tom qui porte tout"

        "Luca m’as raconté comment il a atterri ici, ça fait combien de temps que t’es avec eux toi ?"

        e  "Alors moi j’ai rejoint Tom et Luca, il y a 1 semaine je crois."

        "Et t’étais où avant ?"

        hide emilien_neutral
        show emilien_sad

        e "Avec ma famille … J’ai construit la radio pour pouvoir trouver la zone libre. Je pourrais y amener mes parents et les mettre à l’abri."

        hide emilien_sad
        show tom_neutral

        "Et toi Tom c’est quoi ton histoire ?"

        hide tom_neutral
        show tom_sad

        "Moi, je venais d’emménager ici. Je vivais avec ma soeur, qui faisait le meilleur curry du monde, et ma mère. Mais on était juste à côté de l’hôpital, donc… J’espère que ma mère a pu trouver la zone libre."

        hide tom_sad

    hide supermarket
    jump city



label city:

    scene city with dissolve

    "...On se remet en marche..."

    show emilien_neutral

    e "J’ai réussi à recueillir d’autres infos sur la zone libre. Je crois que j’ai une adresse. De ce que j’ai pu entendre à la radio, elle a l’air de se situer à l’entrée principale de la ville."

    hide emilien_neutral
    show luca_happy

    l "On devraient s’y rendre au plus vite alors"

    hide luca_happy
    show tom_scared

    t "Je crois qu’on a de la compagnie !"

    hide tom_scared
    show zombie

    "...Un zombie apparaît..."

    hide zombie


    "CCCCCCCOOOOOOOOOMMMMMMMBBBBBBBAAAAAATTTTTT"