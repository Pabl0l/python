import sys
import os
import shutil

# Verificar si se proporciona el argumento para la ruta final del directorio principal
if len(sys.argv) < 2:
    print("Por favor, proporciona la parte final de la ruta del directorio principal.")
    sys.exit(1)

# Obtener la parte final de la ruta desde el argumento de la línea de comandos
final_de_ruta = sys.argv[1]

# Directorio principal donde se encuentran las subcarpetas
directorio_principal = os.path.join(r'C:\Users\Pabl0l\Desktop\Bordados\Descargados', final_de_ruta)

# Directorio donde se creará la nueva subcarpeta para los archivos .pes
nueva_subcarpeta = os.path.join(directorio_principal, '0_Todos_Aquí')

# Crear la nueva subcarpeta si no existe
if not os.path.exists(nueva_subcarpeta):
    os.makedirs(nueva_subcarpeta)

# Recorrer todas las subcarpetas del directorio principal
for root, dirs, files in os.walk(directorio_principal):
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)
        # Listar solo los archivos .pes en la subcarpeta actual (Cambia el formato al que tú quieras, .pdf, .jpg, .rar, etc...)
        pes_files = [filename for filename in os.listdir(dir_path) if filename.endswith('.pes')]
        # Verificar si la subcarpeta contiene al menos un archivo .pes
        if pes_files:
            # Iterar sobre los archivos .pes en la subcarpeta
            for filename in pes_files:
                source_file_path = os.path.join(dir_path, filename)
                # Construir el nuevo nombre de archivo con el nombre de la subcarpeta de origen
                new_filename = f"{dir_name}_{filename}"
                # Ruta completa del archivo en la nueva subcarpeta
                destination_file_path = os.path.join(nueva_subcarpeta, new_filename)
                # Verificar si el archivo ya existe en la nueva subcarpeta
                if os.path.exists(destination_file_path):
                    # Si existe, agregar un sufijo único al nombre
                    base, extension = os.path.splitext(new_filename)
                    counter = 1
                    while os.path.exists(destination_file_path):
                        new_filename = f"{base}_{counter}{extension}"
                        destination_file_path = os.path.join(nueva_subcarpeta, new_filename)
                        counter += 1
                # Copiar el archivo a la nueva subcarpeta con el nuevo nombre
                shutil.copy(source_file_path, destination_file_path)

# Una vez finalizado, se habrán copiado los archivos .pes de las subcarpetas
# a la nueva_subcarpeta dentro del directorio principal, manteniéndolos en sus
# ubicaciones originales y renombrándolos para evitar conflictos de nombres.
