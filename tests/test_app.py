from fastapi import status


def test_root_deve_retornar_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == status.HTTP_200_OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_html_deve_retornar_ola_mundo(client):
    response = client.get('/html')  # Act

    assert response.status_code == status.HTTP_200_OK  # Assert
    assert 'Olá Mundo' in response.text


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword',
        },
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        'id': 1,
        'username': 'testuser',
        'email': 'test@example.com',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'users': [
            {
                'username': 'testuser',
                'email': 'test@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == status.HTTP_200_OK

    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/999',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_get_user_by_id(client):
    response = client.get('/users/1')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_get_user_by_id_not_found(client):
    response = client.get('/users/999')

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/users/999')

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
