from PIL import Image
import os
from tkinter import Tk, filedialog

# --- Seleccionar carpeta con ventana de Windows ---
root = Tk()
root.withdraw()  # Oculta la ventana principal
input_dir = filedialog.askdirectory(title="Selecciona la carpeta donde estan las imagenes")

if not input_dir:
    print("No se selecciono ninguna carpeta. Saliendo...")
    exit()

# --- Procesar todas las imagenes ---
count = 0
errors = 0

for root_dir, dirs, files in os.walk(input_dir):
    for file in files:
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            file_path = os.path.join(root_dir, file)
            output_path = os.path.splitext(file_path)[0] + ".webp"

            try:
                with Image.open(file_path) as img:
                    img.save(output_path, "webp", quality=90)
                print("Convertido:", file_path, "->", output_path)
                count += 1
            except Exception as e:
                print("Error con", file_path, ":", e)
                errors += 1

print("\nConversion finalizada.")
print("Imagenes convertidas:", count)
if errors:
    print("Errores encontrados:", errors)
