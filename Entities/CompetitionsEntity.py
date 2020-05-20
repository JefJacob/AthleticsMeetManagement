class CompetitionsEntity:
    def __init__(self, compid, compname, compsubname, startdate, enddate, facility, location, comptype, compsubtype, season):
        self.CompId = compid
        self.CompName = compname
        self.CompSubName = compsubname
        self.StartDate = startdate
        self.EndDate = enddate
        self.Facility = facility
        self.Location = location
        self.CompType = comptype
        self.CompSubType = compsubtype
        self.Season = season

    def __repr__(self):
        return f'{self.CompId} -> {self.CompName} -> {self.CompSubName} -> {self.StartDate} -> {self.EndDate} -> {self.Facility} -> {self.Location} -> {self.CompType} -> {self.CompSubType}  -> {self.Season}'