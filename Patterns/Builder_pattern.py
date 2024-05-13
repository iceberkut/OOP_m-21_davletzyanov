from abc import ABC, abstractmethod


class Car:
    def __init__(self, engine=2.3, body: int = 1, transmission: int = 1):
        self.engine = engine
        self.body = body
        self.transmission = transmission

    def __str__(self):
        text = '\n'
        text += f'engine:{self.engine}\n'
        text += f'body:{self.body}\n'
        text += f'transmission:{self.transmission}\n'
        return text


class Builder(ABC):
    @abstractmethod
    def set_engine(self, engine: float):
        pass

    @abstractmethod
    def set_body(self, body: int):
        pass

    @abstractmethod
    def set_transmission(self, transmission: int):
        pass


class CarBuilder(Builder):
    _params = {
        'engine': 0.0,
        'body': 0,
        'transmission': 0
    }

    def set_engine(self, engine):
        self._params['engine'] = engine
        return self

    def set_body(self, body):
        self._params['body'] = body
        return self

    def set_transmission(self, transmission):
        self._params['transmission'] = transmission
        return self

    def get_result(self) -> Car:
        return Car(
            engine=self._params['engine'],
            body=self._params['body'],
            transmission=self._params['transmission']
        )


class SedanBuilder(CarBuilder):
    _params = {
        'engine': 43.2,
        'body': 3,
        'transmission': 3
    }

    def set_engine(self, engine):
        self._params['engine'] = engine
        return self

    def set_body(self, body):
        self._params['body'] = body
        return self

    def set_transmission(self, transmission):
        self._params['transmission'] = transmission
        return self




class CarDirector:
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def construct_car(self):
        return self.builder.set_engine(2.3).set_transmission(4).set_body(2).get_result()


sedan_builder = SedanBuilder()
director = CarDirector(sedan_builder)
sedan = director.construct_car()
print("Created sedan:", sedan)
