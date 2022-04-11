from tests.conftest import client
from server import loadFile


def test_home_should_status_code_ok(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find('Welcome to the GUDLFT Registration Portal!') != -1


"""
/showSummary
"""


def test_summary_login_user_success(client, first_club_fixture):
    response = client.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find('Please enter your secretary email to continue') == -1
    assert data.find('Welcome, ' + first_club_fixture['email']) != -1


def test_summary_loadFile_success(file_name_of_data_test, first_club_fixture, firt_competition_past_fixture):
    test_clubs = loadFile(file_name_of_data_test['TEST_DATA_CLUBS'])
    test_competitions = loadFile(file_name_of_data_test['TEST_DATA_COMPETITIONS'])
    assert test_clubs[0] == first_club_fixture
    assert test_competitions[0] == firt_competition_past_fixture


def test_summary_display_competition_successfully(client, first_club_fixture, firt_competition_past_fixture):
    response = client.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find(firt_competition_past_fixture['name']) != -1
    assert data.find('Number of Places: ' + firt_competition_past_fixture['numberOfPlaces']) != -1


"""
/book/<competition>/<club>
"""


def test_book_should_status_code_ok(client, first_club_fixture, firt_competition_past_fixture):
    login = client.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
    assert login.status_code == 200
    response = client.get(f"/book/{firt_competition_past_fixture['name']}/{first_club_fixture['name']}")
    assert response.status_code == 200


def test_book_user_is_logged_in(client, first_club_fixture, firt_competition_past_fixture):
    login = client.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
    assert login.status_code == 200
    response = client.get(f"/book/{firt_competition_past_fixture['name']}/{first_club_fixture['name']}")
    data = response.data.decode()
    assert response.status_code == 200
    assert data.find(firt_competition_past_fixture['name']) != -1


def test_book_user_is_not_logged_in(client, first_club_fixture, firt_competition_past_fixture):
    response = client.get(f"/book/{firt_competition_past_fixture['name']}/{first_club_fixture['name']}")
    data = response.data.decode()
    assert response.status_code == 200
    assert data.find("You are not logged in") != -1


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


"""
ISSUE5 :
Changement du test à cause de l'implémentation du controle de la date des compétitions
Il n'est plus possible d'accéder à une compétition terminée
Modification :
    - changement de la ficture: firt_competition_past_fixture -> second_competition_post_fixture
    - Ajout d'un nouveau test si la compétition est terminée dans test_server_issue5.py
"""


def test_purchaseplaces_display_flash_message_after_buying_places_on_post_competition(
    client,
    first_club_fixture,
    second_competition_post_fixture
):
    login = client.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
    assert login.status_code == 200
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
    assert data.find("Great-booking complete!") != -1
