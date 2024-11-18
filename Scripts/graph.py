"""El codigo permite crear gráficos en tiempo dinámico
Presenta un grafico lineal en tiempo real
toma datos cada medio segundo
se usará para presentar los datos provenientes del PLC
Se utiliza la librería matplotlib y numpy"""
#Importar modulos necesarios
import Scripts.Modbus_client as client
import matplotlib.pyplot as plt
import numpy as np

#Funcion para mostrar la gráfico en tiempo real
def SingleRealTime_line(ip="",addres=0,n=1):
    x = np.linspace(0,n,n) #Creación de un vector de 1 hasta n con n valores de tamaño
    y=np.zeros((n,))#Creación de un vector de 0 con tamaño (n,1)
    plt.ion() #Crea un modo interactivo
    fig = plt.figure() #Crea una figura 
    ax = fig.add_subplot(111) #Genera dentro de la figura un Axes ára graficar
    line1, = ax.plot(x,y,'-b') #Grafica la linea inicial
    for i in range(0,n): #Comienzo de grafica en tiempo real
        y[i] =  client.read_inputs(ip,addres)#Lectura de valores al PLC y guardar en la posición de y
        line1.set_ydata(y) #Se envía los datos al eje y
        ax.set_ylim(0,y.max()+1000) # Se coloca límites en el eje y
        ax.set_xlim(0,x[i]) #Se coloca limites en el x para que el grafico crezca en función del tiempo y el tamaño de los datos
        fig.canvas.draw() #Muestra la figura
        fig.canvas.flush_events() #Limpia los eventos para mejorar la velocidad de la gráfica
        plt.pause(0.5) #Espera 0,5 segundos
    plt.ioff()# Desabilita el modo interactivo
    plt.plot(x,y) #Grafica todos los datos tomados 
    plt.show()#Muestra la figura ploteada
    return
