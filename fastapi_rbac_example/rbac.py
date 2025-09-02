
from typing import List
from fastapi import HTTPException, status

def requires_permissions(required: List[str]):
    """Return a callable that checks permissions on a user object.
    Usage in FastAPI route: requires_permissions(['kb.manage'])(current_user)
    where current_user is the result of get_current_user dependency.
    """
    def checker(user):
        # user is expected to have 'permissions' attribute (list of strings)
        user_perms = getattr(user, 'permissions', [])
        # simple check: all required permissions must be present (AND)
        missing = [p for p in required if p not in user_perms]
        if missing:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Missing permissions: {missing}')
        return True
    return checker
