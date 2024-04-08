from cli import Cli
from converter import TTBConverter
from inquirer import List, Text, prompt
from os import getcwd, system
from os.path import exists
from sys import exit


# def get_conversion_method() -> ConversionMethod:
#   method: dict[str, str] | None = prompt([List("method", "Method for conversion:", [cm.value for cm in ConversionMethod])])

#   if method is None: raise Exception("need conversion method!"); exit(1)
#   return ConversionMethod(method["method"])


if __name__ == "__main__":
  cli = Cli()
  converter = TTBConverter(cli.flags, cli.file)

  if cli.file is None: converter.shell_mode()
  else: converter.convert_file()

    # Open translated file (or create one) and write translated code to it.
    #   with open(translated_file, 'w' if exists(translated_file) else 'x') as file:
    #     file.write(translated_content)
    #     file.close()

    # case None: ...
