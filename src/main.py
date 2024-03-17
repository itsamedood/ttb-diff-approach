from converter import TTBConverter
from inquirer import List, Text, prompt
from method import ConversionMethod
from os import getcwd, system
from os.path import exists
from sys import exit


def get_conversion_method() -> ConversionMethod:
  method: dict[str, str] | None = prompt([List("method", "Method for conversion:", [cm.value for cm in ConversionMethod])])

  if method is None: raise Exception("need conversion method!"); exit(1)
  return ConversionMethod(method["method"])


if __name__ == "__main__":
  converter = TTBConverter()
  method = get_conversion_method()

  match method:
    case ConversionMethod.BY_TEXT:
      print("Type `!help` for commands. `!exit` to exit.\n")

      try:
        while True:
          text = input("~ ")

          if text[0] == '!':
            match text[1:]:
              case "help":
                print("""
!help  - Display this list of commands.
!clear - Clear the terminal.
!exit  - Exit the program.
  """)
              case "clear": system("clear")
              case "exit": exit(0)
              case cmd: print("'%s' is not a command." %cmd)

            continue  # Continue after every command so we don't translate `!<cmd>`.

          print(converter.translate(text))
      except KeyboardInterrupt: print("Exited via keyboard interrupt.\n")

    case ConversionMethod.BY_FILE:
      # Get path to file.
      ppath: dict[str, str] | None = prompt([Text("path", "Path to file:", getcwd())])
      if ppath is None: raise Exception("need path to file!"); exit(1)

      path = ppath["path"]
      if not exists(path): raise Exception("'%s' doesn't exist!" %path); exit(1)

      translated_content = ''

      # Open given file and translate it, storing the translation for later.
      with open(path, 'r') as file:
        content = file.read()
        translated_content = converter.translate(content)
        file.close()

      # Get file path without extension at the end.
      pathwe = ''
      extra_chars = 0
      for c in path[::-1]:
        extra_chars += 1
        if c == '.': break

      pathwe = path[:len(path)-extra_chars]
      translated_file = "%s.bf" %pathwe

      # Open translated file (or create one) and write translated code to it.
      with open(translated_file, 'w' if exists(translated_file) else 'x') as file:
        file.write(translated_content)
        file.close()
