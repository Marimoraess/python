import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import socket
import ssl
import urllib.request
from urllib.parse import urlparse
from datetime import datetime

# --- Lógica de Segurança (Backend) ---

def get_domain(url):
    try:
        if not url.startswith('http'):
            url = 'https://' + url
        parsed = urlparse(url)
        return parsed.netloc
    except:
        return ""

def check_ssl(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                expire_date = datetime.strptime(cert['notAfter'], r'%b %d %H:%M:%S %Y %Z')
                days_left = (expire_date - datetime.now()).days
                return True, f"Válido (Expira em {days_left} dias)"
    except Exception as e:
        return False, f"Erro/Inválido: {str(e)}"

def check_security_headers(url):
    if not url.startswith('http'):
        url = 'https://' + url
    
    headers_info = [
        ("X-Frame-Options", "Proteção Clickjacking"),
        ("X-Content-Type-Options", "Proteção MIME Sniffing"),
        ("Strict-Transport-Security", "Força HTTPS (HSTS)"),
        ("Content-Security-Policy", "Proteção XSS"),
        ("Referrer-Policy", "Privacidade de Referência")
    ]
    
    log = ""
    score = 0
    
    try:
        # Usando urllib (padrão do Python) em vez de requests para não precisar instalar nada
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'} # Finge ser um navegador
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            server_headers = response.info()
            status_code = response.getcode()
            
            log += f"Status do Servidor: {status_code}\n\n"
            
            for header, desc in headers_info:
                # Busca o cabeçalho ignorando maiúsculas/minúsculas
                val = server_headers.get(header)
                if val:
                    log += f"[OK] {header}: Presente\n"
                    score += 1
                else:
                    log += f"[X]  {header}: AUSENTE ({desc})\n"
            
            return log, score, len(headers_info)
            
    except Exception as e:
        return f"Erro ao conectar: {str(e)}", 0, 5

# --- Interface Gráfica (Frontend) ---

def run_check():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Atenção", "Digite uma URL válida!")
        return

    # Limpa resultado anterior
    result_area.config(state='normal')
    result_area.delete(1.0, tk.END)
    result_area.insert(tk.END, f"Analisando {url}...\nPor favor, aguarde.\n\n")
    result_area.update() # Força atualização da tela

    domain = get_domain(url)
    
    # 1. Checa SSL
    ssl_ok, ssl_msg = check_ssl(domain)
    result_area.insert(tk.END, "-"*40 + "\n")
    result_area.insert(tk.END, f"CERTIFICADO SSL: {'✅' if ssl_ok else '❌'} {ssl_msg}\n")
    result_area.insert(tk.END, "-"*40 + "\n\n")

    # 2. Checa Cabeçalhos
    headers_log, score, total = check_security_headers(url)
    result_area.insert(tk.END, "CABEÇALHOS DE SEGURANÇA:\n")
    result_area.insert(tk.END, headers_log)
    result_area.insert(tk.END, "\n" + "-"*40 + "\n")
    
    # Nota Final
    final_score = (score / total) * 10
    result_area.insert(tk.END, f"NOTA FINAL: {score}/{total}")
    
    result_area.config(state='disabled') # Impede edição do texto

# Configuração da Janela
root = tk.Tk()
root.title("SiteGuard Desktop - Verificador de Segurança")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

# Widgets
frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
frame.pack(fill='both', expand=True)

lbl_instrucao = tk.Label(frame, text="Digite o site (ex: google.com):", bg="#f0f0f0", font=("Arial", 10))
lbl_instrucao.pack(anchor='w')

url_entry = tk.Entry(frame, font=("Arial", 12), width=40)
url_entry.pack(pady=5, fill='x')

btn_verificar = tk.Button(frame, text="VERIFICAR SEGURANÇA", command=run_check, bg="#0078D7", fg="white", font=("Arial", 10, "bold"), pady=10)
btn_verificar.pack(pady=10, fill='x')

# Área de Texto com rolagem
result_area = scrolledtext.ScrolledText(frame, width=50, height=20, font=("Consolas", 10))
result_area.pack(pady=10, fill='both', expand=True)
result_area.config(state='disabled')

# Rodar o programa
root.mainloop()