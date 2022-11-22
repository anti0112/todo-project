import pytest

@pytest.mark.django_db
def test_user_create(client):
    data = {
        'id': 1,
        'username': 'anti',
        'password': 'passsword8896',
        'first_name': 'first name',
        'last_name': 'last name',
        'email': 'email@gmail.com',
        'password_repeat': 'passsword8896'
    }
   
    response = client.post(
        path='/core/signup',
        data=data,
        content_type='application/json',
    )
    
    
    assert response.status_code == 201
    assert response.data['email'] == data['email']
    assert response.data['first_name'] == data['first_name']
    assert response.data['id'] == data['id']
    assert response.data['last_name'] == data['last_name']
    assert response.data['username'] == data['username']