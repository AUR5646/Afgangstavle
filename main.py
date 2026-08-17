from model import DepartureBoardModel
from views import DepartureBoardView
from controller import DepartureBoardController 

def main():
    model = DepartureBoardModel()
    view = DepartureBoardView()
    controller = DepartureBoardController(view, model)

    controller.getSchedule()

    view.root.mainloop()


if __name__ == "__main__":
    main()


