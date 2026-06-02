from app.data.users_db import users


def get_users():
    return users


def get_user_by_id(user_id: int):

    return next(
        (u for u in users if u["id"] == user_id),
        None
    )


def create_user(user_data):

    new_user = {
        "id": len(users) + 1,
        **user_data
    }

    users.append(new_user)

    return new_user


def update_user(user_id, user_data):

    for index, user in enumerate(users):

        if user["id"] == user_id:

            users[index] = {
                "id": user_id,
                **user_data
            }

            return users[index]

    return None


def patch_user(user_id, user_data):

    for user in users:

        if user["id"] == user_id:

            user.update(user_data)

            return user

    return None


def delete_user(user_id):

    for user in users:

        if user["id"] == user_id:

            users.remove(user)

            return True

    return False