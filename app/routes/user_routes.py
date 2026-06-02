from fastapi import APIRouter, HTTPException, Depends, status

from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
    UserUpdate,
    UserPatch
)

from app.services.user_service import (
    get_users,
    create_user,
    update_user,
    patch_user,
    delete_user
)

from app.dependencies.user_dependencies import (
    get_user_or_404,
    validate_email,
    validate_role
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get(
    "/",
    response_model=list[UserResponse],
    summary="Listar usuarios"
)
def list_users():
    return get_users()


@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Obtener usuario por ID"
)
def get_user(user=Depends(get_user_or_404)):
    return user


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear usuario"
)
def create(user: UserCreate):

    validate_email(user.email)
    validate_role(user.role)

    return create_user(user.model_dump())


@router.put(
    "/{user_id}",
    response_model=UserResponse,
    summary="Actualizar usuario completamente"
)
def update(user_id: int, user: UserUpdate):

    validate_role(user.role)

    updated = update_user(
        user_id,
        user.model_dump()
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return updated


@router.patch(
    "/{user_id}",
    response_model=UserResponse,
    summary="Actualizar usuario parcialmente"
)
def patch(user_id: int, user: UserPatch):

    update_data = user.model_dump(
        exclude_unset=True
    )

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No se enviaron datos para actualizar"
        )

    updated = patch_user(
        user_id,
        update_data
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return updated


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    summary="Eliminar usuario"
)
def delete(user_id: int):

    deleted = delete_user(user_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return {
        "message": "Usuario eliminado correctamente"
    }