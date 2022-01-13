import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

email = outlook.createItem(0)

email.To = "piuuhh02@gmail.com"
email.Subject = "E-mail by python"
email.HTMLBody = """
<p>Olá este é um e-mail automático enviado pelo python</p>

<p>A fatura da sede 6 da empresa foi de 2000 reais</p
<p>foi vendido 10 produtos</p

<p>abs,</p>
<p>Pio</p>
"""

email.Send()
print("email enviado")