#Importamos el tkinter
import tkinter as tk #Alias al tinter tkinter

def abrirVentanaPrincipal():
    ventana2 = tk.Tk()
    ventana2.title("SISTEMA PRINCIPAL")
    ventana2.geometry("500x700")
    ventana2.resizable(False,False)
    

    #Creando las variables 
    numTarjeta = tk.StringVar()
    codigo = tk.StringVar()
    


    #Creando la estructura 
    label_n_tarjeta = tk.Label(ventana2,text="N° Tarjeta", font=("Arial",15,"bold"))
    label_n_tarjeta.grid(row=0,column=0,padx=80,pady=10)
    label_codigo = tk.Label(ventana2,text="Codigo", font=("Arial",15,"bold"))
    label_codigo.grid(row=0,column=1,padx=80,pady=10)
    #Creando la estructura parte 02
    txtTarjeta = tk.Entry(ventana2,textvariable=numTarjeta,font=("Arial",12))
    txtTarjeta.grid(row=1,column=0,pady=10)
    txtCodigo = tk.Entry(ventana2,textvariable=codigo,font=("Arial",12))
    txtCodigo.grid(row=1,column=1,padx=10)

    incalcular= tk.Label(ventana2,text="calcular", font=("Arial",15,"bold"))
    incalcular.grid(row=2,column=2,padx=80,pady=10)

    txtcodigo = tk.Entry(ventana2,textvariable=codigo,font=("Arial",12))
    txtcodigo.grid(row=2,column=2,pady=10)

    ventana2.mainloop() #poner siempre al ultimo

abrirVentanaPrincipal()
