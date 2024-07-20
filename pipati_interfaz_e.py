import tkinter as tk  # Importa la biblioteca tkinter para la interfaz gráfica
import random  # Importa el módulo random para generar opciones aleatorias

class RockPaperScissors:
    def __init__(self, root):
        # Inicializa la ventana principal
        self.root = root  # Asigna la ventana principal a self.root para acceso dentro de la clase
        self.root.title("Piedra, Papel, Tijera")  # Establece el título de la ventana
        self.root.geometry("600x600")  # Establece el tamaño de la ventana a 600x600 píxeles

        # Crea un marco para los botones en la parte inferior de la ventana
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.BOTTOM, pady=20)  # Coloca el marco en la parte inferior con un margen superior de 20 píxeles

        # Crea un lienzo donde se mostrará el mensaje
        self.canvas = tk.Canvas(root, width=600, height=500, bg='white')
        self.canvas.pack(pady=20)  # Coloca el lienzo en la ventana principal con un margen superior de 20 píxeles

        # Crea el botón "Piedra" y lo agrega al marco de los botones
        self.rock_button = tk.Button(self.button_frame, text="Piedra", command=self.rock, width=10, height=2)
        self.rock_button.pack(side=tk.LEFT, padx=10, pady=10)  # Coloca el botón a la izquierda con márgenes horizontales y verticales de 10 píxeles

        # Crea el botón "Papel" y lo agrega al marco de los botones
        self.paper_button = tk.Button(self.button_frame, text="Papel", command=self.paper, width=10, height=2)
        self.paper_button.pack(side=tk.LEFT, padx=10, pady=10)  # Coloca el botón a la izquierda con márgenes horizontales y verticales de 10 píxeles

        # Crea el botón "Tijera" y lo agrega al marco de los botones
        self.scissors_button = tk.Button(self.button_frame, text="Tijera", command=self.scissors, width=10, height=2)
        self.scissors_button.pack(side=tk.LEFT, padx=10, pady=10)  # Coloca el botón a la izquierda con márgenes horizontales y verticales de 10 píxeles

    def rock(self):
        # Acción cuando se hace clic en el botón "Piedra"
        user_choice = "Piedra"
        computer_choice = self.random_choice()  # Genera la elección de la computadora
        result = self.determine_winner(user_choice, computer_choice)
        self.display_message(f"Elegiste {user_choice}.", f"Computadora eligió {computer_choice}.", f"{result}")

    def paper(self):
        # Acción cuando se hace clic en el botón "Papel"
        user_choice = "Papel"
        computer_choice = self.random_choice()  # Genera la elección de la computadora
        result = self.determine_winner(user_choice, computer_choice)
        self.display_message(f"Elegiste {user_choice}.", f"Computadora eligió {computer_choice}.", f"{result}")

    def scissors(self):
        # Acción cuando se hace clic en el botón "Tijera"
        user_choice = "Tijera"
        computer_choice = self.random_choice()  # Genera la elección de la computadora
        result = self.determine_winner(user_choice, computer_choice)
        self.display_message(f"Elegiste {user_choice}.", f"Computadora eligió {computer_choice}.", f"{result}")

    def random_choice(self):
        # Genera una elección aleatoria entre "Piedra", "Papel" y "Tijera"
        options = ["Piedra", "Papel", "Tijera"]
        return random.choice(options)  # Retorna la opción seleccionada aleatoriamente

    def determine_winner(self, user_choice, computer_choice):
        # Determina el ganador del juego
        if user_choice == computer_choice:
            return "Es un empate!"
        elif (user_choice == "Piedra" and computer_choice == "Tijera") or \
             (user_choice == "Papel" and computer_choice == "Piedra") or \
             (user_choice == "Tijera" and computer_choice == "Papel"):
            return "¡Ganaste!"
        else:
            return "¡Perdiste!"

    def display_message(self, user_message, computer_message, winner_message):
        # Limpia el lienzo antes de mostrar un nuevo mensaje
        self.canvas.delete("all")
        # Muestra los mensajes en el centro del lienzo en dos líneas diferentes
        self.canvas.create_text(300, 220, text=user_message, font=("Arial", 24), fill="black")
        self.canvas.create_text(300, 280, text=computer_message, font=("Arial", 24), fill="black")
        self.canvas.create_text(300, 320, text=winner_message, font=("Arial", 24), fill="black")

if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal de Tkinter
    app = RockPaperScissors(root)  # Crea una instancia de RockPaperScissors y pasa la ventana principal
    root.mainloop()  # Inicia el bucle principal de la aplicación
