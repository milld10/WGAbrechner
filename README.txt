WG Abrechnungsprogramm
----------------------

Aufbau von .txt-Datei:
|-----------|
|t 3.45 tceo|
|-----------|

t     Einkäufer
3.45  Betrag, welcher der Einkäufer ausgegeben hat
tceo  Personen, durch die der Betrag geteilt wird

Pro Betrag wird eine Zeile ausgefüllt nach diesem Schema, abgespeichert und richtiger Name der Datei im source code übertragen, sodass Programm richtiges Dokument zur Abrechnung verwendet. -> In Zeile 27 ändern!

Ausführen in der Konsole mit:
$ python abrechnerOETC.py