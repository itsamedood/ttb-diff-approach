from enum import Enum


class ConversionMethod(Enum):
  """
  `text` = Terminal, line by line, you enter text, it prints out the corresponding code.

  `file` = Takes given file via path and produces a translated version with the same name with `.bf` extension.
  """

  BY_TEXT = "text"
  BY_FILE = "file"
