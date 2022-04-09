from tests.conftest import client
from datetime import datetime


def test_should_status_code_ok(client):
	response = client.get('/')
	assert response.status_code == 200

def test_login_user_success(client, club_fixture_first_user):
	rv = client.post('/showSummary', data=dict(email=club_fixture_first_user['email']), follow_redirects=True)
	assert rv.status_code == 200
	data = rv.data.decode()
	assert data.find('Please enter your secretary email to continue') == -1