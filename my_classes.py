from datetime import date

class Person:
    def __init__(self, name, geburtsdatum):  # Geburtsdatum: datetime.date
        self.name = name
        self.__geburtsdatum = geburtsdatum  # privates Attribut

    def berechne_alter(self):
        heute = date.today()
        alter = heute.year - self.__geburtsdatum.year - (
            (heute.month, heute.day) < (self.__geburtsdatum.month, self.__geburtsdatum.day)
        )
        return alter

    def get_geburtsdatum(self):
        return self.__geburtsdatum


class Subject(Person):
    def __init__(self, name, geburtsdatum, gewicht, groesse, geschlecht):
        super().__init__(name, geburtsdatum)
        self.gewicht = gewicht
        self.groesse = groesse
        self.geschlecht = geschlecht

    def estimate_max_hr(self):
        alter = self.berechne_alter()
        return 220 - alter


class Supervisor(Person):
    def __init__(self, name, geburtsdatum, department, email):
        super().__init__(name, geburtsdatum)
        self.department = department
        self.email = email


class Experiment:
    def __init__(self, experiment_id, subject, supervisor, datum, beschreibung):
        self.experiment_id = experiment_id
        self.subject = subject
        self.supervisor = supervisor
        self.datum = datum
        self.beschreibung = beschreibung

