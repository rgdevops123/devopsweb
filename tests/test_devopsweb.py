
def test_root_page(base_client):
    response = base_client.get('/')
    assert response.status_code == 302


def test_login_page(base_client):
    response = base_client.get('/login')
    assert response.status_code == 200


def test_register_page(base_client):
    response = base_client.get('/register')
    assert response.status_code == 200


def test_home_page_with_no_login(base_client):
    response = base_client.get('/home')
    assert response.status_code == 403


def test_valid_login_logout(base_client, init_database):
    response = base_client.post('/login',
                                data=dict(email='testuser@email.com', password='123'),
                                follow_redirects=True)
    assert response.status_code == 200

    response = base_client.get('/logout',
                               follow_redirects=True)
    assert response.status_code == 200


def test_home_page(login_disabled_client):
    response = login_disabled_client.get('/home')
    assert response.status_code == 200
