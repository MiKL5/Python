import os


chemin = "docs/samples/modules&Functions/os/3"

folder = os.path.join(chemin , "folder" , "subfolder")
print(folder)

# os.removedirs(folder , exist_ok=True) # ne fonctionne pas

if os.path.exists(folder):
    os.removedirs(folder)