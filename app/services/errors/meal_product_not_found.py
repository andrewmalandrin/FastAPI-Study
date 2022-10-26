class MealProductNotFound(Exception):

    def __init__(self):
        self.message = 'Meal product not found'
        super().__init__(self.message)
