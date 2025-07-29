import os


chemin = "docs/samples/modules&Functions/os/1"

# New folder
folder = os.path.join(chemin , "folder" , "subfolder")
print(folder) # Verifying
if not os.path.exists(folder):
    os.makedirs(folder)
    # os.mkdir(folder)