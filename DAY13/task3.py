from fastapi import APIRouter,Depends
from auth import get_current_users

router = APIRouter
@router.get("\tasks")
def get_tasks(current_user :str=Depends(get_current_users)):
    return {
        "message":"fetched succesfully",
        "users":current_user
        }