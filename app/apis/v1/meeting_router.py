from datetime import datetime

from fastapi import APIRouter, HTTPException

from app.dtos.create_meeting_response import CreateMeetingResponse
from app.dtos.get_meeting_response import GetMeetingResponse
from app.dtos.update_meeting_request import UpdateMeetingDataRangeRequest
from app.services.meeting_service_mysql import (
    service_create_meeting_mysql,
    service_get_meeting_mysql,
)

mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"])


@mysql_router.post("", description="meeting을 생성합니다.")
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code=(await service_create_meeting_mysql()).url_code)


@mysql_router.get("/{meeting_url_code}", description="meeting을 조회합니다.")
async def api_get_meeting_mysql(meeting_url_code: str) -> GetMeetingResponse:
    if meeting := await service_get_meeting_mysql(meeting_url_code):
        return GetMeetingResponse(
            url_code=meeting.url_code,
            start_time=datetime.now().date(),
            end_time=datetime.now().date(),
            title="test",
            location="test",
        )
    else:
        raise HTTPException(status_code=404, detail=f"meeting: {meeting_url_code} not found")


@mysql_router.patch("/{meeting_url_code}/date_range", description="meeting의 날짜 range를 설정합니다.")
async def api_update_meeting_date_range_mysql(
    meeting_url_code: str, update_meeting_data_range_request: UpdateMeetingDataRangeRequest
) -> GetMeetingResponse:
    return GetMeetingResponse(
        url_code="abc", start_time=datetime.now().date(), end_time=datetime.now().date(), title="test", location="test"
    )
