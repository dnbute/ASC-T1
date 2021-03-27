Nume: Bute Dragoș-Cristian
Grupă: 332CA

## Tema 1

# Descrierea generală

**Producer**
Producer-ul parcurge lista sa de produse iar pentru fiecare produs
incearcă să îl introducă in market, repetand acest lucru de un numar de ori pentru fiecare produs.
Dacă reușește trece mai departe după un timp predefinit per produs,
iar daca nu, reincearcă dupa un alt timp stabilit la initializarea thread-ului

**Consumer**
Fiecare consumer parcurge coșurile sale, adaugând sau scoțând produse în/din acesta.
Operatiile acestea sunt repetate de un numar de ori specific operației respective,
consumer-ul fiind nevoit să aștepte o scurtă perioadă de timp dacă adăugarea în coș
eșuează, similar producer-ului

**Marketplace**
Marketplace-ul coordonează interacțiunea dintre consumeri și produceri.
Acesta înregistrează producătorii și le primește produsele pănă la o anumită
limita per producător.
Acesta de asemenea pune la dispoziția consumatorilor produsele din market, în același
timp oferind consumatorilor coșurile necesare.

* Este destul de lentă soluția din punctul meu de vedere însă trece testele


# Implementare


* Toată tema a fost implementată
* Cea mai grea parte a fost înțelegerea enunțului + deslușirea scheletului



# Resurse utilizate

* Laboratoarele de ASC în general
* Documentația Python
* Probabil Stack Overflow însă nu țin minte exemple concrete



# Git

https://github.com/dnbute/ASC-T1 - Momentan privat, îl fac public după deadline-ul hard
