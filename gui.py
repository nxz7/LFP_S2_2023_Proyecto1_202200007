
import tkinter as tk
from tkinter import ttk, filedialog
import json
import io
import sys
from tok import tok
from matematicas import matematicas
from AFD import AFD

    
def Analizar_clicked():
    global archivo_abierto  

    if archivo_abierto:

        with open(archivo_abierto, 'r') as json_file:
            json_data = json_file.read()

        automata = AFD()
        automata.analizar_char(json_data, matematicas('division'))
        text_box.delete(1.0, tk.END)
        sys.stdout = io.StringIO()  
        automata.imprimir_tokens()
        output = sys.stdout.getvalue()  
        sys.stdout = sys.__stdout__  

        text_box.insert(tk.END, output)
    else:
        text_box.insert(tk.END, "selecciona un archivo para analizar primero.\n")

def Errores_clicked():
    text_box.insert(tk.END, "Examinando errores\n")

def Reporte_clicked():
    text_box.insert(tk.END, "Generando diagramas\n")

archivo_abierto = None  #el que esta abierto para luego guardar
#---------------------

#---------------------
def Archivo_opcion(event):
    global archivo_abierto, loaded_json_data 
    selected_item = combo_box.get()
    if selected_item == "Abrir":
        archivo_abierto = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if archivo_abierto:
            with open(archivo_abierto, 'r') as json_file:
                loaded_json_data=json_file.read()
                #json_inf = json.load(loaded_json_data)
                text_box.insert(tk.END, loaded_json_data)

                #automata.analizar_json(json.dumps(json_inf), matematicas('suma'))  
    elif selected_item == "Guardar":
        if archivo_abierto:
            inf_contenido = text_box.get(1.0, tk.END)  
            with open(archivo_abierto, 'w') as json_file:
                print("inf_contenido :")
                print(inf_contenido )
                json_file.write(inf_contenido )
        else:
            text_box.insert(tk.END, "No hay archivo abierto para guardar.\n")

    elif selected_item == "Guardar como":
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if file_path:
            inf_contenido = text_box.get(1.0, tk.END)  
            with open(file_path, 'w') as json_file:
                json_file.write(inf_contenido )

    elif selected_item == "Salir":
        root.destroy()

root = tk.Tk()
root.title("PROYECTO LFP - 202200007 - ANALISIS LEXICO")
root.configure(bg="lemon chiffon")

# botones y funciones
buttonAnalizar = tk.Button(root, text="Analizar", command=Analizar_clicked, bg="white", fg="blue")
buttonErrores = tk.Button(root, text="Errores", command=Errores_clicked, bg="white", fg="blue")
buttonReporte = tk.Button(root, text="Reporte", command=Reporte_clicked, bg="white", fg="blue")

# Archivo y sus opciones en un combobox
combo_box = ttk.Combobox(root, values=["Abrir", "Guardar", "Guardar como", "Salir"])
combo_box.set("Archivo")
combo_box.bind("<<ComboboxSelected>>", Archivo_opcion)
text_box = tk.Text(root)

# acomodarlos en la ventana
buttonAnalizar.grid(row=0, column=0, padx=10, pady=10)
buttonErrores.grid(row=1, column=0, padx=10, pady=10)
buttonReporte.grid(row=2, column=0, padx=10, pady=10)
combo_box.grid(row=1, column=1, padx=10, pady=10)
text_box.grid(row=0, column=2, rowspan=3, padx=10, pady=10)

root.mainloop()
print("prueba")