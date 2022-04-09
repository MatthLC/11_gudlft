import pytest

from server import create_app


@pytest.fixture
def client():
	app = create_app({'TESTING': True})
	with app.test_client() as client:
		yield client

@pytest.fixture
def club_fixture_first_user():
	club_data = {
        "name":"test1 GUDLFT",
        "email":"test1_email@gudlft.com",
        "points":"20"
    }
	return club_data

@pytest.fixture
def club_fixture_second_user():
	club_data = {
        "name":"test2 GUDLFT",
        "email":"test2_email@gudlft.com",
        "points":"20"
    }
	return club_data

@pytest.fixture
def past_competition_fixture():	
	competition_data = {
        "name": "competition test1",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "25"
    }
	return competition_data

@pytest.fixture
def post_competition_fixture():	
	competition_data = {
        "name": "competition test2",
        "date": "2024-10-22 13:30:00",
        "numberOfPlaces": "13"
    }
	return competition_data