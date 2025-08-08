from pathlib import Path


p = Path.home()

p

p / "main.py" # 1 slash par concaténattion 

p.joinpath("Documents", "main.py")

(p / "main.py").suffix # extention py

p.joinpath("Documents", "main.py").suffix
