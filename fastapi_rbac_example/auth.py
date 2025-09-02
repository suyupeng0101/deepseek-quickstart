
from pydantic import BaseModel
from typing import List, Optional
from fastapi import HTTPException, status, Request
import jwt

SECRET = 'changeme_secret'  # in production use secure key management

class User(BaseModel):
    username: str
    roles: List[str] = []
    permissions: List[str] = []

# mock role -> permissions mapping for demo
ROLE_PERMISSIONS = {
    'employee': ['profile.read', 'chat.start', 'ticket.create'],
    'manager': ['profile.read', 'profile.read_team', 'ticket.create', 'ticket.approve'],
    'agent_admin': ['kb.manage', 'kb.read', 'chat.read_logs'],
    'hr': ['hr.read', 'hr.write']
}

def get_permissions_from_roles(roles):
    perms = set()
    for r in roles:
        perms.update(ROLE_PERMISSIONS.get(r, []))
    return list(perms)

def decode_jwt(token: str):
    try:
        payload = jwt.decode(token, SECRET, algorithms=['HS256'])
        return payload
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')

def get_current_user(request: Request) -> User:
    auth = request.headers.get('Authorization')
    if not auth or not auth.startswith('Bearer '):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Missing Authorization')
    token = auth.split(' ', 1)[1]
    payload = decode_jwt(token)
    # payload expected to contain 'sub' and 'roles'
    roles = payload.get('roles', [])
    user = User(username=payload.get('sub', 'unknown'), roles=roles)
    user.permissions = get_permissions_from_roles(roles)
    return user
