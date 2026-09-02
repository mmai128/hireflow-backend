from fastapi import APIRouter, HTTPException

from app.schemas.user import UserCreate, UserResponse, UserUpdate


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


users_db = []


@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    new_user = {
        "id": len(users_db) + 1,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "password": user.password
    }

    users_db.append(new_user)

    return new_user


@router.get("/", response_model=list[UserResponse])
async def get_users():
    return users_db


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )
@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, updated_data: UserUpdate):
    for user in users_db:
        if user["id"] == user_id:
            if updated_data.name is not None:
                user["name"] = updated_data.name

            if updated_data.email is not None:
                user["email"] = updated_data.email

            if updated_data.age is not None:
                user["age"] = updated_data.age

            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )
@router.delete("/{user_id}")
async def delete_user(user_id: int):
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            deleted_user = users_db.pop(index)

            return {
                "message": "User deleted successfully",
                "user_id": deleted_user["id"]
            }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )