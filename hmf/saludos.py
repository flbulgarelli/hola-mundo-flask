from datetime import datetime

recientes = []

def registrar_saludo(nombre, ip):
    recientes.append({
        'ip': ip,
        'nombre': nombre,
        'fecha': datetime.now()
    })
