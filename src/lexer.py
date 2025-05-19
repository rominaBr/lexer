import tkinter as tk
import ply.lex as lex
from tkinter import filedialog, scrolledtext, messagebox
from decimal import Decimal, ROUND_DOWN
import re


tokens = (
    'LLAVEI', 'LLAVED', # { }
    'CORCHETEI', 'CORCHETED', # [ ]
    'COMA',
    'TOK_EQUIPOS', 'TOK_VERSION', 'TOK_FIRMA_DIG',
    'TOK_NOMBRE_EQUIPO', 'TOK_IDENTIDAD_EQ', 'TOK_LINK',
    'TOK_ASIGNATURA', 'TOK_CARRERA', 'TOK_UNIVERSIDAD', 'TOK_DIRECCION',
    'TOK_CALLE', 'TOK_CIUDAD', 'TOK_PAIS', 'TOK_ALIANZA', 'TOK_INTEGRANTES',
    'TOK_NOMBRE', 'TOK_EDAD', 'TOK_CARGO', 'TOK_FOTO', 'TOK_EMAIL', 'TOK_HABILIDADES',
    'TOK_SALARIO', 'TOK_ACTIVO', 'TOK_PROYECTOS', 'TOK_ESTADO', 'TOK_RESUMEN',
    'TOK_TAREAS', 'TOK_FECHA_INICIO', 'TOK_FECHA_FIN', 'TOK_VIDEO', 'TOK_CONCLUSION',
    'DATE', 'EMAIL', 'URL', 'STRING', 'NUMERO', 'FLOAT',
    'TRUE', 'FALSE', 'NULL', 'VACIO', 'TO_DO', 'INPROGRESS', 'CANCELED', 'DONE', 'ONHOLD',
    'PRODUCTANALYST', 'PROJECTMANAGER', 'UXDESIGNER', 'MARKETING', 'DEVELOPER', 'DEVOPS', 'DBADMIN'    
)

t_LLAVEI = r'\{'
t_LLAVED = r'\}'
t_CORCHETEI = r'\['
t_CORCHETED = r'\]'
t_COMA = r'\,'


def t_TOK_EQUIPOS(t):
    r'\"equipos\":'
    return t

def t_TOK_VERSION(t):
    r'\"versi(o|ó)n\":'
    return t

def t_TOK_FIRMA_DIG(t):
    r'\"firma_digital\":'
    return t

def t_TOK_NOMBRE_EQUIPO(t):
    r'\"nombre_equipo\":'
    return t

def t_TOK_IDENTIDAD_EQ(t):
    r'\"identidad_equipo\":'
    return t

def t_TOK_LINK(t):
    r'\"link\":'
    return t

def t_TOK_ASIGNATURA(t):
    r'\"asignatura\":'
    return t

def t_TOK_CARRERA(t):
    r'\"carrera\":'
    return t

def t_TOK_UNIVERSIDAD(t):
    r'\"universidad_regional\":'
    return t

def t_TOK_DIRECCION(t):
    r'\"direcci(o|ó)n\":'
    return t

def t_TOK_CALLE(t):
    r'\"calle\":'
    return t

def t_TOK_CIUDAD(t):
    r'\"ciudad\":'
    return t

def t_TOK_PAIS(t):
    r'\"pa(i|í)s\":'
    return t

def t_TOK_ALIANZA(t):
    r'\"alianza_equipo\":'
    return t

def t_TOK_INTEGRANTES(t):
    r'\"integrantes\":'
    return t

def t_TOK_NOMBRE(t):
    r'\"nombre\":'
    return t

def t_TOK_EDAD(t):
    r'\"edad\":'
    return t

def t_TOK_CARGO(t):
    r'\"cargo\":'
    return t

def t_TOK_FOTO(t):
    r'\"foto\":'
    return t

def t_TOK_EMAIL(t):
    r'\"email\":'
    return t

def t_TOK_HABILIDADES(t):
    r'\"habilidades\":'
    return t

def t_TOK_SALARIO(t):
    r'\"salario\":'
    return t

def t_TOK_ACTIVO(t):
    r'\"activo\":'
    return t

def t_TOK_PROYECTOS(t):
    r'\"proyectos\":'
    return t

def t_TOK_ESTADO(t):
    r'\"estado\":'
    return t

def t_TOK_RESUMEN(t):
    r'\"resumen\":'
    return t

def t_TOK_TAREAS(t):
    r'\"tareas\":'
    return t

def t_TOK_FECHA_INICIO(t):
    r'\"fecha_inicio\":'
    return t

def t_TOK_FECHA_FIN(t):
    r'\"fecha_fin\":'
    return t

def t_TOK_VIDEO(t):
    r'\"video\":'
    return t

def t_TOK_CONCLUSION(t):
    r'\"conclusi(o|ó)n\":'
    return t

def t_VACIO(t):
    r'""'
    t.value= ""
    return t

