# config/__init__.py

# Configuración de constantes y variables globales
import os

# Token de acceso para la API de WhatsApp Business
WHATSAPP_ACCESS_TOKEN = os.getenv('WHATSAPP_ACCESS_TOKEN', 'your-default-token')

# Ruta para guardar los informes transcritos
REPORTS_DIR = os.getenv('REPORTS_DIR', 'reports')

# Otros parámetros de configuración
SOME_OTHER_CONFIG = 'value'

