                                       
import pandas as pd
from PyQt6.QtCore import pyqtSignal
from tkinter import filedialog

class Macro():
    def __init__(self, hoja:str):
        super().__init__()
        self.hoja = hoja
        self.archivos = None
    
    def eliminar_col(self, columnas:list[str]):
        if self.archivos:
            for archivo in self.archivos:
                try:
                    df = pd.read_excel(archivo, self.hoja)
                    column_ac = df.columns.tolist()
                    elim_col = [elemento for elemento in column_ac if elemento not in columnas]
                    df = df.drop(columns=elim_col)
                    df.to_excel(archivo, sheet_name=self.hoja)
                except Exception as e:
                    print(f"Error al eliminar columnas en {archivo}: {e}")

    def eliminar_fil(self, filas:list):
        if self.archivos:
            for archivo in self.archivos:
                try:
                    df = pd.read_excel(archivo, self.hoja)
                    fil_ac = df.index.tolist()
                    elim_fil = [elemento for elemento in fil_ac if elemento not in filas]
                    df = df.drop(index=elim_fil)
                    df.to_excel(archivo, self.hoja)
                except Exception as e:
                    print(f"Error al eliminar filas en {archivo}: {e}")

    def columnas(self, listaop:list[int], Eli:str):
        if self.archivos:
            for archivo in self.archivos:
                try:
                    df = pd.read_excel(archivo, self.hoja)
                    indice = df.columns.get_loc(Eli)
                    recupera = df.iloc[:, :indice + 1]
                    nueva = df.iloc[:, indice + 1:]
                    filas = []
                    for esc in listaop:
                        fila = nueva.iloc[esc].tolist()
                        nueva_fila = [str(elemento).replace(" 00:00:00", "") for elemento in fila]
                        filas.append(nueva_fila)
                    columnas = [" ".join(map(str, valores)) for valores in zip(*filas)]
                    nueva.columns = columnas
                    for i, (col, val) in enumerate(recupera.items()):
                        nueva.insert(i, col, val)

                    nueva = nueva.drop(index=listaop)
                    nueva = nueva.reset_index(drop=True)

                    nueva.to_excel(archivo, self.hoja)
                except Exception as e:
                    print(f"Error al procesar columnas en {archivo}: {e}")

    def col_fil(self, N_columna:str, N_valor:str, R_si:bool, Box_col:str, Box_fil:str, R_no:bool):
        if self.archivos:
            for archivo in self.archivos:
                df = pd.read_excel(archivo , self.hoja)
                try:
                    if N_columna and N_valor:
                        if R_si and Box_col != "Ninguno":
                            Eli = Box_col
                            indice = df.columns.get_loc(Eli)
                            recuperar = df.iloc[:, :indice + 1]
                            filtrar = (df.melt(id_vars=recuperar.columns.tolist(), var_name=N_columna, 
                                                    value_name=N_valor)
                                    .query(f"`{N_valor}` == @Box_fil")
                                    .reset_index(drop=True))
                        elif R_no and Box_col == "Ninguno":
                            filtrar = (df.melt(var_name=N_columna, value_name=N_valor)
                                    .reset_index(drop=True))
                        elif R_si and Box_col == "Ninguno":
                            filtrar = (df.melt(var_name=N_columna, value_name=N_valor)
                                    .query(f"`{N_valor}` == @Box_fil")
                                    .reset_index(drop=True))
                        elif R_no and Box_col != "Ninguno":
                            Eli = Box_col
                            indice = df.columns.get_loc(Eli)
                            recuperar = df.iloc[:, :indice + 1]
                            filtrar = (df.melt(id_vars=recuperar.columns.tolist(), var_name=N_columna, 
                                                    value_name=N_valor)
                                    .reset_index(drop=True))
                        else:
                            filtrar = df.copy()

                    filtrar.to_excel(archivo, self.hoja)
                except Exception as e:
                    print(f"Error al filtrar columnas y filas en {archivo}: {e}")

                    
    def tabla_rel(self, T_col: str, Box_buscar: str, nuevo: pd.DataFrame, Box_colN: str, Box_colA: str):
        if self.archivos:
            for archivo in self.archivos:
                try:
                    df = pd.read_excel(archivo, self.hoja)
                    N_col = T_col
                    if N_col == "":
                        N_col = Box_buscar

                    relacionar = df.merge(
                        nuevo[[Box_colN, Box_buscar]].rename(columns={Box_buscar: N_col}),
                        left_on=Box_colA,
                        right_on=Box_colN,
                        how="left"
                    )

                    relacionar = relacionar.drop(columns=[Box_colN])

                    relacionar.to_excel(archivo, self.hoja)

                except KeyError as e:
                    print(f"Error de clave en el archivo {archivo}: {e}")
                except FileNotFoundError as e:
                    print(f"Archivo no encontrado: {e}")
                except Exception as e:
                    print(f"Error inesperado al relacionar datos en {archivo}: {e}")



                





            


