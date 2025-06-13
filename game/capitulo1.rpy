init python:
    import random

label cap1:
    define nombre_viajero="???"
    play music musicaIntro fadein 1.0
    scene blackout
    "No sabes cuanto tiempo pasó"
    "Te levantas en un lugar curioso"
    stop music fadeout 1.0

    $ renpy.movie_cutscene(skyrimAwake)

    play music musicaAldea fadein 1.0

    if tiempo_perdido:
        play music asalto1 fadein 1.0
        scene aldea1_noche
        "Estás en una calle o algo raro, es de noche y el ambiente se nota tenso"
        "Parece Puerto Montt de noche o algo"
        asaltante "Estas muerto!, no debiste entrar a este barrio"
        asaltante "Te acabas de condenar!"
        hide asaltante
        "En efecto, era Puerto Montt parece, ahí asaltan a cada rato!!"
        yo "Está bien les dare todo lo que tengo! pero calmense"
        hide yo

        menu correrOno:
            "Piensas en correr o algo"
            "Correr":
                yo "Sus problemas economicos y falta de valores no son mi problema, adios!"
                hide Yo
                play music correr fadein 0.6
                "Sales corriendo"
                $ escapar=renpy.random.randint(1,10)
                if escapar==1:
                    "No logras escapar y te desintegran"
                    jump finalMalo1
                else:
                    "Escapas de milagro"
                    scene calleSegura
                    yo "Casi me atrapan esos tipos, alcanzé a correr si"
                    "Miras atras y no parecen haberte seguido"
                    "En tu bolsillo, hayas un aparato raro"
                    yo"Que es esto?"
                    show AparatoRaro#png
                    "Derrepente escuchas alguien que te habla"
                    "Y guardas rapido el aparato"
                    viajero"Ey"
                    viajero"Ey tu, veo que tienes algo que es mio!"
                    yo"Quien eres?"
                    viajero"Soy yo!"
                    yo"Quien erees?!"
                    viajero"Que soy yo!!"
                    hide viajero
                    "De repente de las sombras aparece un personaje que parece sacado de ciencia ficcion"
                    "Y es "
                    $ nombre_viajero = "Waffles"
                    viajero"Bueno me presento soy el doctor Waffles y necesito tu ayuda"
                    viajero"Verás, creo que no somos de la misma dimension o puede que sí"
                    viajero"Pero es posible que en nuestras dimensiones tengamos el mismo problema en ellas!"
                    viajero"Corrupción, economia inestable, delincuencia desempleo\ny se lo que estás pensando"
                    viajero"Que de seguro estoy loco o algo, que esas cosas son normales"
                    viajero"El problema es que si no solucionamos eso, el mundo va\na literalmente explotar!"
                    hide viajero
                    "Te quedas pensando un rato"
                    yo"Espera como se que realmente me vas a ayudar?"
                    yo"Yo ni siquiera vivo aquí en esta ciudad!"
                    yo"No reconozco nada de aqui!"
                    yo"Tampoco recuerdo de donde venia antes, solo aparecí aqui"
                    viajero"Veras, el aparato que tienes puede ayudarte a volver"
                    viajero"Pero tambien debes ayudarme, ese aparato es mio"
                    viajero"Sería un 50 / 50 no es decir quedamos a mano"
                    yo"Y que clase de ayuda?"
                    viajero"Mi mundo va a explotar por las mismas razones sin embargo"
                    viajero"Unos seres poderosos causan estos problemas!"
                    viajero"Se alimentan del caos de la humanidad, debemos detenerlos sino"
                    viajero"Pronto no sera suficiente su alimento con nuestros mundos y los haran estallar!"
                    yo"Espera deja procesar, quieres que te ayude a aniquilar seres poderosos"
                    yo"Que ni conozco??"
                    yo"Viejo ni si quiera tengo empleo en mi mundo como quieres...??!"
                    hide Yo
                    hide viajero
                    play music peligro1 fadein 1.0
                    scene portal
                    "De la nada aparece algo como un portal y hace un sonido grave y amenazante"

                    viajero"Vamos debemos irnos rapido!, dame el aparato!!"
                    yo"Ehh"
                    menu devolverAparato:
                        "Devuelves el aparato sin pensarlo":
                            viajero"Dame eso!"
                            hide viajero
                            "Doctor Wafle enciende el aparato"
                            "Empieza a aparecer otra especie de portal"
                            viajero"Vamosnos de aquí rapido!"
                            hide viajero
                            "Te metes rapido al portal junto al Doc."

                        "No devuelves el aparato y te quedas con el por alguna razón":
                            yo"Mira está bien que quieras salvar los mundos pero esto.."
                            yo"Ni si quiera es real!"
                            viajero"Que haces!! van a acabar con nosotros!"
                            hide viajero
                            hide Yo
                            "Piensas que hacer con el aparato"
                            menu usarlooNO:
                                "Presionar botones al azar, eso siempre funciona":
                                    jump origendelMal
                                "Correr, eso funcionó la ultima vez":
                                    jump finalMalo2

            "No correr y entregar pertenencias":
                "Te roban lo poco que tienes en el bolsillo derecho"
                "Celular, billetera, llaves, botella con agua, cuadernos.."
                "Destornillador bauker, lapices, monitor de 20 pulgadas, silla desplegable.etc"

                asaltante "Nada de valor tienes idiota, no valiste la pena"
                #Video golpe bonk
                "Te golpean con algo y no recuerdas nada mas"
                "Tienes unas visiones raras y parece que estas olvidando cosas"
                play music viajeAlPrologo fadein 1.0
                scene viajeAlPrologo
                yo "Eh que es esto!?"
                hide yo
                "Apenas y recuerdas tu nombre"
                yo "Que esta pasando?"
                #Video viaje tiempo o algo
                jump prologo
    else:
        scene aldea1 with fade
        "Estás en una plaza o algo, un lugar de un pueblo de seguro"
        "Esta lloviendo y el ambiente esta calmado"
        "Un ruido de alguien corriendo rompe la calma"
        #Reproducir video de choque con el loco
        play sound ChoqueP
        scene blackout
        pause 2.0