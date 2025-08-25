from datetime import datetime

from fastapi import APIRouter

from app.dtos.CreateParticipantResponse import CreateParticipantResponse

participant_mysql_router = APIRouter(prefix="/v1/mysql/participants", tags=["Participant"])


@participant_mysql_router.post("", description="participant를 생성합니다.")
async def api_create_participant(create_participant: CreateParticipantResponse) -> CreateParticipantResponse:
    return CreateParticipantResponse(participant_id=123, participant_date=datetime.now().date())
