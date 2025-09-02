
# FastAPI RBAC Example

## Overview
Simple demonstration of RBAC-style permission checking in FastAPI.
- `auth.py` contains a simple JWT decoding and role->permission mapping for demo.
- `rbac.py` offers `requires_permissions()` helper used in routes.
- `main.py` exposes endpoints that use the helper to enforce permissions.

NOTE: This is a minimal demo. In production, integrate with real identity provider (OIDC), secure secret management, and more robust permission checks.

## Run
1. Create virtual env and install requirements:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Run app:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
3. Example tokens (HS256, SECRET='changeme_secret'):
   - employee token payload: { "sub": "alice", "roles": ["employee"] }
   - manager token payload: { "sub": "bob", "roles": ["manager"] }
   - admin token payload: { "sub": "carol", "roles": ["agent_admin"] }
   You can generate JWTs with `jwt` library or online tools (use same SECRET).
