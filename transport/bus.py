from abstract.abs_transport import AbsTransport


class Bus(AbsTransport):
    def start_engine(self):
        print("Starting engine")

    def travel_to_destination(self):
        print("Travelling via Bus")