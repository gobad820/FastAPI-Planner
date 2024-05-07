from pydantic import BaseModel, EmailStr, SecretStr
from typing import List, Optional
from models.events import Event


class User(BaseModel):
    email: EmailStr
    username: str
    password: SecretStr
    events: Optional[List[Event]]

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "strong!!!",
                "password": "1234",
                "events": [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: SecretStr

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }

#  curl -X 'POST' \ # curl = client URL, -X : mean request
# 'http://127.0.0.1:8000/user/signin' \
# -H 'accept: application/json' \ -H mean HTTP Header, Request Header
# -H 'Content-Type: application/json' \ Entity Header
# -d '{ "email": "fastapi@packt.com", "password": "Stro0ng!","events":[] }'  # -d mean Data

# HTTP 헤더는 크게 4가지 유형으로 분류됩니다:
# 1. General Headers: 클라이언트와 서버 모두에서 사용되며, 메시지 전체에 적용되는 헤더입니다. 예를 들어, `Cache-Control`, `Connection` 등이 있습니다.
# 2. Request Headers: 클라이언트에서 서버로의 요청에만 사용되며, 요청에 대한 추가 정보를 제공합니다. 예를 들어, `Accept`, `User-Agent`, `Host` 등이 있습니다.
# 3. Response Headers: 서버에서 클라이언트로의 응답에만 사용되며, 응답에 대한 추가 정보를 제공합니다. 예를 들어, `Server`, `Set-Cookie`, `WWW-Authenticate` 등이 있습니다.
# 4. Entity Headers: 요청이나 응답의 본문에 대한 추가 정보를 제공합니다. 예를 들어, `Content-Type`, `Content-Length`, `Last-Modified` 등이 있습니다.

# HTTP 헤더는 이름과 값의 쌍으로 구성되며, 각 헤더는 콜론(`:`)으로 구분됩니다. 예를 들어, `Content-Type: application/json`은 `Content-Type`이라는 이름의 헤더가 `application/json`이라는 값을 가지고 있음을 나타냅니다. 이는 요청이나 응답의 본문이 JSON 형식의 데이터를 포함하고 있음을 나타냅니다.

# `Content-Type` 헤더는 Entity Header에 속하며, HTTP 메시지의 본문(body)이 어떤 형식으로 인코딩되어 있는지를 알려줍니다. 따라서 `Content-Type: application/json`은 HTTP 메시지의 본문이 JSON 형식으로 인코딩되어 있다는 것을 나타냅니다.
# 반면에 Request Header는 클라이언트가 서버에게 보내는 요청에 대한 정보를 포함합니다. `Accept` 헤더는 이 중 하나로, 클라이언트가 이해할 수 있는 컨텐츠 타입을 나타냅니다. 예를 들어, `Accept: application/json`은 클라이언트가 JSON 형식의 응답을 이해할 수 있음을 나타냅니다.
# 따라서, `Content-Type`과 `Accept` 헤더는 각각 HTTP 메시지의 본문이 어떤 형식으로 인코딩되어 있는지, 그리고 클라이언트가 어떤 형식의 응답을 이해할 수 있는지를 나타내는 역할을 합니다. 이 두 헤더가 모두 `application/json`으로 설정되어 있다면, 클라이언트와 서버 모두 JSON 형식의 데이터를 주고받을 수 있음을 의미합니다.
