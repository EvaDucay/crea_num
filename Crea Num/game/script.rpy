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






































    "Qui vais-je choisir pour combattre ?"

    menu:
        "Qui vais-je choisir pour combattre ?"

        "Luca":
            $ fighterX = "Luca"
            "Luca à l'attaque !"
            hide luca_scared
            show luca_angry

        "Emilien":
            $ fighterX = "Emilien"
            "Emilien à l'attaque !"
            hide luca_scared
            show emilien_angry

        "Tom":
            $ fighterX = "Tom"
            "Tom à l'attaque !"
            hide luca_scared
            show tom_angry

    if fighterX == "Tom":

        hide tom_angry
        show tom_scared
        t " Arghhhhhh…."
    
        menu:
            "….Tom a été touché par le zombie, la blessure à l’air grave…"        
           
            "Tom, panique pas mais je crois que tu t’es fait mordre par le zombie":
                $ temp = False
            "AHHHH reste loin de moi!!!":
                $ temp = False

        hide tom_scared
        show emilien_scared
        menu:
            
            e "Oh mon dieu, c’est pas bon signe du tout! Ca a l’air d’être une morsure profonde…."

            "Tu penses que c’est grave?":
                e "Il ne lui reste pas beaucoup de temps avant qu’il se transforme, ca peut être dangereux…"
            "Ca veut dire qu’il va bientôt se transformer en zombie…" :   
                e "Il ne lui reste pas beaucoup de temps avant qu’il se transforme, ca peut être dangereux…"
        
        hide emilien_scared
        show luca_scared
        l "C’est pas vrai ! On avait vraiment pas besoin de ça…" 
    
        menu: 
            l "Désolé, mais je pense que pour notre bien, il faut l’abandonner ici."

            "L’abandonner?? On peut pas faire ca, t’oublie que c’est ton ami":
                $ temp = False
            "Je suis d’accord,on peut pas prendre le risque de le garder c’est trop dangereux…":
                $ temp = False


        hide luca_scared
        show tom_sad
        menu:
            
            t  "Il n’as pas tort, je peux devenir violent."
            
            "Mais non, tu restes avec nous, on va trouver la zone libre et peut être que là bas ils auront un remède pour toi ! Pas question d’abandonner quelqu’un.":
                $ temp = False
            "Je suis désolée Tom mais il vaut mieux pour tout le monde que tu partes…Fais attention à toi... ":
                "…Après un voyage difficile, on est enfin arrivé à la zone libre."
                "Malheureusement, les familles d’Emilien,, de Tom et de Luca ne sont jamais arrivés jusque là, et on s’est tous séparés."
                "En parlant de [fighterX]… je pense souvent à lui ces temps-ci. Est-ce qu’il erre dehors, transformé en zombie ?"
                "Il devient de plus en plus difficile de vivre en zone libre. J’ai du mal à dormir la nuit. Et quand je me retourne dans mon hamac, j’ai l’impression de ne pas être allée au bout de l’histoire."
                return

        hide tom_sad
        show emilien_neutral
        e  "Je suis d’accord on peut pas l’abandonner, Tom tient bon on va trouver une solution."

    elif fighterX == "Emilien":
        show emilien_scared
        e "Arghhhhhh…"
        
        menu:
            "….Emilien a été touché par le zombie, la blessure à l’air grave…"

            "Emilien, tu te sens bien?":
                e " Oh mon dieu… je me suis fait mordre ??? Je vais mourir ?"
            "AHHHH reste loin de moi!!!":
                e " Oh mon dieu… je me suis fait mordre ??? Je vais mourir ?"

        hide emilien_scared
        show tom_scared
        t  "J’ai déjà vu ça… il va bientôt se tranformer en zombie"
        
        hide tom_scared
        show luca_scared
        l "C’est pas vrai ! On avait vraiment pas besoin de ça…"
        
        menu:
            l "Désolé, mais je pense que pour notre bien, il faut l’abandonner ici."

            "Dit pas n’importe quoi, tu vois bien qu’il est encore humain !":
                $ temp = False
            "T’as raison, il faut qu’on s’éloigne de lui avant qu’on se fasse mordre nous aussi.":
                $ temp = False

        hide luca_scared
        show emilien_sad
        menu:
            e "…Ca sert à rien que je continue avec vous si c’est pour me transformer en zombie… il vaut mieux que vous me laissiez là…."
            
            "Mais non, tu restes avec nous, on va trouver la zone libre et peut être que la bas il auront un remède pour toi, pas question d’abandonner quelqu’un":
                $ temp = False
            "Je suis désolée Emilien mais il vaut mieux pour tout le monde que tu restes derrière…Fais attention à toi...":
                "…Après un voyage difficile, on est enfin arrivé à la zone libre."
                "Malheureusement, les familles d’Emilien,, de Tom et de Luca ne sont jamais arrivés jusque là, et on s’est tous séparés."
                "En parlant de [fighterX]… je pense souvent à lui ces temps-ci. Est-ce qu’il erre dehors, transformé en zombie ?"
                "Il devient de plus en plus difficile de vivre en zone libre. J’ai du mal à dormir la nuit. Et quand je me retourne dans mon hamac, j’ai l’impression de ne pas être allée au bout de l’histoire."
                return

        hide emilien_sad
        show tom_neutral
        t "T’inquiètes Emilien, on va trouver une solution."


    else:
        show luca_scared
        l "Arghhhhhh…."
        
        menu:
            "….Luca a été touché par le zombie, la blessure à l’air grave…"

            "Ca va Luca?!":
                hide luca_scared
                show emilien_scared
                e "C’est pas bon signe du tout"
            "AAAAh il saigne vraiment beaucoup!":
                hide luca_scared
                show emilien_scared
                e "C’est pas bon signe du tout"
                      
        e " ça a l’air d’être une morsure profonde."

        hide emilien_scared
        show tom_scared
        menu:
            
            t  "J’ai déjà vu ça… il lui reste pas beaucoup de temps avant qu’il se transforme en zombie…"
            
            "Et on fait quoi alors ? L’abandonner?? On peut pas faire ca, t’oublie que c’est ton ami !":
                $ temp = False
            "Qu’est ce qu’on va faire ? Le garder avec nous, c’est trop dangereux…":
                $ temp = False
        

        hide tom_scared
        show luca_sad
        menu:
        
            l "Laissez tomber, je savais que ça allait arriver mais je pensais que ça serait Emilien qui se ferait mordre en premier… Je vais continuer de mon côté"
            
            "On va trouver la zone libre et peut être que là bas ils auront un remède pour toi. Pas question d’abandonner quelqu’un !":
                $ temp = False
            "… Fais attention à toi":
                "…Après un voyage difficile, on est enfin arrivé à la zone libre."
                "Malheureusement, les familles d’Emilien,, de Tom et de Luca ne sont jamais arrivés jusque là, et on s’est tous séparés."
                "En parlant de [fighterX]… je pense souvent à lui ces temps-ci. Est-ce qu’il erre dehors, transformé en zombie ?"
                "Il devient de plus en plus difficile de vivre en zone libre. J’ai du mal à dormir la nuit. Et quand je me retourne dans mon hamac, j’ai l’impression de ne pas être allée au bout de l’histoire."
                return

        hide luca_sad
        show emilien_neutral
        e "Il faut qu’on trouve comment le soigner rapidement!"
        

    "…On continue de marcher vers la sortie de la ville pour essayer de rejoindre la zone libre…"
    hide emilien_neutral
    show will_scared
    w "AIDEZ-MOI S’IL VOUS PLAIT !!!"


    if fighterX == "Emilien":

        menu:
            "Qui vais-je choisir pour combattre ?"

            "Luca":
                $ fighter = "Luca"
                "Luca à l'attaque !"
                hide will_scared
                show luca_angry

            "Tom":
                $ fighter = "Tom"
                "Tom à l'attaque !"
                hide will_scared
                show tom_angry

    elif fighterX == "Luca":

        menu:
            "Qui vais-je choisir pour combattre ?"

            "Emilien":
                $ fighter = "Emilien"
                "Luca à l'attaque !"
                hide will_scared
                show emilien_angry

            "Tom":
                $ fighter = "Tom"
                "Tom à l'attaque !"
                hide will_scared
                show tom_angry

    else :

        menu:
            "Qui vais-je choisir pour combattre ?"

            "Emilien":
                $ fighter = "Emilien"
                "Emilien à l'attaque !"
                hide will_scared
                show emilien_angry

            "Tom":
                $ fighter = "Luca"
                "Luca à l'attaque !"
                hide will_scared
                show luca_angry



    if fighter == "Luca":
        hide luca_angry

    elif fighter == "Tom":
        hide tom_angry

    else :
        hide emilien_angry

    show will_happy

    menu:

        w "Merci!! De m’avoir sauvé!!!"

        "Tu vas bien ?":
            w  "Je vais bien ! Merci de demander."
        "On avait pas trop le choix":
            w  "Je vais bien ! Merci de demander."

    hide will_happy
    show emilien_angry
    e "Mais d’où tu viens? C’est comme si t’avais attiré exprès les zombies à nous ?"

    hide emilien_angry
    show will_neutral
    menu:
        
        w  "J’étais tranquillement en train de manger quand ce zombie est venu me courir après."

        "Et t’as pas trouver mieux à faire que de courir vers nous et nous mettre en danger?":
            hide will_neutral
            show will_happy
            w "Je vois que vous avez un blessé, je peux peut être vous aider?"

        "Heureusement que t’es tombé sur nous":
            hide will_neutral
            show will_happy
            w "Je vois que vous avez un blessé, je peux peut être vous aider?"

    hide will_happy
    show luca_angry
    l "T’en a déjà assez fait comme ça."

    hide luca_angry
    show will_happy
    w "Je vous ai même pas dit mon prénom, je m’appelle Will Wilson !"

    hide will_happy
    show luca_angry
    l "Cool, tu peux partir maintenant"

    hide luca_angry
    show tom_neutral
    t "Attends, si on le laisse seul, il va se faire bouffer par les zombies…"


    



    hide tom_neutral
    show will_sad
    menu:
        w "J’ai personne depuis l’apocalypse, tout mes proches sont des zombies maintenant…"

        "On peut le garder une personne en plus ca nous fera pas de mal…":
            $ temp = False

        "Reste, mais rend toi utile et porte [fighterX]":
            $ temp = False


    hide will_sad
    show will_scared
    menu:
        
        w  "C’est une morsure de zombie qu’il a?"

        "Oui, il s’est fait mordre pendant un combat":
            $ temp = False
            
        "Non, c’est une morsure de lapin":
            $ temp = False

    menu:
        w "Vous êtes au courant qu’il peut se transformer en zombie à tout moment, et qu’une fois zombie il ne vous reconnaîtra plus et il sera hors de contrôle et c’est très dangereux?"

        "Merci, on y avait pas pensé! On abandonne personne ici, mais si ça te fait si peur tu peux partir.":
            hide will_scared
            show will_neutral
            w "D’accord, mais une fois zombie qu’est ce que vous allez faire de lui? J’aimerai bien vous aider mais j’aime pas trop le sang…"
    
        "C’est vrai, mais on prend le risque parce qu’on peut pas l'abandonner, c’est notre ami!":
            hide will_scared
            show will_neutral
            w "D’accord, mais une fois zombie qu’est ce que vous allez faire de lui? J’aimerai bien vous aider mais j’aime pas trop le sang…"
    

    "On essaie de rejoindre la zone Libre, on espère y trouver un remède contre les morsures de zombie."

    hide will_neutral
    show will_happy
    w "La Zone Libre, j’allais m’y rendre avant de me faire attaquer par ce zombie."

    hide will_happy
    show emilien_happy
    e "Ah oui?? Donc tout ce qu’on a entendu grâce à ma radio c’est vrai? Elle existe donc vraiment cette zone?"

    hide emilien_happy
    show tom_angry
    t "Attends, tu veux dire que même toi, t’étais pas convaincu que la zone libre est réelle ?"

    hide tom_angry
    show will_neutral
    w "Bien sûr que c’est vrai ! D’apres ce qu’on m’a dit, elle se trouve à l’entrée principale de la ville"

    hide will_neutral
    show luca_neutral
    l "…Décidément tu nous apprends vraiment rien."

    hide luca_neutral
    show emilien_neutral
    e "Tu pourrais être plus précis ?"


    hide emilien_neutral
    show will_happy
    menu:
        w "Je peux mieux faire et vous y amener si vous le voulez. Je connais un raccourci en passant par l’hôpital!"
   
        "L’hôpital infesté de zombies ? C’est vraiment un raccourci ton histoire?":
            hide will_happy
            show will_neutral
            w  "Le centre-ville est encore pire. La plupart des zombies sont partis de l’hopital, faites moi confiance!"


        "Peut être qu’on trouvera quelque chose pour soigner la morsure là bas avant d’ariver à la zone libre?":
            hide will_happy
            show will_neutral
            w  "Le centre-ville est encore pire. La plupart des zombies sont partis de l’hopital, faites moi confiance!"



    
    "OK, [fighterX] a besoin qu’on arrive rapidement à la zone libre, donc si c’est plus court par l’hôpital et qu’on peut en profiter pourr récupérer des médicaments, on te suit."

    "… On arrive à l'hôpital…"

    hide will_neutral
    show emilien_neutral
    e  "C’est trop grand, on va perdre du temps si on reste groupé. Je propose qu’on se divise en deux comme au supermarché, et qu’on prenne chacun un étage."

    hide emilien_neutral
    show will_scared
    w "J’aime pas trop rester dans cet endroit…je vais rester en bas avec votre ami blessé. Bonnes fouilles !"



    if fighterX == "Emilien":

        menu:
            "…Je choisis de faire équipe avec :"

            "Luca":
                $ teammate = "Luca"
                "C'est parti !"
                hide will_scared
                show luca_happy

            "Tom":
                $ teammate = "Tom"
                "C'est parti !"
                hide will_scared
                show tom_happy

    elif fighterX == "Luca":

        menu:
            "…Je choisis de faire équipe avec :"

            "Emilien":
                $ teammate = "Emilien"
                "C'est parti !"
                hide will_scared
                show emilien_happy

            "Tom":
                $ teammate = "Tom"
                "C'est parti !"
                hide will_scared
                show tom_happy

    else :

        menu:
            "…Je choisis de faire équipe avec :"

            "Emilien":
                $ fighter = "Emilien"
                "C'est parti !"
                hide will_scared
                show emilien_happy

            "Luca":
                $ fighter = "Luca"
                "C'est parti !"
                hide will_scared
                show tom_happy
                


    if teammate =="Emilien":

        menu: 
            "...Je fais équipe avec Emilien..."
        
            "On sait même pas où commencer…":
                hide emilien_happy
                show emilien_neutral
                e "On devrait essayer de chercher un médicament, peut être un anti douleur"

            "Je te laisse chercher tout seul ,je vais m’asseoir, je suis trop fatiguée":
                hide emilien_happy
                show emilien_neutral
                e "On devrait essayer de chercher un médicament, peut être un anti douleur"


        "… On fait le tour des pièces…"
        "…. Je ne trouve rien qui pourrait nous être utile…"

        "Emilien, je crois bien qu’on se fatigue pour rien, il n'y a vraiment rien ici."

        hide emilien_neutral
        show emilien_angry
        e "Il ne reste que des papiers inutiles, l’hôpital à déjà été fouillé, et les gens n’ont rien laissé."
        "… Un vêtement attire le regard d’Emilien.."
        

        hide emilien_angry
        show emilien_neutral

        menu:
        
            e "regarde…Cette blouse a un nom dessus, ça te dit pas quelque chose?"
            

            "Toutes les blouses ont des nom dessus c’est un peu le principe ici je crois":
                $ objet = "ton nom écrit sur une blouse " 

            "Laisse moi voir de plus près":
                $ objet = "ton nom écrit sur une blouse " 


        hide emilien_neutral
        show emilien_angry
        menu:
        
            e "C’est le nom de notre nouvel ami qui y est inscrit!"

            "C’est qui notre nouvel ami?":
                $ temp = False

            "Will??":
                $ temp = False


        
        e "On dirait bien que le Docteur Will Wilson ne nous a pas tout dit"
        "Pourquoi nous cacher ça?"
        hide emilien_angry
        show emilien_neutral
        e "Ca on va bientôt le découvrir"
        "...Ça n’as pas vraiment de sens…Pourquoi il nous a accompagnés à l’hôpital sans nous dire qu’il y travaillait? Et pourquoi il n’aime pas cet endroit?"

    elif teammate == "Tom":

        menu:
            "Je fais équipe avec Tom"
            
            "On sait même pas quoi chercher":
                hide tom_happy
                show tom_neutral
                t "Je vais chercher de ce côté"
            
            "Essaie de chercher des médicaments":
                hide tom_happy
                show tom_neutral
                t "Je vais chercher de ce côté"

        

        "… On fait le tour des pièces…"
        "…. Je ne trouve rien qui pourrait nous être utile…"
        "Je crois bien que se fatigue pour rien…"
        hide tom_neutral
        show tom_angry
        t "Il reste que des tas de papier par terre"
        "Tom passe devant une photo et s’arrête.."
        
        hide tom_angry
        show tom_neutral
        menu: 

            t  "Ce type me dit quelque chose, je suis sûr de l’avoir déjà croisé ?"
             

            "Laisse moi voir de plus près… WILL ?!":
                $ objet = "ta photo accrochée sur les murs de l'hopital"
                hide tom_neutral
                show tom_angry
                t "WILL !!! Mais qu’est ce qu’il fait sur une photo avec pleins de médecins?"

            "Creuse toi les méninges. C’est pas si compliqué…":
                $ objet = "ta photo accrochée sur les murs de l'hopital"
                hide tom_neutral
                show tom_angry
                t "WILL !!! Mais qu’est ce qu’il fait sur une photo avec pleins de médecins?"


        
        "Tom, je pense que Will travaille ici. Il doit être médecin, un détail qu’il a dû oublier de mentionner"
        hide tom_angry
        show tom_neutral
        t "Pourquoi nous cacher ça?"

        "Ca on va bientôt le découvrir"
        "...Ça n’as pas vraiment de sens…Pourquoi il nous a accompagnés à l’hôpital sans nous dire qu’il y travaillait? Et pourquoi il n’aime pas cet endroit?"

    else:


        menu:
            "Je fais équipe avec Luca"

            "On sait même pas où commencer…":
                hide luca_happy
                show luca_neutral
                l "C’est toi qui voulais venir ici…Je prends la partie droite donc prends lagauche et essaie de regarder si il y a quelque chose d’utile !"
        

            "Je te laisse chercher tout seul ,je vais m’asseoir, je suis trop fatiguée":
                hide luca_happy
                show luca_neutral
                l "C’est toi qui voulais venir ici…Je prends la partie droite donc prends lagauche et essaie de regarder si il y a quelque chose d’utile !"
        


        "Ca marche"
        "… On fait le tour des pièces…"
        "…. Je ne trouve rien qui pourrait nous être utile…"
        "Je crois bien que se fatigue pour rien…"
        hide luca_neutral
        show luca_angry
        l "On arrive trop tard, quelqu’un est déjà passé avant nous"
        "… Le regard de Luca se pose sur un tas de papier.."
        
        menu:
            l "Regarde ça…ça te dit pas quelque chose?"
             
        
            "Ce sont des dossiers médicaux":
                $ objet = "ta signature sur des dossiers médicaux"
                l  "Des dossiers signé par le docteur Will Wilson. Je savais qu’il était louche!"
                

            "Laisse moi voir de plus près":
                $ objet = "ta signature sur des dossiers médicaux"
                l  "Des dossiers signé par le docteur Will Wilson. Je savais qu’il était louche!"

    


        "Will?? Il travaillait ici? Pourquoi nous cacher ca?"
        hide luca_angry
        show luca_neutral
        l "On va pas tarder à le découvrir.. viens !"
        "...Ça n’as pas vraiment de sens…Pourquoi il nous a accompagnés à l’hôpital sans nous dire qu’il y travaillait? Et pourquoi il n’aime pas cet endroit?"

        "…On doit retrouver les autres et confronter WILL…"
        "… On se dirige vers l’entrée de l’hôpital, mais elle est bloquée… par un ZOMBIE.."



    if fighterX == "Emilien":

        menu:
            "Qui vais-je choisir pour combattre ?"

            "Luca":
                $ fighter = "Luca"
                "Luca à l'attaque !"
                hide luca_scared
                show luca_angry

            "Tom":
                $ fighter = "Tom"
                "Tom à l'attaque !"
                hide luca_scared
                show tom_angry

    elif  fighterX == "Luca":

        menu:
            "Qui vais-je choisir pour combattre ?"

            "Emilien":
                $ fighter = "Emilien"
                "Luca à l'attaque !"
                hide emilien_scared
                show emilien_angry

            "Tom":
                $ fighter = "Tom"
                "Tom à l'attaque !"
                hide luca_scared
                show tom_angry

    else :

        menu:
            "Qui vais-je choisir pour combattre ?"

            "Emilien":
                $ fighter = "Emilien"
                "Luca à l'attaque !"
                hide emilien_scared
                show emilien_angry

            "Luca":
                $ fighter = "Luca"
                "Luca à l'attaque !"
                hide luca_scared
                show luca_angry
                    



    "… Je crois que Will nous doit des explications…"
    "T’aurais pu nous dire que tu travaillais à l'hôpital ?"

    show will_scared
    w "De quoi tu parles?"
    "Tu peux arrêter de faire semblant on a trouvé [objet]"
    hide will_scared
    show will_happy
    w "Ah…je voyais pas trop l’intérêt de vous dire que je travaillais ici ?"

    "C’est vrai qu’avec un blessé, un médecin ca nous aurait pas du tout été utile"
        
    hide will_happy
    show will_sad
    menu:
        
        w "D’accord c’est vrai que j’ai eu tort, mais je ne savais pas encore si je pouvais vous faire confiance. Et puis ma spécialité c’est la virologie, pas les premiers secours !"
        
        "Je peux comprendre, mais maintenant soit honnête et dis nous si tu sais quelque chose sur un possible remède contre une morsure":
            hide will_sad
            show will_happy
            w "J’ai vu que vous teniez beaucoup à sauver votre ami, j’ai peut être une solution pour vous"

        " J’avais raison de me méfier de toi":
            hide will_sad
            show will_happy
            w "J’ai vu que vous teniez beaucoup à sauver votre ami, j’ai peut être une solution pour vous"

        
    "Et qu’est ce qui nous dit que tu n’es pas en train de nous mentir ?"
    w "J’ai aucun intérêt à mentir maintenant. Et puis il y a quelques temps, j’ai fait des recherches sur un potentiel remède contre une morsure de zombie au cas où…. et je crois avoir trouvé un antidote puissant !"
    "Et c’est quoi cet ingrédient miracle ?"


    menu :
        w "DE LA VERVEINE!"
        "Hahaha de la verveine? Très drôle.":
            hide will_happy
            show will_neutral
            w "T’as le droit de ne pas me croire mais si tu veux sauver ton ami tu ferais mieux de chercher de la verveine. Un collègue en faisant pousser au 5ème étage."
    

        "Et comment t’as découvert ca?":
            hide will_happy
            show will_neutral
            w "T’as le droit de ne pas me croire mais si tu veux sauver ton ami tu ferais mieux de chercher de la verveine. Un collègue en faisant pousser au 5ème étage."
    

        "T’as pas l’air assez futé pour découvrir quoi que ce soit…":
            hide will_happy
            show will_neutral
            w "T’as le droit de ne pas me croire mais si tu veux sauver ton ami tu ferais mieux de chercher de la verveine. Un collègue en faisant pousser au 5ème étage."
    


    "….De la verveine? Est ce que je peux vraiment faire confiance à Will? Ça me parait tellement ridicule? Mais en même temps il est médecin…"
    
    "…Je regarde [fighterX], il a l’air vraiment mal en point… je ne suis pas sûre qu’il tienne jusqu’à la zone libre tout seul…"
    "…On pourrait essayer, on a rien à perdre…."
    "C’est une mission importante, et je ne sais pas du tout à quoi ça ressemble, la verveine. Il faut que je décide bien de qui va m’accompagner…."
    
    if fighterX == "Emilien":

        menu:
            "Qui vais-je choisir pour combattre ?"

            "Luca":
                $ teammate = "Luca"
                "C'est parti !"
                hide will_scared
                show luca_happy

            "Tom":
                $ teammate = "Tom"
                "C'est parti !"
                hide will_scared
                show tom_happy

            "Personne":
                $ teammate = "Personne"
                "C'est parti !"
                hide will_scared

    elif fighterX == "Luca":

        menu:
            "Qui vais-je choisir pour combattre ?"

            "Emilien":
                $ teammate = "Emilien"
                "C'est parti !"
                hide will_scared
                show emilien_happy

            "Tom":
                $ teammate = "Tom"
                "C'est parti !"
                hide will_scared
                show tom_happy
            
            "Personne":
                $ teammate = "Personne"
                "C'est parti !"
                hide will_scared
    

    else :

        menu:
            "Qui vais-je choisir pour combattre ?"

            "Emilien":
                $ fighter = "Emilien"
                "C'est parti !"
                hide will_scared
                show emilien_happy

            "Luca":
                $ fighter = "Luca"
                "C'est parti !"
                hide will_scared
                show luca_happy
            
            "Personne":
                $ teammate = "Personne"
                "C'est parti !"
                hide will_scared


    if teammate =="Emilien":

        "Will a parlé de verveine, tu vois à quoi ça ressemble?"
        hide emilien_happy
        show emilien_neutral
        e "J’en ai déjà vu en faisant du camping, donc ça devrait aller..mais faut vraiment qu’on fasse attention et qu’on confonde pas la verveine avec une autre plante."
        
        "… On fait le tour des pièces…"
        "…. Sur un balcon, il y a trois pots d’herbes…"
        "Emilien, je crois qu’il y a un des pots qui contient de la verveine?"
        e "Laisse moi voir."
        "… Il observe chaque pot méticuleusement, et finit par en prendre un .."
        hide emilien_neutral
        show emilien_happy
        e "C’est bon on tient de la verveine, on peut y aller"



    elif teammate == "Tom":

        "Will a parlé de verveine"
        

        hide tom_happy
        show tom_neutral
        menu:
            
            t "Et ça ressemble à quoi ça?"
            "C’est une herbe, ça doit être vert ?":
                hide tom_neutral
                show tom_angry
                t "Il aurait pu nous montrer une photo Will"

            "Je sais pas du tout":
                hide tom_neutral
                show tom_angry
                t "Il aurait pu nous montrer une photo Will"


        

        "… On fait le tour des pièces…"
        "…. Sur le balcon il y a trois pots d’herbes…"
        "Tom, je crois qu’il y a un des pots qui contient de la verveine."
        t "Mais toutes les plantes se ressemblent là"
        "…Il sent les trois pots…"
        hide tom_angry
        show tom_happy
        t "C’est BON, c’est ce pot la, ca sent le tisane que ma soeur se faisait, c’est de la verveine, c’est sûr"

        t "On peut y aller"

        
    elif teammate == "Luca": 
        
        hide luca_happy
        show luca_neutral
        menu:
            
            l "Bon, rappelle moi à quoi ça ressemble la verveine ?"
            "Ca ressemble à de l’herbe":
                hide luca_neutral
                show luca_happy
                l " On est mal parti. Je pensais que toi au moins tu savais cuisiné."

            "Ca ressemble à de la menthe":
                hide luca_neutral
                show luca_happy
                l " On est mal parti. Je pensais que toi au moins tu savais cuisiné."

            "Tu sais pas à quoi ça ressemble non plus ?":
                hide luca_neutral
                show luca_happy
                l " On est mal parti. Je pensais que toi au moins tu savais cuisiné."


        

        "… On fait le tour des pièces…"
        "…. Sur le balcon il y a trois pots d’herbes…"
        "Luca, je crois qu’il y a un des pots qui contient de la verveine."
        hide luca_happy
        show luca_neutral
        l "Laisse moi voir"

        "… Il observe chaque pot, et finit par en prendre un, un peu au hasard j’ail’impression .."
        hide luca_neutral
        show luca_happy
        l "Je pense que c’est de la verveine, on peut y aller"


    else:
        "Je n’ai rien trouvé au 5ème étage, mais je suis tombée sur un pot de plante au 4ème étage. Ca ressemble à de la verveine, je vais ramener ça au cas où…"


    




    "…. On retrouve [fighterX].."
    "C’est bon on a la verveine, il faut que tu manges ça pour guérir !"
    "…Il prend quelques feuilles et les met dans sa bouche…"
    "… Maintenant, les yeux rivés sur lui, on attend que quelque chose se passe…"
    "…1 min…"
    "…5 min…."
    "….15 min…."
    "WILL, il se passe rien du tout, pourquoi ça ne fonctionne pas??"
    
    
    show will_neutral
    w  "Je ne sais pas moi."

    "Pourtant on a bien ramené de la verveine, il l’as bien ingurgité, tu l’as dit toi même: ça devait le soigner!"
    hide will__neutral
    show will_happy
    w  "J’ai dit ça moi?"

    "OUI TU L’AS DIT, c’était encore un mensonge?"
    w  "Et bien on peut pas tout à fait dire que c’est un mensonge, plutôt une demie-vérité…"

    "WILL SOIT CLAIR POUR UNE FOIS, c’est notre ami et on a besoin de le sauver ! Aide nous s’il te plaît!"
    w "Tu dis nous beaucoup “nous” pour une personne qui est toute seule..."
    "...Je me retourne…pourquoi est-ce que mes amis sont tous couchés par terre ?"
    "Qu’est ce que tu as fais à mes amis?!"
    
    menu:
        w "Ils sont juste endormis, ne t’inquiètes pas trop… pour revenir à l’antidote, il est vrai que le remède n’est pas tout à fait complet, la verveine seule ne suffit pas"

        "Et tu ne pouvais pas nous prévenir plus tôt??":
            hide will_happy
            show will_neutral
            w "Je voulais voir à quel point vous étiez près à sauver votre ami…"


        "Pourquoi encore nous mentir?":
            hide will_happy
            show will_neutral
            w "Je voulais voir à quel point vous étiez près à sauver votre ami…"



    
    "Mais...comment tu sais tout ça ? Pourquoi tu es aussi bien informé sur le virus ?"

    hide will_neutral
    show will_happy
    menu:
        
        w " La vérité… c’est que c’est moi qui suis à l'origine de l'épidémie de zombies. C’est moi qui ai crée le virus."

        "QUOI??? JE SAVAIS QUE T’ETAIS UN MALADE!":
            $ temp = False

        "QUOI??? JE SAVAIS QUE T’ETAIS UN PYSCHOPATHE ! TU PORTES DU JAUNE!":
            $ temp = False

        "….Mytho…":
            $ temp = False


    hide will_happy
    show will_angry
    w "Mes supérieurs m’ont ordonné de produire le virus. Mais je n’avais plusespoir en l’humanité et je voulais y mettre fin…donc j’ai laissé fuiter le virus.L’humain est égoïste, lâche et violent! Les gens sont beaucoup plus honnêtes une fois zombifiés, ils ne peuvent plus cacher leur vraie nature !"
    
    hide will_angry
    show will_sad
    w"...Mais quand je vous vois vous entraider, je me dis que j’ai peut être eu tort…"

    menu:
            w"Laissez moi vous aider pour de vrai cette fois !"

            "Je choisis d’attaquer Will seule": 
                "Je me jette sur Will pour le surprendre. J’arrive à lui donner un coup de poing mais il m’attrape par le bras et m’envoie voler. Ma tête heurte le mur et …"

                "….Aïe ma tête!!…"

                "…J’ouvre les yeux…"

                "…. Je suis dans ma chambre, dans mon lit … tout ca c’était n’était donc qu’un cauchemar? Mais ça m’a paru si réel…"

                "Demain, j’irai parler à Tom, Luca et Emilien. Je pense qu’on peut devenir amis!"
                return

            "Je choisis d’abandonner mes amis et de courir vers la sortie":
                "Je me tourne et cours vers la sortie! Je ne peux pas sauver mes amis de toute façon, il est déjà trop tard. J’entends des pas derrière moi. Le couloir s’étire. Je trébuche, et quelq’un me plaque au sol. Je sens une aiguille qui s’enfonce dans mon cou." 
                "Tom, Luca, Emilien,....je suis désolée…si seulement je pouvais revenir en arrière…."
                return

            "Je choisis de faire confiance à Will":
                "Will a réveillé mes amis."



    if teammate == "Personne":

        "D’après Will, j’ai ramené de l’herbe à chat. Il est parti chercher la verveine, mais [fighterX] est de plus en plus mal, c’est dangereux…"


        if fighterX == "Luca":
            l "ARGGHH… COURREZ…J’ai qu’une seule envien, c’est de vous manger la cervelle ! Eloignez vous de mMoOOiiiiIII…"

            "QUOI?? Essaie de te contenir"
            l "Je ne pPeEEuuUUXx pas, c’est trop tard… COURSSS"
        
        elif fighterX == "Tom":
            t "ARGGHH… COURREZ…J’ai qu’une seule envien, c’est de vous manger la cervelle ! Eloignez vous de mMoOOiiiiIII…"

            "QUOI?? Essaie de te contenir"
            t "Je ne pPeEEuuUUXx pas, c’est trop tard… COURSSS"

        else :
            e "ARGGHH… COURREZ…J’ai qu’une seule envien, c’est de vous manger la cervelle ! Eloignez vous de mMoOOiiiiIII…"

            "QUOI?? Essaie de te contenir"
            e "Je ne pPeEEuuUUXx pas, c’est trop tard… COURSSS"

        "Je me tourne et cours vers la sortie! J’entends des pas derrière moi. Le couloir s’étire. Je trébuche, et quelq’un me plaque au sol. Je hurle et mon épaule … des dents …"

        return

    








    hide will_sad
    show will_neutral
    menu:
            
        w "Après tout ce que je vous ai fait vous avez quand même choisi de me garder, je vous doit bien la vérité cette fois"
    
        "Il est temps oui":
            $ temp = False

        "Comment être sûr que ce sera la vérité cette fois?":
            $ temp = False


        
    menu:
        w "Je n’ai plus rien à gagner à vous mentir, il y a bien un remède, et il faut bien utiliser de la verveine. Mais pour que le remède soit vraiment efficace il faut que la verveine soit mélangé à ton sang."
        
        "Hahaha, mentir ne te fatigue vraiment pas":
            $ temp = False

        "Mon sang??":
            $ temp = False


    w "Je sais que c’est compliqué d’avoir confiance en moi, mais je vous promets qu' une seule goutte de ton sang mélangé à la verveine suffit pour sauver votre ami."
    hide will_neutral
    show emilien_angry
    e "Si ça peut le sauver!"
    hide emilien_angry
    show luca_neutral
    l "On l’a déjà trainé jusque là, autant aller au bout."
    "Parle pour toi c’est quand même mon sang qu’on va utiliser"
    hide luca_neutral
    show will_neutral
    w "Tu ne vas rien sentir!"
    "Bon ok, Will, j’espère que cette fois c’est bien la vérité"
    "… Je me pique le doigt et récolte une goutte de sang que je dépose sur une feuille de verveine…"
    "…Je tends la feuille à [fighterX], qui l’ingère…"
    "Comme tout à l’heure, les yeux rivés sur lui, on attend que quelque chose se passe…"
    "….5min…"

    if teammate == "Emilien":

        "…Sa blessure commence à disparaître, ça a l’air de fonctionner…"
        hide will_neutral
        
        
        if fighterX == "Luca" :
            show luca_happy
            l "Je crois que ca marche Je suis guéri!"
            hide luca_happy

        elif fighterX == "Tom":
            show tom_happy
            t "Je crois que ca marche Je suis guéri!"
            hide tom_happy

        else :
            show emilien_happy
            e "Je crois que ca marche Je suis guéri!"
            hide emilien_happy

    
        show will_happy
        w "Je vous l'avais bien dit de me faire confiance"
        "Donc mon sang + la verveine c’est le remède?? C’est complètement tordu"
        hide will_happy
        show emilien_happy
        e "Tu te rends compte ca veut dire qu’on peut sauver tout le monde, on a un remède!"
        "C’est vrai qu’il faudrait que je fasse une prise de sang et on pourra distribuer le remède"
        hide emilien_happy
        show will_happy
        w "Je peux vous aider pour la prise de sang, j’ai de l’expérience"
        hide will_happy
        show luca_neutral
        l "On devrait d’abord se rendre à la zone libre, on verra ça la bas"
        "…On arrive enfin en zone libre…"
        "Will passera bientôt devant un juge, mais en attendant il gère la production du remède."
        "On a pu l’essayer sur la petite soeur d’Emilien, la grande soeur de Tom et le frère de Luca et ils sont tous revenus à eux!"
        "L’humanité croit de nouveau à son futur!"
        return


    elif teammate == "Tom":
    
        "… Je me pique le doigt et récolte une goutte de sang que je dépose sur une feuille de verveine…"
        "…BOUMMM…."
        "…une grosse explosion se produit…"
        "Qu’est ce qu’il s’est passé???"

        hide will_neutral
        show tom_scared
        t "T’es un ZOMBIE"
        "C EST TOI LE ZOMBIE"
        hide tom_scared
        show emilien_scared
        e "Calmez vous, je crois qu’on s’est tous transformé en zombies"
        "WILLL???"
        hide emilien_scared
        show will_sad
        w "Je comprends pas, la verveine et ton sang, ce mélange, il devait être efficace"
        hide will_sad
        show emilien_angry
        e"Je crois comprendre d'où vient le problème, c’est pas de la verveine que vous avez ramené c’est de la menthe!!!!!"
        hide emilien_angry
        show luca_angry
        l "Des incapables…"
        hide luca_angry
        show tom_happy
        t"En fait c’est pas si mal d’être un zombie, j’ai l’impression d’être encore plus en forme"
        hide tom_happy
        show emilien_happy
        e "Il a pas tord je crois que je pourrais soulever une montagne"
        "…On a pas exactement finit par rejoindre la zone libre…"
        "Mais on a retrouvé la petite soeur d’Emilien, la grande soeur de Tom et le frère de Luca qui avaient tous été transformé!"
        "Au final, c’est pas si mal d’être un zombie…mais les proies commencent à manquer…"
        return




    elif teammate == "Luca":
    
        "…Sa blessure commence à disparaître, ça a l’air de fonctionner…"

        hide will_neutral

        if fighterX == "Luca" :
            show luca_happy
            l "Je crois que ca marche Je suis guéri!"
            hide luca_happy

        elif fighterX == "Tom":
            show tom_happy
            t "Je crois que ca marche Je suis guéri!"
            hide tom_happy

        else :
            show emilien_happy
            e "Je crois que ca marche Je suis guéri!"
            hide emilien_happy

        show will_happy
        w "Je vous l'avais bien dit de me faire confiance"
        "Mais il a toujours le teint gris, c’est normal ça?"
        hide will_happy
        show will_scared
        w "Non, avec la verveine et ton sang il devrait complètement guéri et être revenu à la normal"
        "C’est pas trop le cas"
        hide will_scared
        show emilien_angry
        e "Je crois comprendre d'où vient le problème, c’est pas de la verveine que vous avez ramené c’est du basilic!!!!!"
        hide emilien_angry
        show luca_angry
        l "Des incapables…"
        hide luca_angry
        
        if fighterX == "Luca" :
            show luca_happy
            l "Mais les gars ça me démange plus de vous manger la cervelle c’est une bonne chose, le teint je pense que je peux m’y faire."
            hide luca_happy

        elif fighterX == "Tom":
            show tom_happy
            t "Mais les gars ça me démange plus de vous manger la cervelle c’est une bonne chose, le teint je pense que je peux m’y faire."
            hide tom_happy

        else :
            show emilien_happy
            e "Mais les gars ça me démange plus de vous manger la cervelle c’est une bonne chose, le teint je pense que je peux m’y faire."
            hide emilien_happy


        
        "D’accord donc le mélange basilic, sang ça adoucit les zombies, cool, tout à fait logique."
        show luca_happy
        l "On pourrait en faire boire à tous les zombies de la ville"
        "Oui et on ouvre un bar."
        hide luca_happy
        show emilien_happy
        e "Mes parents ont un local vide on pourrait s’installer là bas?"
        "C’est délirant mais pourquoi pas?"
        "…Et voilà ma success story, co-propriétaire d’un bar, qui a comme cocktail best seller le jus de basilic et mon sang…"
        "…. Mais si grâce a ça on peut vivre en cohabitation avec les zombies, qui ne nous prennent plus en chasse…."
        "On espère encore retrouver les familles de Tom, Emilien et Luca"
        "Will est condamné à faire la plonge pour un bon moment."
        return