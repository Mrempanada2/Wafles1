#Personajes
#cap1


image yo Bien = "personajes/yoBien.png"
image yo Magnate = "personajes/yoMagnate.png"
image yo Neutro = "personajes/yoNeutro.png"
image yo Ok = "personajes/yoOk.png"
image yo Susto="personajes/yoSusto.png"
image asaltante = "personajes/asaltante.png"
image doc misterioso = "personajes/docMisterio.png"
image doc MUYsorprendido="personajes/docMuySorprendido.png"
image doc Neutro="personajes/docNeutro.png"
image doc Happy="personajes/docHappy.png"
image doc WTF="personajes/docWTF.png"
image monstruo uno="personajes/monstruo1.png"
image monstruo dos="personajes/monstruo2.png"
image monstruo tres="personajes/monstruo3.png"



define yo = Character("Yo", color="FFA500", who_bold=True)
define docn="???"
define doc = Character("[docn]", color="09e5ff", dynamic=True)
define asaltante = Character("asaltante", color="fcf43e")
define CriaturaCorrupta = Character("[CriaturaCorruptaN]", color="e70101", dynamic=True)
define Boss=Character("Boss", color="ff003e")
#define mute=False

init python:
    def hablar(personaje, foto, texto,mute=False):
        renpy.show(foto, at_list=[left])
        if not mute:
            if personaje == yo:
                renpy.play("audio/vozYo.ogg", channel="sound")
            elif personaje == doc:
                renpy.play("audio/vozDoc.ogg", channel="sound")
            elif personaje == CriaturaCorrupta:
                renpy.play("audio/vozMalvada.ogg", channel="sound")
            else:
                renpy.play("audio/vozNPC.ogg", channel="sound")
        renpy.say(personaje, texto)
        renpy.hide(foto)








