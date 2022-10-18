class ProductNotFound(Exception):
    
    def __init__(self):
        self.message = 'Product not found'
        super().__init__(self.message)
