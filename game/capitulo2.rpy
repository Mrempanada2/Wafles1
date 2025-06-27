
label cap2:

    define Ayudar=True

    play music musicaSillón fadein 1.0 
    scene black with fade
    "Parece que perdiste la conciencia o algo"
    "Aún sin abrir los ojos, sientes el suelo que tienes al rededor tuyo"
    "Es solido"

    stop music fadeout 0.5
    scene caseta with fade
    play music caseta fadein 0.5
    yo"Donde.."
    yo"Donde estoy!"
    "A tu alrededor hay algunos suministros en la caseta"
    "Estas en medio del desierto y parece ser un puesto de investigación"
    yo"Dooooc donde estás?"
    $ hablar(yo,"yo Neutro","Doc, estás por ahí?")
    ####Sonido radio llamando

    $ hablar(yo,"yo Neutro","Eh, que suena?",True)
    "Te acercas a la mesa donde hay varios objetos"
    "Un barómetro, licuadora, computadores, en fin varios objetos curiosos"
    #####Radio imagen aparecer

    "Lo que suena es la radio , alguien está llamando o enviando un mensaje"
    $ hablar(yo,"yo Susto","Como se contesta esta cosa!")
    "Logras contestar la radio al fin"
    $ hablar(doc, "doc Neutro", "Hey, te encuentras bien? según mis calculos deberias estar en la caseta")
    $ hablar(doc, "doc Neutro", "La caseta a la que envié este mensaje",True)
    $ hablar(doc, "doc Neutro", "Tengo este complejo de centros de investigación en este desierto, una larga historia",True)
    $ hablar(doc, "doc WTF", "Pero a lo que veniamos!, escucha hay objetos en la caseta, abastecete con lo que sea util")
    $ hablar(doc, "doc WTF", "Y luego nos vemos en la ubicación en la que dispararé una bengala, cuando el sol baje, a las 20PM !",True)
    $ hablar(doc, "doc Neutro", "Salir ahora es peligroso, el sol esta pegando fuerte y no traemos equipo adecuado!")
    $ hablar(doc, "doc Neutro", "Yo llevaré los suministros de agua y comida para ambos, así que solo encargate del resto de objetos",True)
    $ hablar(yo,"yo Ok","Oye, pero.. como se que tengo que llevar?")
    $ hablar(yo,"yo Neutro","No tengo idea de tu plan",True)
    $ hablar(doc, "doc Neutro", "Vale necesito que traigas la licuadora, que traigas tambien 2 baterias de..")
    
    stop music fadeout 0.5
    scene casetaTormenta with fade
    "En ese instante un viento muy fuerte derriba la antena receptora de tu caseta"
    $ hablar(yo,"yo Susto","Maldicion, vale recogeré lo que considere util y esperaré la señal a la noche")
    "Así que recoges lo importante y esperas hasta la noche.."

    play music desierto1 fadein 0.5
    scene casetaNoche with fade
    
    "Es momento, ya casi las 20 Pm"
    "Te asomas a la ventana"
    $ renpy.movie_cutscene("video/bengala.ogv")

    "Ubicas la bengala, esta bastante cerca así que comienzas inmediatamente a viajar"
    scene black with fade
    "Sales de la caseta, el ambiente está empezando a helarse"
    "Un rato caminarás hacia la señal"
    scene exteriorDesierto1 with fade
    $ hablar(doc, "doc Happy", "Bien hecho!")
    $ hablar(doc, "doc Neutro", "Vale, se me olvido mencionarte que si no ajustamos correctamente los parámetros de viaje..",True)
    $ hablar(yo,"yo Neutro","Puede que lleguemos a lugares distintos uno del otro, si, ya me dí cuenta")
    $ hablar(doc, "doc Neutro", "Exacto, vale movamonos, por el camino te explicaré el plan")
    $ hablar(yo,"yo Bien","Y a donde vamos exactamente?")
    scene black with fade
    "Caminan por algo de 1 hora y media, el frio es escandaloso y se siente mucho"
    pause 0.3

    play music desierto2 fadein 0.5 
    scene exteriorDesierto2 with fade
    $ hablar(yo,"yo Neutro","Doc, creo es buena idea parar a descansar?")
    $ hablar(doc, "doc WTF", "De ninguna manera!, no podemos permitirnos quedarnos expuestos por ahora, debemos llegar a un lugar seguro")
    $ hablar(doc, "doc WTF", "Esas bestias nos están buscando, y solo hay 1 lugar seguro aquí cerca!")
    "Caminan otra hora mas y llegan a un lugar como una mini-fortaleza en el desierto"
    $ hablar(doc, "doc Happy", "Vale, ahora si podemos descansar, mañana te explicaré el plan")
    $ hablar(doc, "doc Happy", "O mejor dicho, mas tarde.")
    $ hablar(yo,"yo Ok","Oye, como podemos estár tan seguros en este lugar?")
    $ hablar(doc, "doc Neutro", "Esta fortaleza tiene un sistema de ocultamiento, jamas nos hayaran a menos que pasen por aquí exactamente")
    $ hablar(doc, "doc Happy", "En este desierto de 5 millones de kilometros cuadrados jaja",True)
    $ hablar(doc, "doc Neutro", "Ademas, a diferencia de cuando estabamos en la ciudad, no hemos causado multiples portales a otras dimensiones",True)
    $ hablar(doc, "doc WTF", "Las criaturas pueden detectar fluctuaciones en el espacio-tiempo, y aquí no hay ninguna")
    $ hablar(doc, "doc Neutro", "Asi que.. hasta mas tarde!")
    play music fortaleza fadein 0.5

    scene black with fade
    "Entran a la fortaleza y duermen en literas"
    "El doctor Emmet enciende el sistema de ocultamiento"
    pause 0.5
    play music tenso1 fadein 0.5
    ###Musica tensa pero no tanto
    "Sin embargo algo te despierta en la noche"
    "Ves por la ventana y la escena es terrible, hay un escuadron de criaturas a pocos metros de la fortaleza"
    $ hablar(yo,"yo Susto","Doctor Emmet, donde estás?",True)
    "Susurras para no llamar atencion al exterior"
    "El doctor Emmet no está en la litera"
    "Alguien te habla desde la oscuridad"
    $ hablar(doc, "doc MUYsorprendido", "Oye! rapido ven salgamos por acá no es seguro mi detector me señalo presencia de criaturas!",True)
    $ hablar(doc, "doc MUYsorprendido", "Están directamente afuera de esta fortaleza!",True)
    $ hablar(doc, "doc MUYsorprendidoF", "No enciendas la luces, corremos el riesgo que nos descubran!",True)
    $ hablar(doc, "doc MUYsorprendido", "Ven sigueme!",True)
    "Sigues al doc hasta una sala aislada"


    scene salaPlan with fade
    $ hablar(doc, "doc WTF", "Ya que no podemos salir ahora, saldremos en cuanto sea apenas seguro!")
    $ hablar(doc, "doc WTF", "Por ahora discutiremos el plan",True)
    "Emmet te explica porque deben llegar a un punto de convergencia universal, que está en el desierto"
    "Tiene las coordenadas de alguna forma y la hora y fecha exacta en la que habra una gran canalización de energia"
    "Es en 12 horas exactas a partir de este momento"
    $ hablar(doc, "doc Neutro", "Y ese es el plan, debemos estar ahí!")
    "El doc va a mirar por un periscopio al exterior"
    $ hablar(doc, "doc Neutro", "Vale!, es seguro salir salgamos ahora antes que sea imposible")
    $ hablar(yo,"yo Bien","Si, tienes razón quien sabe cuando podrian volver")
    $ hablar(doc, "doc Neutro", "Vamos, no hay tiempo!")


    play music desierto2 fadein 0.5
    scene black with fade
    "Tu y el doctor Emmet salen de la mini-fortaleza y se adentran al campo abierto"
    "Pasado un rato llegan a un punto donde los caminos se separan"
    "Justo al medio hay una caseta de investigación"
    "El doc te señala que te quedes en la caseta en sigilo, el tomara uno de los caminos a comprobar su mapa digital, que esta tomando mal las lecturas"

    play music desierto1 fadein 0.5
    scene casetaAlt1 with fade
    "Tienes una radio walkie talkie para comunicarte con el doc"
    "Despues de un rato te llama"
    $ hablar(doc, "doc Neutro", "Estas ahi?")
    $ hablar(yo,"yo Bien","Si!",True)
    $ hablar(doc, "doc Neutro", "Perfecto, creo es momento de contarte en que parte del plan necesito que me ayudes")
    $ hablar(doc, "doc Neutro", "El tema es que si logramos restablecer el orden derrotando a, digamos nuestro nemesis")
    $ hablar(doc, "doc Neutro", "Debemos volver a nuestras dimensiones y destruir los aparatos!",True)
    $ hablar(doc, "doc Neutro", "No podemos dejarlos existir, y mucho menos usarlos para beneficio propio!")
    play music tenso1 fadein 0.5
    "Piensas sobre lo de destruir los aparatos"
    "Podrias sacar mucho beneficio si te quedaras con alguno de ellos"
    "Quiza podrias solucionar los problemas de tu mundo"
    "Problemas sociales como la desigualdad podrian ser erradicados facilmente, controlando la mente de las personas"
    "Para bien obvio"
    "Podrias hasta ajustar el nivel de oferta y demanda, evitar la centralización para que pudieras obtener empleo"
    "Y tambien arreglar los problemas de corrupción, cambiando la forma de pensar primitiva de algunos lideres"
    "Algo raro pasa, te duele la cabeza"
    "..."
    "Algo te dice en tu mente de la nada, que podrias hacerte rico incluso"

    menu destruirAparatos:
        "Prometes destruir los aparatos una vez finalizada la misión?"
        "Por supuesto doc, no lo dudaré":
            $ hablar(doc, "doc Neutro", "Es un alivio saber que piensas así")
            $ hablar(doc, "doc Neutro", "De no ser por eso, quiza te convertirias en mi proximo nemesis")
            $ hablar(doc, "doc Neutro", "Y tambien el de la sociedad")
            $ Ayudar=True 
        "Creo que lo pensaré(no lo harás o talvez si?)":
            $ hablar(doc, "doc Neutro", "Hmm, vale más vale que si consideres hacerlo")
            $ hablar(doc, "doc Neutro", "Si la sociedad donde vives es disfuncional, la presencia de estos objetos",True)
            $ hablar(doc, "doc WTF", "Podrían corromper hasta la mente mas pura",True)
            $ hablar(doc, "doc WTF", "Es es el equivalente a tener mucho dinero o poder!")
            if not preayudar:
                $ Ayudar=False
                $ hablar(doc, "doc WTF", "Al punto en el que estamos, deberías dejar de intentar tonterias sabes?")
            else:
                $ Ayudar=True
    $ hablar(doc, "doc Neutro", "Vale, es hora de movernos!")
    $ hablar(doc, "doc Neutro", "Necesito que salgas y tomes el camino marcado, no encontraremos mas adelante",True) 

    scene black with fade
    "Sales de la caseta y vas por el camino señalado"

    play music desierto1 fadein 0.5
    scene exteriorDesierto3
    "Te encuentras con el doc mas adelante"
    $ hablar(doc, "doc Neutro", "Perfecto, estamos por llegar al lugar de convergencia, deberia mostrar señales de energia en 1 hora")
    $ hablar(yo,"yo Bien","Bien")
    $ hablar(doc, "doc Neutro", "Creo que es momento que comprendas la situación, ya que antes no tuve tiempo para contarte, veras..")
    "El doc te da una larga y complicada explicación sobre nuestro enemigo principal, los mundos, el dispositivo que controla mentes"
    "Algo de que el enemigo al que se enfrentan, de algún modo de alimenta del caos humano"
    "Y ha causado solo problemas en los mundos y en tu mundo!"
    "No entiendes nada pero quieres irte pronto"

    $ hablar(doc, "doc WTF", "Espero hayas entendido la explicación, no podemos salvar los mundos si no conocermos la historia y porque luchamos!")
    menu entenderHistoria:
        "Le dices la verdad o no?"
        "La verdad, no entendí muy bien y me interesa saber bien sobre esto.":
            "Si te interesa saber que está pasando realmente"
            if preayudar and Ayudar:
                "Quieres arreglar los mundos y tambien el tuyo!"
                $ hablar(yo,"yo Bien","Explicame bien doc, quiero saber que está pasando, quiero ayudar!")
            elif preayudar and not Ayudar:
                "Tienes cierta incertidumbre sobre lo correcto"
                $ hablar(yo,"yo Bien","Explicame bien doc, no entiendo nada")
            elif not preayudar and not Ayudar:
                "A pesar de tus dudas, parece importante enterarse de que pasa pero no mas que simplemente volver a tu vida normal"
                $ hablar(yo,"yo Bien","Explicame bien para que nos podamos ir rapido!")
            elif not preayudar and Ayudar:
                "Al principio de todo esto estabas algo indeciso"
                "Pero ahora si quieres ayudar a ti al doc y al resto de personas"
                "Es momento de salvar la sociedad y los mundos!"
                $ hablar(yo,"yo Bien","Quiero salvar los mundos y reparar el mio! asi que cuentame la historia doc!")
            "Al parecer todo tambien tiene una relación con los problemas de tu mundo!"

            play music heroico1 fadein 0.5
            $ hablar(doc, "doc Happy", "Ok, supuse que no habias entendido nada, asi que te explicare mas facil todo")
            $ hablar(doc, "doc Neutro", "Verás, supongamos que mm nose como llamarlo esta criatura que robo mi invento",True)
            $ hablar(doc, "doc Neutro", "Esta criatura se ha vuelto poderosa, un verdadero maestro de los Vórtices dimensionales!")
            $ hablar(doc, "doc WTF", "Sin embargo, su poder ha sido obtenido en base a engaño y violencia")
            $ hablar(doc, "doc WTF", "Su sistema se adaptó a alimentarse del caos de dimensiones",True)
            $ hablar(doc, "doc Neutro", "En tu mundo ha alterado las mentes de los habitantes para ser indiferentes")
            $ hablar(doc, "doc Neutro", "Ha causado desbalance en la sociedad y economia!",True)
            $ hablar(doc, "doc Neutro", "Desajuste de oferta-demanda")
            $ hablar(doc, "doc Neutro", "Centeralización y falta de apoyo a pymes!",True)
            $ hablar(doc, "doc Neutro", "Ha incentivazo malas inversiones estatales y corrupción!",True)
            $ hablar(doc, "doc Neutro", "Todo esto deteriorando la salud mental y llevando a un ciclo sin fin",True)
            $ hablar(doc, "doc Neutro", "Donde solo los mas fuertes sobreviven y el resto es ignorado!")
            $ hablar(doc, "doc WTF", "Puede parecer exagerado pero así funciona esto!")
            $ hablar(doc, "doc WTF", "Esta bestia de alimenta de ese caos literalmente, sin el no puede vivir",True)
            $ hablar(doc, "doc WTF", "Y para obtener mas poder, simplemente viaja de dimensión en dimension controlando a los habitantes")
            $ hablar(doc, "doc WTF", "Y si no se rinden, acaba con esos mundos!",True)
            $ hablar(doc, "doc WTF", "Debemos acabar con El Maestro del Vórtice!")

            if preayudar and Ayudar:
                $ hablar(yo,"yo Bien","Vale! entonces el problema es multidimensional")
                $ hablar(yo,"yo Bien","Vamos, debemos actuar rapido antes de que sea demasiado tarde")
                $ Equipamiento2=True
                "El doc casi confia plenamente en ti! Aunque tu no sabes esto"
                "En base a lo que piensa el doc de ti te dará equipamiento para derrotar a tus proximos enemigos"
                "Es el nivel de confianza que tiene de ti"
                $ hablar(doc, "doc Neutro", "Vale, dentro de poco el portal se abrirá!")
                $ hablar(doc, "doc Neutro", "Toma estos objetos, son de lo mejor porque se que puedo confiar en ti")
                $ hablar(doc, "doc Neutro", "Te serviran para enfrentarnos a nuestras amenazas mas adelante!")

            elif preayudar and not Ayudar:
                $ hablar(yo,"yo Bien","Um ok entiendo algo mejor!")
                $ hablar(yo,"yo Bien","Deberiamos movernos rapido o la verdad nose tu dime que hacemos ahora")
                $ Equipamiento1=True
                "El doc tiene confianza en que ayudaras a derrotar al Maestro del Vórtice"
                "Aunque sabe que estas algo indeciso!"
                "Pero tu no sabes lo que el piensa de todos modos"
                "En base a lo que piensa el doc de ti te dará equipamiento para derrotar a tus proximos enemigos"
                "Es el nivel de confianza que tiene de ti"
                $ hablar(doc, "doc Neutro", "Vale, dentro de poco el portal se abrirá!")
                $ hablar(doc, "doc Neutro", "Usa estos objetos, te serviran para enfrentarnos a nuestros enemigos mas adelante!")
                $ hablar(doc, "doc Neutro", "Son de una categoria buena, se que les puedes dar un buen uso!")

            elif not preayudar and not Ayudar:
                "No le das mucha importancia al tema, pero intentarás lo mejor"
                $ hablar(yo,"yo Bien","Ok vale movamonos rapido si?")
                $ Equipamiento1=True
                "El doc tiene confianza en que ayudaras a derrotar al Maestro del Vórtice"
                "Aunque sabe que eres algo complicado y desconfiado"
                "El hecho de que hayas sincero y escuchado la historia, le sirve"
                "Pero tu no sabes lo que piensa el de todos modos!"
                "En base a lo que piensa el doc de ti te dará equipamiento para derrotar a tus proximos enemigos"
                "Es el nivel de confianza que tiene de ti"
                $ hablar(doc, "doc Neutro", "Vale, dentro de poco el portal se abrirá!")
                $ hablar(doc, "doc Neutro", "Usa estos objetos, te serviran para enfrentarnos a nuestros enemigos mas adelante!")
                $ hablar(doc, "doc Neutro", "Son de una categoria buena, se que les puedes dar un buen uso!")

            elif not preayudar and Ayudar:
                $ hablar(yo,"yo Bien","Estoy convencido de mi razón, debemos acabar con esto de raíz")
                $ hablar(yo,"yo Bien","Vamos a ello!")
                $ Equipamiento3=True
                "El doctor Emmet se ha dado cuenta de que, en poco tiempo has evolucionado"
                "Sabes que tienes potencial de ser un heroe y salvar las dimensiones"
                "Ademas de reparar la sociedad de tu mundo"
                "Pero tu no sabes esto!"
                "En base a lo que piensa el doc de ti te dará equipamiento para derrotar a tus proximos enemigos"
                "Es el nivel de confianza que tiene de ti"
                $ hablar(doc, "doc Neutro", "Vale, dentro de poco el portal se abrirá!")
                $ hablar(doc, "doc Neutro", "Me he dado cuenta que eres alguien que a pesar de que en un inicio se mostro algo")
                $ hablar(doc, "doc Neutro", "Algo indeciso y con miedo talvez")
                $ hablar(doc, "doc Neutro", "Te has convertido en poco tiempo en alguien valiente y dispuesto a ayudar")
                $ hablar(doc, "doc Neutro", "Tomas mis mejores objetos y equipamiento, te servirán para enfrentarnos a lo que viene!")
            define comprend=True

        "Si, perfecto lo comprendo de pies a cabeza, vamos a ello!":
            "En realidad pues no entendiste nada y estas apresurado a irte"
            "El bien del resto de las personas el la ultima de tus prioridades"
            "Solo quieres irte!"

            if preayudar and Ayudar:
                $ hablar(yo,"yo Bien","Vale! debemos acabar con esto rapido supongo no?")
                $ hablar(yo,"yo Bien","Pero estoy aquí para ayudar de todos modos!",True)
                $ Equipamiento1=True
                "El doc tiene confianza en que ayudaras a derrotar al Maestro del Vórtice"
                "Aunque sabe que estas algo indeciso!"
                "Tambien sabe que no te interesa la historia ni tampoco ayudar demasiado a los demas"
                "Aunque lo hayas ayudado antes, todo demuestra que solo quieres irte rapido"
                "O que eres un apresurado simplemente!"
                "Pero tu no sabes lo que el piensa de todos modos"
                "En base a lo que piensa el doc de ti te dará equipamiento para derrotar a tus proximos enemigos"
                "Es el nivel de confianza que tiene de ti"
                $ hablar(doc, "doc Neutro", "Vale, dentro de poco el portal se abrirá!")
                $ hablar(doc, "doc Neutro", "Usa estos objetos, te serviran para enfrentarnos a nuestros enemigos mas adelante!")
                $ hablar(doc, "doc Neutro", "Son de una categoria buena, se que les puedes dar un buen uso!")

                
            elif preayudar and not Ayudar:
                $ hablar(yo,"yo Bien","Em ok, vamos a por ello dime que hay que hacer")
                $ Equipamiento0=True
                "El doc considera que estas algo indeciso pero confia un poco en ti de todos modos"
                "Tu no sabes lo que piensa de todos modos"
                "En base a lo que piensa el doc de ti te dará equipamiento para derrotar a tus proximos enemigos"
                "Es el nivel de confianza que tiene de ti"
                $ hablar(doc, "doc Neutro", "Vale, dentro de poco el portal se abrirá!")
                $ hablar(doc, "doc Neutro", "Escucha te voy a ser sincero!, no puedo confiarte objetos tan buenos y poderosos como los que tengo!")
                $ hablar(doc, "doc Neutro", "Podrías incluso tomar una desición tonta en el lugar al que vamos!")
                $ hablar(doc, "doc Neutro", "Pero toma esto, podria servirte")

            elif not preayudar and not Ayudar:
                "No le das mucha importancia al tema"
                $ hablar(yo,"yo Bien","Doc, vamos rapido ya entendi lo que dice okey?")
                $ hablar(yo,"yo Bien","Quiero volver a mi dimension vale? es lo que importa")
                $ Equipamiento0=True
                "El doc sabe que eres un apresurado e indiferente"
                "Casi duda si valio la pena ayudarte antes, de todos modos no habia nadie mejor"
                "Tu no sabes lo que piensa el de todos modos"
                "En base a lo que piensa el doc de ti te dará equipamiento para derrotar a tus proximos enemigos"
                "Es el nivel de confianza que tiene de ti"
                $ hablar(doc, "doc Neutro", "Vale, dentro de poco el portal se abrirá!")
                $ hablar(doc, "doc Neutro", "Escucha te voy a ser sincero!, no puedo confiarte objetos tan buenos y poderosos como los que tengo!")
                $ hablar(doc, "doc Neutro", "Podrías incluso tomar una desición tonta en el lugar al que vamos!")
                $ hablar(doc, "doc Neutro", "Pero toma esto, podria servirte")


            elif not preayudar and Ayudar:
                $ hablar(yo,"yo Bien","Si! lo estoy entendiendo mejor creo, pero debemos apresurarnos o no?")
                $ Equipamiento1=True
                "El doc tiene confianza en que ayudaras a derrotar al Maestro del Vórtice"
                "Aunque sabe que estas algo indeciso!"
                "Tambien sabe que no te interesa la historia ni tampoco ayudar demasiado a los demas"
                "Aunque lo hayas ayudado antes, todo demuestra que solo quieres irte rapido"
                "O que eres un apresurado simplemente!"
                "Si embargo ve que tienes potencial de convertirte en un heroe, un heroe descuidado!"
                "Pero tu no sabes lo que el piensa de todos modos"
                "En base a lo que piensa el doc de ti te dará equipamiento para derrotar a tus proximos enemigos"
                "Es el nivel de confianza que tiene de ti"
                $ hablar(doc, "doc Neutro", "Vale, dentro de poco el portal se abrirá!")
                $ hablar(doc, "doc Neutro", "Usa estos objetos, te serviran para enfrentarnos a nuestros enemigos mas adelante!")
                $ hablar(doc, "doc Neutro", "Son de una categoria buena, se que les puedes dar un buen uso!")
            define comprend=False
                


    $ hablar(yo,"yo Bien","Y ahora?")
    if comprend and not preayudar and Ayudar:
        play music heroico1 fadein 0.5
    else:
        play music peligro1 fadein 2.0 volume 0.3

    scene exteriorDesierto3Deform with fade
    "Derrepente, se comienza a deformar el espacio nuevamente, aparece un portal similar a los que has visto!"
    "Pero es mas grande y evoca un aura maligna!"
    $ hablar(doc, "doc Neutro", "Mira! el portal se ha abierto vamos dentro!")
    $ hablar(doc, "doc Neutro", "El Maestro del Vórtice se encuentra dentro, lo deduje hace unos dias!")
    $ hablar(doc, "doc Neutro", "Rapido!")
    jump cap3

    









