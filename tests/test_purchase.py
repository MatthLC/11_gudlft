from tests.conftest import client


"""
/purchasePlaces
"""


def test_purchaseplaces_should_status_code_ok(client, first_club_fixture, firt_competition_past_fixture):
    response = client.post(
        '/purchasePlaces',
        data=dict(
            club=first_club_fixture['name'],
            competition=firt_competition_past_fixture['name'],
            places=3
        )
    )
    assert response.status_code == 200


def test_purchaseplaces_user_is_logged_in(client, first_club_fixture, firt_competition_past_fixture):
    login = client.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
    assert login.status_code == 200
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
    assert data.find('Welcome, ' + first_club_fixture['email']) != -1


def test_purchaseplaces_user_is_not_logged_in(client, first_club_fixture, firt_competition_past_fixture):
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
    assert data.find("You are not logged in") != -1


def test_purchaseplaces_display_flash_message_after_buying_places(
    client,
    first_club_fixture,
    firt_competition_past_fixture
):
    login = client.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
    assert login.status_code == 200
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
    assert data.find("Great-booking complete!") != -1
