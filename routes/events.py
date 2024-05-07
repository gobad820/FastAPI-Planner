from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event
from typing_extensions import List

event_router = APIRouter(tags=["Events"])

events = []


# 응답 형태를 List[Event]로, 일치하지 않으면 오류 또한 reseponse_model을 통해 List[Event]를 JSON타입으로 변경 가능
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    return events


@event_router.get("/{id}", response_model=Event)
async def rerieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist, 없는 ID입니다."
    )


# 매개변수가 Event 타입, Body(...)를 통해서 Content-Type이 application/json인 경우 JSON 본문을 파이썬 딕셔너리로 변환한다.
# 해당 값을 default value로 선언
@event_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return {"message": "이벤트 생성 성공"}


@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {"message": "이벤트 삭제 성공"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="없는 ID입니다."
    )


@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {"message": "모든 이벤트 삭제 성공"}
