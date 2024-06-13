from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})    # requrest: Jinja2Templates에 기본적으로 써 줘야함

@app.get("/about")
async def about():
    return {"message": "이것은 마이 메모 앱의 소개 페이지입니다"}

# 메모 생성: 세션 관리를 위해 request 사용
@app.post("/memos/")
async def create_memo(request: Request, memo: MemoCreate, db: Session = Depends(get_db)):
    username = request.session.get("username")
    if username is None:
        raise HTTPException(status_code=401, detail="Not allowed")
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, defailt="User not found")
    new_memo = Memo(user_id=user.id, title=memo.title, content=memo.content)
    db.add(new_memo)
    db.commit()
    db.refresh(new_memo) 
    return {"id": new_memo.id, "title": new_memo.title, "content": new_memo.content}

# 메모 조회
@app.get("/memos/")
async def list_memos(request: Request, db: Session = Depends(get_db)):
    username = request.session.get("username")
    if username is None:
        raise HTTPException(status_code=401, detail="Not allowed")
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, defailt="User not found")
    
    memos = db.query(Memo).filter(Memo.user_id == user.id).all()
    # return [{"id": memo.id, "title": memo.title, "content": memo.content} for memo in memos]
    return templates.TemplateResponse("memo.html", {"request": request, "memos": memos})

# 메모 수정
@app.put("/memos/{memo_id}")
async def update_memo(request: Request, memo_id: int, memo: MeMoUpdate, db: Session = Depend(get_db)):
    username = request.session.get("username")
    if username is None:
        raise HTTPException(status_code=401, detail="Not allowed")
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, defailt="User not found")
    
    db_memo = db.query(Memo).filter(Memo.user_id == user.id, Memo.id == memo_id).first()
    if db_memo is None:
        return ({"error": "Memo not found"})
    
    if memo.title is not None:
        db_memo.title = memo.title
    if memo.content is not None:
        db_memo.content = memo.content
        
    db.commit()
    db.refresh(db_memo)
    return db_memo

# 메모 삭제
@app.delete("/memos/{memo_id}")
async def delete_memo(request: Request, memo_id: int, db: Session = Depend(get_db)):
    username = request.session.get("username")
    if username is None:
        raise HTTPException(status_code=401, detail="Not allowed")
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, defailt="User not found")
    
    db_memo = db.query(Memo).filter(Memo.user_id == user.id, Memo.id == memo_id).first()
    if db_memo is None:
        return ({"error": "Memo not found"})
    
    db.delete(db_memo)
    db.commit()
    return ({"message": "deleted!"})

# 회원 가입
@app.post("/signup")
async def signup(signup_data: UserCreate, db: Session = Depends(get_db)):
    new_user = User(username=signup_data.usename, email=signup_data.email, hashed_password=signup_data.hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user) 
    return {"message": "Account created success", "user_id": new_user.id}

# 로그인
@app.post("/login")
async def login(requrest: Request, signup_data: UserLogin, db: Session = Depends(get_db)):
    pass