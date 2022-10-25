class DietNotFound(Exception):
    
    def __init__(self):
        self.message = 'Diet not found'
        super().__init__(self.message)