def t_TO_DO(t):
    r'\"(T|t)o\s(D|d)o\"'
    t.value = t.value[1:-1]   # Elimina las comillas
    return t

def t_INPROGRESS(t):
    r'\"(I|i)n\s(P|p)rogress\"'
    t.value = t.value[1:-1]
    return t

def t_CANCELED(t):
    r'\"(C|c)anceled\"'
    t.value = t.value[1:-1]    
    return t

def t_DONE(t):
    r'\"(D|d)one\"'
    t.value = t.value[1:-1]    
    return t

def t_ONHOLD(t):
    r'\"(O|o)n\s(H|h)old\"'
    t.value = t.value[1:-1]
    return t

def t_PRODUCTANALYST(t):
    r'\"(P|p)roduct\s(A|a)nalyst\"'
    t.value = t.value[1:-1]
    return t

def t_PROJECTMANAGER(t):
    r'\"(P|p)roject\s(M|m)anager\"'
    t.value = t.value[1:-1]
    return t

def t_UXDESIGNER(t):
    r'\"(U|u)(X|x)\s(D|d)esigner\"'
    t.value = t.value[1:-1]
    return t

def t_MARKETING(t):
    r'\"(M|m)arketing\"'
    t.value = t.value[1:-1]
    return t

def t_DEVELOPER(t):
    r'\"(D|d)eveloper\"'
    t.value = t.value[1:-1]
    return t

def t_DEVOPS(t):
    r'\"(D|d)evops\"'
    t.value = t.value[1:-1]
    return t

def t_DBADMIN(t):
    r'\"(D|d)(B|b)\s(A|a)dmin\"'
    t.value = t.value[1:-1]
    return t

def t_STRING(t):
    r'"(\\.|[^"\\])*"'
    t.value = t.value[1:-1]

    # Verifica si es una fecha
    if re.fullmatch(r'(19\d{2}|20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])', t.value):
        try:
            import datetime
            datetime.datetime.strptime(t.value, '%Y-%m-%d')
            t.type = 'DATE'
        except ValueError:
            pass  # Si falla, se queda como STRING

    # Verifica si es un email
    elif re.fullmatch(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', t.value):
        t.type = 'EMAIL'

    # Verifica si es una URL
    elif re.fullmatch(r'https?://[a-zA-Z0-9\-._~:/?#\[\]@!$&\'()*+,;=%]+', t.value):
        t.type = 'URL'

    return t


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = Decimal(t.value).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t
    

def t_TRUE(t):
    r'true'
    t.value = True
    return t

def t_FALSE(t):
    r'false'
    t.value = False
    return t

def t_NULL(t):
    r'null'
    t.value = None
    return t


t_ignore = ' \t\n'

def t_error(t):
    messagebox.showerror("Error",f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()



def cargar_archivo():
    archivo_json = filedialog.askopenfilename(
        title="Seleccionar archivo JSON",
        filetypes=[("Archivos JSON", "*.json"), ("Todos los archivos", "*.*")]
    )

    if archivo_json:
        with open(archivo_json, "r", encoding="utf-8") as f:
            contenido = f.read()

        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, contenido)



def obtener_json():
    contenido = text_area.get(1.0, tk.END).strip()
    output_area.config(state='normal')  # Habilita edición para escribir
    output_area.delete(1.0, tk.END)     # Limpia la salida

    if contenido:
        lexer.input(contenido)

        for tok in lexer:
            output_area.insert(tk.END, f'{tok.type}: {tok.value}\n')
    else:
        output_area.insert(tk.END, "No hay JSON ingresado\n")

    output_area.config(state='disabled') 


root = tk.Tk()
root.title("Analizador Léxico")
root.geometry("1000x600")
root.iconbitmap("LogoSSL.ico")

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

main_frame.columnconfigure(0, weight=1)  # Entrada JSON (izquierda)
main_frame.columnconfigure(1, weight=2)  # Resultado Lexer (derecha)
main_frame.rowconfigure(0, weight=1)

# Panel izquierdo (entrada JSON)
frame_entrada = tk.Frame(main_frame)
frame_entrada.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

btn_cargar = tk.Button(frame_entrada, text="Cargar JSON", command=cargar_archivo)
btn_cargar.pack(pady=5)

text_area = scrolledtext.ScrolledText(frame_entrada, wrap=tk.WORD)
text_area.pack(fill=tk.BOTH, expand=True)

btn_obtener = tk.Button(frame_entrada, text="Procesar JSON", command=obtener_json)
btn_obtener.pack(pady=5)

# Panel derecho (resultado lexer)
frame_salida = tk.Frame(main_frame)
frame_salida.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

label_resultado = tk.Label(frame_salida, text="Resultado del Lexer", font=("Arial", 12, "bold"))
label_resultado.pack(pady=5)

output_area = scrolledtext.ScrolledText(frame_salida, wrap=tk.WORD, state='disabled')
output_area.pack(fill=tk.BOTH, expand=True)


root.mainloop()


