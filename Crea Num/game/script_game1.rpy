image bg hopital = "./images/Backgrounds/background3_hopital.png"

init python:
    def icons_update(st):
        pass

    def icons_events(event, x, y, st):
        if event.type == 1025: #event click (1025)
            if event.button == 1: #left mouse 1, middle 2, right: 3
                for icon in icons_list:
                    if icon is not None:
                        if icon.x <= x <= (icon.x + icon_size) and icon.y <= y <= (icon.y + icon_size):
                            findMatches(icon)
                            break

    def findMatches(cicon):
        global ammo_left
        if ammo_left > 0:
            matches = []
            matches.append(cicon)

            for icon in matches:
                #match right
                if icon.index + 1 < grid_size and icons_list[icon.index + 1] is not None:
                    if icon.icon_type == icons_list[icon.index + 1].icon_type and (icon.index + 1) % icons_per_row != 0 and icons_list[icon.index + 1] not in matches:
                        matches.append(icons_list[icon.index + 1])          
                # match down
                if icon.index <= grid_size - icons_per_row - 1 and icons_list[icon.index + icons_per_row] is not None:
                    if icon.icon_type == icons_list[icon.index + icons_per_row].icon_type and icons_list[icon.index + icons_per_row] not in matches:
                        matches.append(icons_list[icon.index + icons_per_row])
                # match left
                if icon.index - 1 >= 0 and icons_list[icon.index - 1] is not None: 
                    if icon.icon_type == icons_list[icon.index - 1].icon_type and icon.index % icons_per_row != 0 and icons_list[icon.index - 1] not in matches:
                        matches.append(icons_list[icon.index - 1])
                # match up
                if icon.index >= icons_per_row and icons_list[icon.index - icons_per_row] is not None:
                    if icon.icon_type == icons_list[icon.index - icons_per_row].icon_type and icons_list[icon.index - icons_per_row] not in matches:
                        matches.append(icons_list[icon.index - icons_per_row])

            # if len(matches) != 1:
            deleteMatches(matches)
            ammo_left -= 1

    def deleteMatches(matches):
        global zombi_kill
        global grid_size
        zombi_kill = zombi_kill + len(matches)
        for icon in matches:
            icons_list[icon.index] = None
            icon.destroy() 
            

        renpy.restart_interaction()
        icons.redraw(0)
        shiftIcons()
        if zombi_kill == grid_size:
            renpy.show_screen("game1OverScreen")

    def shiftIcons():
        for i, icon in enumerate(reversed(icons_list)):
            rindex = (grid_size - 1) - i

            if icon is None and rindex >= icons_per_row:
                rm = 0
                while icons_list[rindex - (icons_per_row * rm)] is None and rindex - (icons_per_row * rm) >= icons_per_row:
                    rm += 1
                if icons_list[rindex - (icons_per_row * rm)] is not None:
                    icons_list[rindex - (icons_per_row * rm)].y += (icon_size * rm) + (icon_padding * rm)
                    icons_list[rindex] = icons_list[rindex - (icons_per_row * rm)]
                    icons_list[rindex - (icons_per_row * rm)] = None
                    icons_list[rindex].index = rindex

        for i in range (grid_size - icons_per_row, grid_size - 1):
            if icons_list[i] is None:
                cm = 0
                while icons_list[i + cm] is None and i + cm < grid_size - 1:
                    cm += 1
                if icons_list[i + cm] is not None:
                    icons_list[i + cm].x -= (icon_size * cm + icon_padding * cm)
                    icons_list[i] = icons_list[i + cm]
                    icons_list[i + cm] = None 
                    icons_list[i].index = i
                    for icon in range(int(grid_size / icons_per_row)):
                        if icons_list[(i + cm) - (icons_per_row * icon)] is not None:
                            icons_list[(i + cm) - (icons_per_row * icon)].x -= (icon_size * cm + icon_padding * cm)
                            icons_list[i - (icons_per_row * icon)] = icons_list[(i + cm) - (icons_per_row * icon)]
                            icons_list[(i + cm) - (icons_per_row * icon)] = None 
                            icons_list[i - (icons_per_row * icon)].index -= cm

        icons.redraw(0)
        renpy.retain_after_load()

