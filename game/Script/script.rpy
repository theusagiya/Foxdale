
define pov = Character("[povname]")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg airplace

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show green sex

    # These display lines of dialogue.

    p "Hey! are you sexcanhototop@15?"

    p "Wellcome to Foxdale! I think I'll your guide, well... I hope that you like here!"

    p "Por mais urbana que seja a cidade, ela te faz sentir-se em casa a todo momento"
    p "E me desculpe, tenho sempre te chamado pelo seu apelido"



    python:
        povname = renpy.input("Qual o seu nome mesmo?", length=32)
        povname = povname.strip()

        if not povname:
             povname = "Enzo"

    pov "tudo bem, não gosto muito do meu nome mesmo, mas me chamo [povname]!"

    p "Está ficando tarde acho que devemos ir! Posso te ajudar com as malas."

    pov "Claro, meu uncle deve estar nos esperando!"

    scene bg unclehouse

    p "Está ficando tarde acho que devemos ir! Posso te ajudar com as malas."





    # This ends the game.

    return
