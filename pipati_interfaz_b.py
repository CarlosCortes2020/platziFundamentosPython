import tkinter as tk  # Importa la biblioteca tkinter para la interfaz gráfica

class RockPaperScissors:
    def __init__(self, root):
        # Inicializa la ventana principal
        self.root = root
        self.root.title("Piedra, Papel, Tijera")  # Establece el título de la ventana
        self.root.geometry("600x600")  # Establece el tamaño de la ventana a 600x600 píxeles

        # Crea un lienzo donde se mostrará el mensaje
        self.canvas = tk.Canvas(root, width=600, height=550, bg='white')
        self.canvas.pack()

        # Crea un marco para los botones en la parte inferior de la ventana
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.BOTTOM, pady=20)  # Coloca el marco en la parte inferior con un margen superior de 20 píxeles

        # Crea el botón "Piedra" y lo agrega al marco de los botones
        self.rock_button = tk.Button(self.button_frame, text="Piedra", command=self.rock)
        self.rock_button.pack(side=tk.LEFT, padx=10)  # Coloca el botón a la izquierda con un margen horizontal de 10 píxeles

        # Crea el botón "Papel" y lo agrega al marco de los botones
        self.paper_button = tk.Button(self.button_frame, text="Papel", command=self.paper)
        self.paper_button.pack(side=tk.LEFT, padx=10)  # Coloca el botón a la izquierda con un margen horizontal de 10 píxeles

        # Crea el botón "Tijera" y lo agrega al marco de los botones
        self.scissors_button = tk.Button(self.button_frame, text="Tijera", command=self.scissors)
        self.scissors_button.pack(side=tk.LEFT, padx=10)  # Coloca el botón a la izquierda con un margen horizontal de 10 píxeles

    def rock(self):
        # Acción cuando se hace clic en el botón "Piedra"
        self.display_message("Elegiste Piedra")

    def paper(self):
        # Acción cuando se hace clic en el botón "Papel"
        self.display_message("Elegiste Papel")

    def scissors(self):
        # Acción cuando se hace clic en el botón "Tijera"
        self.display_message("Elegiste Tijera")

    def display_message(self, message):
        # Limpia el lienzo antes de mostrar un nuevo mensaje
        self.canvas.delete("all")
        # Muestra el mensaje en el centro del lienzo
        self.canvas.create_text(300, 275, text=message, font=("Arial", 24), fill="black")

if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal de Tkinter
    app = RockPaperScissors(root)  # Crea una instancia de RockPaperScissors y pasa la ventana principal
    root.mainloop()  # Inicia el bucle principal de la aplicación
