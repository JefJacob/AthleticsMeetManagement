from Repo.DBConn import DBConn
from Entities.ResultsEntity import ResultsEntity

def get_results(athleteid, compid, eventid):
    with DBConn() as connection:
        cursor=connection.cursor()
        cursor.execute('Select * from Results where athleteid=? and compid=? and eventid=?',(athleteid, compid, eventid))
        row = cursor.fetchone()
        if row:
            results = ResultsEntity(row.CompId,row.EventId,row.AthleteId,row.Mark,row.Position,row.Wind)
        else:
            results=None
    return results

def add_results(results):
    with DBConn() as connection:
        cursor = connection.cursor()
        cursor.execute('Insert into results(CompId	,EventId	,AthleteId	,Mark	,Position	,Wind) values (?,?,?,?,?,?)',(results.CompId	,results.EventId	,results.AthleteId	,results.Mark	,results.Position	,results.Wind))


def delete_results(comp_id, event_id, athlete_id):
    with DBConn() as connection:
        cursor = connection.cursor()
        cursor.execute('Delete from results where CompId=? and EventId=? and AthleteId=?', (comp_id, event_id, athlete_id))



# print(get_results(3340,2001,4162))