import os


source_file = os.path.realpath(__file__)
source_dir  = os.path.dirname(source_file)
root_dir    = os.path.dirname(source_dir)
data_dir    = os.path.join(source_dir, "DATA")