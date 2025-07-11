init python:
    import random

label cap1:
    define Duda=False
    define preayudar=False
    define saltoPrematuro=False
    define Equipamiento0=False
    define Equipamiento1=False
    define Equipamiento2=False
    define Equipamiento3=False

    define CriaturaCorruptaN="???"
    play music musicaIntro fadein 1.0
    scene blackout with fade
    "No sabes cuanto tiempo pasó"
    "Te levantas en un lugar curioso"
    stop music fadeout 1.0

    scene black
    $ renpy.movie_cutscene("video/skyrimAwake.ogv")

    if tiempo_perdido:
        jump cap1asalto
    else:
        play music musicaAldea2 fadein 1.0 volume 0.5
        scene aldea1 with fade
        "Estás en una plaza o algo, un lugar de un pueblo de seguro"
        "Es como de atardecer"
        yo"Eh? donde estoy"
        yo"No conozco este lugar"
        "No te quedas parado y caminas un rato"
        scene black with fade
        play sound pasosRapidos
        "Se hace hasta tarde pero no puedes comunicarte con nadie"
        "La mayoría de la gente habla un idioma distinto"
        "pronto te marginan y excluyen"
        "Y los pocos que hablan un idioma similar, no logran entenderte nada y te creen loco"
        "Entras a un callejon amplio buscando respuestas"
        jump aparatoRaro



label cap1asalto:
    play music musicaAldea1 fadein 1.0 volume 0.4
    scene aldea1_noche with fade

    "Estás en una calle , es atardecer aunque se está calmado todo al parecer"
    $ hablar(yo,"yo Neutro","Pero que me acaba de pasar!")
    "Es dificil procesar lo sucedido..."
    "De pronto, algo rompe la escasa calma que lograbas obtener"

    play music combate1 fadein 1.0
    $ hablar(asaltante,"asaltante","Que haces en este barrio? entrega todo!")
    hide asaltante

    "Piensas- (Apenas llego y ya me asaltan!)"
    $ hablar(yo,"yo Susto","Hey! quienes son ustedes!")
    $ hablar(yo,"yo Susto","Diganme que esto no es real, es una pesadilla!!",True)

    menu correrOno:
        "Piensas en correr o algo"

        "Correr":
            $ hablar(yo, "yo Susto", "Adioss!")
            "Sales corriendo"
            $ escapar=renpy.random.randint(1,10)

            if escapar==1:
                stop music
                scene black with fade
                play sound bonk
                "No logras escapar y te desintegran"
                jump finalMalo1

            else:
                play music musicaAldea1 fadein 1.0 volume 0.4
                scene calle with fade
                "Escapas de milagro"
                yo "Casi me atrapan esos tipos"
                "Miras atras y no parecen haberte seguido"
                jump aparatoRaro

        "No correr y entregar pertenencias":

            "Te roban lo poco que tienes en el bolsillo derecho"
            "Celular, billetera, llaves, botella con agua, cuadernos.."
            "Destornillador bauker, lapices, monitor de 20 pulgadas, silla desplegable.etc"
            $ hablar (asaltante, "asaltante", "Nada util llevas encima!, ni si quiera valiste la pena")

            play sound bonk volume 0.8
            scene black with fade
            stop music
            pause 0.3
            "Te golpean con algo y no recuerdas nada mas"
            scene stunned with fade
            "Tienes unas visiones raras y parece que estas olvidando cosas"
            pause 1.0
            scene viajeportal with fade

            yo"Eh que es esto!?"
            "Apenas y recuerdas tu nombre ahora mismo y va de mal en peor"
            yo "Que esta pasando?"
            "..."
            "Todo parece desvanecerse.."
            pause 2.0
            jump prologo


