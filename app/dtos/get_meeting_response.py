from datetime import date

from pydantic import BaseModel

from app.dtos.frozen_config import FROZEN_CONFIG


class GetMeetingResponse(BaseModel):
    model_config = FROZEN_CONFIG

    url_code: str
    start_time: date | None = None
    end_time: date | None = None
    title: str
    location: str
