import tkinter as tk  # Importa el módulo tkinter para crear la interfaz gráfica

# Define la clase DraggableNode para crear y mover nodos en un canvas
class DraggableNode:
    def __init__(self, canvas, x, y, text):
        self.canvas = canvas  # Guarda una referencia al canvas
        # Crea un óvalo en el canvas y guarda su ID
        self.id = self.canvas.create_rectangle(x - 50, y - 20, x + 50, y + 20, fill="blue")
        # Crea un texto en el canvas y guarda su ID
        self.text_id = self.canvas.create_text(x, y, text=text, fill="white")
        # Vincula eventos del mouse para el óvalo
        self.canvas.tag_bind(self.id, "<Button-1>", self.on_click)
        self.canvas.tag_bind(self.id, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.id, "<Double-Button-1>", self.on_double_click)
        self.canvas.tag_bind(self.id, "<Button-3>", self.select_node)  # Botón derecho del mouse para seleccionar el nodo
        # Vincula eventos del mouse para el texto
        self.canvas.tag_bind(self.text_id, "<Button-1>", self.on_click)
        self.canvas.tag_bind(self.text_id, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.text_id, "<Double-Button-1>", self.on_double_click)
        self.canvas.tag_bind(self.text_id, "<Button-3>", self.select_node)  # Botón derecho del mouse para seleccionar el nodo
        self.entry = None  # Inicializa la variable para el Entry widget
        self.selected = False  # Indica si el nodo está seleccionado
        self.resize_handle = None  # ID del manejador de redimensionamiento

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
        # Mueve el manejador de redimensionamiento si está presente
        if self.resize_handle:
            self.canvas.move(self.resize_handle, dx, dy)
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
        self.canvas.itemconfig(self.text_id, text=self.wrap_text(new_text))  # Actualiza el texto del nodo
        self.entry.destroy()  # Elimina el Entry widget
        self.entry = None  # Restablece la variable Entry a None
        # Ajusta el tamaño del óvalo según la longitud del texto
        self.adjust_oval_size(new_text)

    def wrap_text(self, text):
        # Divide el texto en líneas si una línea tiene más de 10 caracteres
        words = text.split(' ')
        lines = []
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 1 > 10:
                lines.append(current_line)
                current_line = word
            else:
                if current_line:
                    current_line += ' '
                current_line += word
        lines.append(current_line)
        return '\n'.join(lines)

    def adjust_oval_size(self, text):
        x, y = self.canvas.coords(self.text_id)  # Obtiene la posición del texto
        lines = text.split('\n')
        max_width = max(len(line) for line in lines) * 10  # Calcula el ancho del texto (ajusta el multiplicador según el tamaño del texto)
        height = len(lines) * 20  # Calcula la altura del texto
        # Ajusta el tamaño del óvalo según la longitud del texto
        self.canvas.coords(self.id, x - max_width/2 - 10, y - height/2 - 10, x + max_width/2 + 10, y + height/2 + 10)
        # Reposiciona el texto en el centro del óvalo
        self.canvas.coords(self.text_id, x, y)

    def select_node(self, event):
        if not self.selected:
            self.selected = True
            x0, y0, x1, y1 = self.canvas.coords(self.id)
            # Crea un manejador de redimensionamiento en la esquina inferior derecha del óvalo
            self.resize_handle = self.canvas.create_rectangle(x1-10, y1-10, x1+10, y1+10, outline="black", fill="white")
            self.canvas.tag_bind(self.resize_handle, "<B1-Motion>", self.resize_node)
        else:
            self.deselect_node()

    def deselect_node(self):
        if self.selected:
            self.selected = False
            if self.resize_handle:
                self.canvas.delete(self.resize_handle)
                self.resize_handle = None

    def resize_node(self, event):
        x0, y0, x1, y1 = self.canvas.coords(self.id)
        new_width = event.x - x0
        new_height = event.y - y0
        # Ajusta el tamaño del óvalo según el nuevo tamaño
        self.canvas.coords(self.id, x0, y0, x0 + new_width, y0 + new_height)
        # Reposiciona el manejador de redimensionamiento
        self.canvas.coords(self.resize_handle, x0 + new_width - 10, y0 + new_height - 10, x0 + new_width + 10, y0 + new_height + 10)
        # Ajusta el texto al nuevo tamaño del óvalo
        self.adjust_oval_size(self.canvas.itemcget(self.text_id, "text"))

# Función para crear un nuevo nodo en la posición donde se hizo clic en el canvas
def create_node(event):
    x, y = event.x, event.y
    DraggableNode(event.widget, x, y, "Nuevo Nodo")

# Función principal para crear la interfaz gráfica
def main():
    root = tk.Tk()  # Crea la ventana principal de Tkinter
    root.title("Nodo Movible en Canvas")  # Establece el título de la ventana
    canvas = tk.Canvas(root, width=800, height=600, bg="white")  # Crea un widget Canvas de 800x600 píxeles
    canvas.pack()  # Empaca el canvas en la ventana

    # Vincula el evento de clic del mouse en el canvas para crear un nuevo nodo
    canvas.bind("<Button-3>", create_node)  # Usa el botón derecho del mouse para crear nuevos nodos

    center_x, center_y = 400, 300  # Coordenadas del centro del canvas
    node = DraggableNode(canvas, center_x, center_y, "Nodo Central")  # Crea un nodo en el centro del canvas

    root.mainloop()  # Inicia el bucle principal de Tkinter

if __name__ == "__main__":
    main()  # Ejecuta la función principal si este archivo se ejecuta como script

