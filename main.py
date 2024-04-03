from transport.airplane import Airplane
from transport.bus import Bus


def main():
    travel(Bus, 'New York')
    travel(Airplane, 'Amsterdam')

def travel(transport, destination):
    msg = "Travelling to {} via {}".format(destination, transport.__name__)
    print("|"*20, msg, "|"*20)
    means = transport(destination)
    means.take_trip()

if __name__ == '__main__':
    main()