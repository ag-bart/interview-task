screen gameUI():

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "UI/stats_idle.png"
        hover "UI/stats_hover.png"
        action ShowMenu("StatsUI")


screen StatsUI():

    add "UI/bg stats.png"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40

            vbox:
                spacing 10
                text "Relationship points (Alex):" size 40


            vbox:
                spacing 10
                text "[a.relationship]" size 40


    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/return_%s.png"
        action Return()
