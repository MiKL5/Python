import os


chemin = "docs/samples/modules&Functions/os/2"

# New folder
folder = os.path.join(chemin , "folder" , "subfolder")
print(folder) # Verifying
os.makedirs(folder , exist_ok=True) # Don't create if it exists

folder = os.path.join(chemin , "folder" , "subfolder", "subsub")
print(folder)
os.makedirs(folder , exist_ok=True)