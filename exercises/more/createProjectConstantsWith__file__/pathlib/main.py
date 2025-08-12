from pathlib import Path


source_file = Path(__file__).resolve()
source_dir  = source_file.parent
root_dir    = source_dir.parent
data_dir    = source_dir / "DATA"