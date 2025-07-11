
label cap3:
    play music tenso1 fadein 1.0 volume 0.8
    scene infierno1 with fade

    if saltoPrematuro:

        "Apareces en lo que parece ser"
        "El mismisimo infierno!"
        $ hablar(yo,"yo Susto","Ehh?")
        $ hablar(yo,"yo Susto","Donde estoy??",True)
        $ hablar(yo,"yo Neutro","Bueno tratare de salir de aqui sin que me atrapen",True)
        show aparatoRaro
        $ hablar(yo,"yo Ok","Con esto de seguro puedo salir facil no?")
        "Pero el aparato no reacciona, al parecer lo estropeaste"
        $ hablar(yo,"yo Susto","Oh no..")
        $ hablar(yo,"yo Susto","Ehh?",True)
        "Frente a ti aparece una criatura terrible"
        $ hablar(CriaturaCorrupta,"monstruo uno","*Lenguaje incomprensible*")
        play sound disparo1
        scene black with fade
        "La criatura te aniquila en menos de 5 segundos"
        "No tuviste chance, nunca supiste que habia pasado, quien era ese anciano y como llegaste a esto"
        "Has muerto!"
        return
    
    "Llegas a la guarida del Maestro del vórtice"
    "Parece el mismisimo infierno"
    "Esta vez estas con el doc, no hubieron errores de viaje dimensional"
    $ hablar(yo,"yo Neutro","Así que esta es su guarida")
    $ hablar(doc, "doc Neutro", "Así es, ya estamos aquí")
    
    if Equipamiento3:
        play music combate4 volume 0.3
        show equipo3
        "Es hora de ponerle fin a esto!"
        "Ya no tienes miedo ni duda"
    elif Equipamiento0:
        play music combate11 volume 0.5
        show equipo0
        "Piensas en como podrías defenderte la verdad"
        "Pero no le pedirás mejores cosas al doc"
        "Al fin y al cabo has sido algo idiota!, es imposible que te confie algo mejor"
    elif Equipamiento1:
        play music combate2 volume 0.5
        show equipo1
        "Estas algo asustado"
    elif Equipamiento2:
        play music combate3 volume 0.5
        show equipo2
        "Tu desición es muy firme, siempre ha sido así"
    $ hablar(doc, "doc WTF", "Ves esa estructura del fondo?")
    $ hablar(doc, "doc Neutro", "Ahí se oculta el maestro del Vórtice",True)
    "Empiezan a moverse hacia el lugar"
    "Con un patin volador hecho de materiales raros como.. licuadoras?"
    scene infierno2 with fade

    if Equipamiento0:
        show equipo0
        "Apenas van llegando a la entrada y los están esperando criaturas peligrosas"
        "Al parecer defienden al Maestro del Vórtice"
        "Y los acaban de ver a ustedes!"
        "Las criaturas van corriendo hacia ustedes"
        $ hablar(doc, "doc WTF", "Acabaré con ustedes!")
        "El doc ataca con una metralleta laser contra las criaturas"
        "Sin embargo una criatura lo flanquea y lo golpea lanzandolo lejos"
        "No puedes hacer mucho con lo que tienes!"
        "La criatura se abalanza sobre ti"
        $ hablar(CriaturaCorrupta,"monstruo dos","*Sonidos enojado*")
        "Un disparo laser del doc la convierte en ceniza"
        $ hablar(doc, "doc WTF", "Uff faltó poco!")
        $ hablar(yo,"yo Ok","Gracias doc")
        $ hablar(doc, "doc WTF", "Vale vamos dentro")
        scene infierno3 with fade
        show equipo0
        "Apenas van entrando y.."
        play sound rugidoA
        "Desde arriba, cae una criatura horrible"
        "Te golpea y sales lejos"
        "El doc esquivo el golpe y está al lado contrario de la sala!"
        $ hablar(maestro,"Maestro Neutral","Idiotas!")
        $ hablar(maestro,"Maestro Neutral","Creen que no me doy cuenta de que estaban tratando de atraparme?",True)
        $ hablar(maestro,"Maestro Neutral","Todo este tiempo los esperé!")
        $ hablar(maestro,"Maestro Neutral","SOY EL MAESTRO DEL VÓRTICE, NO TIENEN OPORTUNIDAD DE NINGUNA FORMA!")
        $ maestrO="Maestro del Vórtice"
        $ hablar(doc, "doc MUYsorprendido", "No tiene sentido!, estuvimos ocultando nuestro pasos!")
        $ hablar(maestro,"Maestro Neutral","Eso creyeron!")
        $ hablar(maestro,"Maestro Neutral","Era parte de mi trampa atraerlos hasta acá!",True)
        $ hablar(doc, "doc WTF", "Hablas demasiado!")
        "En eso el doc saca un lanzamisiles y le dispara al monstruo!"
        play sound explosion
        "El misil lo impacta "
        "Pero el monstruo emerge del humo!"
        "Idiotas!"
        "El monstruo el cual está evidentemente herido, golpea al doc y lo lanza lejos"
        "El doc deja caer su dispositivo de portales dimensionales"
        "Lo recoges rapido, talvez puedas huir!"
        "Pero el Doctor Emmet está fuero de juego ahora! solo el sabe usarlo correctamente!"
        $ hablar(maestro,"Maestro Neutral","Doctor Emmet! sigues igual de arrogante que cuando nos conocimos en el pasado!")
        $ hablar(maestro,"Maestro Neutral","No has cambiado nada JAJA",True)
        $ hablar(maestro,"Maestro Neutral","Derrotarte fue tan facil como robar tus inventos y quemar tu laboratorio!",True)
        $ hablar(maestro,"Maestro Neutral","Gracias a tí, mi poder seguirá expandiendose!")
        "Ahora el monstruo se acerca a ti"
        $ hablar(maestro,"Maestro Neutral","Te ves insignificante!, acabaré contigo rapido no vaya a ser que me des algún problema!")
        "El monstruo levanta su puño"
        $ hablar(doc, "doc WTF", "Idiota! toma esto!")
        "El doc, al parecer uso un dispositivo para recuperarse rapido"
        "Le dispara otro cohete!"
        $ hablar(maestro,"Maestro Mal","Que es esto?")
        "El cohete se ensarta en la espalda del Maestro del Vórtice"
        "Y luego estalla"
        play sound rugidoB
        $ hablar(maestro,"Maestro Mal","AAHHHHH NOOO!",True)
        "El cohete daña al monstruo que va a caer en cima tuyo!"
        $ hablar(yo,"yo Susto","Maldicion!")
        $ hablar(yo,"yo Susto","Nooo")
        "Por un momento ves margen para esquivarlo pasando por debajo de el!"
        pause 1.0
        "Logras esquivarlo!"
        "En una mirada desesperada lo ves atras tuyo, ha dejado expuesto algo en su espalda, brilla con fuerza"
        "Parece ser su corazon, nucleo o lo que sea!"
        "Con el aparato de dimensiones en mano, lo lanzas con fuerza a ese lugar"
        $ hablar(yo,"yo Susto","Toma esto!")
        "El aparato revienta y el monstruo cae al suelo hecho cenizas"
        "Se abre un portal en el lugar"
        $ hablar(doc, "doc Happy", "Bien hecho!")
        $ hablar(doc, "doc Happy", "Lo hemos derrotado!",True)
        $ hablar(doc, "doc Happy", "Despues de tanto tiempo!",True)
        $ hablar(doc, "doc WTF", "Sin embargo",True)
        $ hablar(doc, "doc WTF", "Se que no vas a destruir los aparatos que has obtenido o me equivoco?")
        "Asientes con la cabeza"
        hide equipo0
        $ hablar(yo,"yo Neutro","N- No puedo doc ")
        $ hablar(yo,"yo Neutro","Estos objetos me servirian mucho en mi mundo",True)
        $ hablar(yo,"yo Neutro","Hablo de usarlos para bien!",True)
        $ hablar(doc, "doc WTF", "Comprendo! pero no tienes tanta actitud como para poder conservarlos de las garras del mal!",True)
        $ hablar(doc, "doc WTF", "Me veré obligado a")
        $ hablar(doc, "doc WTF", "Devolverte al pasado! y borrarte la memoria de lo sucedido!",True)
        $ hablar(doc, "doc WTF", "Con algo de suerte nunca llegarás a este mundo, no te lo tomes personal, es lo mejor para las dimensiones",True)
        $ hablar(doc, "doc WTF", "Y tambien para tí amigo!",True)
        $ hablar(yo,"yo Neutro","Creo estuve algo equivocado todo este tiempo, y talvez debía haber pensado en los demas y no solo en mi")
        $ hablar(doc, "doc Neutro", "Y si, tienes algo de razon pero de todos modos debo devolverte a tu dimension sin recuerdos")
        $ hablar(doc, "doc Neutro", "No vaya a ser que uses lo que has aprendido para mal y para convertirte en un nuevo enemigo oculto de la sociedad!")
        $ hablar(doc, "doc Happy", "Hasta la vista.")
        stop music fadeout 0.5
        scene viajeportal with fade 
        "El doc te dispara con algo que te convierte a forma no fisica, estas en un portal"
        "Pero sientes como si olvidaras todo"
        play music musicaAldea1 fadein 0.5 volume 0.8
        scene black
        "Al final nunca llegas a ese mundo en esta nueva linea temporal, pero tratarás de hacer lo mejor con lo que tengas a mano para mejorar todo"
        "Porque al parecer si recuerdas algo de lo vivido, lo tienes en tu conciencia"
        "Fin"
        return

    elif Equipamiento1:
        show equipo1
        "Apenas van llegando a la entrada y los están esperando criaturas peligrosas"
        "Al parecer defienden al Maestro del Vórtice"
        "Los acaban de detectar a ti y al doc!"
        "Van hacia ustedes a atacarlos!"
        $ hablar(yo,"yo Bien","Oh no!")
        play sound disparo1
        "Con tu arma eliminas a un monstruo antes de que se acerque demasiado"
        "El doc se encarga de los otros 2"
        $ hablar(doc, "doc WTF", "Bien hecho!")
        $ hablar(doc, "doc WTF", "Vale vamos dentro, rapido!")
        scene infierno3 with fade
        show equipo1
        play music combate1 fadein 0.5 volume 0.5
        "Apenas van entrando cuando de pronto.."
        play sound rugidoA
        "Desde arriba, cae una criatura horrible"
        "Te golpea y sales lejos"
        "El doc esquivo el golpe y está al lado contrario de la sala!"
        $ hablar(maestro,"Maestro Neutral","Idiotas!")
        $ hablar(maestro,"Maestro Neutral","Creen que no me doy cuenta de que estaban tratando de atraparme?",True)
        $ hablar(maestro,"Maestro Neutral","Todo este tiempo los esperé!")
        $ maestrO="Maestro del Vórtice"
        $ hablar(maestro,"Maestro Neutral","SOY EL MAESTRO DEL VÓRTICE, NO TIENEN OPORTUNIDAD DE NINGUNA FORMA!")
        $ hablar(doc, "doc WTF", "No tiene sentido!, estuvimos ocultando nuestro pasos!")
        $ hablar(maestro,"Maestro Neutral","Eso creyeron!")
        $ hablar(maestro,"Maestro Neutral","Era parte de mi trampa atraerlos hasta acá!",True)
        $ hablar(doc, "doc WTF", "Hablas demasiado!")
        play sound explosion
        "En eso el doc saca un lanzamisiles y le dispara al monstruo!"
        play sound disparo1
        "Le disparas al monstruo con tu arma!"
        $ hablar(yo,"yo Susto","Toma esto!")
        "Luego de un arduo combate, el monstruo cae"
        "Sin embargo el doc y tu han sido heridos"
        $ hablar(doc, "doc MUYsorprendido", "Lo logramos pero")
        $ hablar(doc, "doc MUYsorprendido", "No me siento del todo bien!",True)
        $ hablar(yo,"yo Susto","Yo tampoco doc, yo tampoco")
        $ hablar(doc, "doc WTF", "Escuchame, si viajamos ahora a nuestros hogares, posiblemente moririamos")
        $ hablar(doc, "doc WTF", "Para viajar se requiere estar bien fisicamente, no en este estado!",True)
        $ hablar(yo,"yo Susto","Y que haremos!")
        $ hablar(doc, "doc WTF", "Trataremos de aguantar lo que podamos hasta recuperarnos, tengo algunos objetos que nos serviran para sanarnos!",True)
        $ hablar(yo,"yo Neutro","Pues tendremos que aguantar aquí el tiempo necesario doc.")
        hide equipo1
        "Luego de esconderse un tiempo de los enemigos que llegaron a ver el cadaver de su maestro"
        "Empiezan a notar que, el aparato de portales se vuelve mas estable"
        $ hablar(doc, "doc Neutro", "Hey! ven a ver esto")
        $ hablar(yo,"yo Bien","que es?")
        $ hablar(doc, "doc Neutro", "El aparato de portales se estabiliza, las dimensiones vuelven a la normalidad al haber eliminador al Maestro del Vórtice")
        $ hablar(doc, "doc Happy", "Podemos usar los portales, ahora son seguros para cualquier cosa")
        $ hablar(yo,"yo Ok","Estas seguro?")
        $ hablar(doc, "doc Happy", "Si! lo he comprobado en multiples ocasiones en ambientes controlados, así que volvamos a casa")
        $ hablar(doc, "doc Happy", "Fue un gusto conocerte amigo")
        $ hablar(yo,"yo Bien","Gracias doc! tambien fue un gusto y sin duda aprendi bastante")
        $ hablar(yo,"yo Bien","Tal vez nos volvamos a encontrar en el futuro!")
        $ hablar(doc, "doc Happy", "...O en el pasado")
        "En eso el doc abre 2 portales, y cada uno se va a su dimension"
        stop music fadeout 1.0
        scene viajeportal with fade
        "Viajas a tu casa, y el doc? quien sabe donde ira ahora.."
        "..."
        play music victoria fadein 1.0
        scene black
        "Fue un viaje genial!"
        "Quien sabe, talvez con actitud todos podemos ayudar a contribuir a la sociedad!"
        "No derrotando monstruos interdimensionales, pero si colaborando con nuestras comunidades!"
        "FIN"
        return
        
    elif Equipamiento2:
        show equipo2
        "Apenas van llegando a la entrada y los están esperando criaturas peligrosas"
        "Al parecer defienden al Maestro del Vórtice"
        "Ya los vieron!"
        "Se dirigen hacia ustedes para atacarlos!"
        play sound disparo2
        $ hablar(doc, "doc WTF", "Toma esto!")
        "El doc y tu acaban con los primeros enemigos"
        "Pero vienen mas!"
        "Haz sido rodeado por enemigos!"
        play sound explosion
        "El doc dispara un cohete contra los enemigos y te salva esta vez!"
        $ hablar(doc, "doc Happy", "Perfecto! vamos dentro")
        $ hablar(yo,"yo Bien","Gracias doc, vale vamos con cuidado!")
        scene infierno3 with fade
        play music combate2 fadein 0.5 volume 0.5
        "Apenas van entrando cuando de pronto.."
        play sound rugidoA
        "Desde arriba, cae una criatura horrible"
        "Te golpea y sales lejos"
        "El doc esquivo el golpe y está al lado contrario de la sala!"
        $ hablar(maestro,"Maestro Neutral","Idiotas!")
        $ hablar(maestro,"Maestro Neutral","Creen que no me doy cuenta de que estaban tratando de atraparme?",True)
        $ hablar(maestro,"Maestro Neutral","Todo este tiempo los esperé!")
        $ maestrO="Maestro del Vórtice"
        $ hablar(maestro,"Maestro Neutral","SOY EL MAESTRO DEL VÓRTICE, NO TIENEN OPORTUNIDAD DE NINGUNA FORMA!")
        play sound disparo2
        $ hablar(yo,"yo Bien","Hablas demasiado! toma esto!")
        "Le disparas al monstruo en la cara"
        "Este se tambalea, pero se recupera rapidamente y carga contra ti!"
        $ hablar(doc,"doc WTF","HEY")
        play sound explosion
        "El doc dispara un cohete poderoso contra el monstruo"
        "Este se tambalea nuevamente"
        "Rodeas al monstruo mientras le disparas repetidas veces!"
        "El doc lo ataca con 1 cohete mas!"
        play sound rugidoB
        $ hablar(maestro,"Maestro Neutral","AAAAH",True)
        $ hablar(maestro,"Maestro Neutral","ESTO NO PUEDE SER",True)
        "El monstruo te golpea y sales lejos!"
        $ hablar(doc, "doc WTF", "NOO!")
        $ hablar(doc, "doc WTF", "Toma esto!")
        "Doc dispara su ultimo cohete"
        "El cual parece no tener un buen destino!, no le dará al monstruo!"
        $ hablar(doc, "doc WTF", "Disparale al cohete cuando este sobre el Maestro!")
        $ hablar(yo,"yo Bien","OKEYY")
        "Apuntas al cohete"
        "fallas la primera vez"
        "Y la segunda"
        "Y tercera"
        "Pero con tu ultimo disparo"
        $ hablar(yo,"yo Bien","AHHHHH")
        "Le das al cohete en pleno vuelo, el cual no iba a atinarle al monstruo"
        "Sino que doc pretendia darle con este justo por encima al Maestro del Vórtice!"
        "Y que tu le dispararas en el aire!"
        "El monstruo cae hecho cenizas!"

        $ hablar(doc, "doc Happy", "Bien hecho!")
        $ hablar(yo,"yo Magnate","Siii")
        hide equipo2
        "El doc y tu alzan los brazos en señal de victoria y celebran gritando al aire"
        $ hablar(doc, "doc Happy", "Fue un gusto conocerte amigo")
        $ hablar(yo,"yo Bien","Gracias doc! tambien fue un gusto y sin duda aprendi bastante")
        $ hablar(yo,"yo Bien","Tal vez nos volvamos a encontrar en el futuro!")
        $ hablar(doc, "doc Happy", "...O en el pasado")
        "En eso el doc abre 2 portales, y cada uno se va a su dimension"
        stop music fadeout 0.5
        scene viajeportal with fade
        "Viajas a tu casa, y el doc? quien sabe donde ira ahora.."
        "..."
        play music victoria fadein 1.0
        scene black
        "Fue un viaje genial!"
        "Quien sabe, talvez con actitud todos podemos ayudar a contribuir a la sociedad!"
        "No derrotando monstruos interdimensionales, pero si colaborando con nuestras comunidades!"
        "FIN"
        return

    elif Equipamiento3:
        hide equipo3
        scene infierno2 with fade
        "Apenas van llegando a la entrada y los están esperando criaturas peligrosas"
        "Al parecer defienden al Maestro del Vórtice"
        $ hablar(CriaturaCorrupta,"monstruo dos", "Sonidos de enojo*",)
        "Actuas rapido y atacas primero"
        play sound disparos3
        $ hablar(yo,"yo Magnate","Toma esto!")
        play sound disparos3
        pause 0.2
        play sound explosion
        "La criatura estalla"
        "Ahora es momento de entrar a la guarida"

        play music combate3 fadein 0.5 volume 0.5
        scene infierno3 with fade
        play sound explosion
        "Vuelan la pared de la guarida a cohetes!"
        "Rapidamente entran"
        play sound rugidoA

        $ maestrO="Maestro del Vórtice"
        $ hablar(maestro,"Maestro Neutral","Eh?")
        $ hablar(maestro,"Maestro Neutral","Como es posible?",True)
        $ hablar(maestro,"Maestro Neutral","Que hacen aquí!")
        $ hablar(doc, "doc WTF", "JAJA")

        $ hablar(maestro,"Maestro Neutral","Esta bien acabaré con ustedes de todas formas!!")
        show equipo3
        $ hablar(maestro,"Maestro Neutral","TOMEN ESTO!",True)
        "El monstruo alza sus puños sobre ustedes"
        "El doc y tu dicen"
        "HABLAS DEMASIADO!"
        play sound disparos3
        "Le disparan con todo lo que tienen!"
        
        pause 0.3
        play sound disparo2
        pause 0.2
        play sound explosion

        "Pero el doc es acorralado por el monstruo!"
        $ hablar(maestro,"Maestro Neutral","Despidete de todo lo que conoces Emmet!")
        $ hablar(yo,"yo Susto","No en mi guardia!")
        play sound disparos3
        "Le disparas a la espalda del monstruo"
        "El doc aprovechando la situacion, Doc se mueve por debajo del monstruo "
        play sound explosion
        "Una vez al otro lado le dispara al monstruo que estaba algo aturdido!"
        $ hablar(maestro,"Maestro Mal","NOOO")
        "El monstruo es pulverizado al instante!"
        $ hablar(doc, "doc Happy", "Bien hecho!")
        $ hablar(yo,"yo Magnate","Siii")
        hide equipo3
        "El doc y tu alzan los brazos en señal de victoria y celebran gritando al aire"
        $ hablar(doc, "doc Neutro", "Hey! ven a ver esto")
        $ hablar(yo,"yo Bien","que es?")
        $ hablar(doc, "doc Neutro", "El aparato de portales se estabiliza, las dimensiones vuelven a la normalidad al haber eliminador al Maestro del Vórtice")
        $ hablar(doc, "doc Happy", "Podemos usar los portales y volver con seguridad a nuestros hogares y dimensiones!")
        $ hablar(yo,"yo Bien","Pues supongo que es hora de la despedida!")
        "El mundo se ha estabilizado y ves por el portal como se crean varias leyes para mejorar la sociedad"
        "Tambien ves menos cosas terribles en la televisión"
        "Sin embargo para acabar con el mal del mundo, debes actuar en el tambien!"
        
        "En eso el doc abre 1 portal"
        $ hablar(doc, "doc Happy", "Hey, estas seguro que te vas tan rapido?")
        $ hablar(doc, "doc Happy", "Podemos quedarnos a acabar con estas criaturas antes que desaparezcan por completo")
        $ hablar(doc, "doc Happy", "Será divertido!")
        menu quedarse:
            "Te quedas a aniquilar monstruos un rato?"
            "Si":
                stop music fadeout 0.5
                play music combate4 fadein 1.0 volume 0.6
                scene black with fade
                "Te quedas a aniquilar monstruos un tiempo mas"
                "Quien sabe, talvez con actitud todos podemos ayudar a contribuir a la sociedad!"
                "No derrotando monstruos interdimensionales, pero si colaborando con nuestras comunidades!"
                "FIN"
                return
            "No":
                $ hablar(doc, "doc Happy", "Okey como quieras, fue un gusto conocerte amigo!")
                $ hablar(yo,"yo Bien","Gracias doc! tambien fue un gusto y sin duda aprendi bastante")
                $ hablar(yo,"yo Bien","Tal vez nos volvamos a encontrar en el futuro!")
                $ hablar(doc, "doc Happy", "...O en el pasado")
                stop music fadeout 0.5
                scene viajeportal with fade
                "Viajas a tu casa, y el doc se quedará con la diversion"
                "La verdad de arrepientes un poco de no quedarte un rato mas!"
                "Lo importante es que estás de vuelta!"
                play music victoria fadein 1.0
                scene black
                "Fue un viaje genial!"
                "Quien sabe, talvez con actitud todos podemos ayudar a contribuir a la sociedad!"
                "No derrotando monstruos interdimensionales, pero si colaborando con nuestras comunidades!"
                "FIN"
                return


    
    
        

