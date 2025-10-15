import tkinter as tk
from tkinter import messagebox
import turtle
import time

def dibujar_frente():
    """Dibuja la parte frontal de la floristería"""
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("skyblue")  # Fondo azul cielo
    screen.title("Parte Frontal - Flowers")
    
    t = turtle.Turtle()
    t.speed(5)
    
    # Dibujar el suelo
    t.penup()
    t.goto(-400, -150)
    t.pendown()
    t.color("green")
    t.begin_fill()
    for _ in range(2):
        t.forward(800)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()
    
    # Dibujar edificio - ROSADO PASTEL
    t.penup()
    t.goto(-200, -150)
    t.pendown()
    t.color("#FFD1DC")  # Rosado pastel claro
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.left(90)
        t.forward(300)
        t.left(90)
    t.end_fill()
    
    # Dibujar techo azul oscuro
    t.penup()
    t.goto(-220, 150)
    t.pendown()
    t.color("#1E3F66")  # Azul oscuro
    t.begin_fill()
    t.goto(0, 250)
    t.goto(220, 150)
    t.goto(-220, 150)
    t.end_fill()
    
    # Dibujar ventana derecha - AZUL MEDIO OSCURO
    t.penup()
    t.goto(60, 0)
    t.pendown()
    t.color("#2E5090")  # Azul medio oscuro
    t.begin_fill()
    for _ in range(2):
        t.forward(60)
        t.left(90)
        t.forward(40)
        t.left(90)
    t.end_fill()
    
    # Dibujar puerta izquierda - AZUL MEDIO OSCURO
    t.penup()
    t.goto(-120, -150)
    t.pendown()
    t.color("#2E5090")  # Azul medio oscuro
    t.begin_fill()
    for _ in range(2):
        t.forward(60)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()
    
    # Plantas colgantes superiores (2 en esquinas)
    for x in [-180, 180]:
        t.penup()
        t.goto(x, 140)
        t.pendown()
        t.color("green")
        # Maceta colgante
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        # Plantas que cuelgan
        t.penup()
        t.goto(x, 125)
        t.pendown()
        t.color("darkgreen")
        for angle in [300, 270, 240]:
            t.setheading(angle)
            t.forward(25)
            t.backward(25)
    
    # Arbustos inferiores laterales
    for x in [-350, 350]:
        t.penup()
        t.goto(x, -130)
        t.pendown()
        t.color("darkgreen")
        t.begin_fill()
        t.circle(25)
        t.end_fill()
    
    t.hideturtle()
    screen.exitonclick()

def dibujar_lateral_derecho():
    """Dibuja la parte lateral derecha de la floristería"""
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("skyblue")  # Fondo azul cielo
    screen.title("Parte Lateral Derecha - Flowers")
    
    t = turtle.Turtle()
    t.speed(5)
    
    # Dibujar el suelo
    t.penup()
    t.goto(-400, -150)
    t.pendown()
    t.color("green")
    t.begin_fill()
    for _ in range(2):
        t.forward(800)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()
    
    # Dibujar edificio lateral - ROSADO PASTEL
    t.penup()
    t.goto(-150, -150)
    t.pendown()
    t.color("#FFD1DC")  # Rosado pastel claro
    t.begin_fill()
    for _ in range(2):
        t.forward(300)
        t.left(90)
        t.forward(200)
        t.left(90)
    t.end_fill()
    
    # Dibujar techo azul oscuro
    t.penup()
    t.goto(-170, 50)
    t.pendown()
    t.color("#1E3F66")  # Azul oscuro
    t.begin_fill()
    t.goto(0, 120)
    t.goto(170, 50)
    t.goto(-170, 50)
    t.end_fill()
    
    # Flor en el centro A NIVEL DEL SUELO
    t.penup()
    t.goto(0, -150)
    t.pendown()
    # Tallo
    t.color("green")
    t.setheading(90)
    t.forward(60)
    # Pétalos
    t.penup()
    t.goto(0, -90)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    # Centro de la flor
    t.penup()
    t.goto(0, -90)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    
    # Plantas colgantes superiores (2 en esquinas)
    for x in [-130, 130]:
        t.penup()
        t.goto(x, 40)
        t.pendown()
        t.color("green")
        # Maceta colgante
        t.begin_fill()
        t.circle(12)
        t.end_fill()
        # Plantas que cuelgan
        t.penup()
        t.goto(x, 28)
        t.pendown()
        t.color("darkgreen")
        for angle in [300, 270, 240]:
            t.setheading(angle)
            t.forward(20)
            t.backward(20)
    
    # Arbustos inferiores laterales
    for x in [-350, 350]:
        t.penup()
        t.goto(x, -130)
        t.pendown()
        t.color("darkgreen")
        t.begin_fill()
        t.circle(25)
        t.end_fill()
    
    t.hideturtle()
    screen.exitonclick()

