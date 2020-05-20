class AthleteResultsEntity:
    def __init__(self,acnum,firstname,lastname,dob,compid,eventid,athleteid, mark, position, wind):
        self.ACNum = acnum
        self.FirstName = firstname
        self.LastName = lastname
        self.DOB = dob
        self.CompId = compid
        self.EventId = eventid
        self.AthleteId = athleteid
        self.Mark = mark
        self.Position = position
        self.Wind = wind

    def __repr__(self):
        return f'CompetitionId: {self.CompId} -> EventId: {self.EventId} -> AthleteId: {self.AthleteId} -> Mark: {self.Mark} -> Position: {self.Position} -> Wind: {self.Wind} '