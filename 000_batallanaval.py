import tkinter as tk  # Importa el módulo Tkinter para la creación de interfaces gráficas
import random  # Importa el módulo random para generar posiciones aleatorias

class BattleshipGame:
    def __init__(self, root):
        # Inicializa el juego, creando la ventana principal y el canvas
        self.root = root
        self.root.title("Battleship Game")  # Establece el título de la ventana
        
        # Configuración del canvas
        self.canvas_size = 300  # Tamaño del canvas
        self.grid_size = 5  # Tamaño de la cuadrícula (5x5)
        self.cell_size = self.canvas_size // self.grid_size  # Tamaño de cada celda en la cuadrícula
        
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg='white')  # Crea el widget canvas
        self.canvas.pack()  # Empaqueta el canvas en la ventana principal
        
        self.ships = []  # Lista para almacenar las posiciones de los barcos
        self.create_grid()  # Llama a la función para crear el grid
        self.place_ships()  # Llama a la función para colocar los barcos
        
        # Eventos del mouse
        self.canvas.bind("<Button-1>", self.handle_click)  # Asocia el evento de clic con la función handle_click
    
    def create_grid(self):
        # Dibuja el grid en el canvas
        for i in range(self.grid_size + 1):
            # Dibuja líneas verticales
            self.canvas.create_line(i * self.cell_size, 0, i * self.cell_size, self.canvas_size)
            # Dibuja líneas horizontales
            self.canvas.create_line(0, i * self.cell_size, self.canvas_size, i * self.cell_size)
    
    def place_ships(self):
        # Coloca los barcos en posiciones aleatorias del grid
        while len(self.ships) < 3:  # Coloca 3 barcos
            row = random.randint(0, self.grid_size - 1)  # Genera una fila aleatoria
            col = random.randint(0, self.grid_size - 1)  # Genera una columna aleatoria
            if (row, col) not in self.ships:  # Si la posición no tiene ya un barco
                self.ships.append((row, col))  # Añade la posición a la lista de barcos
    
    def handle_click(self, event):
        # Maneja los clics del usuario en el canvas
        col = event.x // self.cell_size  # Calcula la columna en base a la posición del clic
        row = event.y // self.cell_size  # Calcula la fila en base a la posición del clic
        if (row, col) in self.ships:  # Si el clic acierta un barco
            self.canvas.create_rectangle(col * self.cell_size, row * self.cell_size, 
                                         (col + 1) * self.cell_size, (row + 1) * self.cell_size, fill='red')  # Marca en rojo
            self.ships.remove((row, col))  # Elimina el barco de la lista de barcos
            if not self.ships:  # Si no quedan barcos
                print("¡Has hundido todos los barcos!")  # Muestra un mensaje de victoria
        else:  # Si el clic falla
            self.canvas.create_rectangle(col * self.cell_size, row * self.cell_size, 
                                         (col + 1) * self.cell_size, (row + 1) * self.cell_size, fill='blue')  # Marca en azul

if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    game = BattleshipGame(root)  # Crea una instancia del juego
    root.mainloop()  # Inicia el bucle principal de la aplicación
