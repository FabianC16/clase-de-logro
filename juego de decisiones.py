print("Estás atrapado en una zona de cuarentena abandonada.")
print("Puedes entrar a una TIENDA saqueada")
print("subir una ESCALERA o")
print("cruzar un TÚNEL oscuro, que haces?")
eleccion1 = input("¿Qué haces? (TIENDA, ESCALERA o TÚNEL): ").strip().lower()

if eleccion1 == "tienda":
    print("\nDentro de la tienda hay una MOCHILA en el suelo y una PUERTA trasera abierta.")
    eleccion2 = input("¿Revisas la MOCHILA o cruzas la PUERTA?: ").strip().lower()

    if eleccion2 == "mochila":
        print("\nEncuentras una PISTOLA, una NAVAJA y un BOTIQUÍN.")
        eleccion3 = input("¿Qué tomas? (PISTOLA, NAVAJA, BOTIQUÍN): ").strip().lower()
        if eleccion3 == "pistola":
            print("¡Sobreviviste! Derribas a un infectado justo a tiempo.")
        elif eleccion3 == "navaja":
            print("No fue suficiente. Un clicker te ataca. Fin del juego.")
        elif eleccion3 == "botiquín":
            print("Te curas, pero quedas indefenso. Un infectado te atrapa. Fin del juego.")
        else:
            print("Opción no válida. Elige PISTOLA, NAVAJA o BOTIQUÍN.")

    elif eleccion2 == "puerta":
        print("\nHaces ruido al cruzar. Dos chasqueadores te detectan.")
        eleccion3 = input("¿Quieres ESCONDERTE o CORRER?: ").strip().lower()
        if eleccion3 == "esconderte":
            print("Te ocultas tras unos estantes. Los chasqueadores pasan de largo. ¡Sobreviviste!")
        elif eleccion3 == "correr":
            print("Uno te alcanza antes de escapar. Fin del juego.")
        else:
            print("Opción no válida. Elige ESCONDERTE o CORRER.")
    else:
        print("Opción no válida. Escribe MOCHILA o PUERTA.")

elif eleccion1 == "escalera":
    print("\nDesde el techo ves un REFUGIO y una FOGATA encendida.")
    eleccion2 = input("¿Te acercas al REFUGIO o a la FOGATA?: ").strip().lower()
    if eleccion2 == "refugio":
        print("El refugio está vacío pero seguro. ¡Sobreviviste!")
    elif eleccion2 == "fogata":
        print("Es una trampa. Saqueadores te capturan. Fin del juego.")
    else:
        print("Opción no válida. Elige REFUGIO o FOGATA.")

elif eleccion1 == "túnel" or eleccion1 == "tunel":
    print("\nAvanzas por el túnel. Puedes ENCENDER tu linterna o IR en silencio.")
    eleccion2 = input("¿Qué haces? (ENCENDER o IR): ").strip().lower()
    if eleccion2 == "encender":
        print("Revelas a un grupo de infectados. Te atacan. Fin del juego.")
    elif eleccion2 == "ir":
        print("Te mueves con sigilo y escapas del túnel. ¡Sobreviviste!")
    else:
        print("Opción no válida. Escribe ENCENDER o IR.")

else:
    print("Opción no válida. Elige TIENDA, ESCALERA o TÚNEL.")
