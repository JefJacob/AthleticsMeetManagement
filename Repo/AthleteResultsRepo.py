from Repo.DBConn import DBConn
from Entities.AthleteResultsEntity import AthleteResultsEntity


def get_all_athlete_results(comp_id, event_id):
    with DBConn() as connection:
        cursor = connection.cursor()
        cursor.execute('Select distinct a.ACNum,a.FirstName,a.LastName,a.DOB,r.CompId,r.EventId,r.AthleteId,r.Mark,r.Position,r.Wind from Athletes a inner join Results r on a.AthleteId = r.AthleteId and CompId=? and EventId=?', (comp_id,event_id))
        athleteresults = [AthleteResultsEntity(row.ACNum,row.FirstName,row.LastName,row.DOB,row.CompId,row.EventId,row.AthleteId,row.Mark,row.Position,row.Wind) for row in  cursor.fetchall()]
    return athleteresults