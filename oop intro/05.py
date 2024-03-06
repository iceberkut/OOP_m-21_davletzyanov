class BigBell:
    def __init__(self):
        self.sound_index = 0

    def sound(self):
        if self.sound_index % 2 == 0:
            print("ding")
        else:
            print("dong")
        self.sound_index += 1


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
