init python:
    import random
    def corkGunTransform(t, st ,at):
        global cork_gun_pos
        global cork_gun_opos


        mousepos = renpy.get_mouse_pos()
        
        if mousepos[0] <= config.screen_width + 200 : #if mousepos[0] <= renpy.get_physical_size()[0] + 200 : 
            cork_gun_pos = (mousepos[0],cork_gun_opos[1])

        t.xpos = cork_gun_pos[0]#mousepos[0]

        cork_gun_pos = (cork_gun_pos[0],0.85+ (mousepos[1]-config.screen_height)/8200) #cork_gun_pos = (cork_gun_pos[0],0.85+ (mousepos[1]-renpy.get_physical_size()[1])/7000)
        t.ypos = cork_gun_pos[1]

        return 0

    def setupTargets():
        target_start_x = 400
        target_row_1_y = 197
        target_row_2_y = 462
        target_row_3_y = 724
        target_spacing = 180
        target_down_time = (0.0,2.0)
        target_up_time = 2.0

        current_column = 0
        for i in range(12):
            if i < 3:
                target_transform = Transform(child="images/target-1-4.png",zoom = target_row_1_zoom)
                target_sprites.append(target_SM.create(target_transform))
                target_sprites[-1].row = 1
                target_sprites[-1].down_time = random.uniform(target_down_time[0],target_down_time[1])
                target_sprites[-1].x = target_start_x +(target_sizes["top"][0]*i)+(target_spacing*i)
                target_sprites[-1].y = target_row_1_y
            elif i < 7:
                target_transform = Transform(child="images/target-1-4.png",zoom = target_row_2_zoom)
                target_sprites.append(target_SM.create(target_transform))
                target_sprites[-1].row = 2
                target_sprites[-1].down_time = random.uniform(target_down_time[0],target_down_time[1])
                target_sprites[-1].x = target_start_x +(target_sizes["middle"][0]*current_column)+(target_spacing*current_column)
                target_sprites[-1].y = target_row_2_y
                current_column+=1
            elif i < 12:
                target_transform = Transform(child="images/target-1-4.png",zoom = target_row_3_zoom)
                target_sprites.append(target_SM.create(target_transform))
                target_sprites[-1].row = 3
                target_sprites[-1].down_time = random.uniform(target_down_time[0],target_down_time[1])
                if i==7:
                    current_column = 0
                else:
                    current_column+=1
                target_sprites[-1].x = target_start_x +(target_sizes["bottom"][0]*current_column)+(target_spacing*current_column)
                target_sprites[-1].y = target_row_3_y
            target_sprites[-1].idle_animation_direction = "up"
            target_sprites[-1].current_frame = 5
            target_sprites[-1].animation_time= 0.0
            target_sprites[-1].hit = False
            target_sprites[-1].up_time = target_up_time

    def targetUpdate(st):
        for li, target in enumerate(target_sprites):
            if target.hit == True:
                if target.current_frame == 1:
                    i=Image("images/target-1-2.png")
                    if target.row == 1:
                        target.animation_time = 0
                        t=Transform(child=i,zoom = target_row_1_zoom)
                    elif target.row == 2:
                        t=Transform(child=i,zoom = target_row_2_zoom)
                    elif target.row == 3:
                        t=Transform(child=i,zoom = target_row_3_zoom)
                    target.current_frame = 2
                    target.set_child(t)
                elif target.current_frame == 2:
                    i=Image("images/target-1-3.png")
                    if target.row == 1:
                        t=Transform(child=i,zoom = target_row_1_zoom)
                    elif target.row == 2:
                        t=Transform(child=i,zoom = target_row_2_zoom)
                    elif target.row == 3:
                        t=Transform(child=i,zoom = target_row_3_zoom)
                    target.current_frame = 3
                    target.set_child(t)
                elif target.current_frame == 3 and target.animation_time >=0.1:
                    i=Image("images/target-1-4.png")
                    if target.row == 1:
                        t=Transform(child=i,zoom = target_row_1_zoom)
                    elif target.row == 2:
                        t=Transform(child=i,zoom = target_row_2_zoom)
                    elif target.row == 3:
                        t=Transform(child=i,zoom = target_row_3_zoom)
                    target.current_frame = 4
                    target.set_child(t)
                elif target.current_frame == 4 and target.animation_time >=0.12:
                    i=Image("images/target-1-3.png")
                    if target.row == 1:
                        t=Transform(child=i,zoom = target_row_1_zoom)
                    elif target.row == 2:
                        t=Transform(child=i,zoom = target_row_2_zoom)
                    elif target.row == 3:
                        t=Transform(child=i,zoom = target_row_3_zoom)
                    target.current_frame = 5
                    target.set_child(t)
                elif target.current_frame == 5 and target.animation_time >=0.13:
                    i=Image("images/target-1-4.png")
                    if target.row == 1:
                        t=Transform(child=i,zoom = target_row_1_zoom)
                    elif target.row == 2:
                        t=Transform(child=i,zoom = target_row_2_zoom)
                    elif target.row == 3:
                        t=Transform(child=i,zoom = target_row_3_zoom)
                    target.current_frame = 5
                    target.animation_time = 0
                    target.hit = False
                    target.set_child(t)
            else:
                if target.idle_animation_direction == "up":
                    if target.animation_time >= target.down_time:

                        if target.current_frame == 5:
                            i= Image("images/target-1-3.png")
                            if target.row == 1:
                                t=Transform(child=i,zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t=Transform(child=i,zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t=Transform(child=i,zoom = target_row_3_zoom)
                            target.current_frame = 3
                            target.set_child(t)
                        elif target.current_frame == 3 and target.animation_time >= target.down_time + 0.1:
                            i= Image("images/target-1-2.png")
                            if target.row == 1:
                                t=Transform(child=i,zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t=Transform(child=i,zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t=Transform(child=i,zoom = target_row_3_zoom)
                            target.current_frame = 2
                            target.set_child(t)
                        elif target.current_frame == 2 and target.animation_time >= target.down_time + 0.12:
                            i= Image("images/target-1-1.png")
                            if target.row == 1:
                                t=Transform(child=i,zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t=Transform(child=i,zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t=Transform(child=i,zoom = target_row_3_zoom)
                            target.current_frame = 1
                            target.idle_animation_direction = "down"
                            target.animation_time = 0
                            target.set_child(t)
                elif target.idle_animation_direction == "down":
                    if target.animation_time >= target.up_time:
                        if target.current_frame == 1:
                            i=Image("images/target-1-2.png")
                            if target.row == 1:
                                t=Transform(child=i,zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t=Transform(child=i,zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t=Transform(child=i,zoom = target_row_3_zoom)
                            target.current_frame = 2
                            target.set_child(t)
                        elif target.current_frame == 2:
                            i=Image("images/target-1-3.png")
                            if target.row == 1:
                                t=Transform(child=i,zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t=Transform(child=i,zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t=Transform(child=i,zoom = target_row_3_zoom)
                            target.current_frame = 3
                            target.set_child(t)
                        elif target.current_frame == 3 and target.animation_time >= target.down_time + 0.1:
                            i=Image("images/target-1-4.png")
                            if target.row == 1:
                                t=Transform(child=i,zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t=Transform(child=i,zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t=Transform(child=i,zoom = target_row_3_zoom)
                            target.current_frame = 4
                            target.set_child(t)
                        elif target.current_frame == 4 and target.animation_time >= target.down_time + 0.12:
                            i=Image("images/target-1-3.png")
                            if target.row == 1:
                                t=Transform(child=i,zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t=Transform(child=i,zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t=Transform(child=i,zoom = target_row_3_zoom)
                            target.current_frame = 5
                            target.set_child(t)
                        elif target.current_frame == 5 and target.animation_time >= target.down_time + 0.13:
                            i=Image("images/target-1-4.png")
                            if target.row == 1:
                                t=Transform(child=i,zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t=Transform(child=i,zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t=Transform(child=i,zoom = target_row_3_zoom)
                            target.current_frame = 5
                            target.idle_animation_direction = "up"
                            target.animation_time = 0
                            target.hit = False
                            target.set_child(t)
            target.animation_time +=0.01
        return 0
    
    def corkEvents(event,x,y,st):
        if event.type == renpy.pygame_sdl2.MOUSEBUTTONUP:
            if event.button == 1 and y < config.screen_height + 100:#############################
                cork_sprites.append(cork_SM.create(cork_transform))
                cork_sprites[-1].original_size = (110/2, 138/2)
                cork_sprites[-1].x = cork_gun_pos[0] + cork_sprites[-1].original_size[0]+50
                cork_sprites[-1].y = cork_gun_pos[1] + 900
                cork_sprites[-1].original_pos = (cork_sprites[-1].x,cork_sprites[-1].y)
                cork_sprites[-1].zoom = 0.5
                cork_sprites[-1].move_to_pos = (cork_gun_pos[0],y)
                cork_SM.redraw(0)
    
    def corkUpdate(st):
        global score
        for cork in cork_sprites:
            if cork.y > cork.move_to_pos[1]:
                cork.y -= abs(cork.move_to_pos[1]- cork.original_pos[1])/10
                t = Transform(child = cork_image)
                cork.zoom -= 0.023
                cork.x += 1.2 #experiment avec cette valeur
                cork.original_size = (cork.original_size[0]*cork.zoom,cork.original_size[1]*cork.zoom)
                t.zoom = cork.zoom
                t.update()
                cork.set_child(t)
            else:
                for i,target in enumerate(target_sprites):
                    if target.row == 1:
                        if target.current_frame == 1 and target.x <=(cork.x - cork.original_size[0]/2) <= (target.x + target_sizes["top"][0]) and target.y <=(cork.y - cork.original_size[1]/2) <= (target.y + target_sizes["top"][1]):
                            target.hit = True
                            score += 5
                            target_SM.redraw(0)
                            cork.destroy()
                            cork_sprites.remove(cork)
                            renpy.restart_interaction()
                            break
                        elif i == len(target_sprites) -1:
                            cork.destroy()
                            cork_sprites.remove(cork)
                    elif target.row == 2:
                        if target.current_frame == 1 and target.x <=(cork.x - cork.original_size[0]/2) <= (target.x + target_sizes["middle"][0]) and target.y <=(cork.y - cork.original_size[1]/2) <= (target.y + target_sizes["middle"][1]):
                            target.hit = True
                            score += 10
                            target_SM.redraw(0)
                            cork.destroy()
                            cork_sprites.remove(cork)
                            renpy.restart_interaction()
                            break
                        elif i == len(target_sprites) -1:
                            cork.destroy()
                            cork_sprites.remove(cork)
                    elif target.row == 3:
                        if target.current_frame == 1 and target.x <=(cork.x - cork.original_size[0]/2) <= (target.x + target_sizes["bottom"][0]) and target.y <=(cork.y - cork.original_size[1]/2) <= (target.y + target_sizes["bottom"][1]):
                            target.hit = True
                            score += 15
                            target_SM.redraw(0)
                            cork.destroy()
                            cork_sprites.remove(cork)
                            renpy.restart_interaction()
                            break
                        elif i == len(target_sprites) -1:
                            cork.destroy()
                            cork_sprites.remove(cork)



        return 0



                
        



transform half_size:
    zoom 1

transform spotlights:
    zoom 0.8
    blend "add"
    alpha 0.5

# screen scene_1:
#   image "images/scene-1-background.png" at half_size
#   imagebutton idle Solid("#FFFFFF00") hover 'images/scene-1-sg-button.png' align(0.7,0.3) at half_size action Show("shooting_gallery")

screen shooting_gallery:
    image "images/targets-background.png" at half_size # on doit changer
    add target_SM
    image "images/shooting-gallery-background.png" at half_size # on doit changer
    image "images/spotlights.png" at spotlights # on peut enlever
    # image "images/cork-gun.png"
    add cork_gun_transform # ca c'est good
    add cork_SM
    # image "images/score-background.png" pos(10,0) at half_size
    text "Score : [score]" color "#FFFFFF" outlines[(absolute(1),"#00000050",absolute(1),absolute(1))] size 40 pos(105,45) anchor(0.0,0.0)
    text "Time : {:.0F}".format(countdown) color "#FFFFFF" outlines[(absolute(1),"#00000050",absolute(1),absolute(1))] size 40 pos(105,95) anchor(0.0,0.0)



    timer 1.0 action If(countdown > 0,true = SetVariable("countdown",countdown- 1.0), false = Show("time_is_up")) repeat If(countdown > 0,true = True,false = False)#remplacer time is up par le reste du jeu


screen time_is_up:
    modal True

    frame:
        xfill True
        yalign 0.5
        background "#ffffff80"
        padding(15,15)
        text "Time is up!" color "#000000" align(0.5,0.5) size 40

        timer 3.0 action [Hide("time_is_up"),Show("final_score")]

screen final_score:
    zorder 2
    modal True

    frame:
        background "#000000BF"
        xfill True
        yfill True
        padding(0,0)

        frame:
            align(0.5,0.5)
            xysize(1485/2,912/2)
            background None
            padding(0,0)
            #image "images/final-score-background.png" at half_size
            text "Your score: [score]"  outlines[(absolute(1),"#00000050",absolute(1),absolute(1))] color"#ffbf5f" size 40 align(0.5,0.5)
    timer 3.0 action [Hide(), Hide("final_score"), Hide("shooting_gallery"), Jump(label_win)]
            #imagebutton auto ""
    


label jeu2:
    # corkgun variables
    $cork_gun_image = Image("images/cork-gun.png")
    $cork_gun_size = (330/2,384/2) #on l'utilise pas c'est trop chiant ses half_size a la RenpyTutoGirl
    $cork_gun_pos = (0,0)
    $cork_gun_opos = (config.screen_width+300,config.screen_height+500)
    $cork_gun_transform = Transform(child = cork_gun_image,zoom=0.8,pos=(cork_gun_opos[0],cork_gun_opos[1]),function = corkGunTransform)
    
    $cork_image = Image("images/cork.png")
    $cork_transform = Transform(child = cork_image,zoom=0.5)
    $cork_sprites = []
    $cork_SM = SpriteManager(update = corkUpdate,event = corkEvents)

    #target variables
    $target_SM = SpriteManager(update= targetUpdate)
    $target_row_1_zoom = 0.5
    $target_row_2_zoom = 0.4
    $target_row_3_zoom = 0.3
    # faudra changer le 376 et le 455
    $target_sizes = {"top":(376 * target_row_1_zoom,455 * target_row_1_zoom),"middle" : (376 * target_row_2_zoom,455*target_row_2_zoom),"bottom" : (376 * target_row_3_zoom,455*target_row_3_zoom)} 
    $target_sprites = []
    $setupTargets()

    #other variable
    $score = 0
    $initial_countdown_time = 15
    $countdown = initial_countdown_time

    call screen shooting_gallery
    return
