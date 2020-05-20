class AthletesEventsEntity:
    def __init__(self, eventid, eventname, eventgender, eventdivision, eventround):
        self.EventId = eventid
        self.EventName = eventname
        self.EventGender = eventgender
        self.EventDivision = eventdivision
        self.EventRound = eventround

    def __repr__(self):
        return f'{self.EventId} -> {self.EventName} -> {self.EventGender} -> {self.EventDivision} -> {self.EventRound} '
