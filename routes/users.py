from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter(tags=['User'], )
users = {}


@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:  # 기가입유저
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="이미 가입이 된 이메일 계정입니다!"
        )
    users[data.email] = data  # email을 hashmap에 넣어준다.
    return {"message": "등록 성공"}


@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:  # 미가입유저
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="가입되지 않은 이메일 주소입니다!"
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="잘못된 비밀번호 입니다."
        )
    return {"message":"로그인 성공"}


