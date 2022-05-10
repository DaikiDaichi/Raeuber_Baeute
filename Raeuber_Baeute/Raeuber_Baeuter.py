# Gegebene Werte:

anzahlKaninchen = 1000
anzahlFuechse = 40
zuwachsrateKaninchen = 0.08
abnahmerateFuechse = 0.2
abnahmerateKaninchenFuchs = 0.002
zunahmerateFuchsKaninchen = 0.0004

# Aufgabe 1+2

NeueAnzahlKaninchen = anzahlKaninchen + anzahlKaninchen * zuwachsrateKaninchen
NeueAnzahlFuechse = anzahlFuechse - abnahmerateFuechse * anzahlFuechse

print(NeueAnzahlKaninchen, "\n", NeueAnzahlFuechse, "\n")

# ======================================================================================================================

# Aufgabe 3

neueAnzahlKaninchen = anzahlKaninchen + (zuwachsrateKaninchen * anzahlKaninchen) - (abnahmerateKaninchenFuchs *
                                                                                    anzahlKaninchen * anzahlFuechse)

neueAnzahlFuechse = anzahlFuechse - (abnahmerateFuechse * anzahlFuechse) + (zunahmerateFuchsKaninchen * anzahlFuechse *
                                                                            anzahlKaninchen)

print(neueAnzahlKaninchen, "\n", neueAnzahlFuechse, "\n")


# ======================================================================================================================

# Aufgabe 4

def popKa5Schritte(anzKa, zKa):
    neueAnzKa = anzKa
    neueAnzKa = neueAnzKa + zKa * neueAnzKa
    neueAnzKa = neueAnzKa + zKa * neueAnzKa
    neueAnzKa = neueAnzKa + zKa * neueAnzKa
    neueAnzKa = neueAnzKa + zKa * neueAnzKa
    neueAnzKa = neueAnzKa + zKa * neueAnzKa
    return neueAnzKa


print(popKa5Schritte(anzahlKaninchen, zuwachsrateKaninchen))


def popKa5Schritte2(anzKa, zKa):
    schritte = 5
    zaehler = 0
    neueAnzKa = anzKa
    while zaehler < schritte:
        neueAnzKa = neueAnzKa + zKa * neueAnzKa
        zaehler = zaehler + 1
    return neueAnzKa


print(popKa5Schritte2(anzahlKaninchen, zuwachsrateKaninchen), "\n")

# ----------------------------------------------------------------------------------------------------------------------

schritte = int(input("Geben Sie die Anzahl der Wiederholungen an: "))

def popKaSchritte(anzKa, zKa, schritte):
    neueAnzKa = anzKa
    for i in range(schritte):
        neueAnzKa = neueAnzKa + zKa * neueAnzKa
    neueAnzKa = round(neueAnzKa)
    return neueAnzKa

print(popKaSchritte(anzahlKaninchen, zuwachsrateKaninchen, schritte))

