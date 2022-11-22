#%%
class Restaurante():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = ['chocolate', 'morango', 'banana']

    def describe_restaurant(self):
        print("O restaurante " + self.restaurant_name.title() +
              " é um " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("O restaurante " + self.restaurant_name.title() + " está aberto.")


restaurante = Restaurante('chine', 'chinesa')
restaurante.describe_restaurant()
restaurante.open_restaurant()


class IceCreamStand(Restaurante):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

    def show_flavors(self):
        print("Os sabores de sorvete da " +
              self.restaurant_name.title() + " são: " + str(self.flavors))


iceCream = IceCreamStand('ice cream', 'chinesa')
iceCream.show_flavors()

# %%
