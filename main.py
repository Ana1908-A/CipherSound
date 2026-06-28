import random
import string

def generar_contrasena(longitud, numeros, mayusculas, simbolos):
    caracteres = string.ascii_lowercase

    if numeros:
        caracteres += string.digits

    if mayusculas:
        caracteres += string.ascii_uppercase

    if simbolos:
        caracteres += "!@#$%&*?"

    contrasena = ""

    for i in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena


def evaluar_seguridad(contrasena):
    puntos = 0

    if len(contrasena) >= 8:
        puntos += 1

    if any(c.isdigit() for c in contrasena):
        puntos += 1

    if any(c.isupper() for c in contrasena):
        puntos += 1

    if any(c in "!@#$%&*?" for c in contrasena):
        puntos += 1

    if puntos >= 3:
        return "FUERTE"
    else:
        return "DÉBIL"


def activar_sonido(resultado):
    print("\a")

    if resultado == "FUERTE":
        print("🔊 Sonido de éxito activado")
    else:
        print("⚠️ Sonido de advertencia activado")


def mostrar_presentacion():
    print("=" * 60)
    print("🔐 CIPHERSOUND")
    print("GENERADOR DE CONTRASEÑAS SEGURAS CON SONIDO")
    print("=" * 60)
    print()
    print("Este sistema permite generar una contraseña segura")
    print("según las opciones seleccionadas por el usuario.")
    print("Además, evalúa el nivel de seguridad y activa")
    print("una alerta sonora o visual según el resultado.")
    print()
    print("Opciones disponibles:")
    print("- Longitud de la contraseña")
    print("- Inclusión de números")
    print("- Inclusión de letras mayúsculas")
    print("- Inclusión de símbolos")
    print("- Evaluación de seguridad")
    print("- Alerta de sonido")
    print("-" * 60)


def ejecutar_programa():
    mostrar_presentacion()

    repetir = "s"

    while repetir == "s":
        try:
            longitud = int(input("\nIngrese la longitud de la contraseña: "))

            if longitud <= 0:
                print("La longitud debe ser un número mayor que cero.")
                continue

            numeros = input("¿Incluir números? (s/n): ").lower() == "s"
            mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == "s"
            simbolos = input("¿Incluir símbolos? (s/n): ").lower() == "s"

            contrasena = generar_contrasena(
                longitud,
                numeros,
                mayusculas,
                simbolos
            )

            resultado = evaluar_seguridad(contrasena)

            print()
            print("=" * 60)
            print("RESULTADO DEL SISTEMA")
            print("=" * 60)
            print("Contraseña generada:")
            print(contrasena)
            print()
            print("Nivel de seguridad:")
            print(resultado)
            print()

            activar_sonido(resultado)

            print("=" * 60)

            repetir = input("\n¿Quieres generar otra contraseña? (s/n): ").lower()

        except ValueError:
            print("Error: debe ingresar un número válido para la longitud.")

    print()
    print("=" * 60)
    print("Gracias por usar CipherSound.")
    print("Programa finalizado.")
    print("=" * 60)


ejecutar_programa()
