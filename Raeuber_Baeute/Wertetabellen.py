# Anfangswerte
anzahlKaninchen = 1000
anzahlFuechse = 40

# feste Werte
zuwachsrateKaninchen = 0.08
abnahmerateFuechse = 0.2
abnahmerateKaninchenFuchs = 0.002
zunahmerateFuchsKaninchen = 0.0004


# Funktionen
def popKa(schritte, anzKa, zKa):
    neueAnzKa = anzKa
    for i in range(schritte):
        neueAnzKa = neueAnzKa + zKa * neueAnzKa
    neueAnzKa = round(neueAnzKa)
    return neueAnzKa


def popFu(schritte, anzFu, zFu):
    neueAnzFu = anzFu
    for i in range(schritte):
        neueAnzFu = neueAnzFu - zFu * neueAnzFu
    neueAnzFu = round(neueAnzFu)
    return neueAnzFu


def popKaFu(schritte, anzKa, zKa, abKaFu, anzFu, abFu, zuFuKa):
    NanzKa = anzKa
    NAnzFu = anzFu
    for i in range(schritte):
        NanzKa = NanzKa + zKa * NanzKa - abKaFu * NanzKa * NAnzFu
        NAnzFu = NAnzFu - abFu * NAnzFu + zuFuKa * NAnzFu * anzahlKaninchen

    NanzKa = round(NanzKa)
    NAnzFu = round(NAnzFu)

    return NanzKa, NAnzFu


# Hauptprogramm
schritte = int(input("Geben Sie die Anzahl der Wiederholungen an: "))

popKa = popKa(schritte, anzahlKaninchen, zuwachsrateKaninchen)
popFu = popFu(schritte, anzahlFuechse, abnahmerateFuechse)
KapopKaFu, FupopKaFu = popKaFu(schritte, anzahlKaninchen, zuwachsrateKaninchen, abnahmerateKaninchenFuchs, anzahlFuechse,
                               abnahmerateFuechse, zunahmerateFuchsKaninchen)

print(popKa, "\n", popFu, "\n", KapopKaFu, "\n", FupopKaFu)