def dibujar_lateral_izquierdo():
    """Dibuja la parte lateral izquierda de la floristería"""
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("skyblue")  # Fondo azul cielo
    screen.title("Parte Lateral Izquierda - Flowers")
    
    t = turtle.Turtle()
    t.speed(5)
    
    # Dibujar el suelo
    t.penup()
    t.goto(-400, -150)
    t.pendown()
    t.color("green")
    t.begin_fill()
    for _ in range(2):
        t.forward(800)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()
    
    # Dibujar edificio lateral - ROSADO PASTEL
    t.penup()
    t.goto(-150, -150)
    t.pendown()
    t.color("#FFD1DC")  # Rosado pastel claro
    t.begin_fill()
    for _ in range(2):
        t.forward(300)
        t.left(90)
        t.forward(200)
        t.left(90)
    t.end_fill()
    
    # Dibujar techo azul oscuro
    t.penup()
    t.goto(-170, 50)
    t.pendown()
    t.color("#1E3F66")  # Azul oscuro
    t.begin_fill()
    t.goto(0, 120)
    t.goto(170, 50)
    t.goto(-170, 50)
    t.end_fill()
    
    # Flor en el centro A NIVEL DEL SUELO
    t.penup()
    t.goto(0, -150)
    t.pendown()
    # Tallo
    t.color("green")
    t.setheading(90)
    t.forward(60)
    # Pétalos
    t.penup()
    t.goto(0, -90)
    t.pendown()
    t.color("pink")
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    # Centro de la flor
    t.penup()
    t.goto(0, -90)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    
    # Plantas colgantes superiores (2 en esquinas)
    for x in [-130, 130]:
        t.penup()
        t.goto(x, 40)
        t.pendown()
        t.color("green")
        # Maceta colgante
        t.begin_fill()
        t.circle(12)
        t.end_fill()
        # Plantas que cuelgan
        t.penup()
        t.goto(x, 28)
        t.pendown()
        t.color("darkgreen")
        for angle in [300, 270, 240]:
            t.setheading(angle)
            t.forward(20)
            t.backward(20)
    
    # Arbustos inferiores laterales
    for x in [-350, 350]:
        t.penup()
        t.goto(x, -130)
        t.pendown()
        t.color("darkgreen")
        t.begin_fill()
        t.circle(25)
        t.end_fill()
    
    t.hideturtle()
    screen.exitonclick()