label aparatoRaro:    
    scene calle with fade
    play music musicaAldea1 fadein 1.0 volume 0.4
    if tiempo_perdido:
        "En tu bolsillo, hayas un aparato raro"
        yo"Que es esto?"
        show aparatoRaro
        "Un aparato de ciencia ficcion al parecer!"
    else:
        "Una vez incorporado en la calle, te llama la atencion algo del suelo y lo recoges"
        "Es curioso"
        show aparatoRaro
        "Un dispositivo raro, aparentemente de ciencia ficción!"
        yo"Y esto que es?"

    "Derrepente escuchas alguien que te habla"
    "Mantienes el aparato en tu mano"
    hide aparatoRaro
    
    play music musicaIntro fadein 1.0
    doc"Ey!"
    "Te das la vuelta a ver"
    $ hablar(doc, "doc misterioso", "Ey tu, veo que tienes algo que es mio!")
    $ hablar(yo, "yo Neutro", "Quien eres!")
    $ hablar(doc, "doc misterioso", "Soy yo!")
    $ hablar(yo, "yo Neutro", "Quien ereees!!?")
    $ hablar(doc, "doc misterioso", "Que soy yo!!")
    $ hablar(yo, "yo Bien", "a vale :V")
    play music musicaAldea2 fadein 1.0 volume 0.4
    "De repente de las sombras aparece un personaje que parece sacado de ciencia ficcion"
    "Y es... "
    $ docn = "Doc Emmet"
    $ hablar(doc, "doc Neutro", "Buenas, me presento soy el doctor Emmet")
    $ hablar(doc, "doc Neutro", "Lo lamento, debí haberte asustado",True)
    $ hablar(doc, "doc Neutro", "Pero se de donde vienes y la verdad creo que tenemos el mismo problema")
    "Te planteas salir corriendo"
    $ hablar(doc, "doc Neutro", "Podrias explicarme que recuerdas antes de llegar aquí?")
    $ hablar(yo, "yo Bien", "Vale pero no te me acerques aun eh")
    "Le cuentas al doctor Emmet B. como llegaste a este lugar"
    $ hablar(doc, "doc Neutro", "Hmm interesante, verás")
    $ hablar(doc, "doc Neutro", "El momento y lugar en el que viajas entre dimensiones es clave",True)
    $ hablar(doc, "doc Neutro", "Un mal movimiento y podrias haber quedado atrapado en algún lugar de esta dimension")
    $ hablar(doc, "doc Neutro", "Vale tuviste bastante suerte",True)
    $ hablar(doc, "doc Neutro", "Lo que te acaba de ocurrir lo llamo ruptura del waffle multiversal")
    $ hablar(doc, "doc Neutro", "Su nombre viene de la base de que un waffle debe estar en perfecto estado si queremos comerlo como se debe!")
    $ hablar(doc, "doc Neutro", "Nada de recocido o grietas raras que puedan derramar la mermelada",True)
    $ hablar(doc, "doc Neutro", "Pues en nuestras realidades ocurre algo parecido")
    $ hablar(doc, "doc Neutro", "Me explico, una minima grieta en nuestra realidad y se estropea por completo comprendes?")
    "Asientes con la cabeza"
    $ hablar(doc, "doc Neutro", "Creo que en parte es mi culpa, algunos de mis inventos causaron multiples paradojas")
    $ hablar(doc, "doc Neutro", "Porque cayeron en manos equivocadas!",True)
    $ hablar(doc, "doc Neutro", "Veras, uno de mis inventos podia cambiar la forma de pensar de una persona")
    $ hablar(doc, "doc Neutro", "Sin embargo, alguien robo ese aparato y quemo mi laboratorio esa misma noche")
    $ hablar(doc, "doc Neutro", "En su nueva dimension, ese tal ladron se ha vuelto muy poderoso y corrupto",True)
    $ hablar(doc, "doc Neutro", "Y no solo eso, sino que quiere apoderarse de el resto de dimensiones")
    $ hablar(doc, "doc Neutro", "Como la nuestra!",True)
    $ hablar(doc, "doc WTF", "El hecho de que hayas viajado a este lugar de esa forma tan rara",True)
    $ hablar(doc, "doc WTF", "Indica que este rufian ya está intentando abrir portales a nuestros mundos!")
    $ hablar(doc, "doc Neutro", "Y posiblemente causaste en tu mundo, un evento de probabilidad que tiende a 0!",True)
    $ hablar(doc, "doc Neutro", "Lo cual era abrir un portal a esta dimension, y ahora puede que ese ser corrupto, nos esté buscando")
    $ hablar(yo, "yo Bien", "Dices que estoy condenado?? estamos condenados??")
    $ hablar(doc, "doc WTF", "Bueno no del todo, y por eso te contaré mi plan")
    $ hablar(doc, "doc WTF", "Debemos salvar nuestras dimensiones y luego regresarte a tu hogar!")
    $ hablar(yo, "yo Bien", "Vaya, lo dices con mucha seguridad la verdad como si fuera 100 por 100 Cierto!")
    "El doc se agarra la cabeza y piensa"
    "Y tu tratas de recordar como fue que llegaste aquí, fuera del golpe en la mesa claro"
    "Talvez alguna señal de que algo no andaba bien se pudo presentar antes?"
    $ hablar(doc, "doc Neutro","Ok, lo creas o no.. si quieres irte de aquí deberás cooperar conmigo")
    $ hablar(doc, "doc Neutro","Digamos que es 50 / 50",True)
    $ hablar(yo, "yo Bien", "hum ok, pero por tu parte que necesitas?")
    "La verdad, no sabes si creerle o no"
    "Al fin y al cabo te parece un anciano loco!"

    stop music fadeout 1.0
    play music peligro1 fadein 2.0 volume 0.3
    scene portal with fade
    "De la nada aparece algo como un portal y hace un sonido grave y amenazante"
    $ hablar(doc, "doc WTF", "rapido! debemos irnos, dame el aparato!")
    show aparatoRaro
    menu devolverAparato:
        "Devuelves el aparato sin pensarlo":
            $ preayudar=True
            $ Duda=False
            jump aparatoDevuelto
        "No devuelves el aparato y te quedas con el por alguna razón":
            $ hablar(yo, "yo Susto", "Mira está bien que quieras salvar los mundos pero esto..")
            $ hablar(yo, "yo Susto", "Es una locura!!",True)
            $ hablar(doc, "doc MUYsorprendido","Que haces idiota!!?")
            "Piensas que hacer con el aparato"
            $ Duda=True
            menu usarlooNO:
                "Presionar botones al azar, eso siempre funciona":
                    "Presionas los botones mas llamativos hasta que derrepente"
                    hide aparatoRaro
                    stop music
                    scene viajeportal with fade
                    "Ya no estas aquí, estas en otro lado distinto, al parecer despertaste del sueño?"
                    "No le hayas sentido a lo que ven tus ojos, es surrealista."
                    "Tampoco puedes ver tu cuerpo, pero parece que esto podria funcionar"
                    "Te sientes algo idiota"
                    $ saltoPrematuro=True
                    jump cap3
                "Simplemente correr!":
                    hide aparatoRaro
                    "Sales corriendo"
                    "El doc es atrapado por unas criaturas que aparecieron del portal"
                    $ hablar(doc, "doc MUYsorprendido","NOO MALDICIOON!")
                    $ CriaturaCorruptaN="???"
                    $ hablar(CriaturaCorrupta,"monstruo uno","*Lenguaje incomprensible*")
                    jump finalMalo2
                "Devolver el aparato, en que pensabas?":
                    "A regañadientes le devuelves el objeto al doctor Emmet"
                    $ hablar(doc, "doc WTF","Vamos! dame eso, no lo entiendes aún?")
                    $ Duda=True
                    hide aparatoRaro
                    jump aparatoDevuelto

