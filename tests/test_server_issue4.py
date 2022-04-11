from tests.conftest import client


"""
Issue 2 : BUG: Clubs should not be able to use more than their points allowed
/book/<competition>/<club>
"""


def test_cant_take_more_than_twelve_places(client, first_club_fixture, firt_competition_past_fixture):
    login = client.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
    assert login.status_code == 200

    response = client.post(
        '/purchasePlaces',
        data=dict(
            club=first_club_fixture['name'],
            competition=firt_competition_past_fixture['name'],
            places=13
        )
    )
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find("You can order maximum 12 places.") != -1


def test_cant_take_more_than_twelve_places_with_many_tries(client, first_club_fixture, firt_competition_past_fixture):
    login = client.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
    assert login.status_code == 200

    response = client.post(
        '/purchasePlaces',
        data=dict(
            club=first_club_fixture['name'],
            competition=firt_competition_past_fixture['name'],
            places=10
        )
    )

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

    assert data.find("You can order maximum 12 places.") != -1
