class Flags:
  verbose = False
  compact = int | None
  output: str | None = None

  helpmsg = """TTBDA (Text To Brainfuck Different Approach)
Usage: ttbda --[flags] [file]
Flags:
  --verbose       | Debugging information.
  --compact=<int> | Output has no spaces, just Brainfuck characters. Given int is length of line before a newline is added.
  --output=<str>  | Path to file to write output to.
"""

  def __init__(self) -> None:
    ...
