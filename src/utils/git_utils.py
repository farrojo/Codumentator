# git_utils.py
"""
Funciones para interactuar con Git dentro del proyecto Codumentator.
"""

import subprocess

def run_git_command(command):
    """Ejecuta un comando de Git y devuelve la salida."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout
