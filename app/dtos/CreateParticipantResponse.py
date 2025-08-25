from datetime import date

from pydantic import BaseModel

from app.dtos.frozen_config import FROZEN_CONFIG


class Participant(BaseModel):
    model_config = FROZEN_CONFIG

    id: int
    date: date


class CreateParticipantResponse(BaseModel):
    model_config = FROZEN_CONFIG

    participant_id: int
    participant_date: date
