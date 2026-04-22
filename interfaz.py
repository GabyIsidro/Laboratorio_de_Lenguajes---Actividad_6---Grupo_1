import tkinter as tk
from tkinter import ttk, messagebox

from modelos.JugadorCampo import JugadorCampo
from modelos.Arquero import Arquero

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Estadísticas del Equipo")
        self.root.geometry("400x300")
        
        # Aquí guardaremos los objetos (Arqueros y Jugadores de Campo)
        self.listaEquipo = []
        
        self.crearMenu()

    def crearMenu(self):
        lbl_titulo = tk.Label(self.root, text="Menú Principal", font=("Helvetica", 16, "bold"))
        lbl_titulo.pack(pady=20)

        # Botones del menú principal
        btn_cargar = tk.Button(self.root, text="Cargar Jugador", width=25, command=self.abrirVentanaCarga)
        btn_cargar.pack(pady=10)

        btn_consultar = tk.Button(self.root, text="Consultar Estadísticas", width=25, command=self.abrirVentanaConsultas)
        btn_consultar.pack(pady=10)

        btn_salir = tk.Button(self.root, text="Salir", width=25, command=self.root.quit)
        btn_salir.pack(pady=10)

    def abrirVentanaCarga(self):
        # Toplevel crea una ventana secundaria por encima de la principal
        ventana_carga = tk.Toplevel(self.root)
        ventana_carga.title("Cargar Nuevo Jugador")
        ventana_carga.geometry("350x420")

        # Variables de Tkinter para capturar lo que el usuario escribe
        var_num = tk.StringVar()
        var_ape = tk.StringVar()
        var_pos = tk.StringVar(value="Defensor")
        var_min = tk.StringVar(value="0")
        var_gol = tk.StringVar(value="0")

        tk.Label(ventana_carga, text="N° Camiseta:").pack(pady=5)
        tk.Entry(ventana_carga, textvariable=var_num).pack()

        tk.Label(ventana_carga, text="Apellido:").pack(pady=5)
        tk.Entry(ventana_carga, textvariable=var_ape).pack()

        tk.Label(ventana_carga, text="Posición:").pack(pady=5)
        # Combobox para limitar las opciones de posición
        opciones = ["Arquero", "Defensor", "Mediocampista", "Delantero"]
        combo_pos = ttk.Combobox(ventana_carga, textvariable=var_pos, values=opciones, state="readonly")
        combo_pos.pack()

        tk.Label(ventana_carga, text="Minutos Jugados:").pack(pady=5)
        tk.Entry(ventana_carga, textvariable=var_min).pack()

        lbl_goles = tk.Label(ventana_carga, text="Goles Marcados:")
        lbl_goles.pack(pady=5)
        entry_goles = tk.Entry(ventana_carga, textvariable=var_gol)
        entry_goles.pack()

        # Lógica para deshabilitar los goles si eligen "Arquero"
        def actualizar_estado_goles(*args):
            if var_pos.get() == "Arquero":
                var_gol.set("0")
                entry_goles.config(state="disabled")
            else:
                entry_goles.config(state="normal")
        
        # El método trace_add vigila si cambia la posición y ejecuta la función
        var_pos.trace_add("write", actualizar_estado_goles)
        actualizar_estado_goles() # Llamada inicial por si el default cambia

        def guardar():
            try:
                num = int(var_num.get())
                ape = var_ape.get().strip()
                pos = var_pos.get()
                mins = int(var_min.get())

                #Validaciones
                if num < 0 or mins < 0:
                    messagebox.showerror("Error","El número de camiseta y los minutos no pueden ser negativos.")
                    return
                
                if not ape or not ape.replace(" ", "").isalpha():
                    messagebox.showerror("Error","El apellido no puede estar vacío y debe contener solo letras.")
                    return
                
                for jugador in self.listaEquipo:
                    if jugador.numeroCamiseta == num:
                        messagebox.showerror("Error","Ya existe un jugador con ese número de camiseta.")
                        return
                
                # Instanciamos el objeto correspondiente según la posición
                if pos == "Arquero":
                    nuevo_jugador = Arquero(num, ape, mins)
                else:
                    goles = int(var_gol.get())
                    if goles < 0:
                        messagebox.showerror("Error","Los goles no pueden ser negativos.")
                        return
                    nuevo_jugador = JugadorCampo(num, ape, pos, mins, goles)
                
                self.listaEquipo.append(nuevo_jugador)
                messagebox.showinfo("Éxito", f"Jugador {ape} cargado correctamente.")
                ventana_carga.destroy()

            except ValueError:
                messagebox.showerror("Error", "Revise los datos ingresados. Camiseta, minutos y goles deben ser números enteros.")

        tk.Button(ventana_carga, text="Guardar", command=guardar).pack(pady=20)

    def abrirVentanaConsultas(self):
        ventana_consultas = tk.Toplevel(self.root)
        ventana_consultas.title("Estadísticas del Equipo")
        ventana_consultas.geometry("500x350")

        if not self.listaEquipo:
            tk.Label(ventana_consultas, text="No hay jugadores cargados en el sistema.").pack(pady=20)
            return

        # Área de texto para mostrar los datos
        txt_area = tk.Text(ventana_consultas, width=60, height=18)
        txt_area.pack(pady=10, padx=10)

        # Recorremos la lista. Aquí se ve el POLIMORFISMO en acción.
        for jugador in self.listaEquipo:
            # Tkinter llama a mostrarDatos(). No importa si es Arquero o JugadorCampo,
            # Python sabrá cuál método ejecutar.
            datos = jugador.mostrarDatos()
            txt_area.insert(tk.END, datos + "\n" + "-"*40 + "\n")
        
        txt_area.config(state="disabled") # Lo ponemos en solo lectura
