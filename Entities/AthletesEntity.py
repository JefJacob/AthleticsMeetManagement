class AthletesEntity:
    def __init__(self, athleteid, acnum, firstname, lastname, dob):
        self.AthleteId = athleteid
        self.ACNum = acnum
        self.FirstName = firstname
        self.LastName = lastname
        self.DOB = dob

    def __repr__(self):
        return f'{self.AthleteId} -> {self.ACNum} -> {self.FirstName} -> {self.LastName}'
