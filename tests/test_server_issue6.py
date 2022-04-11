from tests.conftest import client


def test_cant_access_booking_if_no_point(client, third_club_fixture, second_competition_post_fixture):

    login = client.post('/showSummary', data=dict(email=third_club_fixture['email']), follow_redirects=True)
    assert login.status_code == 200
    booking = client.post(
        '/purchasePlaces',
        data=dict(
            club=third_club_fixture['name'],
            competition=second_competition_post_fixture['name'],
            places=1
        )
    )
    assert booking.status_code == 200
    response = client.get(f"/book/{second_competition_post_fixture['name']}/{third_club_fixture['name']}")
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find('Your cannot book places anymore. You are out of points') != -1
