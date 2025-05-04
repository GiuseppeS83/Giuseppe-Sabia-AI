import random
import string

def genera_password(lunghezza=12):
    """Genera una password casuale."""
    if lunghezza < 8:
        print("È consigliato utilizzare password di almeno 8 caratteri.")
        lunghezza = 8

    # Caratteri da includere nella password
    caratteri = string.ascii_letters + string.digits + string.punctuation

    # Creazione della password casuale
    password = ''.join(random.choice(caratteri) for _ in range(lunghezza))
    return password

# Esempio di utilizzo
if __name__ == "__main__":
    lunghezza_password = int(input("Inserisci la lunghezza della password: "))
    password_generata = genera_password(lunghezza_password)
    print(f"La tua password generata è: {password_generata}")
