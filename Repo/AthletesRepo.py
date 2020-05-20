from Repo.DBConn import DBConn
from Entities.AthletesEntity import AthletesEntity

def get_athlete(ACNum):
    with DBConn() as connection:
        cursor=connection.cursor()
        cursor.execute('Select * from Athletes where ACNum=?',ACNum)
        row = cursor.fetchone()
        if row:
            athletes = AthletesEntity(row.AthleteId,row.ACNum,row.FirstName,row.LastName, row.DOB)
        else:
            athletes = None
    return athletes

# print(get_athleteId('7192687'))
