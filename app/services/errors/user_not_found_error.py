class UserNotFound(Exception):
    
    def __init__(self):
        self.message = 'User not found'
        super().__init__(self.message)