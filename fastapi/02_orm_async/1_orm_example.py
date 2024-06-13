from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from typing import Optional


DATABASE_URL = ""

engine = create_engine(DATABASE_URL)

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    
    id = Column()
    username = Column()
    email = Column()


class UserCreate(BaseModel):
    username: str
    mail: str
    
def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

# db에 데이터를 넣는 함수
@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # db라는 이름으로 Session(세션)을 만드는데 get_db라는 함수를 호출한다(?)
    # 나만의 코드로 만들만한 자유도X -> 기본 코드만 복붙하여 쓰는 것이 빠르게 개발할 수 있는 방법
    new_user = User(username=user.username, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "username": new_user.username, "email": new_user.email}
    
class User(Base):
    __tablename__ = "User"
    
    id = Column(Integer, primary_key=True, autoincrement=True, commment="기본 키")
    username = Column(String(50), unique=True, nullable=False, index=True, comment="사용자 이름")
    email = Column(String(120), unique=True, nullable=False, commend="이메일 주소")
    is_active = Column(Boolean, default=True, comment="활성 상태")
    created_at = Column(DateTime, default=datetime.utcnow, comment="생성 타임스탬프")
    parent_id = Column(Integer, ForeignKey("Parent.id"), commend="상위 id")
    
    
@app.post("/users/")
def create_user(username: str, email: str, db: Session = Depends(get_db)):
    new_user = User(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "username": new_user.username, "email": new_user.email}

@app.post("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return {"error": "user not found"}
    return {"id": db_user.id, "username": db_user.username, "email": db_user.email}

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None

# 특정 데이터 수정
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return {"error": "User not found"}
    
    if user.username is not None:
        db_user.username = user.username
    if user.email is not None:
        db_user.email = user.email
        
    db.commit()
    db.refresh(db_user)
    return {"id": db_user.id, "username": db_user.username, "email": db_user.email}

# 특정 데이터 삭제: get같은 메서드를 사용해도 상관없지만 관용적으로!
@app.delete("users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return {"error": "사용자를 찾을 수 없습니다"}
    
    db.delete(db_user)
    db.commit()
    return {"message": "사용자가 성공적으로 삭제되었습니다"}