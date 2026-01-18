def mostrar_menu():
    """Función que muestra las opciones del menú"""
    print("\n" + "="*40)
    print("           MENÚ PRINCIPAL")
    print("="*40)
    print("1. Calculadora básica")
    print("2. Lista de tareas")
    print("3. Información del usuario")
    print("4. Juego de adivinanza")
    print("5. Salir")
    print("="*40)

def calculadora():
    """Función para realizar operaciones básicas"""
    print("\n--- CALCULADORA ---")
    try:
        num1 = float(input("Ingresa el primer número: "))
        operador = input("Ingresa el operador (+, -, *, /): ")
        num2 = float(input("Ingresa el segundo número: "))
        
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Error: No se puede dividir entre cero")
                return
        else:
            print("Operador no válido")
            return
        
        print(f"Resultado: {num1} {operador} {num2} = {resultado}")
    except ValueError:
        print("Error: Ingresa números válidos")

def lista_tareas():
    """Función para manejar una lista de tareas"""
    tareas = []
    
    while True:
        print("\n--- LISTA DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Volver al menú principal")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            tarea = input("Ingresa la nueva tarea: ")
            tareas.append({"tarea": tarea, "completada": False})
            print("Tarea agregada exitosamente!")
            
        elif opcion == '2':
            if tareas:
                print("\nTus tareas:")
                for i, tarea in enumerate(tareas, 1):
                    estado = "✓" if tarea["completada"] else "✗"
                    print(f"{i}. [{estado}] {tarea['tarea']}")
            else:
                print("No tienes tareas pendientes")
                
        elif opcion == '3':
            if tareas:
                print("\nTareas disponibles:")
                for i, tarea in enumerate(tareas, 1):
                    if not tarea["completada"]:
                        print(f"{i}. {tarea['tarea']}")
                
                try:
                    indice = int(input("Número de tarea a completar: ")) - 1
                    if 0 <= indice < len(tareas):
                        tareas[indice]["completada"] = True
                        print("¡Tarea marcada como completada!")
                    else:
                        print("Número de tarea inválido")
                except ValueError:
                    print("Ingresa un número válido")
            else:
                print("No tienes tareas para completar")
                
        elif opcion == '4':
            break
        else:
            print("Opción no válida")

def info_usuario():
    """Función para recopilar y mostrar información del usuario"""
    print("\n--- INFORMACIÓN DEL USUARIO ---")
    nombre = input("¿Cuál es tu nombre? ")
    edad = input("¿Cuál es tu edad? ")
    ciudad = input("¿En qué ciudad vives? ")
    
    print(f"\nHola {nombre}!")
    print(f"Tienes {edad} años y vives en {ciudad}")
    print("¡Gracias por compartir tu información!")

def juego_adivinanza():
    """Juego simple de adivinar un número"""
    import random
    
    print("\n--- JUEGO DE ADIVINANZA ---")
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 7
    
    print("He pensado en un número entre 1 y 100")
    print(f"Tienes {max_intentos} intentos para adivinarlo")
    
    while intentos < max_intentos:
        try:
            intento = int(input(f"\nIntento {intentos + 1}: "))
            intentos += 1
            
            if intento == numero_secreto:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos")
                return
            elif intento < numero_secreto:
                print("El número es mayor")
            else:
                print("El número es menor")
                
        except ValueError:
            print("Por favor, ingresa un número válido")
            intentos -= 1  # No contar intentos inválidos
    
    print(f"\nSe acabaron los intentos. El número era {numero_secreto}")

def main():
    """Función principal que controla el menú"""
    print("¡Bienvenido al programa!")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (1-5): ")
            
            if opcion == '1':
                calculadora()
            elif opcion == '2':
                lista_tareas()
            elif opcion == '3':
                info_usuario()
            elif opcion == '4':
                juego_adivinanza()
            elif opcion == '5':
                print("\n¡Gracias por usar el programa!")
                print("¡Hasta luego!")
                break
            else:
                print("\n❌ Opción no válida. Por favor selecciona una opción del 1 al 5.")
                
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario!")
            print("¡Hasta luego!")
            break

# Ejecutar el programa
if __name__ == "__main__":
    main()