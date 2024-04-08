from re import match


class Flags:
  verbose = False
  compact: int | None = None
  out: str | None = None

  helpmsg = """TTBDA (Text To Brainfuck Different Approach)
Usage: ttbda --[flags] [file]
Flags:
  --help          | Displays this help menu.
  --verbose       | Debugging information.
  --compact=<int> | Output has no spaces, just Brainfuck characters. Given int is length of line before a newline is added.
  --out=<str>     | Path to file to write output to.
"""

  def __init__(self, _argv) -> None:
    flags = [a[2:] for a in _argv if a [:2] == "--"]  # Array of flags without `--`.

    for flag in flags:
      if flag[-1] == '=': raise Exception("Flag ends with `=`. Value required.")

      if match(r"\w+=.+", flag):  # TEST STRING: compact=50 [✅]
        fsplit = flag.split('=', 1)
        name, value = fsplit[0], fsplit[1]

        match name:
          case "compact":
            if (value.isdigit()): self.compact = int(value)
            else: raise Exception("Flag 'compact' requires an int value.")

          case "out": self.out = value
          case name: raise Exception("'%s' isn't a valid flag." %flag)

      else:  # Flags with no args / `=`.
        match flag:
          case "help": print(self.helpmsg)
          case "verbose": self.verbose = True
          case flag: raise Exception("'%s' isn't a valid flag." %flag)
