import tkinter as tk
from interfaz import Interfaz

def main():
    ventanaPrincipal = tk.Tk()
    app = Interfaz(ventanaPrincipal)
    ventanaPrincipal.mainloop()

if __name__ == "__main__":
    main()