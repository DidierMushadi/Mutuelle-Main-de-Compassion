from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.member import MemberRead
from app.core.security import verify_password, create_access_token, get_current_active_user
from app.crud.member import get_member_by_email
from app.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user = await get_member_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.mot_de_passe):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Identifiants incorrects")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=MemberRead)
async def read_users_me(current_user=Depends(get_current_active_user)):
    return current_user