label aparatoDevuelto:
    if Duda:
        $ hablar(doc, "doc WTF","Sigueme y no intentes otra ridiculez!")
    else:
        $ hablar(doc, "doc WTF","Vale, ahora sigueme!")

    hide aparatoRaro
    "Doctor Emmet enciende el aparato"
    play sound portal
    "Hace unos ruidos raros que nunca habias escuchado en tu vida"
    "Sientes como si el sonido estuviera en tu cabeza"
    "Es como si fuera un goteo o algo pero muy profundo!"
    "Empieza a manifestarse en la punta del aparato, otro portal!"
    $ hablar(doc, "doc WTF","Vámonos rapido!!")
    "Te metes rapido al portal junto al Doc."
    stop music
    scene viajeportal with fade
    "No le hayas sentido a lo que ven tus ojos, es surrealista."
    "Tampoco puedes ver tu cuerpo, es como si fueras una entidad distinta"

    jump cap2

label finalMalo1:
    #Musica de derrota o algo
    scene black with fade
    "Dejas de existir en este universo sin conocer sus misterios"
    "No te resistas a los asaltos :V"
    "FIN"
    return

label finalMalo2:
    #La misma musica
    scene black with fade
    "Los monstruos te persiguen"
    $ hablar(CriaturaCorrupta,"monstruo uno","*Lenguaje incomprensible*")
    "Te terminan capturando y no pudiste ni salvar al doctor Emmet ni tampoco a tí"
    "Te hace falta mas actitud!"
    "FIN"
    return


