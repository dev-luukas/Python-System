vokabel = {
    "dux, ducis": "der Anführer",
    "what": "was"
}

def ask():
    while True:
        for wort, bedeutung in vokabel.items():
            userinput = input(f"Was bedeutet '{wort}'? ").strip().lower()
        if userinput == bedeutung.lower():
            print("Richtig!")
        else:
            print(f"Falsch! Die richtige Antwort ist: {bedeutung}")

ask()
