class Occurrence:
  """
  Used for checking how many times in a row a character occurs.

  ```txt
  Given: "abcaabcabbbcabcccc"

  Get:
  a = 1
  b = 1
  c = 1
  a = 2
  b = 1
  c = 1
  a = 1
  b = 3
  c = 1
  a = 1
  b = 1
  c = 4
  ```
  """

  def __init__(self, _char: str) -> None:
    self.char = _char
    self.count = 1
