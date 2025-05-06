class Score:
    def __init__(self):
        self.points = 0
    
    
    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass
