from flags import Flags
from sys import argv


class Cli:
  def __init__(self) -> None:
    args = argv[1:]  # Excluding executed command.
    last_arg = args[-1] if len(args) > 0 else None
    print(argv, args)

    self.flags = Flags(argv)
    self.file = last_arg if last_arg is not None and not last_arg[:2] == '--' else None
