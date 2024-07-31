import tkinter as tk  # Importa el módulo tkinter para crear la interfaz gráfica

class DraggableNode:
    def __init__(self, canvas, x, y, text):
        self.canvas = canvas  # Guarda una referencia al canvas
        # Crea un óvalo en el canvas y guarda su ID
        self.id = self.canvas.create_oval(x - 50, y - 20, x + 50, y + 20, fill="blue")
        # Crea un texto en el canvas y guarda su ID
        self.text_id = self.canvas.create_text(x, y, text=text, fill="white")
        # Vincula eventos del mouse para el óvalo
        self.canvas.tag_bind(self.id, "<Button-1>", self.on_click)
        self.canvas.tag_bind(self.id, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.id, "<Double-Button-1>", self.on_double_click)
        # Vincula eventos del mouse para el texto
        self.canvas.tag_bind(self.text_id, "<Button-1>", self.on_click)
        self.canvas.tag_bind(self.text_id, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.text_id, "<Double-Button-1>", self.on_double_click)
        self.entry = None  # Inicializa la variable para el Entry widget

    def on_click(self, event):
        self.start_x = event.x  # Guarda la posición x inicial del clic
        self.start_y = event.y  # Guarda la posición y inicial del clic

    def on_drag(self, event):
        # Calcula el desplazamiento en x e y
        dx = event.x - self.start_x
        dy = event.y - self.start_y
        # Mueve el óvalo y el texto en el canvas
        self.canvas.move(self.id, dx, dy)
        self.canvas.move(self.text_id, dx, dy)
        # Actualiza las posiciones iniciales para el siguiente movimiento
        self.start_x = event.x
        self.start_y = event.y

    def on_double_click(self, event):
        if self.entry:
            return  # Si ya hay un Entry widget, no hace nada

        # Obtiene la posición del texto
        x, y = self.canvas.coords(self.text_id)
        # Crea un Entry widget en esa posición
        self.entry = tk.Entry(self.canvas)
        self.entry.place(x=x - 20, y=y - 10)
        # Establece el texto actual en el Entry
        self.entry.insert(0, self.canvas.itemcget(self.text_id, "text"))
        self.entry.focus_set()
        # Vincula la tecla Enter y la pérdida de foco para guardar el texto
        self.entry.bind("<Return>", self.save_text)
        self.entry.bind("<FocusOut>", self.save_text)

    def save_text(self, event):
        new_text = self.entry.get()  # Obtiene el nuevo texto del Entry
        self.canvas.itemconfig(self.text_id, text=new_text)  # Actualiza el texto del nodo
        self.entry.destroy()  # Elimina el Entry widget
        self.entry = None  # Restablece la variable Entry a None
        # Ajusta el tamaño del óvalo según la longitud del texto
        self.adjust_oval_size(new_text)

    def adjust_oval_size(self, text):
        x, y = self.canvas.coords(self.text_id)  # Obtiene la posición del texto
        text_width = 10 * len(text)  # Calcula el ancho del texto (puedes ajustar el multiplicador según el tamaño del texto)
        # Ajusta el tamaño del óvalo según la longitud del texto
        self.canvas.coords(self.id, x - text_width/2 - 10, y - 20, x + text_width/2 + 10, y + 20)

def main():
    root = tk.Tk()  # Crea la ventana principal de Tkinter
    root.title("Nodo Movible en Canvas")  # Establece el título de la ventana
    canvas = tk.Canvas(root, width=800, height=600, bg="white")  # Crea un widget Canvas de 800x600 píxeles
    canvas.pack()  # Empaca el canvas en la ventana

    center_x, center_y = 400, 300  # Coordenadas del centro del canvas
    node = DraggableNode(canvas, center_x, center_y, "Nodo Central")  # Crea un nodo en el centro del canvas

    root.mainloop()  # Inicia el bucle principal de Tkinter

if __name__ == "__main__":
    main()  # Ejecuta la función principal si este archivo se ejecuta como script
