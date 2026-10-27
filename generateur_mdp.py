import secrets
import string

longueur = int(input("Longueur du mot de passe : "))

caracteres = string.ascii_letters + string.digits + "!@#$%"

mot_de_passe = "".join(secrets.choice(caracteres) for i in range(longueur))

print(f"Ton mot de passe : {mot_de_passe}")
