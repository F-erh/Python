@pytest.mark.asyncio
async def test_get(setup):
    """Test get one animal."""
    animal_svc = animal_service.Animal(model, setup.repo)
    animal = await setup.repo.get('Animal', setup.animal.id)
    animal_svc.animal = animal

    animal_svc.animal = animal
    await animal_svc.get(5)

@pytest.mark.asyncio
async def test_save(setup):
    """Test the save(get) method."""
    animal = animal_service.Animal(model, setup.repo)
    entity_instance = model.Input.Animal(nome='Cascata', idade=3)
    await animal.save(entity_instance)

    animal_list = await animal.get_list()
    assert animal_list[0]['nome']=='cascata' and animal_list[0]['idade'] == '3'

############################################################################

    async def delete(self, id):
        """Delete the animal."""
        return await super().delete(id)
    
    async def save(self, data):
        """Save animals."""
        data.nome = data.nome.lower()
        return await super().save(data)
    
    async def get_id(self, id):
        """Get the animal by id."""
        animal = await super().get(id)
        return animal if animal and not animal.deleted else None