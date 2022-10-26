class MealNotFound(Exception):
    
    def __init__(self):
        self.message = 'Meal not found'
        super().__init__(self.message)
