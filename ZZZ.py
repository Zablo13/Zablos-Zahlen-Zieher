from string import ascii_uppercase
 
# Mapping: Ziffer -> Zahl und Zahl -> Ziffer
digits = "0123456789" + ascii_uppercase
char_to_value = {ch: i for i, ch in enumerate(digits)}
value_to_char = {i: ch for i, ch in enumerate(digits)}
 
print("Universeller Umrechner für Zahlensysteme 2 bis 36!")
 
def from_base(num_str, base):
    """Wandelt eine Zahl aus beliebigem System in Dezimal um"""
    value = 0
    for ch in num_str.upper():
        if ch not in char_to_value or char_to_value[ch] >= base:
            raise ValueError(f"Ungültiges Zeichen '{ch}' für Basis {base}")
        value = value * base + char_to_value[ch]
    return value
 
def to_base(num, base):
    """Wandelt eine Dezimalzahl in beliebiges System um"""
    if num == 0:
        return "0"
    result = ""
    while num > 0:
        num, rest = divmod(num, base)
        result = value_to_char[rest] + result
    return result
 
def main():
    while True:
        try:
            menge = input("Bitte Zahl eingeben (oder 'exit' zum Beenden): ")
            if menge.lower() == "exit":
                break
            systemzahl = input("Aus welchem Zahlensystem? (2–36, Enter = 10): ")
            systemzahl = int(systemzahl) if systemzahl else 10
 
            dezimal = from_base(menge, systemzahl)
            print("Dezimal:", dezimal)
 
            zielsystem = int(input("In welches Zahlensystem umrechnen? (2–36): "))
            ergebnis = to_base(dezimal, zielsystem)
            print("Ergebnis:", ergebnis)
        except Exception as e:
            print("Fehler:", e)
 
if __name__ == "__main__":
    main()
