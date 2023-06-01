import datetime
import time

sw = 0


def answer(com):
    global sw
    match com:
        case "start":
            sw = time.time()
            return "The stopwatch is running"
        case "stop":
            if sw == 0:
                return "The stopwatch is not running"
            else:
                return time.strftime("%H:%M:%S", time.gmtime(int(time.time() - sw)))
                sw = 0
        case "now":
            return datetime.datetime.now().time()
        case "--help":
            return (
                "List of commands to control:\n"
                + "start - start the stopwatch\n"
                + "stop - stop the stopwatch and get the time\n"
                + "now - the time is now\n"
                + "exit - command for exit\n"
                + "--help - info about command\n"
            )
        case _:
            return "Command not found"


def main():
    print(
        "Hi, this is an application which stimulates the stopwatch\n\n"
        + "List of commands to control:\n"
        + "start - start the stopwatch\n"
        + "stop - stop the stopwatch and get the time\n"
        + "now - the time is now\n"
        + "exit - command for exit\n"
        + "--help - info about command\n\n"
    )

    command = input(">> ")
    while True:
        match command:
            case "exit":
                break
            case _:
                print(answer(command))
        command = input(">> ")


if __name__ == "__main__":
    main()
