from fastapi import FastAPI
import uvicorn

from routes.users import user_router
from routes.events import event_router
app = FastAPI()
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

'''
왜 안되는거지?
'''
# 이 코드는 Python 스크립트가 직접 실행될 때만 실행되는 코드 블록을 정의합니다.
# if __name__ == "__main__": 구문은 현재 스크립트가 직접 실행되는 경우에만 참이 됩니다.
# 이 스크립트가 다른 스크립트에 의해 임포트되는 경우에는 이 구문은 거짓이 되어 이 안의 코드는 실행되지 않습니다.
if __name__ == "__main__":
    """
    왜 안되는걸까?
    """
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