def dibujar_trasera():
    """Dibuja la parte trasera de la floristería"""
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("skyblue")  # Fondo azul cielo
    screen.title("Parte Trasera - Flowers")
    
    t = turtle.Turtle()
    t.speed(5)
    
    # Dibujar el suelo
    t.penup()
    t.goto(-400, -150)
    t.pendown()
    t.color("darkgreen")
    t.begin_fill()
    for _ in range(2):
        t.forward(800)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()
    
    # Dibujar edificio trasero - ROSADO PASTEL
    t.penup()
    t.goto(-200, -150)
    t.pendown()
    t.color("#FFD1DC")  # Rosado pastel claro
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.left(90)
        t.forward(250)
        t.left(90)
    t.end_fill()
    
    # Dibujar techo azul oscuro
    t.penup()
    t.goto(-220, 100)
    t.pendown()
    t.color("#1E3F66")  # Azul oscuro
    t.begin_fill()
    t.goto(0, 180)
    t.goto(220, 100)
    t.goto(-220, 100)
    t.end_fill()
    
    # Soporte central para plantas
    t.penup()
    t.goto(-80, -150)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(160)
        t.left(90)
        t.forward(20)
        t.left(90)
    t.end_fill()
    
    # Postes del soporte
    for x in [-70, 70]:
        t.penup()
        t.goto(x, -130)
        t.pendown()
        t.color("brown")
        t.begin_fill()
        for _ in range(2):
            t.forward(20)
            t.left(90)
            t.forward(80)
            t.left(90)
        t.end_fill()
    
    # Tabla superior del soporte
    t.penup()
    t.goto(-80, -50)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(160)
        t.left(90)
        t.forward(15)
        t.left(90)
    t.end_fill()
    
    # Plantas en el soporte (2 a cada lado)
    for x in [-40, 40]:
        # Planta izquierda del soporte
        t.penup()
        t.goto(x-25, -40)
        t.pendown()
        t.color("green")
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        
        # Planta derecha del soporte
        t.penup()
        t.goto(x+25, -40)
        t.pendown()
        t.color("green")
        t.begin_fill()
        t.circle(15)
        t.end_fill()
    
    # Plantas colgantes superiores (2 en esquinas)
    for x in [-180, 180]:
        t.penup()
        t.goto(x, 90)
        t.pendown()
        t.color("green")
        # Maceta colgante
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        # Plantas que cuelgan
        t.penup()
        t.goto(x, 75)
        t.pendown()
        t.color("darkgreen")
        for angle in [300, 270, 240]:
            t.setheading(angle)
            t.forward(25)
            t.backward(25)
    
    # Arbustos inferiores laterales
    for x in [-350, 350]:
        t.penup()
        t.goto(x, -130)
        t.pendown()
        t.color("darkgreen")
        t.begin_fill()
        t.circle(25)
        t.end_fill()
    
    t.hideturtle()
    screen.exitonclick()

def descripcion_floristeria(opcion):
    """Función que devuelve la descripción según la opción seleccionada"""
    
    descripciones = {
        1: """🌺 PARTE FRONTAL DE LA FLORISTERÍA 🌺

• Color de fachada: ROSADO PASTEL CLARO
• Techo: Azul oscuro
• Ventana derecha: Azul medio oscuro
• Puerta izquierda: Azul medio oscuro
• Plantas colgantes: 2 en esquinas superiores
• Arbustos: 2 en laterales inferiores
• Fondo: Cielo azul""",
        
        2: """🌼 PARTE LATERAL DERECHA 🌼

• Color de fachada: ROSADO PASTEL CLARO
• Techo: Azul oscuro
• Decoración: Flor amarilla a nivel del suelo
• Plantas colgantes: 2 en esquinas superiores
• Arbustos: 2 en laterales inferiores
• Fondo: Cielo azul""",
        
        3: """🌷 PARTE LATERAL IZQUIERDA 🌷

• Color de fachada: ROSADO PASTEL CLARO
• Techo: Azul oscuro
• Decoración: Flor rosa a nivel del suelo
• Plantas colgantes: 2 en esquinas superiores
• Arbustos: 2 en laterales inferiores
• Fondo: Cielo azul""",
        
        4: """🌿 PARTE TRASERA DE LA FLORISTERÍA 🌿

• Color de fachada: ROSADO PASTEL CLARO
• Techo: Azul oscuro
• Soporte central: Estructura de madera para plantas
• Plantas en soporte: 4 plantas (2 a cada lado)
• Plantas colgantes: 2 en esquinas superiores
• Arbustos: 2 en laterales inferiores
• Fondo: Cielo azul"""
    }
    
    return descripciones.get(opcion, "Opción no válida")

def mostrar_descripcion():
    """Función para mostrar la descripción y el dibujo"""
    try:
        opcion = int(entry.get())
        if 1 <= opcion <= 4:
            # Mostrar descripción
            descripcion = descripcion_floristeria(opcion)
            messagebox.showinfo("Descripción de la Floristería", descripcion)
            
            # Mostrar dibujo correspondiente
            if opcion == 1:
                dibujar_frente()
            elif opcion == 2:
                dibujar_lateral_derecho()
            elif opcion == 3:
                dibujar_lateral_izquierdo()
            elif opcion == 4:
                dibujar_trasera()
                
        else:
            messagebox.showerror("Error", "❌ Por favor, ingresa un número entre 1 y 4")
    except ValueError:
        messagebox.showerror("Error", "❌ Por favor, ingresa un número válido (1, 2, 3 o 4)")

def limpiar_entrada():
    """Función para limpiar el campo de entrada"""
    entry.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Flowers - Descripción Externa con Dibujos")
