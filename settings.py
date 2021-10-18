class Settings:
    """A separate class for the settings"""
    #Mai intai fereastra de setari

    def __init__(self):
        """Constructor for the settings class"""
        self.screen_width = 1200
        self.screen_heigth = 800
        self.bg_color = (0,0,0)
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 230, 230)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 - > right; -1 -> left
        self.fleet_direction = 1


