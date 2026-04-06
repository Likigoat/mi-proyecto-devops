import html
import os
import sys

errors = []

if not os.path.exists("src/index.html"):
    errors.append("No se encontró src/index.html")

if not os.path.exists("src/styles.css"):
    errors.append("No se encontró src/styles.css")

if not os.path.exists("README.md") or os.path.getsize("README.md") == 0:
    errors.append("README.md no existe o está vacío")

if errors:
    print("Errores encontrados:")
    for error in errors:
        print("-", error)
    sys.exit(1)
    
with open("src/index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

if html_content.count("<p>") < 1:
    errors.append("index.html debe contener al menos un párrafo")
    
if html_content.count("<h3>") < 1:
    errors.append("index.html debe contener al menos un encabezado <h1>")


with open("src/styles.css", "r") as file:
    css = file.read()

if not css.strip():
    errors.append("El archivo styles.css está vacío")
elif css.count("{") < 2:
    errors.append("styles.css debe contener al menos dos reglas CSS")

if errors:
    print("Errores encontrados:")
    for error in errors:
        print("-", error)
    sys.exit(1)

else:
    print("Proyecto validado correctamente")

