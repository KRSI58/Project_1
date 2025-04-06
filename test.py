# Hier sollen die Klassen aufgerufen und ausgegeben werden.
from my_classes import Subject, Supervisor, Experiment

# Beispielhafte Testdaten
subject1 = Subject(subject_id="S001", age=25, weight=75, height=180, gender="male")
supervisor1 = Supervisor(name="Dr. Müller", department="Sportwissenschaft", email="mueller@example.com")

experiment1 = Experiment(
    experiment_id="EXP001",
    subject=subject1,
    supervisor=supervisor1,
    date="2025-04-06",
    description="Laufband-Stufentest"
)

# Ausgabe zur Kontrolle
print(f"Experiment-ID: {experiment1.experiment_id}")
print(f"Teilnehmer: {experiment1.subject.subject_id}, Alter: {experiment1.subject.age}")
print(f"Supervisor: {experiment1.supervisor.name}, Email: {experiment1.supervisor.email}")
print(f"Geschätzte max. Herzfrequenz: {experiment1.subject.estimate_max_hr()} bpm")
