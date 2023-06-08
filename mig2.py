#!/usr/bin/python3
import os
import time
import PyPDF2
import gtts	 
import tkinter as tk
from tkinter import tkk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import matplotlib
import pygame
from tkPDFViewer import tkPDFViewer as pdff

audio_path ="archivo_de_audiof.mp3"
def convertir_a_audio():
    # Obtener la ruta del archivo PDF seleccionado
    pdf_path = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])

    if pdf_path:
        try:
            # Extraer texto del PDF
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
            #print(text)
        
            # Obtener el idioma seleccionado
            language = idiomas_codigos[combo_idiomas.get()]
            #print(idiomas_codigos)
            #print(type(language))

            # Crear objeto de conversión de texto a voz
            audio = gtts.gTTS(text=text, lang=language, slow=slow_audio_speed)
            #time.sleep(10)
            #audio_info = pygame.mixer.Sound(audio_path)
            #duration = audio_info.get_length()
            #print(audio)
            
            # Guardar archivo de audio
            print('si')
            time.sleep(2)
            audio.save(audio_path)
            print('n')

            # Reproducir archivo de audio con pygame
            #pygame.init()
            #pygame.mixer.init()
            #pygame.mixer.music.load(audio_path)
            #pygame.mixer.music.play(1)
            

            # Actualizar los controles de reproducción
            #btn_reproducir.config(state=tk.NORMAL)
            #btn_pause.config(state=tk.NORMAL)
            #btn_resume.config(state=tk.DISABLED)

            # Obtener la duración del archivo de audio

            # Iniciar la barra de progreso
            #progress_bar.config(maximum=duration)
            #actualizar_barra_progreso()
            #print('listo')

            messagebox.showinfo("Éxito", "La conversión se ha completado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante la conversión: {str(e)}")
    else:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ningún archivo PDF.")
	    

def actualizar_barra_progreso():
    current_time = pygame.mixer.music.get_pos() / 1000#Obtener el tiempo actual en segundos
    style = ttk.Style()
    style.configure('my.Progressbar', troughcolor='black', bordercolor='white', foreground='white', relief='flat')
    progress_bar.config(value=current_time,style='my.Progressbar')
    if pygame.mixer.music.get_busy():
	    window.after(1000, actualizar_barra_progreso)#Actualizar la barra cada segundo

def pausar_reproduccion():
    pygame.mixer.music.pause()
    btn_pause.config(state=tk.DISABLED)
    btn_resume.config(state=tk.NORMAL)
    btn_reproducir.config(state=tk.NORMAL)

def reanudar_reproduccion():
    pygame.mixer.music.unpause()
    btn_pause.config(state=tk.NORMAL)
    btn_resume.config(state=tk.DISABLED)
    btn_reproducir.config(state=tk.NORMAL)

def iniciar_reproduccion():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()
    btn_pause.config(state=tk.NORMAL)
    btn_resume.config(state=tk.DISABLED)

    #clock = pygame.time.Clock()
    #while pygame.mixer.music.get_busy():
	#    clock.tick(60)
	#    pygame.event.poll()
def funcion():
    global btn_reproducir
    global btn_pause
    global btn_resume
    ventana_secundaria = tk.Toplevel()
    #ventana_secundaria.attributes('-fullscreen',True)
    #ventana_secundaria.state("zoomed")
    ventana_secundaria.title("Reproductor")
    #ventana_secundaria.config(width=1000, height=1000)
ventana_secundaria.geometry("550x750")
btn_reproducir = tk.Button(ventana_secundaria, text="Reproducir", state=tk.NORMAL, command=iniciar_reproduccion)
btn_reproducir.pack(pady=10)

    btn_pause = tk.Button(ventana_secundaria, text="Pausar", state=tk.DISABLED, command=pausar_reproduccion)
    btn_pause.pack(pady=10)

    btn_resume = tk.Button(ventana_secundaria, text="Reanudar", state=tk.DISABLED, command=reanudar_reproduccion)
    btn_resume.pack(pady=10)


    btn_reproducir.config(state=tk.NORMAL)
    btn_pause.config(state=tk.NORMAL)
    btn_resume.config(state=tk.DISABLED)
visorpdf = pdff.ShowPdf()
loc_visorpdf = visorpdf.pdf_view(ventana_secundaria,pdf_location = pdf_path,width = 50, height = 100)
loc_visor.pack()
	

# Diccionario de idiomas
idiomas = {
    'es': 'Español',
    'en': 'Inglés',
    'fr': 'Francés',
    'pt': 'Portugués',
    'zh': 'Chino',
    'it': 'Italiano'
}

# Configuración de la velocidad de reproducción
slow_audio_speed = True  # Cambiar a False para una velocidad más rápida

# Crear la ventana de la interfaz
window = tk.Tk()
window.title("Conversor de PDF a Audio")

#Pruebas de abrir paginas nuevas
#btn_convertir = tk.Button(window, text="otra pagina", command=funcion)
#btn_convertir.pack(pady=20)

# Agregar una lista desplegable de idiomas con nombres completos
idiomas_codigos = {v: k for k, v in idiomas.items()}  # Invertir el diccionario para obtener los códigos de idioma
combo_idiomas = ttk.Combobox(window, values=list(idiomas.values()))
combo_idiomas.current(0)  # Establecer el idioma predeterminado
combo_idiomas.pack(pady=10)

# Agregar un botón para seleccionar el archivo PDF y realizar la conversión
btn_convertir = tk.Button(window, text="Seleccionar PDF", command=lambda:[convertir_a_audio(),funcion()])
btn_convertir.pack(pady=20)

#Agregar un bóton para iniciar la reproducción
#btn_reproducir = tk.Button(ventana_secundaria, text="Reproducir", state=tk.NORMAL, command=iniciar_reproduccion)
#btn_reproducir.pack(pady=10)
# Agregar botones para pausar y reanudar la reproducción
#btn_pause = tk.Button(ventana_secundaria, text="Pausar", state=tk.DISABLED, command=pausar_reproduccion)
#btn_pause.pack(pady=10)

#btn_resume = tk.Button(ventana_secundaria, text="Reanudar", state=tk.DISABLED, command=reanudar_reproduccion)
#btn_resume.pack(pady=10)

#Agregar una barra de progreso para mostrar el avance de la reproducción
#progress_bar = ttk.Progressbar(window, orient='horizontal', mode='determinate')
#progress_bar.pack(pady=10)


# Ejecutar la interfaz
window.mainloop()
