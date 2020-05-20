from flask import Flask, render_template, request, redirect, url_for
from Repo import CompetitionsRepo, AthletesEventsRepo, AthleteResultsRepo, AthletesRepo, ResultsRepo
from Entities import CompetitionsEntity, AthletesEventsEntity, AthleteResultsEntity, ResultsEntity
app = Flask(__name__)


@app.route('/')
def home():
    competitions = CompetitionsRepo.get_all_competitions()
    return render_template('viewCompetitions.jinja2', competitions=competitions)


@app.route('/events/<int:comp_id>')
def view_events(comp_id):
    athlete_events = AthletesEventsRepo.get_all_events(comp_id)
    competition = CompetitionsRepo.get_competition(comp_id)
    return render_template('viewEvents.jinja2', athlete_events=athlete_events, competition=competition)


@app.route('/athletes/<int:comp_id>/<event_id>')
def view_athlete_results(comp_id, event_id):
    athlete_results = AthleteResultsRepo.get_all_athlete_results(comp_id, event_id)
    competition = CompetitionsRepo.get_competition(comp_id)
    athlete_event = AthletesEventsRepo.get_athletes_event(event_id)
    return render_template('viewAthleteResults.jinja2', athlete_event=athlete_event, competition=competition, athlete_results=athlete_results)


@app.route('/competitions/create', methods=['GET', 'POST'])
def create_competition():
    if request.method == 'POST':
        compname = request.form.get('compname')
        compsubname = request.form.get('compsubname')
        start = request.form.get('start')
        end = request.form.get('end')
        facility = request.form.get('facility')
        location = request.form.get('location')
        ctype = request.form.get('ctype')
        csubtype = request.form.get('csubtype')
        season = request.form.get('season')
        competition = CompetitionsEntity.CompetitionsEntity('0',compname,compsubname,start,end,facility,location,ctype,csubtype,season)
        CompetitionsRepo.add_competition(competition)
        return redirect(url_for('home'))
    return render_template('createCompetitions.jinja2')


@app.route('/events/create/<int:comp_id>', methods=['GET', 'POST'])
def create_event(comp_id):
    if request.method == 'POST':
        ename = request.form.get('ename')
        egender = request.form.get('egender')
        edivision = request.form.get('edivision')
        eround = request.form.get('eround')
        enote = request.form.get('enote')
        athlete_event = AthletesEventsEntity.AthletesEventsEntity(0, ename+" "+enote if enote  else ename,egender, edivision, eround)
        new_athlete_event = AthletesEventsRepo.add_athletes_event(athlete_event)
        return redirect(url_for('view_athlete_results', comp_id=comp_id,event_id=new_athlete_event.EventId))
    competition = CompetitionsRepo.get_competition(comp_id)
    masterlist = AthletesEventsRepo.get_masterlist()
    event_division = AthletesEventsRepo.get_event_rounds()
    return render_template('createEvents.jinja2', competition=competition, masterlist=masterlist, event_division=event_division)


@app.route('/athletes/create/<int:comp_id>/<event_id>', methods=['GET', 'POST'])
def create_athlete_result(comp_id,event_id):
    if request.method == 'POST':
        competition = CompetitionsRepo.get_competition(comp_id)
        athlete_event = AthletesEventsRepo.get_athletes_event(event_id)
        acnum = request.form.get('acnum')
        athlete = AthletesRepo.get_athlete(acnum)
        if not athlete:
            return render_template('createAthleteResults.jinja2', competition=competition, athlete_event=athlete_event, message="Invalid AC Number")
        mark = request.form.get('mark')
        position = request.form.get('position')
        wind = request.form.get('wind')
        # athlete_result = AthleteResultsEntity.AthleteResultsEntity(acnum, athlete.FirstName, athlete.LastName, athlete.DOB, mark, position, wind)
        results = ResultsEntity.ResultsEntity(competition.CompId, athlete_event.EventId, athlete.AthleteId, mark, position, wind)
        ResultsRepo.add_results(results)
        return redirect(url_for('view_athlete_results', comp_id=comp_id, event_id=athlete_event.EventId))
    competition = CompetitionsRepo.get_competition(comp_id)
    athlete_event = AthletesEventsRepo.get_athletes_event(event_id)
    return render_template('createAthleteResults.jinja2', competition=competition, athlete_event=athlete_event)


@app.route('/', methods=['POST'])
def delete_competition():
    compid = request.form.get('compid')
    CompetitionsRepo.delete_competition(compid)
    competitions = CompetitionsRepo.get_all_competitions()
    return render_template('viewCompetitions.jinja2', competitions=competitions)


@app.route('/events/<int:comp_id>', methods=['POST'])
def delete_event(comp_id):
    event_id = request.form.get('event_id')
    AthletesEventsRepo.delete_event(comp_id, event_id)
    athlete_events = AthletesEventsRepo.get_all_events(comp_id)
    competition = CompetitionsRepo.get_competition(comp_id)
    return render_template('viewEvents.jinja2', athlete_events=athlete_events, competition=competition)


@app.route('/athletes/<int:comp_id>/<event_id>', methods=['POST'])
def delete_athlete_result(comp_id, event_id):
    athlete_id = request.form.get('athlete_id')
    ResultsRepo.delete_results(comp_id, event_id, athlete_id)
    athlete_results = AthleteResultsRepo.get_all_athlete_results(comp_id, event_id)
    competition = CompetitionsRepo.get_competition(comp_id)
    athlete_event = AthletesEventsRepo.get_athletes_event(event_id)
    return render_template('viewAthleteResults.jinja2', athlete_event=athlete_event, competition=competition,
                           athlete_results=athlete_results)


if __name__ == '__main__':
    app.run(debug=True)


