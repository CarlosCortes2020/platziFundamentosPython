import tkinter as tk  # Importa el módulo Tkinter para la creación de interfaces gráficas

def draw_grid(canvas, width, height, interval):
    # Función para dibujar un grid en el canvas
    # canvas: el widget de canvas donde se dibuja el grid
    # width: el ancho del canvas
    # height: la altura del canvas
    # interval: la distancia entre las líneas del grid

    for i in range(0, width, interval):
        # Dibuja líneas verticales
        # (i, 0) es el punto de inicio y (i, height) es el punto final de la línea vertical
        canvas.create_line([(i, 0), (i, height)], tag='grid_line')
    
    for i in range(0, height, interval):
        # Dibuja líneas horizontales
        # (0, i) es el punto de inicio y (width, i) es el punto final de la línea horizontal
        canvas.create_line([(0, i), (width, i)], tag='grid_line')

# Configuración de la ventana principal
root = tk.Tk()  # Crea una ventana principal
root.title("Grid en Canvas")  # Establece el título de la ventana

# Configuración del canvas
canvas_width = 500  # Ancho del canvas
canvas_height = 500  # Altura del canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')  # Crea un widget de canvas
canvas.pack()  # Empaqueta el canvas en la ventana principal

# Dibujar el grid
grid_interval = 50  # Espaciado entre líneas del grid
draw_grid(canvas, canvas_width, canvas_height, grid_interval)  # Llama a la función para dibujar el grid

# Ejecutar la aplicación
root.mainloop()  # Inicia el bucle principal de la aplicación
