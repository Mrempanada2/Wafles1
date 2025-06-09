
label prologo:
    window hide

    play music musicaIntro fadein 1.0
    scene blackout
    show text "Es tarde, hay mucho sueño." at truecenter zorder 2 with dissolve
    pause 2.0
    hide text with dissolve
    show text "Debería irme a dormir." at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    hide expression Solid("#00000088") with dissolve
    stop music fadeout 1.0

    play music musicaSillón fadein 1.0
    scene fondocasa1_loop with fade
    yo "Me dio sueño viendo la tele"
    yo "Creo que me voy a dormir"
    yo "Pero antes voy a la cocina a tomar agua o algo"
    window hide
    "(Estabas viendo programas chistosos raros)"
    stop music fadeout 1.0

    scene fondocasa2_tele with fade
    "Vas a apagar la tele"
    "Algo sonó raro"
    yo "Que?"
    pause 0.1
    stop music
    $ renpy.movie_cutscene(videoExplosion, stop_music=True)

    scene goku
    play sound shock1
    "La tele revienta estrepitosamente"
    "Estaba vieja de todos modos así que te da lo mismo"
    "Y te vas a la cocina de una vez"
    pause 0.5

    play music musicaCocina fadein 1.0 volume 0.5
    scene imagencocina_loop with fade
    "Está terrible de oscuro"
    "La mesa bloquea el paso"
    "Si vas por la izquierda tardas más, pero es más seguro ya que hay más luz"
    "Si vas por la derecha, es más rápido, pero hay menos luz"

    menu Derecha_o_izquerda:
        "por donde vas?"
        "Izquerda de la mesa":
            $ tiempo_perdido = True
            scene Agua1
            "Es mejor irse a la segura a que caerse o algo"
            scene izquerdaAgua
            pause 1.0
            scene blackout
            play sound tomarAgua
            "Tomas agua y te devuelves por el camino mas corto"
            stop sound
            play sound pasosRapidos
            "Tan apurado te ibas a acostar que te pegas en la esquina de la mesa"
            stop music
            stop sound
            $ renpy.movie_cutscene(videocaida, stop_music=True)
            play sound gmodDeath
            scene stunned with fade
            "Te caiste de hocico"

            jump cap1

        "Derecha de la mesa":
            $ tiempo_perdido = False
            scene Agua1
            "Así llegas mas rapido porque eres un flojo igual"
            scene derechaAgua
            pause 1.0
            scene blackout
            play sound pasosRapidos
            "Vas llegando de memoria pero"
            stop music
            stop sound
            $ renpy.movie_cutscene(videocaida, stop_music=True)
            play sound gmodDeath
            scene stunned with fade
            "Te pegaste en el dedo meñique del pie con la mesa y te caiste de hocico"

            jump cap1