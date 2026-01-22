class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        if x_1 <= self.pos_x <= x_2 and y_1 <= self.pos_y <= y_2:
            return True
        else:
            return False


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        hit_units = []

        left   = x - self.__fire_range
        right  = x + self.__fire_range
        bottom = y - self.__fire_range
        top    = y + self.__fire_range

        for unit in units:
            if unit.in_area(left, bottom, right, top):
                hit_units.append(unit)
            
        return hit_units
