# api/funciones_auxiliares.py

import html
import bleach  
import bcrypt 

def sanitize_input(user_input):
    """
    Sanitiza la entrada de los usuarios para evitar inyecciones XSS.
    """
    escaped_input = html.escape(user_input)  # Escapa caracteres especiales en HTML
    return bleach.clean(escaped_input)  # Limpia cualquier HTML no permitido
    
def cipher_password(password):
  hashAndSalt = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(10));
  return hashAndSalt
def compare_password(password_hash,password):
   if password_hash is None:
      return False
   try:
      return bcrypt.checkpw(password,password_hash)
   except:
      return False
