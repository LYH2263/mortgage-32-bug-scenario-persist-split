def attach_run_ids(response: dict) -> dict:
    ids = response.get("run_ids") or []
    if ids:
        response["persisted_count"] = len(ids)
    return response
