from tests.conftest import client
from datetime import datetime


def test_cannot_take_places_from_past_competition(
    client,
    first_club_fixture,
    firt_competition_past_fixture
):
    loggin = client.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
    response = client.post(
        '/purchasePlaces',
        data=dict(
            club=first_club_fixture['name'],
            competition=firt_competition_past_fixture['name'],
            places=3
        )
    )
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find("This competition is no more available.") != -1


def test_can_take_places_from_post_competition(client, first_club_fixture,second_competition_post_fixture):
	loggin = client.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
	response = client.post(
		'/purchasePlaces',
		data=dict(
			club=first_club_fixture['name'],
			competition=second_competition_post_fixture['name'],
			places=3
		)
	)

	assert response.status_code == 200
	data = response.data.decode()
	assert data.find('Great-booking complete!') != -1


def test_cannot_access_to_past_competition(client, first_club_fixture,firt_competition_past_fixture):
	loggin = client.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
	response = client.get(f"/book/{firt_competition_past_fixture['name']}/{first_club_fixture['name']}")
	assert response.status_code == 200
	data = response.data.decode()
	assert data.find("This competition is closed.") != -1

def test_can_access_to_post_competition(client, first_club_fixture, second_competition_post_fixture):
	loggin = client.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
	response = client.get(f"/book/{second_competition_post_fixture['name']}/{first_club_fixture['name']}")
	assert response.status_code == 200
