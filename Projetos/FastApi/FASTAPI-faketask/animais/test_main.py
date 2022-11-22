
# tests/test_app.py
"""App routes test file."""
import pytest
import main
from async_asgi_testclient import TestClient

@pytest.mark.asyncio
async def test_animals(setup):
    """Test the /animals route."""
    headers = {"accept": "application/json", "x-requested-with": "melius"}
    async with TestClient(main.app) as client:
        response = await client.get("/animals", headers=headers)
        assert response.status_code == 200