class Settings():

    def __init__(self):
        self.screen_width = 800;
        self.screen_height = 400;
        self.bg_color = (230, 230, 230);

        # 飞船设置
        self.ship_speed_factor = 1.5;

        # 子弹设置
        self.bullet_speed_factor = 1;
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
