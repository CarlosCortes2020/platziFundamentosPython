import tkinter as tk

class RockPaperScissors:
    def __init__(self, root):
        # Inicializa la ventana principal
        self.root = root
        self.root.title("Piedra, Papel, Tijera")
        self.root.geometry("600x600")
        
        # Crea un marco para los botones
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.BOTTOM, pady=20)
        
        # Crea los botones y los agrega al marco
        self.rock_button = tk.Button(self.button_frame, text="Piedra", command=self.rock)
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(self.button_frame, text="Papel", command=self.paper)
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(self.button_frame, text="Tijera", command=self.scissors)
        self.scissors_button.pack(side=tk.LEFT, padx=10)

    def rock(self):
        print("Elegiste Piedra")

    def paper(self):
        print("Elegiste Papel")

    def scissors(self):
        print("Elegiste Tijera")

if __name__ == "__main__":
    # Crea la ventana principal de Tkinter
    root = tk.Tk()
    # Crea una instancia de RockPaperScissors y pasa la ventana principal
    app = RockPaperScissors(root)
    # Inicia el bucle principal de la aplicación
    root.mainloop()
