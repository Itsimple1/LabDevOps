import pytest

from main import answer


@pytest.mark.parametrize(
    ("command", "output"),
    [
        ("start", "The stopwatch is running"),
        (
            "--help",
            (
                "List of commands to control:\n"
                + "start - start the stopwatch\n"
                + "stop - stop the stopwatch and get the time\n"
                + "now - the time is now\n"
                + "exit - command for exit\n"
                + "--help - info about command\n"
            ),
        ),
    ],
)
def test_answer(command, output):
    assert answer(command) == output
