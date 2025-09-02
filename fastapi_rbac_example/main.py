
from fastapi import FastAPI, Depends, HTTPException, status
from typing import List
from auth import get_current_user, User
from rbac import requires_permissions

app = FastAPI(title="RBAC Example")

@app.get('/public')
def public_endpoint():
    return {'msg': 'this is public'}

@app.get('/profile')
def read_profile(current_user: User = Depends(get_current_user)):
    # any authenticated user can read own profile
    return {'user': current_user.dict()}

@app.get('/team-data')
def read_team_data(current_user: User = Depends(get_current_user)):
    # require permission 'profile.read_team'
    requires_permissions(['profile.read_team'])(current_user)
    return {'msg': f'team data for {current_user.username}'}

@app.post('/kb/create')
def create_kb_item(current_user: User = Depends(get_current_user)):
    # require kb.manage permission
    requires_permissions(['kb.manage'])(current_user)
    return {'msg': 'kb item created'}
