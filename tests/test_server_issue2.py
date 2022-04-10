from tests.conftest import client

"""
Issue 2 : BUG: Clubs should not be able to use more than their points allowed
/book/<competition>/<club>
"""
"""
ISSUE5 :
Changement du test à cause de l'implémentation du controle de la date des compétitions
Il n'est plus possible d'accéder à une compétition terminée
Modification :
    - changement de la ficture: firt_competition_past_fixture -> second_competition_post_fixture
"""
def test_success_booking_places(client, first_club_fixture, second_competition_post_fixture):
	loggin = client.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
	response = client.post(
		'/purchasePlaces',
		data=dict(
			club=first_club_fixture['name'],
			competition=second_competition_post_fixture['name'],
			places=5
		)
	)
	assert response.status_code == 200
	data = response.data.decode()
	assert data.find("Great-booking complete!") != -1
	
def test_cant_take_more_than_possible_places(client, first_club_fixture, second_competition_post_fixture):
	loggin = client.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
	maximum_places = second_competition_post_fixture['numberOfPlaces']

	response = client.post(
		'/purchasePlaces',
		data=dict(
			club=first_club_fixture['name'],
			competition=second_competition_post_fixture['name'],
			places=int(maximum_places) + 1
		)
	)
	assert response.status_code == 200
	data = response.data.decode()
	assert data.find("Not enough point available.") != -1


def test_required_places_is_negative(client, first_club_fixture, second_competition_post_fixture):
	loggin = client.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
	response = client.post(
		'/purchasePlaces',
		data=dict(
			club=first_club_fixture['name'],
			competition=second_competition_post_fixture['name'],
			places=-1
		)
	)
	assert response.status_code == 200
	data = response.data.decode()
	assert data.find('Please, enter a positive number') != -1