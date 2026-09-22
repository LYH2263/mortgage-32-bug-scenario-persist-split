from fastapi import APIRouter, HTTPException
from app.schemas.schedule import CompareRequest
from app.services.mortgage_service import MortgageService, PlanValidationError
from app.services.compare_persist_split import attach_run_ids
router = APIRouter()


@router.post("/compare")
def post_compare(body: CompareRequest):
    with MortgageService() as s:
        try:
            out = s.compare(body.principal, body.plans, body.loan_id, body.persist)
            return attach_run_ids(out)
        except PlanValidationError as e:
            raise HTTPException(status_code=422, detail=str(e))
