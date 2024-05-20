class BirthdayTracker:
    def __init__(self):
        self.birthday_tracker = []

    def add(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

        entry = {self.name: self.birthdate}
        self.birthday_tracker.append(entry)
        
    def view_all(self):
        return self.birthday_tracker
    
    def update_birthdate(self, name, newbirthdate):
        for key in self.birthday_tracker:
            if key.keys() == name:
                self.birthday_tracker[key] = newbirthdate
        return self.birthday_tracker