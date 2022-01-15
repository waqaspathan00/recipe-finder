
class Food(dict):
    """ by inheriting from dict, Food objects become automatically serializable for JSON formatting """

    def __init__(self, data):
        """ create a serialized food object with desired fields """
        id = data["id"]
        name = data["title"]
        image = data["image"]

        super().__init__(self, id=id, name=name, image=image)


class Ingredient(dict):
    """ by inheriting from dict, Ingredient objects become automatically serializable for JSON formatting """

    def __init__(self, data):
        name = data["name"]
        amount = data["amount"]["us"]["value"]
        unit = data["amount"]["us"]["unit"]

        super().__init__(self, name=name, amount=amount, unit=unit)

class Step(dict):

    def __init__(self, data):
        number = data["number"]
        step = data["step"]

        super().__init__(self, number=number, step=step)
