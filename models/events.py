from pydantic import BaseModel
# typing 모듈의 List는 타입 힌트를 제공하는 역할을 한다. 즉 List를 타입 힌트로 사용가능 하게 한다.
from typing import List


class Event(BaseModel):
    # pydantic 통해 __init__ 메서드 대신 아래의 형태로 사용 가능!
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    # pydantic 모델에서 메타데이터를 설정하는데 사용된다.
    class Config:
        # schema_extra 속성을 사용해서 JSON Schema에 추가 정보를 제공할 수 있다.(Swagger UI)
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }

# Swagger UI는 API를 시각화하고, 사용자가 API를 탐색하고, API의 메서드를 호출할 수 있는 도구입니다. 이는 OpenAPI 명세를 기반으로 작동합니다.
# FastAPI는 Swagger UI를 자동 생성, 웹 브라우저에서 볼 수 있게 한다.