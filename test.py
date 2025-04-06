# Hier sollen die Klassen aufgerufen und ausgegeben werden.
from datetime import date
from my_classes import Subject, Supervisor, Experiment

# Subject und Supervisor mit Geburtsdatum erstellen
subject1 = Subject(
    name="Simon",
    geburtsdatum=date(2001, 8, 2),
    gewicht=63,
    groesse=183,
    geschlecht="männlich"
)

supervisor1 = Supervisor(
    name="Gabriel",
    geburtsdatum=date(2000, 1, 1),
    department="Sporttechnologie",
    email="gabriel@example.com"
)

experiment1 = Experiment(
    experiment_id="EXP002",
    subject=subject1,
    supervisor=supervisor1,
    datum="2025-04-06",
    beschreibung="Leistungsergometer-Test"
)

# Ausgabe zur Kontrolle
print(f"Alter des Subjects: {subject1.berechne_alter()} Jahre")
print(f"Maximale Herzfrequenz: {subject1.estimate_max_hr()} bpm")
print(f"Supervisor: {supervisor1.name}, Alter: {supervisor1.berechne_alter()}")

