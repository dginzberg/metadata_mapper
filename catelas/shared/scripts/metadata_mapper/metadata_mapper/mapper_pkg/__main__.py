# app_pkg/main --
from .mapper_controller import Mapper_Controller


def run():
    controller = Mapper_Controller()
    controller.start_mapping()


if __name__ == "__main__":
    run()
