from tkinter import *
import pandas as pd
from pandastable import Table , TableModel
from PIL import Image, ImageTk
from Columnas import Modificar
from Col_fil import Col_fil

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

        ### Imagen Fila
        self.ifila = Image.open(r"Iconos\fila.png")
        self.ifila = self.ifila.resize((30, 30), Image.Resampling.LANCZOS)
        self.ifila = ImageTk.PhotoImage(self.ifila)
        self.key = Button(self.tool_frame, command=self.modificar, image=self.ifila, compound="left")
        self.key.pack(side=LEFT, padx=10, pady=10)

        self.key.bind("<Enter>", self.mostrar_tooltip)
        self.key.bind("<Leave>", self.ocultar_tooltip)

        self.tooltip = Label(text="Modificar las columnas", bg="yellow", fg="black")
        self.tooltip.pack_forget()

        ## imagane col_fil
        self.icol = Image.open(r"Iconos\convertir.png")
        self.icol = self.icol.resize((30,30), Image.Resampling.LANCZOS)
        self.icol = ImageTk.PhotoImage(self.icol)

        self.Bcol = Button(self.tool_frame, command= self.col , image = self.icol, compound= "left")
        self.Bcol.pack(side = LEFT, padx= 20 , pady = 10)

        self.Bcol.bind("<Enter>", self.mostrar_toolcol)
        self.Bcol.bind("<Leave>", self.ocultar_toolcol)

        self.Tcol = Label(text = "Transforma las columnas a fila", bg = "yellow" , fg = "black")
        self.Tcol.pack_forget()

        ## Imagen de relacionar 

        self.irel = Image.open(r"Iconos\relacion.png")
        self.irel = self.irel.resize((30,30), Image.Resampling.LANCZOS)
        self.irel = ImageTk.PhotoImage(self.irel)

        self.Brel = Button(self.tool_frame , command = self.rela , image = self.irel , compound = "left")
        self.Brel.pack(side = LEFT , padx = 30, pady = 10)

        self.Brel.bind("<Enter>" , self.mostrar_toolrel)
        self.Brel.bind("<Leave>" , self.ocultar_toolrel)

        self.Trel = Label(text= "Crea una columna y relaciona con otra tabla" , bg = "yellow" , fg = "black")
        self.Trel.pack_forget()


        ## Imagen de macro 
        self.imacro = Image.open(r"Iconos\camara-fotografica.png")
        self.imacro = self.imacro.resize((30,30), Image.Resampling.LANCZOS)
        self.imacro = ImageTk.PhotoImage(self.imacro)

        self.Bmacro = Button(self.tool_frame, command = self.macro , image = self.imacro , compound = "left" )
        self.Bmacro.pack(side = LEFT , padx = 40 , pady = 10)

        self.Bmacro.bind("<Enter>", self.mostrar_toolmacro)
        self.Bmacro.bind("<Leave>", self.ocultar_toolmacro)

        self.Tmacro = Label(text = "Modifica otros excels los mismo que este", bg = "yellow", fg = "black")
        self.Tmacro.pack_forget()

        ## Imagen de guardar

        self.iguardar = Image.open(r"Iconos\guardar-el-archivo.png")
        self.iguardar = self.iguardar.resize((30,30), Image.Resampling.LANCZOS)
        self.iguardar = ImageTk.PhotoImage(self.iguardar)

        self.Bguardar = Button(self.tool_frame , command = self.guardar , image = self.iguardar , compound = "left")
        self.Bguardar.pack(side = LEFT , padx = 50 , pady = 10)

        self.Bguardar.bind("<Enter>", self.mostrar_toolsave)
        self.Bguardar.bind("<Leave>", self.ocultar_toolsave)

        self.Tguardar = Label(text = "guardar el archivo", bg = "yellow" , fg = "black")
        self.Tguardar.pack_forget()
        


    def lectura(self):
        try:
            data = pd.read_excel(self.archivo, sheet_name=self.hoja)
            return data
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return pd.DataFrame()
        
    def modificar(self):

        self.table.model.df["Indice"] = self.table.model.df.index
       
        self.table.model.df.to_excel(self.archivo, sheet_name=self.hoja, index=False)
        
        
        self.columnas = Modificar(self.archivo, self.hoja)
        
        
        self.columnas.closed.connect(self.actualizar_tabla)
        
        self.columnas.show()

    def col(self):
        self.table.model.df["Indice"] = self.table.model.df.index

        self.table.model.df.to_excel(self.archivo, sheet_name = self.hoja , index = False)

        self.col_fil = Col_fil(self.archivo , self.hoja)

        self.col_fil.closed.connect(self.actualizar)
        self.col_fil.show()

    def rela(self):
        pass

    def macro(self):
        pass

    def guardar(self):
        pass

    def actualizar_tabla(self):
    
        new_df = self.lectura()
        new_df = new_df.set_index("Indice")

        self.table.model.df = pd.DataFrame()

        self.table.redraw()

        self.nuevo_df(new_df)

    def actualizar(self):
        self.destroy()
        self.tabla = Tables(self.archivo , self.hoja)
        self.tabla.mainloop()

    def nuevo_df(self, nuevo_df):
        try:
            nuevo_df = nuevo_df.infer_objects(copy=False)  

            self.table.model.df = nuevo_df  
            self.table.redraw()

            
        except Exception as e:
            print(f"Error al actualizar la tabla: {e}")
            

    def mostrar_tooltip(self, event):
        self.tooltip.place(x=event.x_root, y=event.y_root -30)  

    def ocultar_tooltip(self, event):
        self.tooltip.place_forget()

    
    def mostrar_toolcol(self, event):
        self.Tcol.place(x = event.x_root , y = event.y_root - 40)

    def ocultar_toolcol(self, event):
        self.Tcol.place_forget()

    def mostrar_toolrel(self, event):
        self.Trel.place(x = event.x_root , y = event.y_root - 40)

    def ocultar_toolrel(self , event):
        self.Trel.place_forget()
    
    def mostrar_toolmacro(self, event):
        self.Tmacro.place(x = event.x_root , y = event.y_root - 40)
    
    def ocultar_toolmacro(self , event):
        self.Tmacro.place_forget()

    def mostrar_toolsave(self, event):
        self.Tguardar.place(x = event.x_root , y = event.y_root -40)
    
    def ocultar_toolsave(self , event):
        self.Tguardar.place_forget()

if __name__ == "__main__":
    app = Tables("ruta/a/tu/archivo.xlsx", "NombreHoja")
    app.mainloop()
