from fastapi import HTTPException
from app.data.users_db import users


def get_user_or_404(user_id: int):

    user = next(
        (u for u in users if u["id"] == user_id),
        None
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return user


def validate_role(role: str):

    allowed_roles = [
        "admin",
        "user",
        "support"
    ]

    if role not in allowed_roles:
        raise HTTPException(
            status_code=400,
            detail="Rol no permitido"
        )


def validate_email(email: str):

    for user in users:
        if user["email"] == email:
            raise HTTPException(
                status_code=400,
                detail="Correo ya registrado"
            )