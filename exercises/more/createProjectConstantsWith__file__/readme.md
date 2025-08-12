# **Créer les constantes du projet avec `__file__`**<a href="../../../"><img align="right" src="../../../assets/Python-logo-notext.svg" alt="Python" height="64px"></a>
## **Avec OS**
```py
source_file = os.path.realpath(__file__)
source_dir  = os.path.dirname(source_file)
root_dir    = os.path.dirname(source_dir)
data_dir    = os.path.join(source_dir, "DATA")
```
## **Avec Pathlib**
```py
source_file = Path(__file__).resolve()
source_dir  = source_file.parent
root_dir    = source_dir.parent
data_dir    = source_dir / "DATA"