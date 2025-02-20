# file_utils.py

# file_utils.py
"""
Funciones de utilidad para manejar archivos en Codumentator.
"""

import os

def read_file(filepath):
    """Lee el contenido de un archivo."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
