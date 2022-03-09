"""Animal service."""
from melius.services.base import Service


class Animal(Service):
    """Animal service."""

    def __init__(self, model, repo, model_repo=None):
        """Initiate the base service."""
        super().__init__(model, repo)
        self.model_repo = model_repo

    async def delete(self, id):
        """Delete the animal."""
        return await super().delete(id)
    
    async def save(self, data):
        """Save animals."""
        data.nome = data.nome.lower()
        return await super().save(data)
    
    async def get_id(self, id):
        """Get the animal by id."""
        fields = ['id', 'nome', 'idade']
        animal = await super().get(
            id,
            fields=fields
        )
        return animal

    async def get_list(self, **kwargs):
        """Get the animal by name."""
        limit = kwargs.get('limit')
        offset = kwargs.get('offset')
        return await super().get_list(
            fields=['nome', 'idade'],
            limit=limit,
            offset=offset)


    async def update(self, id, data):
        """Update the animal name."""
        data.nome = data.nome.lower()
        return await super().update(id, data)

