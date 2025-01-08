from tkinter import *
import pandas as pd
from pandastable import Table , TableModel
from PIL import Image, ImageTk
from Columnas import Modificar

class Tables(Tk):
    def __init__(self, archivo, hoja, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.archivo = archivo
        self.hoja = hoja

        self.frame = Frame(self)
        self.frame.pack(fill=BOTH, expand=1)
        self.table = Table(self.frame, dataframe=self.lectura(), showtoolbar=False, showstatusbar=True, editable=True)
        self.table.show()

        self.tool_frame = Frame(self)
        self.tool_frame.pack(fill=X)

        self.ifila = Image.open(r"Iconos\fila.png")
        self.ifila = self.ifila.resize((30, 30), Image.Resampling.LANCZOS)
        self.ifila = ImageTk.PhotoImage(self.ifila)
        self.key = Button(self.tool_frame, command=self.modificar, image=self.ifila, compound="left")
        self.key.pack(side=LEFT, padx=10, pady=10)

        self.key.bind("<Enter>", self.mostrar_tooltip)
        self.key.bind("<Leave>", self.ocultar_tooltip)

        self.tooltip = Label(text="Modificar las columnas", bg="yellow", fg="black")
        self.tooltip.pack_forget()

    def lectura(self):
        try:
            data = pd.read_excel(self.archivo, sheet_name=self.hoja)
            return data
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return pd.DataFrame()
        
    def modificar(self):
       
        self.table.model.df.to_excel(self.archivo, sheet_name=self.hoja, index=False)
        
        
        self.columnas = Modificar(self.archivo, self.hoja)
        
        
        self.columnas.closed.connect(self.actualizar_tabla)
        
        self.columnas.show()

    def actualizar_tabla(self):
    
        new_df = self.lectura()
        print(new_df.index.tolist())
        print(self.table.model.df.index.tolist())

            

    def mostrar_tooltip(self, event):
        self.tooltip.place(x=event.x_root, y=event.y_root -30)  

    def ocultar_tooltip(self, event):
        self.tooltip.place_forget()

if __name__ == "__main__":
    app = Tables("ruta/a/tu/archivo.xlsx", "NombreHoja")
    app.mainloop()
