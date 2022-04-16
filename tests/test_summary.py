from tests.conftest import client


"""
/showSummary
"""


def test_summary_login_user_success(client, first_club_fixture):
    response = cslient.post('/showSummary', data=dict(email=first_club_fixture['email']), follow_redirects=True)
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
