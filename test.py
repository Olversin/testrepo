import random
import string

def generador_pintudo(longitud=12, mayusculas=True, numeros=True, especiales=True):
    """
    Genera una contraseña pintuda y segura.
    
    Args:
        longitud (int): Longitud de la contraseña (default: 12).
        mayusculas (bool): Incluir mayúsculas (default: True).
        numeros (bool): Incluir números (default: True).
        especiales (bool): Incluir caracteres especiales (default: True).
    
    Returns:
        str: La contraseña pintuda generada.
    """
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if especiales:
        caracteres += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if longitud < 8:
        return "¡usa al menos 8 caracteres! 🤨"
    
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return f"Tu contraseña pintuda es: {contraseña}"

# Ejemplo de uso
print("=" * 50)
print("GENERADOR DE CONTRASEÑAS PINTUDAS".center(50))
print("=" * 50)
longitud = int(input("Longitud de la contraseña (mínimo 8): "))
print(generador_pintudo(longitud))