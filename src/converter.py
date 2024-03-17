class TTBConverter:
  """ Text To Brainfuck Converter. """

  conversion_dict: dict[str, tuple[int, int, int]]
  """
  Dictionary of `str`->`tuple[int, int, int]`

  The tuple holds the ints required to produce the chars ASCII value (according to `assets/asciitable.png`).

  `H` = 72
  (8, 9, 0) -> (8 * 9) + 0 = 72
  """

  def __init__(self) -> None:
    self.conversion_dict = {
      # 'CHAR': (i, j, k)
      #            vvv
      #        (i * j) + k

      # Special #
      '\n': (2, 5, 0),    # 10
      ' ': (4, 8, 0),     # 32

      # Symbols (1) #
      '!': (3, 11, 0),    # 33
      '"': (3, 11, 1),    # 34
      '#': (5, 7, 0),     # 35
      '$': (6, 6, 0),     # 36
      '%': (6, 6, 1),     # 37
      '&': (6, 6, 2),     # 38
      "'": (4, 10, -1),   # 39
      '(': (4, 10, 0),    # 40
      ')': (4, 10, 1),    # 41
      '*': (6, 7, 0),     # 42
      '+': (6, 7, 1),     # 43
      ',': (4, 11, 0),    # 44
      '-': (5, 12, 0),    # 45
      '.': (5, 12, 1),    # 46
      '/': (5, 12, 2),    # 47

      # Numbers #
      '0': (7, 7, -1),    # 48
      '1': (7, 7, 0),     # 49
      '2': (5, 10, 0),    # 50
      '3': (5, 10, 1),    # 51
      '4': (5, 10, 2),    # 52
      '5': (5, 10, 3),    # 53
      '6': (5, 11, -1),   # 54
      '7': (5, 11, 0),    # 55
      '8': (5, 11, 1),    # 56
      '9': (5, 11, 2),    # 57

      # Symbols (2) #
      ':': (6, 10, -2),   # 58
      ';': (6, 10, -1),   # 59
      '<': (6, 10, 0),    # 60
      '=': (6, 10, 1),    # 61
      '>': (6, 10, 2),    # 62
      '?': (8, 8, -1),    # 63
      '@': (8, 8, 0),     # 64

      # Capital Letters #
      'A': (8, 8, 1),     # 65
      'B': (6, 11, 0),    # 66
      'C': (6, 11, 1),    # 67
      'D': (6, 11, 2),    # 68
      'E': (7, 10, -1),   # 69
      'F': (7, 10, 0),    # 70
      'G': (7, 10, 1),    # 71
      'H': (8, 9, 0),     # 72
      'I': (8, 9, 1),     # 73
      'J': (8, 9, 2),     # 74
      'K': (5, 15, 0),    # 75
      'L': (5, 15, 1),    # 76
      'M': (7, 11, 0),    # 77
      'N': (7, 11, 1),    # 78
      'O': (8, 10, -1),   # 79
      'P': (8, 10, 0),    # 80
      'Q': (8, 10, 1),    # 81
      'R': (8, 10, 2),    # 82
      'S': (8, 10, 3),    # 83
      'T': (5, 17, -1),   # 84
      'U': (5, 17, 0),    # 85
      'V': (5, 17, 1),    # 86
      'W': (5, 17, 2),    # 87
      'X': (8, 11, 0),    # 88
      'Y': (8, 11, 1),    # 89
      'Z': (9, 10, 0),    # 90

      # Symbols (3) #
      '[': (9, 10, 1),    # 91
      '\\': (9, 10, 2),   # 92
      ']': (9, 10, 3),    # 93
      '^': (10, 10, -6),  # 94
      '_': (10, 10, -5),  # 95
      '`': (10, 10, -4),  # 96

      # Lowercase Letters #
      'a': (10, 10, -3),  # 97
      'b': (10, 10, -2),  # 98
      'c': (9, 11, 0),    # 99
      'd': (10, 10, 0),   # 100
      'e': (10, 10, 1),   # 101
      'f': (10, 10, 2),   # 102
      'g': (10, 10, 3),   # 103
      'h': (10, 10, 4),   # 104
      'i': (10, 10, 5),   # 105
      'j': (10, 10, 6),   # 106
      'k': (10, 10, 7),   # 107
      'l': (10, 10, 8),   # 108
      'm': (10, 10, 9),   # 109
      'n': (10, 11, 0),   # 110
      'o': (10, 11, 1),   # 111
      'p': (10, 11, 2),   # 112
      'q': (10, 11, 3),   # 113
      'r': (10, 11, 4),   # 114
      's': (10, 11, 5),   # 115
      't': (10, 11, 6),   # 116
      'u': (10, 11, 7),   # 117
      'v': (10, 11, 8),   # 118
      'w': (10, 11, 9),   # 119
      'x': (10, 12, 0),   # 120
      'y': (10, 12, 1),   # 121
      'z': (10, 12, 2),   # 122

      # Symbols (4) #
      '{': (10, 12, 3),   # 123
      '|': (10, 12, 4),   # 124
      '}': (10, 12, 5),   # 125
      '~': (10, 12, 6),   # 126
    }

    self.renamed_chars = {
      '>': "GT",
      '<': "LT",
      '+': "Plus",
      '-': "Minus",
      '.': "Period",
      ',': "Comma",
      '[': "LBracket",
      ']': "RBracket",
      ' ': "Space",
      '\n': "\\n",
    }

    self.MAX_LINE_LEN = 45


  def translate(self, _text: str):
    lines: list[str] = []

    for i, c in enumerate(_text):
      try:
        cc = self.renamed_chars[c] if c in self.renamed_chars else c

        # Iteration count, increment count, extra count
        #    vvv             vvv              vvv
        # >+++++++++[<+++++++++++++>-]<-------------. (extra can also be '+'s)
        itrc, incc, extc = self.conversion_dict[c]
        value = (itrc * incc) + extc
        itrs = ''.join(['+' for _ in range(0, itrc)])
        incs = ''.join(['+' for _ in range(0, incc)])
        exts = ''.join(['+' if extc > 0 else '-' for _ in range(0, extc, 1 if extc > 0 else -1)])
        line = f"{'>' if i < 1 else ">>"}{itrs}[<{incs}>-]<{exts}."

        # Calculating spaces needed to make all the `=`s line up in the final code.
        spaces = ''.join([' ' for _ in range(0, (self.MAX_LINE_LEN - len(cc)) - len(line))])

        lines.append(f"{line}{spaces} {cc} = {value}")

      except KeyError: raise Exception(f"unknown character: '{c}' ({ord(c)}).")
    return '\n'.join(lines)
