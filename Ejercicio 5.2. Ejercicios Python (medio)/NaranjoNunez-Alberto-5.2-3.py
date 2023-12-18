# 3A Escribir una función a la que se le pase una cadena <nombre> y 
# muestre por pantalla el saludo ¡hola <nombre>!., siendo <nombre> tu nombre obtenido del teclado.
def heyName(name):
    print("Hola {name}!".format(name=name))

def main():
    heyName(input("¿Cuál es su nombre?\n"))

if __name__ == '__main__':
    main()