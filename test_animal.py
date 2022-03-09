"""Animal service test file."""
from sqlalchemy import null
from domain import model
from melius.utils.magic_import import import_service
import pytest
from datetime import datetime
from async_asgi_testclient import TestClient
from httpx import AsyncClient

animal_service = import_service("services.animal")

@pytest.mark.asyncio
async def test_get_list(setup):
    """Test the get list method."""
    animal_svc = animal_service.Animal(model, setup.repo)
    entity_instance = model.Input.Animal(nome='Cascata', idade=3)
    animal = await animal_svc.save(entity_instance)

    await animal_svc.get(animal.id)
    test = await animal_svc.get(animal.id)
    print(test)
    assert test == 200
    
@pytest.mark.asyncio
async def test_delete(setup):
    """Test the delete method."""
    animal_svc = animal_service.Animal(model, setup.repo)
    entity_instance = model.Input.Animal(nome='Cascata', idade=3)
    animal = await animal_svc.save(entity_instance)

    await animal_svc.delete(animal.id)
    test = await animal_svc.get(animal.id)
    assert test == None
    
@pytest.mark.asyncio
async def test_update(setup):
    """Test the update method."""
    animal_svc = animal_service.Animal(model, setup.repo)
    old_animal = model.Input.Animal(nome='Cascata', idade=3)
    animal = await animal_svc.save(old_animal)

    await animal_svc.update(animal.id,old_animal)
    new_animal = await animal_svc.get(animal.id)
    assert new_animal.nome == 'cascata'
    now = datetime.now()
    assert new_animal.modified_at.day == now.day

@pytest.mark.asyncio
async def test_save(setup):
    """Test the save(get) method."""
    animal = animal_service.Animal(model, setup.repo)
    entity_instance = model.Input.Animal(nome='Cascata', idade=3)
    await animal.save(entity_instance)

    animal_list = await animal.get_list()
    assert animal_list[0]['nome', 'idade'] == 'cascata', 3


@pytest.mark.asyncio
async def test_get_id(setup):
    """Test the get by id method."""
