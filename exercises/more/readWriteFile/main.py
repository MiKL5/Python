from pathlib import Path


p = Path.home() / "PahtLib" / "readme.txt"

p.touch()
# more readme.txt
p.write_text("Hello")
# more readme.txt
p.read_text()