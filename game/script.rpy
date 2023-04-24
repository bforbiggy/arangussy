include "scripts/skanussy.rpy"

define b = Character("Biggy")
define y = Character("You")


label start:
    call intro

    call skan_story
    scene bg gondola with Dissolve(2.5)
    # show biggy smug
    # b "That sure was a beast of a man huh?"
    # b "Onto the next one!!!"
    # y "W-wait! I'm not read-"

    return
