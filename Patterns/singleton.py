# class GameSettings:
#     _instance = None
#     volume: int
#     difficulty: str
#
#     def __init__(self, volume=100, difficulty='Normal'):
#         self.volume = volume
#         self.difficulty = difficulty
#
#     @staticmethod
#     def get_instance():
#         if GameSettings._instance is None:
#             GameSettings._instance = GameSettings()
#         return GameSettings._instance
#
#
# settings1 = GameSettings.get_instance()
# settings2 = GameSettings.get_instance()
#
# print(settings1 is settings2)
#
# settings1.volume = 70
# settings1.difficulty = "Hard"
#
# print(settings2.volume)
# print(settings2.difficulty)

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class GameSettings(metaclass=SingletonMeta):
    def __init__(self, volume=100, difficulty='Normal'):
        self.volume = volume
        self.difficulty = difficulty


settings1 = GameSettings()
settings2 = GameSettings()

print(settings1 is settings2)

settings1.volume = 70
settings1.difficulty = "Hard"

print(settings2.volume)
print(settings2.difficulty)