from Model import Model
from Camera import Camera
from Flash import Flash


class Scene():
    def __init__(self,
                 id: int,
                 width: int,
                 models: Model,
                 cameras: Camera,
                 flashes: Flash):
        self.id = id
        self.width = width
        self.models = models
        self.cameras = cameras
        self.flashes = flashes

    def addModel (self) -> int:
        pass