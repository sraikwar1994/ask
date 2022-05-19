import json

from flask import url_for

from ask_backend.users.models import User


def test__get_user_list__api(client, user):
    response = client.get(url_for("users.user_api"))
    user_data = json.loads(response.text)

    assert response.status_code == 200
    assert user_data[0]["username"] == user.username
    assert user_data[0]["firstname"] == user.firstname
    assert user_data[0]["lastname"] == user.lastname
    assert user_data[0]["email"] == user.email


def test__create_user__api(client):
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    data = {
        "username": "new_user",
        "firstname": "new_user_username",
        "lastname": "new_user_lastname",
        "email": "new_user@email.com",
    }
    response = client.post(
        url_for("users.create_user_api"), data=json.dumps(data), headers=headers
    )
    response_data = json.loads(response.text)

    assert response.status_code == 201
    assert response_data["status"]
    assert User.query.count() == 1


def test__update_user__api(client, user):
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    data = {
        "id": user.id,
        "username": "edited_new_user",
        "firstname": "edited_new_user_username",
        "lastname": "edited_new_user_lastname",
        "email": "edited_new_user@email.com",
    }
    response = client.put(
        url_for("users.update_user_api"), data=json.dumps(data), headers=headers
    )
    res_data = json.loads(response.text)

    assert response.status_code == 200
    assert res_data["username"] == user.username
    assert res_data["firstname"] == user.firstname
    assert res_data["lastname"] == user.lastname
    assert res_data["email"] == user.email


def test__delete_user__api(client, user):
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    data = {
        "id": user.id,
    }
    response = client.delete(
        url_for("users.delete_user_api"), data=json.dumps(data), headers=headers
    )
    res_data = json.loads(response.text)

    assert response.status_code == 200
    assert res_data["status"]
    assert User.query.count() == 0
