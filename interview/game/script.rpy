
init python:

    class Person:

        def __init__(self, character, name, relationship=0):
            self.c = character
            self.name = name
            self.relationship = relationship

        def relationship_points(self, point):
            self.relationship += point

define room_counter = 0 #used in label room_choice


label start:

    $ a = Person(Character("Alex"), "Alex") #base relationship points default to 0

    scene bg hallway
    show screen gameUI
    with fade

    show alex happy
    with dissolve

    a.c "Hi there!"

    a.c "I'm just here to show you around my flat, so the programmer can demonstrate her mad background changing skills."

    a.c "By the way, see that heart in the corner? If you click it, you will see how well we're getting along. Give it a try!"

    a.c "Quite nice, isn't it?"

    menu:

        "Indeed!":

            "I'm happy then!"
            $ a.relationship_points(1)

        "No, not really":

            show alex sad
            "That's a bummer."
            $ a.relationship_points(-1)

    show alex happy

    a.c "You should check the relationship points again."

    a.c "Ok, time to show you around."


label room_choice:

    default menuset = set()

    if room_counter == 0:
        a.c "Where do you wanna go first?"
    elif room_counter == 1:
        a.c "Where to next?"
    elif room_counter == 2:
        a.c "That leaves us with the last room..."
    else:
        pass

    menu:

        set menuset

        "Bedroom":
            jump bedroom

        "Studio":
            jump studio

        "Living room":
            jump living_room


label ending:

    scene bg hallway
    with dissolve

    show alex happy

    a.c "Alright, that's the end."

    if a.relationship > 0:

        a.c "It was a pleasure showing you around!"

    a.c "Bye!"

return


label bedroom:

    scene bg bedroom
    with fade

    show alex happy at right

    a.c "This is my bedroom. Literally a bed in a room."

    $ room_counter += 1

    jump room_choice


label studio:

    scene bg studio
    with fade

    show alex happy at right

    a.c "This is my music studio."

    $ room_counter += 1

    jump room_choice


label living_room:

    scene bg living room at right
    with fade

    show alex happy

    a.c "This is the living room."

    $ room_counter += 1

    jump room_choice
