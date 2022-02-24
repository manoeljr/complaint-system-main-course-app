from fastapi import APIRouter

from managers.user import UserManager

router = APIRouter(tags=["Auth"])


@router.post(
    "/register/",
    status_code=201
)
async def register(user_data):
    token = UserManager.register(user_data)
    return {"token": token}
