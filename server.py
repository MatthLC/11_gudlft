import json
from flask import Flask, render_template, request, redirect, flash, url_for, session


"""
Listing all data to read
"""
DATA_CLUBS = 'clubs' 
DATA_COMPETITIONS = 'competitions'
TEST_DATA_CLUBS = 'test_clubs' 
TEST_DATA_COMPETITIONS = 'test_competitions'

"""
Changed the two function 'loadClubs' & 'loadCompetitions' to 'loadFile'.
parameter : 
 - file_name : Json data name

The list name has the same name as the Json fine.
"""
def loadFile(file_name):
    with open(file_name + '.json') as file:
        data = json.load(file)[file_name]
        return data


"""
Changed the building with 'def create_app'
"""
def create_app(config={}):

    app = Flask(__name__)
    app.config.from_object(config)

    #Set 'TESTING' to True when testing
    app.config.update(config)

    app.secret_key = 'something_special'
    
    
    # Changed the method to have the possibility to apply test on fake database
    if app.config['TESTING'] == True:
        competitions= loadFile(TEST_DATA_COMPETITIONS)
        clubs = loadFile(TEST_DATA_CLUBS)
    else:
        competitions = loadFile(DATA_COMPETITIONS)
        clubs = loadFile(DATA_CLUBS)


    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/showSummary',methods=['POST'])
    def showSummary():
        # Issue 1 : ERROR entering a unknown email crashes the app
        try:
            club = [club for club in clubs if club['email'] == request.form['email']][0]
        except:
            return (render_template('index.html', error="Sorry, that email is not found."), 403)

        # Init user session to check if the user is logged in
        session['username'] = request.form['email']

        return render_template('welcome.html',club=club,competitions=competitions)


    @app.route('/book/<competition>/<club>')
    def book(competition,club):
        if 'username' in session:
            foundClub = [c for c in clubs if c['name'] == club][0]
            foundCompetition = [c for c in competitions if c['name'] == competition][0]
            if foundClub and foundCompetition:
                return render_template('booking.html',club=foundClub,competition=foundCompetition)
            else:
                flash("Something went wrong-please try again")
                return render_template('welcome.html', club=club, competitions=competitions)
        return 'You are not logged in'


    @app.route('/purchasePlaces',methods=['POST'])
    def purchasePlaces():
        if 'username' in session:
            competition = [c for c in competitions if c['name'] == request.form['competition']][0]
            club = [c for c in clubs if c['name'] == request.form['club']][0]
            placesRequired = int(request.form['places'])
            competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
            flash('Great-booking complete!')
            return render_template('welcome.html', club=club, competitions=competitions)
        return 'You are not logged in'


    # TODO: Add route for points display


    @app.route('/logout')
    def logout():
        session.pop('username', None)
        return redirect(url_for('index'))

    return app
