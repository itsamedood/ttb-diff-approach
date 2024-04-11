from cli import Cli
from converter import TTBConverter


if __name__ == "__main__":
  cli = Cli()
  converter = TTBConverter(cli.flags, cli.file)

  if cli.file is None: converter.shell_mode()
  else: converter.convert_file()
