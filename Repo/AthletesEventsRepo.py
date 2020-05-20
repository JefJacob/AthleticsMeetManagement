from Repo.DBConn import DBConn
from Entities.AthletesEventsEntity import AthletesEventsEntity


def get_athletes_events_id(eventname, eventgender, eventdivision, eventround):
    with DBConn() as connection:
        cursor=connection.cursor()
        cursor.execute('Select * from AthleteEvents with (nolock) where eventname=? and eventgender=? and eventdivision=? and eventround=?',(eventname, eventgender, eventdivision, eventround))
        row = cursor.fetchone()
        if row:
            athleteevents = AthletesEventsEntity(row.EventId,row.EventName,row.EventGender,row.EventDivision,row.EventRound)
        else:
            athleteevents=None
    return athleteevents



def get_athletes_event(event_id):
    with DBConn() as connection:
        cursor=connection.cursor()
        cursor.execute('Select * from AthleteEvents where EventId=?', event_id)
        row = cursor.fetchone()
        if row:
            athleteevent = AthletesEventsEntity(row.EventId,row.EventName,row.EventGender,row.EventDivision,row.EventRound)
        else:
            athleteevent=None
    return athleteevent


def get_all_events(comp_id):
    with DBConn() as connection:
        cursor = connection.cursor()
        cursor.execute('Select distinct ae.EventId,ae.EventName,ae.EventGender,ae.EventDivision, ae.EventRound from AthleteEvents ae inner join Results r on ae.EventId = r.EventId and CompId=? order by ae.EventName', comp_id)
        athleteevents = [AthletesEventsEntity(row.EventId,row.EventName,row.EventGender,row.EventDivision,row.EventRound) for row in  cursor.fetchall()]
    return athleteevents


def get_masterlist():
    with DBConn() as connection:
        cursor = connection.cursor()
        cursor.execute('Select * from AthleteEventListAll ')
        masterlist = [row.EventName for row in  cursor.fetchall()]
    return masterlist


def get_event_rounds():
    with DBConn() as connection:
        cursor = connection.cursor()
        cursor.execute('Select distinct EventDivision from AthleteEvents')
        event_division = [row.EventDivision for row in  cursor.fetchall()]
    return event_division


def add_athletes_event(athletesevent):
    with DBConn() as connection:
        cursor = connection.cursor()
        aevent = get_athletes_events_id(athletesevent.EventName,athletesevent.EventGender,athletesevent.EventDivision,athletesevent.EventRound)
        if not aevent:
            cursor.execute('insert into AthleteEvents(EventName	,EventGender	,EventDivision	,EventRound) values(?,?,?,?) ',(athletesevent.EventName	,athletesevent.EventGender	,athletesevent.EventDivision	,athletesevent.EventRound))
    return get_athletes_events_id(athletesevent.EventName	,athletesevent.EventGender	,athletesevent.EventDivision	,athletesevent.EventRound)
# print(get_athletes_events_id('100 Meters Dash','Women','Open','P'))

def get_events_masterlist():
    with DBConn() as connection:
        cursor=connection.cursor()
        cursor.execute('Select EventName from AthleteEventListAll')
        masterlist =[row for row in cursor.fetchall()]
    return masterlist


def delete_event(comp_id,event_id):
    with DBConn() as connection:
        cursor = connection.cursor()
        cursor.execute('Delete from results where CompId=? and EventId=?',(comp_id,event_id))


# print(get_events_masterlist())