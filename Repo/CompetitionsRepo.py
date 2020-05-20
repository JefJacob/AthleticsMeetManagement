from Repo.DBConn import DBConn
from Entities.CompetitionsEntity import CompetitionsEntity

def get_competition_id(compname):
    with DBConn() as connection:
        cursor = connection.cursor()
        cursor.execute('Select * from Competitions where compname=?',compname)
        row = cursor.fetchone()
        if row:
            competitions = CompetitionsEntity(row.CompId,row.CompName,row.CompSubName,row.StartDate,row.EndDate,row.Facility,row.Location,row.CompType,row.CompSubType,row.Season)
        else:
            competitions='No Data'
    return competitions


def get_competition(compid):
    with DBConn() as connection:
        cursor = connection.cursor()
        cursor.execute('Select * from Competitions where CompId=?',compid)
        row = cursor.fetchone()
        if row:
            competitions = CompetitionsEntity(row.CompId,row.CompName,row.CompSubName,row.StartDate,row.EndDate,row.Facility,row.Location,row.CompType,row.CompSubType,row.Season)
        else:
            competitions='No Data'
    return competitions


def get_all_competitions():
    with DBConn() as connection:
        cursor = connection.cursor()
        cursor.execute('Select * from Competitions ')
        # row = cursor.fetchall()
        # if row:
        competitions = [CompetitionsEntity(row.CompId,row.CompName,row.CompSubName,row.StartDate,row.EndDate,row.Facility,row.Location,row.CompType,row.CompSubType,row.Season) for row in  cursor.fetchall()]
        # else:
        #     competitions='No Data'
    return competitions


def add_competition(competition):
    with DBConn() as connection:
        cursor = connection.cursor()
        cursor.execute('insert into competitions(CompName	,CompSubName	,StartDate	,EndDate	,Facility	,Location	,CompType	,CompSubType	,Season ) values(?,?,?,?,?,?,?,?,?)',(	competition.CompName,	competition.CompSubName	,competition.StartDate	,competition.EndDate	,competition.Facility	,competition.Location	,competition.CompType	,competition.CompSubType	,competition.Season))
    return get_competition_id(competition.CompName)


def delete_competition(comp_id):
    with DBConn() as connection:
        cursor = connection.cursor()
        cursor.execute('delete from results where CompId=?',comp_id)
        cursor.execute('delete from competitions where CompId=?', comp_id)

# print(get_competition_id('GenericData-Athletics Ontario Outdoor Championship Series #3- U20 - Open Championships-12Jul2019-002'))
# print(add_competition(CompetitionsEntity(0,'test','','2019-07-12','2019-07-14','Toronto Track and Field Centre','Ontario','I','S','O')))