root.geometry("500x500")
root.configure(bg='#e6f2ff')  # Azul cielo claro para la interfaz principal
root.resizable(False, False)

# Título
titulo = tk.Label(root, 
                 text="🌸 Flowers 🌸", 
                 font=("Arial", 18, "bold"),
                 bg='#e6f2ff',
                 fg='#d94d8c')  # Rosado para el título
titulo.pack(pady=20)

# Instrucciones
instrucciones = tk.Label(root,
                        text="Selecciona qué parte deseas conocer:\n\n"
                             "1. 🏠 Parte Frontal (Ventana + Puerta)\n"
                             "2. ➡️ Parte Lateral Derecha (Flor en suelo)\n" 
                             "3. ⬅️ Parte Lateral Izquierda (Flor en suelo)\n"
                             "4. 🏢 Parte Trasera (Soporte para plantas)\n\n"
                             "Se mostrará descripción + dibujo en Turtle",
                        font=("Arial", 11),
                        bg='#e6f2ff',
                        fg='#333333',
                        justify='left')
instrucciones.pack(pady=10)

# Campo de entrada
frame_entrada = tk.Frame(root, bg='#e6f2ff')
frame_entrada.pack(pady=20)

label_entrada = tk.Label(frame_entrada, 
                        text="Ingresa el número (1-4):",
                        font=("Arial", 10, "bold"),
                        bg='#e6f2ff',
                        fg='#d94d8c')
label_entrada.pack()

entry = tk.Entry(frame_entrada, 
                font=("Arial", 14),
                width=15,
                justify='center',
                bg='#ffffff',
                fg='#d94d8c',
                relief='solid',
                bd=2)
entry.pack(pady=10)

# Configurar la tecla Enter
entry.bind('<Return>', lambda event: mostrar_descripcion())

# Frame para botones
frame_botones = tk.Frame(root, bg='#e6f2ff')
frame_botones.pack(pady=15)

# Botón para mostrar descripción
boton_ver = tk.Button(frame_botones,
                     text="🔍 Ver Descripción + Dibujo",
                     command=mostrar_descripcion,
                     font=("Arial", 12, "bold"),
                     bg='#d94d8c',  # Rosado para botones
                     fg='white',
                     padx=20,
                     pady=8,
                     relief='raised',
                     bd=3)
boton_ver.grid(row=0, column=0, padx=10)

# Botón para limpiar
boton_limpiar = tk.Button(frame_botones,
                         text="🧹 Limpiar",
                         command=limpiar_entrada,
                         font=("Arial", 12, "bold"),
                         bg='#87CEEB',  # Azul cielo para contraste
                         fg='white',
                         padx=20,
                         pady=8,
                         relief='raised',
                         bd=3)
boton_limpiar.grid(row=0, column=1, padx=10)

# Instrucción adicional
instruccion_extra = tk.Label(root,
                            text="💡 Presiona Enter o el botón para ver descripción + dibujo Turtle",
                            font=("Arial", 9, "italic"),
                            bg='#e6f2ff',
                            fg='#666666')
instruccion_extra.pack(pady=10)

# Información sobre Turtle
info_turtle = tk.Label(root,
                      text="🎨 Los dibujos se abrirán en ventanas de Turtle con fondo azul cielo",
                      font=("Arial", 9),
                      bg='#e6f2ff',
                      fg='#d94d8c')
info_turtle.pack(pady=5)

# Información sobre características
info_caracteristicas = tk.Label(root,
                               text="🌸 Laterales: Flores en suelo | 🏗️ Trasera: Soporte para plantas",
                               font=("Arial", 8, "bold"),
                               bg='#e6f2ff',
                               fg='#d94d8c')
info_caracteristicas.pack(pady=5)

# Pie de página
pie = tk.Label(root,
              text="¡Haz clic en los dibujos de Turtle para cerrarlos! 🐢",
              font=("Arial", 10, "italic"),
              bg='#e6f2ff',
              fg='#d94d8c')
pie.pack(side='bottom', pady=15)

# Hacer que la ventana aparezca en el centro de la pantalla
root.eval('tk::PlaceWindow . center')

# Poner el foco en el campo de entrada
entry.focus()

# Ejecutar la aplicación
root.mainloop()