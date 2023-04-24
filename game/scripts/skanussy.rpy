define s = Character("Lauti")

label skan_story:
    scene bg forest with Dissolve(1.5)

    y "Woah.... how'd I end up here?"
    "You pick yourself up off the ground and skan your surroundings."
    "At first you see nothing but then, you see it... a beast"

    show skan angry
    s "What are you doing here? This is my territory. Another step and I'm allowed to act in self-defense."
    menu:
        "I'm sorry I didn't realize. Could you show me where to go?":
            s "Why didn't you say so? Follow me."
        "I need ta get fucked up drinking dat beer baby":
            s "my digga das all u had to say"
    show skan smile

    "Skan leads you through the woods to his home, a cozy cabin nestled deep in the forest. As you enter, you notice a stack of manga books on the coffee table."
    y "You read manga too?"
    s "Yeah, ever heard of Bouncer?"
    menu:
        "Yes":
            s "based"
        "No":
            s "kill yourself"

    return