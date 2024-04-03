from abstract.abs_transport import AbsTransport


class Airplane(AbsTransport):
    def start_engine(self):
        print("Starting jet engines")

    def leave_terminal(self):
        print("Leaving the terminal")

    def travel_to_destination(self):
        print("Travelling...")

    def entertainment(self):
        print("Movie: The Lion King")

    def arrive_at_destination(self):
        print("Arriving at {}".format(self._destination))