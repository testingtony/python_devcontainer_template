"""I want this to work.

Please can I have stuff.
"""

import os
from os import environ
from typing import NamedTuple

# I want this to be a very long string that goes long beyond the end of the line. I want it to do this for a long long
# time now I think that will be good


class Fred(NamedTuple):
    """Woedd."""

    name: str | None
    id: int


try:
    print(f"Can you feel {os.environ} it?")
except RuntimeError:
    print("Bum")


def can_i_make_this_work():
    """Wprds."""
    environ["bpb"]
    pass