screen game1OverScreen:
    $text1 = ""
    $text2 = ""
    $label_next = label_win

    python: 
        if zombi_kill < 100:
            text1 = "Game Over!"
            text2 = "You ran out of time !"
            label_next = label_win
        else:
            text1 = "Game Over!"
            text2 = "You win ! You killed {} zombies !".format(zombi_kill)
            label_next = label_lose

    modal True
    
    frame:
        background "#00000050"
        xfill True
        yfill True
        frame:
            background "#877d6b"
            xysize (500, 250)
            padding (2,2)
            align(0.5, 0.5)
            frame: 
                background "#f6f1e7"
                xfill True
                yfill True

                text text1 size 30 color "#000000" align(0.5, 0.1)
                text text2 size 30 color "#000000" align(0.5, 0.4)
                button:
                    # action Jump("start")
                    background "#FFFFFF"
                    xysize (120, 50)
                    align (0.5, 0.8)
                    text "OK" align (0.5, 0.5) color "#000000"
                    # renpy.hide_screen()
                    # action Jump(label_lose)
                    action [Hide(), Hide("scoreUI"), Hide("SameGame"), Jump(label_next)]

transform half_size:
    zoom 1.2

label setup_icons:
    python:
        for i in range(grid_size):
            rand_image = icon_images[renpy.random.randint(0, 4)]
            idle_path = "Icons/{}.png".format(rand_image)
            hover_path = "Icons/{}_hover.png".format(rand_image)
            idle_image = Image(idle_path)
            hover_image = Image(hover_path)
            icons_list.append(icons.create(Transform(child= idle_image, zoom=0.8)))
            icons_list[-1].index = i
            icons_list[-1].icon_type = rand_image
            icons_list[-1].idle_image = idle_image
            icons_list[-1].hover_image = hover_image

    call screen SameGame
    return

screen scoreUI: 
    frame:
        image "Backgrounds/tache-sang.png" xpos -50 ypos -130 zoom 0.5
        xsize 90
        ysize 70
    timer 0.1 action If(round(countdownTime) > 0, true = SetVariable("countdownTime", countdownTime - 0.1), false = Show("game1OverScreen")) repeat If(round(countdownTime) > 0, true = True, false = NullAction())# every 1 second do ...
    # timer 0.1 action If(round(countdownTime) > 0, true = SetVariable("countdownTime", countdownTime - 0.1), false = SetVariable("game_losed", True)) repeat If(round(countdownTime) > 0, true = True, false = NullAction())# every 1 second do ...
    text "{:.0f}".format(countdownTime) align(0.03, 0.015) color "#000000"
    text "{:.0f}".format(zombi_kill) align(0.03, 0.065) color "#000000"
    text "{:.0f}".format(ammo_left) align(0.09, 0.015) color "#000000"
    frame:
        # background "#f61307f5"
        image "UI/clock-icon.png" xpos 0 ypos 0 zoom 0.7
        xsize 0
        ysize 0
    frame:
        image "UI/zombie_6_dead.png" xpos -5 ypos 50 zoom 0.09
        xsize 0
        ysize 0
    frame:
        image "UI/ammo.png" xpos 95 ypos 0 zoom 0.08
        xsize 0
        ysize 0
    
        

screen SameGame:
    $frame_xsize = (icons_per_row * icon_size) + (icons_per_row * icon_padding) + icon_padding + 4
    $frame_ysize = ((grid_size / icons_per_row ) * icon_size) + ((grid_size / icons_per_row ) * icon_padding) + icon_padding + 4
    timer 5 action SetVariable("ammo_left", ammo_left + 2 ) repeat If(round(ammo_left) < 28, true = True, false = NullAction())# every 1 second do ...

    frame:
        background "#222821f5"
        xalign 0.3
        yalign 0.5
        xsize frame_xsize
        ysize frame_xsize

        $crow = 0
        $ccolumn = 0

        for icon in icons_list:
            $xp = (icon_size * ccolumn) + (icon_padding * ccolumn)
            $yp = (icon_size * crow) + (icon_padding * crow)
            

            image "Icons/grid-cell.png" xpos xp ypos yp zoom 0.8
            if icon is not None:
                $icon.x = xp
                $icon.y = yp

            python:
                if ccolumn % (icons_per_row - 1) != 0 or ccolumn == 0:
                    ccolumn += 1
                else :
                    ccolumn = 0
                    crow += 1
            
        add icons

label start_game1:
    $grid_size = 100
    $icon_size = 90
    $icon_padding = 2
    $icons_per_row = 10
    $icons = SpriteManager(update = icons_update, event = icons_events)
    # $icon_images = ["icon_1", "icon_2", "icon_3", "icon_4", "icon_5"]
    $icon_images = ["zombie_7", "zombie_2", "zombie_10", "zombie_4", "zombie_5"]
    $icons_list = []
    $countdownTime = 60.0
    $zombi_kill = 0
    $ammo_left = 30
    $game_losed = False
    $game_over = False


    scene background at half_size
    show screen scoreUI
    jump setup_icons

    return