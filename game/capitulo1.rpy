label cap1:
    play music musicaIntro fadein 1.0
    scene blackout
    "No sabes cuanto tiempo pasó"
    "Te levantas en un lugar curioso"
    stop music fadeout 1.0

    $ renpy.movie_cutscene(skyrimAwake)

    play music musicaAldea fadein 1.0
    scene aldea1 with fade
    "Estás en una plaza o algo, un lugar de un pueblo de seguro"
    "Esta lloviendo y el ambiente esta calmado"
    "Un ruido de alguien corriendo rompe la calma"
    "Que molestia"
    scene blackout
    play sound ChoqueP
    pause 2.0