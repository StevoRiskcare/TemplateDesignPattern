import abc


class AbsTransport(metaclass=abc.ABCMeta):
    def __init__(self, destination):
        self._destination = destination

    def take_trip(self):
        self.start_engine()
        self.leave_terminal()
        self.entertainment()
        self.travel_to_destination()
        self.arrive_at_destination()

    @abc.abstractmethod
    def start_engine(self):
        pass

    def leave_terminal(self):
        print("Leaving the terminal")

    @abc.abstractmethod
    def travel_to_destination(self):
        print("Travelling...")

    def entertainment(self):
        pass

    def arrive_at_destination(self):
        print("Arriving at {}".format(self._destination))