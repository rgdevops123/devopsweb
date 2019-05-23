
def test_root_page(base_client):
    response = base_client.get('/')
    assert response.status_code == 302
    assert b"/login" in response.data


def test_login_page(base_client):
    response = base_client.get('/login')
    assert response.status_code == 200
    assert b"Login Form" in response.data


def test_register_page(base_client):
    response = base_client.get('/register')
    assert response.status_code == 200
    assert b"Create Account" in response.data


def test_home_page_with_no_login(base_client):
    response = base_client.get('/home')
    assert response.status_code == 403
    assert b"Access Denied" in response.data


def test_valid_login_logout(base_client, init_database):
    response = base_client.post('/login',
                                data=dict(email='testuser@email.com',
                                          password='123'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"Login Form" in response.data

    response = base_client.get('/logout',
                               follow_redirects=True)
    assert response.status_code == 200
    assert b"Login Form" in response.data


def test_home_page(login_disabled_client):
    response = login_disabled_client.get('/home')
    assert response.status_code == 200
    assert b"Home" in response.data


def test_overview_flask_page(login_disabled_client):
    response = login_disabled_client.get('/overview-flask')
    assert response.status_code == 200
    assert b"Flask Overview" in response.data


def test_overview_docker_page(login_disabled_client):
    response = login_disabled_client.get('/overview-docker')
    assert response.status_code == 200
    assert b"Docker Overview" in response.data


def test_overview_kubernetes_page(login_disabled_client):
    response = login_disabled_client.get('/overview-kubernetes')
    assert response.status_code == 200
    assert b"Kubernetes Overview" in response.data


def test_overview_sqlite_page(login_disabled_client):
    response = login_disabled_client.get('/overview-sqlite')
    assert response.status_code == 200
    assert b"SQLite Commands and General Usage" in response.data


def test_overview_postgresql_page(login_disabled_client):
    response = login_disabled_client.get('/overview-postgresql')
    assert response.status_code == 200
    assert b"PostgreSQL Overview" in response.data


def test_overview_ansible_page(login_disabled_client):
    response = login_disabled_client.get('/overview-ansible')
    assert response.status_code == 200
    assert b"Ansible Overview" in response.data


def test_overview_linux_page(login_disabled_client):
    response = login_disabled_client.get('/overview-linux')
    assert response.status_code == 200
    assert b"Linux Overview" in response.data
