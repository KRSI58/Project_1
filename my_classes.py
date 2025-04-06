class Subject:
    def __init__(self, subject_id, age, weight, height, gender):
        self.subject_id = subject_id
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender

    def estimate_max_hr(self):
        # Klassische Formel: 220 - Lebensalter
        return 220 - self.age


class Supervisor:
    def __init__(self, name, department, email):
        self.name = name
        self.department = department
        self.email = email


class Experiment:
    def __init__(self, experiment_id, subject, supervisor, date, description):
        self.experiment_id = experiment_id
        self.subject = subject
        self.supervisor = supervisor
        self.date = date
        self.description = description
