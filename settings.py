class Settings:
    """A separate class for the settings"""
    #Mai intai fereastra de setari

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_heigth = 800
        self.bg_color = (0,0,0)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 230, 230)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # The speed of game after lvl up
        self.speedup_scale = 1.2

        # Speed of score scale
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that can change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 1.0

        # fleet_direction of 1 - > right; -1 -> left
        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)


